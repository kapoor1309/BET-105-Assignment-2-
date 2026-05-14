import sys
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(sys.argv[1], sep="\t")
output = sys.argv[2]
n = int(sys.argv[3])

ks = sorted(df["k"].unique())
data = [df[df["k"] == k]["mean"].values for k in ks]
labels = [f"k={k}" for k in ks]

plt.figure(figsize=(12, 5))
plt.boxplot(data, tick_labels=labels)
plt.title(f"Testing Draws for {n}")
plt.ylabel("Mean")
plt.tight_layout()
plt.savefig(output, dpi=150)
