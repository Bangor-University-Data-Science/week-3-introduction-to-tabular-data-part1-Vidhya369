import pandas as pd
def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
           
            if df[column].nunique() > 10:  # More than 10 unique values
                feature_types['numerical']['continuous'].append(column)
            else:
                feature_types['numerical']['discrete'].append(column)
        elif pd.api.types.is_object_dtype(df[column]):
            
            feature_types['categorical']['nominal'].append(column)
    return feature_types
