import pandas as pd

README_PATH = "README.md"
DATA_PATH = "automation/data.csv"

AUTOGENERATED_TABLE_TOKEN = "<!--- AUTOGENERATED_TABLE -->"
WARNING_HEADER = [
    "<!---",
    "   WARNING: DO NOT EDIT THIS TABLE MANUALLY. IT IS AUTOMATICALLY GENERATED.",
    "-->"
]
TABLE_HEADER = [
    "| **Title** | **Dataset** |",
    "|:---------:|:-----------:|"
]

def _wrap_dataset_link(dataset):
    """Wraps dataset name in Markdown link to dataset."""
    return f"[{dataset}](https://try.fiftyone.ai/datasets/{dataset})"

def read_csv_to_df(path):
    """Reads CSV file and returns a DataFrame."""
    return pd.read_csv(path)

def format_to_md_table(df):
    """Formats DataFrame into a Markdown table."""
    md_table = '\n'.join(TABLE_HEADER) + '\n'
    for _, row in df.iterrows():
        md_table += f"| {row['Title']} | {_wrap_dataset_link(row['Dataset'])} |\n"
    return md_table

def inject_table_into_readme(readme_path, table):
    """Injects the Markdown table into the README file at specified token location."""
    with open(readme_path, 'r') as file:
        content = file.readlines()

    token_indices = [index for index, line in enumerate(content) if AUTOGENERATED_TABLE_TOKEN in line]
    
    if len(token_indices) != 2:
        raise ValueError("README must contain exactly two AUTOGENERATED_TABLE_TOKEN markers")

    new_content = content[:token_indices[0] + 1] + ['\n'.join(WARNING_HEADER) + '\n', table] + content[token_indices[1]:]
    with open(readme_path, 'w') as file:
        file.writelines(new_content)

def main():
    df = read_csv_to_df(DATA_PATH)
    md_table = format_to_md_table(df)
    inject_table_into_readme(README_PATH, md_table)

if __name__ == "__main__":
    main()
