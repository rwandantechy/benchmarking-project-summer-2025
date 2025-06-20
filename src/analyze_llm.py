import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_llm_results(csv_path="data/processed/llm_benchmark_results.csv"):
    df = pd.read_csv(csv_path)
    print(f"Columns in CSV: {list(df.columns)}")
    print("Sample data:")
    print(df.head())

    # Ensure required columns exist
    required_cols = ['model', 'response_time_sec', 'cpu_percent_used', 'ram_used_mb']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(f"Error: Missing columns in CSV file: {missing_cols}")
        return

    # Set Seaborn style
    sns.set(style="whitegrid")

    # Create output directory if it doesn't exist
    os.makedirs("data/processed/plots", exist_ok=True)

    # Generate a separate plot for each model
    for model_name in df['model'].unique():
        model_df = df[df['model'] == model_name]

        fig, axs = plt.subplots(3, 1, figsize=(8, 10))

        sns.barplot(data=model_df, x='model', y='response_time_sec', ax=axs[0], palette="Blues")
        axs[0].set_title("LLM Response Time (seconds)")
        axs[0].set_ylabel("Response Time (s)")

        sns.barplot(data=model_df, x='model', y='cpu_percent_used', ax=axs[1], palette="Oranges")
        axs[1].set_title("CPU Usage (%)")
        axs[1].set_ylabel("CPU Usage (%)")

        sns.barplot(data=model_df, x='model', y='ram_used_mb', ax=axs[2], palette="Greens")
        axs[2].set_title("RAM Used (MB)")
        axs[2].set_ylabel("RAM (MB)")

        for ax in axs:
            ax.set_xlabel("")

        plt.tight_layout()

        # Save using model name
        safe_name = model_name.replace(":", "-")
        output_file = f"data/processed/plots/{safe_name}_benchmark_summary.png"
        plt.savefig(output_file)
        plt.close()

        print(f"[✓] Saved individual plot for model: {model_name} → {output_file}")

if __name__ == "__main__":
    plot_llm_results()

