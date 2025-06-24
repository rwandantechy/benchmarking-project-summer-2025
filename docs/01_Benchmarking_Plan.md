# Benchmarking Plan

## Project Overview
This project benchmarks the inference performance, resource utilization, and power consumption of quantized, distilled, and multimodal language models on embedded and edge computing platforms. The goal is to provide actionable insights for optimizing AI deployments in constrained environments, ensuring reproducibility and transparency.

## Objectives
- Evaluate and compare the performance of selected LLMs and multimodal models.
- Measure resource usage (CPU, RAM) and response times during inference.
- Assess the impact of model size and quantization on efficiency.
- Document and visualize results for reproducibility and future reference.

## Methodology
- Deploy models using Docker containers (Ollama backend).
- Use a standardized prompt for all models to ensure fair comparison.
- Collect system metrics before, during, and after inference.
- Automate benchmarking and logging using Python scripts.
- Analyze and visualize results using pandas, matplotlib, and seaborn.

## Metrics Collected
- Inference response time (seconds)
- CPU usage (% average during inference)
- RAM usage (MB, delta during inference)
- Model output (for qualitative comparison)

## Tools & Frameworks
- Python 3.8+
- Docker & Docker Compose
- Ollama (for model serving)
- pandas, matplotlib, seaborn (analysis & visualization)
- psutil, requests (system and API interaction)
- pytest, black (development & testing)

---
