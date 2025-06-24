# Benchmarking Project — Summer 2025

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
3. **Run a benchmark**
   ```bash
   python benchmark.py --model <model_name>
   # or for system benchmarks
   python src/main.py --iterations 5 --output data/processed/results.csv
   ```

## Documentation
- Detailed methodology, system configuration, and code documentation are available in the `docs/` folder.
- Visual summaries and analysis can be found in `docs/05_Benchmark_Visuals.md` and the `data/processed/` directory.

## Conclusion

For a comprehensive summary and analysis of the benchmarking results, please refer to the full report:

[Benchmarking Report (PDF)](Conclusion/Benchmarking_Report.pdf)
