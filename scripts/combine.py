import sys
import pandas as pd

output = sys.argv[1]
inputs = sys.argv[2:]

dfs = [pd.read_csv(f, sep="\t") for f in inputs]
pd.concat(dfs).to_csv(output, sep="\t", index=False)
