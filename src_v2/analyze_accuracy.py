#!/usr/bin/env python3
"""
analyze_accuracy.py

Analyzes and visualizes the accuracy benchmarking results
for quadratic equations tested on language models.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def load_results(csv_path):
    """
    Load the CSV results into a DataFrame.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"{csv_path} not found.")
    return pd.read_csv(csv_path)


def plot_correctness_summary(df, output_path):
    """
    Generate a barplot summarizing the accuracy
    of each model across all tested questions.
    """
    sns.set_theme(style="whitegrid")

    # group by model and compute accuracy
    accuracy_df = (
        df.groupby("model")["correct"]
        .mean()
        .reset_index()
        .sort_values(by="correct", ascending=False)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(data=accuracy_df, x="model", y="correct", palette="Greens_r")
    plt.ylabel("Accuracy (proportion correct)")
    plt.xlabel("Model")
    plt.title("LLM Quadratic Accuracy Benchmark")
    plt.ylim(0, 1)
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()
    print(f"[✓] Saved accuracy chart to {output_path}")


def main():
    """
    Main execution for accuracy analysis.
    """
    csv_path = "data_v2/processed/llm_accuracy_results.csv"
    output_path = "data_v2/processed/llm_accuracy_summary.png"

    try:
        df = load_results(csv_path)
        plot_correctness_summary(df, output_path)
        print(" Accuracy analysis complete.")
    except Exception as e:
        print(f"[!] Analysis failed: {e}")


if __name__ == "__main__":
    main()

