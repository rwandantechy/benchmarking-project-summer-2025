import requests
import time
import subprocess
import csv
import os
import json
import argparse
from datetime import datetime

# Default prompt used for benchmarking
PROMPT = "Explain the main differences between supervised and unsupervised machine learning, and provide an example of each."

def run_inference(model_name):
    """Send prompt to Ollama model and stream response properly."""
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
                continue  # skip malformed line

    return collected

def get_docker_stats(container_name="ollama"):
    """Returns RAM (MB) and CPU (%) usage of a Docker container."""
    try:
        result = subprocess.check_output(
            ["docker", "stats", container_name, "--no-stream", "--format", "{{json .}}"]
        )
        stats = json.loads(result.decode())

        # Parse memory
        mem_usage_raw = stats["MemUsage"].split('/')[0].strip()
        if "MiB" in mem_usage_raw:
            mem_mb = float(mem_usage_raw.replace("MiB", "").strip())
        elif "GiB" in mem_usage_raw:
            mem_mb = float(mem_usage_raw.replace("GiB", "").strip()) * 1024
        else:
            mem_mb = 0.0

        # Parse CPU
        cpu_str = stats["CPUPerc"].replace("%", "").strip()
        cpu_percent = float(cpu_str)

        return mem_mb, cpu_percent
    except Exception as e:
        print(f"[!] Failed to get Docker stats: {e}")
        return 0.0, 0.0

def benchmark_model(model_name):
    start_time = time.time()
    mem_before, cpu_before = get_docker_stats()

    output = run_inference(model_name)

    mem_after, cpu_after = get_docker_stats()
    end_time = time.time()

    ram_used = max(0.0, round(mem_after - mem_before, 2))
    cpu_used = max(0.0, round(cpu_after - cpu_before, 2))

    metrics = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model": model_name,
        "response_time_sec": round(end_time - start_time, 2),
        "cpu_percent_used": cpu_used,
        "ram_used_mb": ram_used
    }

    return output, metrics

def save_results(metrics, output, output_dir="data/processed"):
    os.makedirs(output_dir, exist_ok=True)

    # Save or append to CSV
    csv_file = os.path.join(output_dir, "llm_benchmark_results.csv")
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=metrics.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(metrics)

    # Save model output
    output_txt = os.path.join(output_dir, f"{metrics['model'].replace(':', '-')}_output.md")
    with open(output_txt, "w") as f:
        f.write(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run benchmark for a specific Ollama model.")
    parser.add_argument("model", help="Model name, e.g., gemma:2b")
    args = parser.parse_args()

    print(f"Running benchmark for {args.model}...")
    output, metrics = benchmark_model(args.model)
    save_results(metrics, output)
    print("[✓] Done. Metrics logged and output saved.")

