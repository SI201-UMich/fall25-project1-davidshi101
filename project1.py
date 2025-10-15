import pandas as pd

def load_data(csv_file):
    penguin_data = pd.read_csv(csv_file)
    return penguin_data