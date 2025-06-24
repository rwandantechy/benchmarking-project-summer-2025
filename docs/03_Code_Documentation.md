# Code Documentation

## Codebase Structure

- `src/`
  - `benchmark.py`: Runs model inference benchmarks, collects system metrics, and saves results.
  - `analyze_llm.py`: Analyzes and visualizes LLM benchmark results, generating summary plots.
  - `analyze_system.py`: Analyzes system-level benchmarks (CPU, memory, disk) and produces visualizations.
  - `config.py`: Loads and saves configuration parameters for benchmarking.
  - `main.py`: Main entry point for running system benchmarks and managing workflow.
  - `__init__.py`: Package marker.

## Data Flow
1. **Benchmark Execution**: `benchmark.py` (or `src/benchmark.py`) runs inference on selected models, collects metrics (CPU, RAM, response time), and saves results to `data/processed/llm_benchmark_results.csv` and per-model output files.
2. **Analysis & Visualization**: `analyze_llm.py` and `analyze_system.py` read the processed CSV files, generate plots, and save visual summaries to `data/processed/`.
3. **Configuration**: `config.py` manages default and user-specified settings for all benchmarks.
4. **Logging**: All major actions and results are logged to `data/processed/benchmark.log`.

## Extending the Codebase
- Add new models by updating the model list and running the benchmark script.
- Adjust configuration via `src/config.json` or directly in `config.py`.
- Add new analysis scripts in `src/` as needed.

---
