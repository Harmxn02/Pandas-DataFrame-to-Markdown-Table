def dataframe_to_markdown(df):
    """
    Convert a Pandas DataFrame to Markdown table format.
    
    Parameters:
        df (DataFrame): The DataFrame to be converted.
        
    Returns:
        str: The Markdown representation of the DataFrame, which you can copy paste into a Markdown file
    """

    # Setting up title and first subtitle, following MD001 and MD022
    markdown = "# Title\n\n"
    markdown += "## Table\n\n"

    # Converting columns to string and joining them with a pipe
    markdown += "| " + " | ".join(df.columns) + " |\n"

    # Adding a separator row
    markdown += "| " + " | ".join(["---"] * len(df.columns)) + " |\n"
    
    # Iterating over the rows, converting them to strings and adding them to the Markdown
    for index, row in df.iterrows():
        markdown += "| " + " | ".join(str(value) for value in row) + " |\n"
    
    
    return markdown




def write_dataframe_to_markdown_file(df, filename):
    """
    Write the Markdown representation of a Pandas DataFrame to a Markdown file.
    
    Parameters:
        df (DataFrame): The DataFrame to be written.
        filename (str): The name of the Markdown file.
    """
    markdown_table = dataframe_to_markdown(df)
    with open(filename, 'w') as f:
        f.write(markdown_table)




if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("./Economic_Indicators.csv")
    write_dataframe_to_markdown_file(df, "table.md")