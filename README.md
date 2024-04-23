# Pandas DataFrame to Markdown Table

Two simple **Python** functions that convert a **Pandas DataFrame** to a **Markdown table**

## How to use

```python
write_dataframe_to_markdown_file(df, filename)
```

| Variable   | Description                                              | Comment                                                                            |
| ---------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `df`       | a Pandas DataFrame                                       | doesn't work with **Polars** because it does not have the function `df.iterrows()` |
| `filename` | filepath where you want your markdown file to be placed. | **has to end with `.md`**                                                          |

## Example usage

```python
write_dataframe_to_markdown_file(df_transposed, "README.md")
write_dataframe_to_markdown_file(df_transposed, "./directory/README.md")
```

## What the markdown file looks like

Check out the `/converted/` directory in the root of this repository for 2 examples.

## The complete code

``` python
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
```

``` python
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
```
