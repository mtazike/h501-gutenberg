from .data import load_gutenberg_data, clean_author_data


def list_authors(by_languages=True, alias=True):
    """
    List Project Gutenberg authors with their aliases, ordered by alias count.
    
    Parameters:
    -----------
    by_languages : bool, default True
        If True, orders authors by number of aliases (proxy for translations)
    alias : bool, default True  
        If True, returns author aliases; if False, returns author names
        
    Returns:
    --------
    list
        List of author aliases (or names) ordered by alias count (descending)
    """
    # Load and clean data using functions from data module
    df = load_gutenberg_data()
    df = clean_author_data(df)
    
    if by_languages:
        # Count number of aliases per author (proxy for popularity/translations)
        author_counts = df.groupby('author').size().sort_values(ascending=False)
        
        # Get the authors in order of alias count
        ordered_authors = author_counts.index.tolist()
        
        if alias:
            # For each author, get their first alias
            result = []
            for author in ordered_authors:
                author_data = df[df['author'] == author]
                # Get the first alias for this author
                author_alias = author_data['alias'].iloc[0]
                result.append(author_alias)
            return result
        else:
            return ordered_authors
    
    else:
        # If by_languages=False, just return all unique authors/aliases
        if alias:
            return df['alias'].dropna().unique().tolist()
        else:
            return df['author'].unique().tolist()