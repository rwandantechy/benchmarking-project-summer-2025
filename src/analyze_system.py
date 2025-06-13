import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_system_results(csv_path="data/processed/benchmark_results.csv", output_file="data/processed/benchmark_summary.png"):
    """
    Generate plots for system benchmark results (response time and memory usage).
    
    Args:
        csv_path (str): Path to the system benchmark CSV file.
        output_file (str): Path where the output PNG plot will be saved.
    """
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
    sns.barplot(data=df, x='benchmark', y='time', hue='benchmark', ax=axs[0], palette="Blues", dodge=False, legend=False)
    axs[0].set_title("System Benchmark - Response Time (seconds)")
    axs[0].set_xlabel("Benchmark")
    axs[0].set_ylabel("Time (s)")
    axs[0].tick_params(axis='x', rotation=45)

    # Plot memory usage per benchmark
    sns.barplot(data=df, x='benchmark', y='memory', hue='benchmark', ax=axs[1], palette="Greens", dodge=False, legend=False)
    axs[1].set_title("System Benchmark - Memory Usage")
    axs[1].set_xlabel("Benchmark")
    axs[1].set_ylabel("Memory")
    axs[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.savefig(output_file)
    print(f"[✓] Plot saved to {output_file}")

if __name__ == "__main__":
    plot_system_results()
