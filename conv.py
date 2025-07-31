import pandas as pd

# Path to your Parquet file
parquet_file = "echannels_survey,parquet"
# Path to save the output CSV file
csv_file = "output_file.csv"

# Read the Parquet file into a DataFrame
df = pd.read_parquet(parquet_file, engine="pyarrow")

# Save DataFrame to a CSV file
df.to_csv(csv_file, index=False)

print(f"File converted successfully to {csv_file}")
