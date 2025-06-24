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

## Output Files
- `data/processed/llm_benchmark_results.csv`: Tabular results of all LLM benchmarks.
- `data/processed/<model>_output.md`: Raw output from each model for qualitative review.
- `data/processed/llm_benchmark_summary_<model>.png`: Visual summary of each model's performance.
- `data/processed/benchmark.log`: Log file with execution details and errors.

## Interpreting Results
- **CSV**: Each row contains timestamp, model name, response time, CPU/RAM usage.
- **Plots**: PNG files visualize performance metrics for each model.
- **Logs**: Check `benchmark.log` for errors, warnings, and execution flow.

---
