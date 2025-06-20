import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_system_results(csv_path="data/processed/benchmark_results.csv"):
    """
    Generate separate plots for each system benchmark (response time & memory).
    Each benchmark gets its own chart.
    """
    df = pd.read_csv(csv_path)

    print(f"Columns in CSV: {list(df.columns)}")
    print("Sample data:")
    print(df.head())

    sns.set(style="whitegrid")

    # Create output directory if not exists
    os.makedirs("data/processed/plots", exist_ok=True)

    benchmarks = df['benchmark'].unique()
    for bench in benchmarks:
        subset = df[df['benchmark'] == bench]

        fig, axs = plt.subplots(1, 2, figsize=(14, 5))

        # Time plot
        sns.barplot(data=subset, x='benchmark', y='time', ax=axs[0], palette='Blues')
        axs[0].set_title(f"{bench} - Response Time")
        axs[0].set_ylabel("Time (s)")
        axs[0].set_xlabel("")

        # Memory plot
        sns.barplot(data=subset, x='benchmark', y='memory', ax=axs[1], palette='Greens')
        axs[1].set_title(f"{bench} - Memory Usage")
        axs[1].set_ylabel("Memory (MB)")
        axs[1].set_xlabel("")

        plt.suptitle(f"System Benchmark - {bench}")
        plt.tight_layout()

        # Save plot
        filename = f"data/processed/plots/system_{bench.replace(' ', '_').lower()}.png"
        plt.savefig(filename)
        print(f"[✓] Saved: {filename}")
        plt.close()

if __name__ == "__main__":
    plot_system_results()

