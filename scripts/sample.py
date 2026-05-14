import sys
import numpy as np

n = int(sys.argv[1])
k = int(sys.argv[2])
repeats = int(sys.argv[3])
seed = int(sys.argv[4])
output = sys.argv[5]

rng = np.random.default_rng(seed + k)

with open(output, "w") as f:
    f.write("k\trepeat\tmean\n")
    for r in range(repeats):
        samples = rng.integers(1, n + 1, size=k)
        f.write(f"{k}\t{r}\t{samples.mean()}\n")
