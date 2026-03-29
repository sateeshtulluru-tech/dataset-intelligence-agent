import pandas as pd

def analyze_dataset(file_path):
    df = pd.read_csv(file_path)

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("\nMissing Values:\n", df.isnull().sum())

    print("\nColumn Types:\n", df.dtypes)

if __name__ == "__main__":
    analyze_dataset("sample.csv")
