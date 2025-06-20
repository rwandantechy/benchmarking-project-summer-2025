import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_system_results(csv_path="data/processed/benchmark_results.csv"):
    """
    Generate individual plots for each system benchmark (CPU, Memory, Disk).
    Shows trends per benchmark over time or iterations.
    """
    df = pd.read_csv(csv_path)

    print(f"[✓] Columns in CSV: {list(df.columns)}")
    print(df.head())

    sns.set(style="whitegrid")
    os.makedirs("data/processed/plots", exist_ok=True)

    benchmarks = df['benchmark'].unique()

    for bench in benchmarks:
        subset = df[df['benchmark'] == bench].copy()
        subset["index"] = range(1, len(subset)+1)  # Use iteration as x-axis

        fig, axs = plt.subplots(1, 2, figsize=(14, 5))

        # Time plot
        sns.barplot(data=subset, x='index', y='time', ax=axs[0], palette='Blues')
        axs[0].set_title(f"{bench} - Response Time")
        axs[0].set_ylabel("Time (s)")
        axs[0].set_xlabel("Run")

        # Memory plot
        sns.barplot(data=subset, x='index', y='memory', ax=axs[1], palette='Greens')
        axs[1].set_title(f"{bench} - Memory Usage")
        axs[1].set_ylabel("Memory (MB)")
        axs[1].set_xlabel("Run")

        plt.suptitle(f"System Benchmark Summary - {bench}")
        plt.tight_layout()
        filename = f"data/processed/plots/system_{bench.replace(' ', '_').lower()}.png"
        plt.savefig(filename)
        print(f"[✓] Saved: {filename}")
        plt.close()

if __name__ == "__main__":
    plot_system_results()

