import pandas as pd

enrichment = pd.read_csv(
    "../input/enrichment.Process.tsv",
    sep="\t"
)

print("Column names:")

for column in enrichment.columns:
    print(column)

print("First rows:")
print(enrichment.head())