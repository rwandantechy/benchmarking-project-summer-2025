#!/usr/bin/env python3
"""
accuracy_benchmark.py

Benchmarks language models on a standardized set of quadratic equations
to measure both resource consumption and objective correctness.
Also saves a per-model markdown with answers.
"""

import argparse
import json
import csv
import os
import requests
import time
import threading
import subprocess
from datetime import datetime


def load_questions(path):
    """
    Load quadratic questions from JSON.
    """
    with open(path, "r") as f:
        return json.load(f)


def measure_cpu_usage(stop_event, cpu_samples):
    """
    Thread function to sample CPU usage while the model runs.
    """
    import psutil
    while not stop_event.is_set():
        cpu_samples.append(psutil.cpu_percent(interval=0.1))


def get_docker_stats(container_name="ollama"):
    """
    Get Docker container RAM (MB) and CPU (%) stats.
    """
    try:
        result = subprocess.check_output([
            "docker", "stats", container_name, "--no-stream", "--format", "{{json .}}"
        ])
        stats = json.loads(result.decode())

        # Parse memory
        mem_usage_raw = stats["MemUsage"].split('/')[0].strip()
        if "MiB" in mem_usage_raw:
            mem_mb = float(mem_usage_raw.replace("MiB", "").strip())
        elif "GiB" in mem_usage_raw:
            mem_mb = float(mem_usage_raw.replace("GiB", "").strip()) * 1024
        else:
            mem_mb = 0.0

        # Parse CPU percent
        cpu_str = stats["CPUPerc"].replace("%", "").strip()
        cpu_percent = float(cpu_str)

        return mem_mb, cpu_percent
    except Exception as e:
        print(f"[!] Could not get Docker stats: {e}")
        return 0.0, 0.0


def benchmark_question(model_name, prompt):
    """
    Send a question to the Ollama model and measure resource/time metrics.
    """
    cpu_samples = []
    stop_event = threading.Event()
    thread = threading.Thread(target=measure_cpu_usage, args=(stop_event, cpu_samples))
    thread.start()

    mem_before, _ = get_docker_stats()
    start_time = time.time()

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model_name, "prompt": prompt, "stream": False},
            timeout=120
        )
        response.raise_for_status()
        data = response.json()
        model_answer = data.get("response", "")
    except Exception as e:
        print(f"[!] Error during inference: {e}")
        model_answer = ""

    end_time = time.time()
    stop_event.set()
    thread.join()

    mem_after, _ = get_docker_stats()
    ram_used = max(0.0, round(mem_after - mem_before, 2))  # positive delta only
    avg_cpu = sum(cpu_samples) / len(cpu_samples) if cpu_samples else 0
    inference_time = end_time - start_time

    return model_answer, inference_time, avg_cpu, ram_used


def check_correctness(answer, expected_roots):
    """
    Simple correctness check.
    """
    for root in expected_roots:
        if str(root) in answer:
            return True
    return False


def save_results_csv(
    csv_path, timestamp, question_id, model_name, answer,
    correct, inference_time, avg_cpu, ram_used
):
    """
    Append results to CSV.
    """
    file_exists = os.path.isfile(csv_path)
    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "timestamp", "question_id", "model", "given_answer", "correct",
                "response_time_sec", "cpu_percent_used", "ram_used_mb"
            ])
        writer.writerow([
            timestamp,
            question_id,
            model_name,
            answer.strip(),
            correct,
            round(inference_time, 2),
            round(avg_cpu, 2),
            round(ram_used, 2)
        ])


def save_results_md(md_path, question_id, prompt, answer, correct):
    """
    Save a question/answer block to markdown.
    """
    with open(md_path, "a") as f:
        f.write(f"## {question_id}\n")
        f.write(f"**Prompt:**\n\n```\n{prompt}\n```\n\n")
        f.write(f"**Model Answer:**\n\n```\n{answer.strip()}\n```\n\n")
        f.write(f"**Correct:** {correct}\n\n---\n")


def main():
    parser = argparse.ArgumentParser(
        description="Accuracy benchmark for quadratic math questions."
    )
    parser.add_argument(
        "model", help="Model name as known to Ollama (e.g., phi3:mini)"
    )
    args = parser.parse_args()
    model_name = args.model

    questions_path = "data_v2/questions/math_questions.json"
    results_csv_path = "data_v2/processed/llm_accuracy_results.csv"
    results_md_path = f"data_v2/processed/{model_name.replace(':', '-')}_accuracy_output.md"

    questions = load_questions(questions_path)

    # Clear markdown if re-running
    if os.path.exists(results_md_path):
        os.remove(results_md_path)

    for q in questions:
        prompt = q["prompt"]
        expected_roots = q["expected_roots"]
        question_id = q["id"]

        print(f"→ Testing {question_id} on {model_name}...")

        answer, inference_time, avg_cpu, ram_used = benchmark_question(
            model_name, prompt
        )
        correct = check_correctness(answer, expected_roots)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_results_csv(
            results_csv_path, timestamp, question_id, model_name, answer,
            correct, inference_time, avg_cpu, ram_used
        )

        save_results_md(
            results_md_path, question_id, prompt, answer, correct
        )

        print(
            f"[✓] {question_id} | correct={correct} | "
            f"{round(inference_time,2)}s | CPU={round(avg_cpu,2)}% | RAM={round(ram_used,2)}MB"
        )

    print("All questions completed.")


if __name__ == "__main__":
    main()
