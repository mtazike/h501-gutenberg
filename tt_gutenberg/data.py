import pandas as pd


def load_gutenberg_data():
    """
    Load the Project Gutenberg authors dataset.
    
    Returns:
    --------
    pandas.DataFrame
        The Gutenberg authors dataset
    """
    url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv'
    return pd.read_csv(url)


def clean_author_data(df):
    """
    Clean the author data by removing rows with missing aliases.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The raw dataset
        
    Returns:
    --------
    pandas.DataFrame
        Cleaned dataset with no missing aliases
    """
    return df.dropna(subset=['alias'])