import pandas as pd

partners = pd.read_csv(
    "../input/ADAMTS12_first_shell_medium.tsv",
    sep="\t"
)

# Keep only non-ADAMTS partners
partners = partners[
    ~partners["node2"].str.startswith("ADAMTS")
]

# Keep the highest score for each partner
partners = partners.sort_values(
    "combined_score",
    ascending=False
)

partners = partners.drop_duplicates(
    "node2"
)

# Keep the top 10 unique partners
partners = partners.head(10)

# Keep useful columns
partners = partners[
    ["node2", "combined_score"]
]

partners = partners.rename(
    columns={
        "node2": "partner_gene",
        "combined_score": "STRING_score"
    }
)

partners.to_csv(
    "../output/ADAMTS12_external_partners.csv",
    index=False
)

print("Top unique non-ADAMTS12 partners:")
print(partners)