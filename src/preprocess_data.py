import pandas as pd

def load_data(file_path):
    df = pd.read_excel(file_path)

    # Ensure correct column names
    required_columns = ["id", "text_snippet", "labels"]
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Missing required columns in dataset!")

    # Convert labels from comma-separated to list format
    df["labels"] = df["labels"].apply(lambda x: x.split(", ") if isinstance(x, str) else [])
    return df

if __name__ == "__main__":
    df = load_data("dataset/data.xlsx")
    print(df.head())
