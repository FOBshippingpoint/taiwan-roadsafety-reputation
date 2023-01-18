import pandas as pd
from pathlib import Path

print("start: 2_clean_death_rate")

data_path = Path("../data")

df_death_rate = pd.read_csv(data_path / "death_rate.csv")

df_reputation = pd.read_excel(data_path / "reputation.xlsx")

df_death_rate = df_death_rate[["SpatialDimValueCode", "FactValueNumeric"]]
df_death_rate = df_death_rate.rename(
    columns={"SpatialDimValueCode": "ADM0_A3", "FactValueNumeric": "deathRate"}
)

df = df_death_rate.merge(df_reputation, how="left", on="ADM0_A3")
df.dropna(how="all")

with open(data_path / "reputation.csv", mode="w", newline="\n", encoding="utf-8") as f:
    df.to_csv(f)

with open(data_path / "reputation.json", "w", encoding="utf-8") as f:
    df.to_json(f, orient="records", force_ascii=False)

print("done")
