import requests
import time
import subprocess
import csv
import os
import json
import argparse
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

def get_docker_ram(container="ollama"):
    try:
        output = subprocess.check_output([
            "docker", "stats", container, "--no-stream", "--format", "{{json .}}"
        ])
        stats = json.loads(output.decode())
        mem = stats["MemUsage"].split("/")[0].strip()
        if "MiB" in mem:
            return float(mem.replace("MiB", "").strip())
        elif "GiB" in mem:
            return float(mem.replace("GiB", "").strip()) * 1024
    except Exception as e:
        print(f"[!] RAM read failed: {e}")
    return 0.0

def benchmark_model(model):
    print(f"Running benchmark for {model}...")
    start = time.time()
    ram_before = get_docker_ram()

    output = run_inference(model)

    ram_after = get_docker_ram()
    end = time.time()

    ram_used = max(0.0, round(ram_after - ram_before, 2))

    metrics = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model": model,
        "response_time_sec": round(end - start, 2),
        "cpu_percent_used": 0.0,  # can be improved later
        "ram_used_mb": ram_used
    }

    return output, metrics

def save_results(metrics, output, output_dir="data/processed"):
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, "llm_benchmark_results.csv")
    is_new = not os.path.exists(csv_path)

    with open(csv_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=metrics.keys())
        if is_new:
            writer.writeheader()
        writer.writerow(metrics)

    with open(os.path.join(output_dir, f"{metrics['model'].replace(':', '-')}_output.md"), "w") as f:
        f.write(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model", help="e.g. gemma:2b")
    args = parser.parse_args()

    output, metrics = benchmark_model(args.model)
    save_results(metrics, output)
    print("[✓] Done. Metrics logged and output saved.")

