import pandas as pd

partners = pd.read_csv(
    "../input/ADAMTS12_first_shell_medium.tsv",
    sep="\t"
)

print("Column names:")
for column in partners.columns:
    print(column)

print("First rows:")
print(partners.head())