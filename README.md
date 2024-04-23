# Pandas DataFrame to Markdown Table

A simple **Python** function that convert a **Pandas DataFrame** to a **Markdown table**

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

# OR
write_dataframe_to_markdown_file(df=df_transposed, filename="README.md")
write_dataframe_to_markdown_file(df=df_transposed, filename="./directory/README.md")
```

## What the markdown file looks like

Check out the `/converted/` directory in the root of this repository for 2 examples.
