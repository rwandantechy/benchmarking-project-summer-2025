import requests
import time
import subprocess
import csv
import os
import json
import argparse
import psutil
from datetime import datetime

PROMPT = "Explain the main differences between supervised and unsupervised machine learning, and provide an example of each."

def run_inference(model_name):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": model_name,
        "prompt": PROMPT,
        "stream": True
    }, stream=True)

    collected = ""
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                collected += data.get("response", "")
            except json.JSONDecodeError:
                continue
    return collected

def get_docker_mem_usage(container_name="ollama"):
    try:
        result = subprocess.check_output([
            "docker", "stats", container_name, "--no-stream", "--format", "{{json .}}"
        ])
        stats = json.loads(result.decode())
        mem_usage = stats["MemUsage"].split('/')[0].strip()
        if "MiB" in mem_usage:
            return float(mem_usage.replace("MiB", "").strip())
        elif "GiB" in mem_usage:
            return float(mem_usage.replace("GiB", "").strip()) * 1024
        return 0.0
    except Exception as e:
        print(f"[!] Could not fetch Docker memory usage: {e}")
        return 0.0

def benchmark_model(model_name):
    mem_before = get_docker_mem_usage("ollama")

    # Sample CPU before running inference
    cpu_usage_before = psutil.cpu_percent(interval=0.1)

    start_time = time.time()
    output = run_inference(model_name)
    end_time = time.time()

    # Sample CPU again after inference (over 1 second interval)
    cpu_usage_after = psutil.cpu_percent(interval=1.0)

    mem_after = get_docker_mem_usage("ollama")

    metrics = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model": model_name,
        "response_time_sec": round(end_time - start_time, 2),
        "cpu_percent_used": round(cpu_usage_after, 2),
        "ram_used_mb": round(mem_after - mem_before, 2)
    }

    return output, metrics

def save_results(metrics, output, output_dir="data/processed"):
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, "llm_benchmark_results.csv")
    file_exists = os.path.isfile(csv_path)

    with open(csv_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=metrics.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(metrics)

    output_file = os.path.join(output_dir, f"{metrics['model'].replace(':', '-')}_output.md")
    with open(output_file, "w") as f:
        f.write(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark an Ollama model.")
    parser.add_argument("model", help="Model name (e.g. phi3:mini)")
    args = parser.parse_args()

    print(f"Running benchmark for {args.model}...")
    output, metrics = benchmark_model(args.model)
    save_results(metrics, output)
    print("[✓] Done. Metrics logged and output saved.")

