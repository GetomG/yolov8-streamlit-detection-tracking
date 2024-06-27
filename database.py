import pandas as pd

def load_waste_types():
    csv_file_path = 'Waste types.csv'
    df_types = pd.read_csv(csv_file_path)
    return df_types
