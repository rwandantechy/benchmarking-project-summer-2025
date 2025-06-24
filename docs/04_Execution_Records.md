# Execution Records

## Running Benchmarks

### 1. Model Inference Benchmark
Run the following command to benchmark a specific model (e.g., `gemma:2b`):
```bash
python benchmark.py --model gemma:2b
```
Or, from the `src/` directory:
```bash
python src/benchmark.py --model gemma:2b
```

### 2. System Benchmark Suite
To run the full system benchmark suite:
```bash
python src/main.py --iterations 5 --output data/processed/results.csv
```

## System Analysis

System analysis benchmarks your hardware (CPU, memory, disk) to provide context for LLM/model performance.

### How to Run
```bash
python src/main.py --iterations 5 --output data/processed/results.csv
```
- Runs a suite of system benchmarks for the specified number of iterations.
- Results are saved to `data/processed/results.csv`.

### Visualize System Results
```bash
python src/analyze_system.py
```
- Generates plots in `data/processed/plots/` summarizing system performance over time.

## Output Files
- `data/processed/llm_benchmark_results.csv`: Tabular results of all LLM benchmarks.
- `data/processed/<model>_output.md`: Raw output from each model for qualitative review.
- `data/processed/llm_benchmark_summary_<model>.png`: Visual summary of each model's performance.
- `data/processed/benchmark.log`: Log file with execution details and errors.

## Interpreting Results
- **CSV**: Each row contains timestamp, model name, response time, CPU/RAM usage.
- **Plots**: PNG files visualize performance metrics for each model.
- **Logs**: Check `benchmark.log` for errors, warnings, and execution flow.

## Managing Models in Dockerized Ollama

### Adding a Model
To pull (download) a model into the Ollama container:

```bash
docker exec -it ollama ollama pull <model_name>
```
**Example:**
```bash
docker exec -it ollama ollama pull phi3:mini
```
This pulls the model into the running Docker container named `ollama`, making it available for inference.

### Removing a Model
To remove a model from the Ollama container:

```bash
docker exec -it ollama ollama rm <model_name>
```
**Example:**
```bash
docker exec -it ollama ollama rm phi3:mini
```
This deletes the model from disk inside the container, freeing up space and ensuring a clean environment before benchmarking another model.

---
