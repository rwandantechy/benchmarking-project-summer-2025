# Benchmark Visuals

This section presents visual summaries of benchmarking results for various language models and system tests. All plots are generated from data in `data/processed/`.

## Model Benchmark Visualizations
For each tested model, a summary plot is generated showing:
- **Response Time (seconds)**
- **CPU Usage (%)**
- **RAM Usage (MB)**

### Example Plots
- ![Gemma-2b Summary](../data/processed/llm_benchmark_summary_gemma-2b.png)
- ![Phi3-mini Summary](../data/processed/llm_benchmark_summary_phi3-mini.png)
- ![Mistral Summary](../data/processed/llm_benchmark_summary_mistral.png)
- ![TinyLlama Summary](../data/processed/llm_benchmark_summary_tinyllama.png)
- ![Llama3.1-latest Summary](../data/processed/llm_benchmark_summary_llama3.1-latest.png)
- ![Llava-7b Summary](../data/processed/llm_benchmark_summary_llava-7b.png)
- ![Orca-mini-latest Summary](../data/processed/llm_benchmark_summary_orca-mini-latest.png)
- ![Notux-8x7b Summary](../data/processed/llm_benchmark_summary_notux-8x7b.png)
- ![CodeLlama-latest Summary](../data/processed/llm_benchmark_summary_codellama-latest.png)

## Key Observations
- Larger models generally consume more RAM and CPU, and have longer response times.
- Quantized and distilled models offer significant efficiency gains.
- Model selection should balance performance needs and hardware constraints.

## Next Steps
- Benchmark additional models and quantization levels.
- Explore hardware acceleration (e.g., GPU, NPU).
- Analyze power consumption for sustained workloads.

---
