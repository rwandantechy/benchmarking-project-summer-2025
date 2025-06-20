import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_per_model_results(csv_path="data/processed/llm_benchmark_results.csv"):
    df = pd.read_csv(csv_path)
    print(f"[✓] Loaded CSV with columns: {list(df.columns)}")

    # Group by model
    models = df['model'].unique()

    for model in models:
        model_df = df[df['model'] == model]

        sns.set(style="whitegrid")
        fig, axs = plt.subplots(3, 1, figsize=(10, 12))

        # Response time
        sns.barplot(data=model_df, x='model', y='response_time_sec', ax=axs[0], palette="Blues", legend=False)
        axs[0].set_title(f"{model} - Response Time (seconds)")
        axs[0].set_ylabel("Response Time (s)")

        # CPU usage
        sns.barplot(data=model_df, x='model', y='cpu_percent_used', ax=axs[1], palette="Oranges", legend=False)
        axs[1].set_title(f"{model} - CPU Usage (%)")
        axs[1].set_ylabel("CPU Usage (%)")

        # RAM usage
        sns.barplot(data=model_df, x='model', y='ram_used_mb', ax=axs[2], palette="Greens", legend=False)
        axs[2].set_title(f"{model} - RAM Used (MB)")
        axs[2].set_ylabel("RAM (MB)")

        for ax in axs:
            ax.set_xlabel("")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=30)

        plt.tight_layout()

        safe_name = model.replace(":", "-")
        output_path = os.path.join("data", "processed", f"llm_benchmark_summary_{safe_name}.png")
        plt.savefig(output_path)
        print(f"[✓] Saved plot for {model} at {output_path}")
        plt.close()

if __name__ == "__main__":
    plot_per_model_results()

