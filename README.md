# Benchmarking Project — Summer 2025

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/rwandantechy/benchmarking-project-summer-2025/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](requirements.txt)

---

## Table of Contents
- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
- [Documentation](#documentation)
- [Conclusion](#conclusion)

---

## Project Overview

This project systematically benchmarks the inference performance, resource utilization, and power consumption of quantized, distilled, and multimodal language models on embedded and edge computing platforms. The results provide actionable insights for optimizing AI deployments in constrained hardware environments, with a focus on reproducibility and thorough documentation.

## Directory Structure

```
benchmarking-project-summer-2025/
├── data/                  # Raw and processed benchmarking data
├── docs/                  # Project documentation and methodology
├── src/                   # Source code for benchmarking and analysis
├── Conclusion/            # Final reports and conclusions
├── Dockerfile             # Docker environment setup
├── docker-compose.yml     # Multi-container orchestration
├── requirements.txt       # Python dependencies
└── README.md              # Project overview and instructions
```

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/rwandantechy/benchmarking-project-summer-2025.git
   cd benchmarking-project-summer-2025
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run a model benchmark (LLM analysis)**
   ```bash
   python benchmark.py --model <model_name>
   ```
   - Benchmarks a specific language model and saves results to `data/processed/llm_benchmark_results.csv`.

4. **Visualize LLM benchmark results**
   ```bash
   python src/analyze_llm.py
   ```
   - Generates plots summarizing LLM performance in `data/processed/`.

5. **Run system analysis (hardware benchmarking)**
   ```bash
   python src/main.py --iterations 5 --output data/processed/results.csv
   ```
   - Benchmarks your system's CPU, memory, and disk for the specified number of iterations.
   - Results are saved to `data/processed/results.csv`.

6. **Visualize system benchmark results**
   ```bash
   python src/analyze_system.py
   ```
   - Generates plots in `data/processed/plots/` summarizing system performance.

---

### Command Summary Table

| Command                                              | Purpose                                 | Output File(s)                                   |
|------------------------------------------------------|-----------------------------------------|--------------------------------------------------|
| `python benchmark.py --model <model_name>`           | Run LLM benchmark                       | `data/processed/llm_benchmark_results.csv`        |
| `python src/analyze_llm.py`                          | Visualize LLM benchmark results         | `data/processed/llm_benchmark_summary_<model>.png`|
| `python src/main.py --iterations 5 --output ...`     | Run system (hardware) benchmarks        | `data/processed/results.csv`                      |
| `python src/analyze_system.py`                       | Visualize system benchmark results      | `data/processed/plots/`                           |

## Documentation
- Detailed methodology, system configuration, and code documentation are available in the `docs/` folder.
- Visual summaries and analysis can be found in `docs/05_Benchmark_Visuals.md` and the `data/processed/` directory.

## Conclusion

For a comprehensive summary and analysis of the benchmarking results, please refer to the full report:

[Benchmarking Report (PDF)](Conclusion/Benchmarking_Report.pdf)
