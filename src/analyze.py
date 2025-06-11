import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/processed/benchmark_results.csv')

# Example plot: Time per benchmark
plt.figure(figsize=(10, 6))
for benchmark_name in df['benchmark'].unique():
    subset = df[df['benchmark'] == benchmark_name]
    plt.plot(subset['iteration'], subset['time'], label=benchmark_name)

plt.xlabel('Iteration')
plt.ylabel('Time (seconds)')
plt.title('Benchmark Times per Iteration')
plt.legend()
plt.tight_layout()

# Save plot as PNG image file
plt.savefig('benchmark_times.png')

# If you want, you can comment out the following line because you don't have GUI:
# plt.show()
