import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_llm_results(csv_path="data/processed/llm_benchmark_results.csv"):
    df = pd.read_csv(csv_path)
    print(f"Columns in CSV: {list(df.columns)}")
    print("Sample data:")
    print(df.head())

    # Verify required columns
    required_cols = ['model', 'response_time_sec', 'cpu_percent_used', 'ram_used_mb']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(f"Error: Missing columns in CSV file: {missing_cols}")
        return

    sns.set(style="whitegrid")

    fig, axs = plt.subplots(3, 1, figsize=(10, 12))

    # Response time
    sns.barplot(data=df, x='model', y='response_time_sec', hue='model', ax=axs[0], palette="Blues", legend=False)
    axs[0].set_title("LLM Response Time (seconds)")
    axs[0].set_xlabel("Model")
    axs[0].set_ylabel("Response Time (s)")

    # CPU usage
    sns.barplot(data=df, x='model', y='cpu_percent_used', hue='model', ax=axs[1], palette="Oranges", legend=False)
    axs[1].set_title("CPU Usage (%)")
    axs[1].set_xlabel("Model")
    axs[1].set_ylabel("CPU Usage (%)")

    # RAM used
    sns.barplot(data=df, x='model', y='ram_used_mb', hue='model', ax=axs[2], palette="Greens", legend=False)
    axs[2].set_title("RAM Used (MB)")
    axs[2].set_xlabel("Model")
    axs[2].set_ylabel("RAM (MB)")

    plt.tight_layout()

    # Automatically use first model name for filename
    model_name_safe = df['model'].unique()[0].replace(':', '-')
    output_file = f"data/processed/llm_benchmark_summary_{model_name_safe}.png"

    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")

if __name__ == "__main__":
    plot_llm_results()
