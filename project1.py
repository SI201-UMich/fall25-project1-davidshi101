# Name: David Shin 
# Student ID: 7303 1645
# Email: davidshi@umich.edu
# Who or what you worked with on this project (including generative AI like ChatGPT): 
# If you worked with generative AI also add a statement for how you used it.  
# Asked ChatGPT hints for errors and suggesting general sturcture of the code

import pandas as pd

def load_data(csv_file):
    penguin_data = pd.read_csv(csv_file)
    if penguin_data is None:
        print("Error: CSV file not loaded properly.")
    else:
        print("CSV file loaded successfully.")
    return penguin_data
csv_file = 'penguins.csv'
penguin_data = load_data(csv_file)
print(penguin_data.head())

def calculate_mean_body_mass_by_sex(penguin_data):
    cleaned = penguin_data.dropna(subset=["sex", "island", "body_mass_g"])
    grouped = cleaned.groupby(["sex", "island"])["body_mass_g"]
    mean_by_sex = grouped.mean().to_dict()
    return mean_by_sex

def calculate_mean_flipper_length_by_species_year(penguin_data):
    cleaned = penguin_data.dropna(subset=["species", "year", "flipper_length_mm"])
    grouped = cleaned.groupby(["species", "year"])["flipper_length_mm"]
    mean_by_species_year = grouped.mean().to_dict()
    return mean_by_species_year

def generate_report(mean_body_mass_by_sex, mean_flipper_length_by_species_year):
    print("Penguin Data Analysis Report")
    print("===================================")
    print("\nMean Body Mass by Sex (with Island):")
    for key, mean_mass in mean_body_mass_by_sex.items():
        sex, island = key
        print(sex, "on", island, ":", mean_mass, "g")
    print("\nMean Flipper Length by Species (split by Year):")
    for key, mean_flipper in mean_flipper_length_by_species_year.items():
        species, year = key
        print(species, "in", year, ":", mean_flipper, "mm")
    print("\n===================================")

def main():
    csv_file = 'penguins.csv'
    penguin_data = load_data(csv_file)

    mean_body_mass_by_sex = calculate_mean_body_mass_by_sex(penguin_data)
    mean_flipper_length_by_species_year = calculate_mean_flipper_length_by_species_year(penguin_data)

    generate_report(mean_body_mass_by_sex, mean_flipper_length_by_species_year)

if __name__ == '__main__':
    main()