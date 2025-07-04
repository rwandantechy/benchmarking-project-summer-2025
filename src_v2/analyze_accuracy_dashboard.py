#!/usr/bin/env python3
"""
analyze_accuracy_dashboard_refined.py

Creates an advanced visualization dashboard for language model benchmarks:
- Response time (with color gradient and min/max annotation)
- CPU usage (horizontal bar chart)
- RAM usage (with outlier highlight)
- Correctness (with icons)
- Summary statistics box
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import argparse
import os

def load_results(csv_path):
    """
    Load the CSV results into a DataFrame.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"{csv_path} not found.")
    return pd.read_csv(csv_path)

def plot_dashboard(df, model_name, output_path):
    """
    Generate the multi-metric visualization dashboard.
    """
    sns.set_theme(style="whitegrid")

    model_df = df[df["model"] == model_name]

    # Defensive guard for missing data
    if model_df.empty:
        print(f"[!] No data found for model {model_name} in CSV.")
        return

    if model_df["correct"].isnull().all():
        print(f"[!] Model {model_name} has no correctness results; skipping dashboard.")
        return

    questions = model_df["question_id"].astype(str)
    response_times = model_df["response_time_sec"]
    cpu_usages = model_df["cpu_percent_used"]
    ram_usages = model_df["ram_used_mb"]
    correctness = model_df["correct"].map({True: "Correct", False: "Incorrect"})

    # Defensive mismatch check
    if len(correctness) != len(questions):
        print("[!] Mismatch between correctness and questions — dashboard skipped.")
        return

    # Summary statistics
    avg_time = response_times.mean()
    pct_correct = correctness.value_counts(normalize=True).get("Correct", 0) * 100
    max_cpu = cpu_usages.max()
    max_ram = ram_usages.max()

    fig, axs = plt.subplots(2, 2, figsize=(18, 13))
    plt.subplots_adjust(top=0.85, hspace=0.35, wspace=0.25)

    # Response time with color gradient
    colors = sns.color_palette("Blues", len(response_times))
    axs[0,0].bar(questions, response_times, color=colors)
    axs[0,0].set_title("Response Time per Question")
    axs[0,0].set_ylabel("Time (s)")
    for i, v in enumerate(response_times):
        axs[0,0].text(i, v + 1, f"{v:.1f}s", ha="center", fontsize=11)

    try:
        max_idx = response_times.idxmax()
        min_idx = response_times.idxmin()
        axs[0,0].annotate('Max', (questions.iloc[max_idx], response_times.iloc[max_idx]),
                          textcoords="offset points", xytext=(0,10), ha='center', color='red', weight='bold')
        axs[0,0].annotate('Min', (questions.iloc[min_idx], response_times.iloc[min_idx]),
                          textcoords="offset points", xytext=(0,10), ha='center', color='green', weight='bold')
    except Exception:
        pass  # handle missing values gracefully

    # CPU usage horizontal bars
    axs[0,1].barh(questions, cpu_usages, color=sns.color_palette("Oranges", len(cpu_usages)))
    axs[0,1].set_title("CPU Usage per Question")
    axs[0,1].set_xlabel("CPU (%)")
    for i, v in enumerate(cpu_usages):
        axs[0,1].text(v + 0.5, i, f"{v:.1f}%", va="center", fontsize=11)
    axs[0,1].set_yticklabels(questions)

    # RAM usage with outlier highlight
    axs[1,0].bar(questions, ram_usages, color=sns.color_palette("Greens", len(ram_usages)))
    axs[1,0].set_title("RAM Usage per Question")
    axs[1,0].set_ylabel("RAM (MB)")
    for i, v in enumerate(ram_usages):
        display_val = f"{v:.1f} MB" if v > 0.5 else "~0 MB"
        axs[1,0].text(i, v + 5, display_val, ha="center", fontsize=11)
    outlier_idx = np.where(ram_usages == max_ram)[0]
    for idx in outlier_idx:
        axs[1,0].bar(questions.iloc[idx], ram_usages.iloc[idx], color='red', alpha=0.5)
        axs[1,0].annotate('Peak', (idx, ram_usages.iloc[idx]),
                          textcoords="offset points", xytext=(0,10), ha='center', color='red', weight='bold')

    # Correctness with icons
    for i, val in enumerate(correctness):
        icon = "✔️" if val == "Correct" else "❌"
        axs[1,1].text(i+0.5, 0.5, icon, ha='center', va='center', fontsize=30)
    axs[1,1].set_xlim(0, len(questions))
    axs[1,1].set_ylim(0, 1)
    axs[1,1].set_xticks(np.arange(0.5, len(questions)+0.5, 1))
    axs[1,1].set_xticklabels(questions)
    axs[1,1].set_yticks([])
    axs[1,1].set_title("Answer Correctness per Question")
    axs[1,1].spines['top'].set_visible(False)
    axs[1,1].spines['right'].set_visible(False)
    axs[1,1].spines['left'].set_visible(False)
    axs[1,1].spines['bottom'].set_visible(False)

    # Summary box
    summary_text = (f"Avg Time: {avg_time:.2f}s\n"
                    f"% Correct: {pct_correct:.1f}%\n"
                    f"Peak CPU: {max_cpu:.1f}%\n"
                    f"Peak RAM: {max_ram:.1f} MB")
    fig.text(0.5, 0.93, f" Accuracy Dashboard for {model_name}", fontsize=18, fontweight="bold", ha='center')
    fig.text(0.99, 0.01, summary_text, fontsize=13, ha='right', va='bottom',
             bbox=dict(facecolor='lightgrey', alpha=0.5, boxstyle='round,pad=0.5'))

    plt.savefig(output_path)
    plt.close()
    print(f"[✓] Saved dashboard to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate advanced accuracy dashboard.")
    parser.add_argument("model", help="The model name in CSV (e.g. phi3:mini)")
    args = parser.parse_args()

    csv_path = "data_v2/processed/llm_accuracy_results.csv"
    output_path = f"data_v2/processed/llm_accuracy_dashboard_{args.model.replace(':', '-')}.png"

    try:
        df = load_results(csv_path)
        plot_dashboard(df, args.model, output_path)
        print(" Dashboard generation complete.")
    except Exception as e:
        print(f"[!] Failed: {e}")

if __name__ == "__main__":
    main()
