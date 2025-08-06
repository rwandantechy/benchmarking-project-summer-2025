# Benchmarking Project — Summer 2025

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/rwandantechy/benchmarking-project-summer-2025/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](requirements.txt)

---
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/rwandantechy/benchmarking-project-summer-2025)
## Table of Contents
- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Benchmarking Workflows](#benchmarking-workflows)
  - [Generative Benchmarking (v1)](#generative-benchmarking-v1)
  - [Accuracy-Focused Benchmarking (v2)](#accuracy-focused-benchmarking-v2)
- [Quadratic Equation Benchmark Questions](#quadratic-equation-benchmark-questions)
- [Getting Started](#getting-started)
- [Managing Models in Dockerized Ollama](#managing-models-in-dockerized-ollama)
- [Documentation](#documentation)
- [Conclusion](#conclusion)

---

## Project Overview

This project benchmarks the inference performance, resource utilization, and accuracy of language models on embedded and edge devices. It supports both open-ended generative tasks (v1) and objective, accuracy-focused tasks (v2, such as solving quadratic equations with known answers). The goal is to provide actionable insights for optimizing AI deployments in resource-constrained environments.

## Directory Structure

| Folder         | Description                                                |
|---------------|------------------------------------------------------------|
| `src/`        | v1: Generative benchmarking, analysis, and utilities       |
| `src_v2/`     | v2: Accuracy-focused benchmarking and analysis scripts     |
| `docs/`       | Project documentation and methodology                      |
| `data/`       | v1: Raw and processed benchmarking data, outputs, and plots|
| `data_v2/`    | v2: Processed results and JSON-based question sets         |
| `Conclusion/` | Final reports and deliverables (e.g., PDF summary)         |

## Benchmarking Workflows

### Generative Benchmarking (v1)
- Benchmarks LLMs on open-ended prompts.
- Measures response time, resource usage, and saves model outputs.
- No objective accuracy metric (answers are subjective).
- Data and scripts: `src/`, `data/`

### Accuracy-Focused Benchmarking (v2)
- Benchmarks LLMs on math questions with objectively correct answers.
- Measures response time, resource usage, and correctness (accuracy).
- Uses a set of standard quadratic equations, one for each root type, stored in JSON.
- Data and scripts: `src_v2/`, `data_v2/`

## Quadratic Equation Benchmark Questions

| Type             | Equation                  | Expected Answer         |
|------------------|--------------------------|------------------------|
| Distinct Real    | x^2 - 7x + 12 = 0        | 3, 4                   |
| Repeated Real    | x^2 - 6x + 9 = 0         | 3                      |
| Complex          | x^2 + 2x + 5 = 0         | -1+2i, -1-2i           |
| Irrational Real  | x^2 - 2 = 0              | 1.414, -1.414          |

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
3. **Run a generative benchmark (v1)**
   ```bash
   python benchmark.py --model <model_name>
   ```
4. **Run an accuracy-focused math benchmark (v2)**
   ```bash
   python src_v2/accuracy_benchmark.py <model_name>
   ```
   - Uses questions from `data_v2/questions/math_questions.json`
   - Results saved to `data_v2/processed/accuracy_benchmark_results.csv`

## Managing Models in Dockerized Ollama

### Adding a Model
```bash
docker exec -it ollama ollama pull <model_name>
```
### Removing a Model
```bash
docker exec -it ollama ollama rm <model_name>
```

## Documentation
- See the `docs/` folder for detailed methodology, system configuration, and code documentation.
- Visual summaries and analysis can be found in `docs/05_Benchmark_Visuals.md` and the `data/processed/` directory.

## Conclusion

For a comprehensive summary and analysis of the benchmarking results, please refer to the full report:

[Benchmarking Report (PDF)](Conclusion/Benchmarking_Report.pdf)
