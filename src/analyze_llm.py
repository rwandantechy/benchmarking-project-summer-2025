import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_latest_model(csv_path="data/processed/llm_benchmark_results.csv"):
    df = pd.read_csv(csv_path)
    print(f"[✓] Loaded CSV with columns: {list(df.columns)}")

    if df.empty:
        print("[!] CSV is empty.")
        return

    # Get the last row (latest benchmarked model)
    latest_entry = df.iloc[-1]
    model_name = latest_entry['model']

    # Use only the latest entry to avoid stacking
    model_df = pd.DataFrame([latest_entry])

    sns.set(style="whitegrid")
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))

    # Plot response time
    sns.barplot(data=model_df, x='model', y='response_time_sec', ax=axs[0], palette="Blues", legend=False)
    axs[0].set_title("Response Time (seconds)")
    axs[0].set_ylabel("Time (s)")

    # Plot CPU usage
    sns.barplot(data=model_df, x='model', y='cpu_percent_used', ax=axs[1], palette="Oranges", legend=False)
    axs[1].set_title("CPU Usage (%)")
    axs[1].set_ylabel("CPU (%)")

    # Plot RAM usage
    sns.barplot(data=model_df, x='model', y='ram_used_mb', ax=axs[2], palette="Greens", legend=False)
    axs[2].set_title("RAM Usage (MB)")
    axs[2].set_ylabel("RAM (MB)")

    for ax in axs:
        ax.set_xlabel("")
        ax.set_xticklabels([model_name], rotation=0)

    plt.tight_layout()

    # Save the plot
    safe_model = model_name.replace(':', '-')
    output_path = f"data/processed/llm_benchmark_summary_{safe_model}.png"
    plt.savefig(output_path)
    print(f"[✓] Saved plot: {output_path}")

if __name__ == "__main__":
    plot_latest_model()

