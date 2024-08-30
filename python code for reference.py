import pandas as pd
from collections import Counter
import re


#creating a function that iterates through a csv and standardizes the names from multiple variations.
# example: takes everything in a column that has "slack" in it and standardizes it to just "slack"
# app_mapping = {'slack': 'slack'}  
def standardize_app_names( app_name, mapping ):
    app_name = app_name.strip().lower()  # Trim spaces and convert to lowercase
    for standard_name, pattern in mapping.items():
        if pattern in app_name:  # Direct string comparison
            return standard_name
    return app_name

# specific function to look for specific items
def standardize_salesforce( app_name ):
    if isinstance( app_name, str ):  # Ensure the value is a string
        app_name = app_name.strip().lower()  # Trim spaces and convert to lowercase
        if any(excluded in app_name for excluded in ['relias', 'rippling', 'documentforce']):
            return app_name  # Return original name if it contains excluded terms
        if 'force' in app_name or 'salesforce' in app_name:  # General pattern matching for Salesforce
            return 'salesforce'
    return app_name  # Return the original value if it's not a string or doesn't match

#creating a function to clean up activity subtypes
def assign_activity_subtype( df, application_name, subtype_name ):
    df.loc[df['application'] == application_name, 'activity_subtype'] = subtype_name

#creating a function to clean up activity types
def assign_activity_type( df, application_name, type_name ):
    df.loc[df['application'] == application_name, 'activity_type'] = type_name

#creating a function to be able to iterate through unique value counts on 'activity_type'
def get_activity_counts( df, activity_type ):
    activity_counts = df[df['activity_type'] == activity_type].groupby(['application', 'activity_subtype']).size().reset_index(name='counts')
    return activity_counts

# Creating a function to iterate through unique value counts on 'activity_subtype'
def get_subtype_counts(df, activity_subtype):
    subtype_counts = df[df['activity_subtype'] == activity_subtype].groupby(['application', 'activity_type']).size().reset_index(name='counts')
    return subtype_counts

#looking for most common words in a column to find trends and key items to focus on
def most_common_words_in_activity_type( df, activity_type, column_name, top_n=10 ):
    # Filter the DataFrame for rows where activity_type matches the specified type
    filtered_df = df[df['activity_type'] == activity_type]
    
    # Combine all the text in the specified column into a single string
    text = ' '.join( filtered_df[column_name].dropna().astype(str).tolist() )
    
    # Tokenize the text, removing non-alphanumeric characters
    words = re.findall( r'\b\w+\b', text.lower() )
    
    # Count the frequency of each word
    word_counts = Counter( words )
    
    # Return the top N most common words
    return word_counts.most_common( top_n )

#looks for the ending of applications and changes the subtype:
def assign_subtype_for_webpage( df, ending, subtype_name ):
    df.loc[df['application'].str.endswith( ending ), 'activity_subtype'] = subtype_name


