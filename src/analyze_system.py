import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_results(csv_path="data/processed/benchmark_results.csv", output_file="data/processed/benchmark_summary.png"):
    # Load the CSV data
    df = pd.read_csv(csv_path)

    # Print columns and sample for verification
    print(f"Columns in CSV: {list(df.columns)}")
    print("Sample data:")
    print(df.head())

    sns.set(style="whitegrid")

    # Create subplots: 2 rows, 1 column
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Plot response time per benchmark
    sns.barplot(data=df, x='benchmark', y='time', ax=axs[0], palette="Blues", hue='benchmark', dodge=False)
    axs[0].set_title("Response Time (seconds)")
    axs[0].set_xlabel("Benchmark")
    axs[0].set_ylabel("Time (s)")
    # Remove legend if exists
    legend = axs[0].get_legend()
    if legend is not None:
        legend.remove()

    # Plot memory usage per benchmark
    sns.barplot(data=df, x='benchmark', y='memory', ax=axs[1], palette="Greens", hue='benchmark', dodge=False)
    axs[1].set_title("Memory Usage")
    axs[1].set_xlabel("Benchmark")
    axs[1].set_ylabel("Memory")
    # Remove legend if exists
    legend = axs[1].get_legend()
    if legend is not None:
        legend.remove()

    plt.tight_layout()
    plt.savefig(output_file)
    print(f"[✓] Plot saved to {output_file}")

if __name__ == "__main__":
    plot_results()
