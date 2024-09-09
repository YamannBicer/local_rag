# query_best_matches.py
import pandas as pd
import difflib

# Load the DataFrame from the CSV file
df = pd.read_csv('db_metadata/entsoe.csv')

# Function to find the closest matches and return the rows
def find_closest_matches(df, user_input):
    closest_matches = difflib.get_close_matches(user_input, df['name'], n=5, cutoff=0.0)
    if closest_matches:
        return df[df['name'].isin(closest_matches)]
    else:
        return "No match found"

# Function to handle the query and return the best matches
def query_best_matches(query_text):
    matches = find_closest_matches(df, query_text)
    if isinstance(matches, str):
        return matches, []
    else:
        return matches['name'].tolist(), matches

if __name__ == "__main__":
    query_text = input("Enter a table name or data name: ")
    best_matches, _ = query_best_matches(query_text)
    print("Best matches:", best_matches)