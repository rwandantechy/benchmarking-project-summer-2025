import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_per_model_results(csv_path="data/processed/llm_benchmark_results.csv"):
    # Load benchmark results
    df = pd.read_csv(csv_path)
    print(f"[✓] Loaded CSV with columns: {list(df.columns)}")

    # Unique models
    models = df['model'].unique()
    sns.set_theme(style="whitegrid")

    for model in models:
        model_df = df[df['model'] == model]

        fig, axs = plt.subplots(3, 1, figsize=(10, 12))
        fig.suptitle(f"Benchmark Summary for {model}", fontsize=16, fontweight='bold')

        # Response Time
        sns.barplot(data=model_df, x='model', y='response_time_sec', hue='model',
                    ax=axs[0], palette='Blues', legend=False)
        axs[0].set_title("Response Time (seconds)")
        axs[0].set_ylabel("Time (s)")
        axs[0].set_xlabel("")

        # CPU Usage
        sns.barplot(data=model_df, x='model', y='cpu_percent_used', hue='model',
                    ax=axs[1], palette='Oranges', legend=False)
        axs[1].set_title("CPU Usage (%)")
        axs[1].set_ylabel("CPU (%)")
        axs[1].set_xlabel("")

        # RAM Used
        sns.barplot(data=model_df, x='model', y='ram_used_mb', hue='model',
                    ax=axs[2], palette='Greens', legend=False)
        axs[2].set_title("RAM Usage (MB)")
        axs[2].set_ylabel("RAM (MB)")
        axs[2].set_xlabel("")

        # Clean x-axis labels
        for ax in axs:
            ax.tick_params(axis='x', rotation=0)

        plt.tight_layout(rect=[0, 0, 1, 0.96])  # Make space for suptitle
        safe_name = model.replace(":", "-")
        output_file = f"data/processed/llm_benchmark_summary_{safe_name}.png"
        plt.savefig(output_file)
        plt.close()
        print(f"[✓] Saved plot: {output_file}")

if __name__ == "__main__":
    plot_per_model_results()

