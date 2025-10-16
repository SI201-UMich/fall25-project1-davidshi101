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
    mean_body_mass_by_sex = penguin_data.groupby('sex')['body_mass_g'].mean().to_dict()
    return mean_body_mass_by_sex

def generate_report(mean_bill_lengths_by_species, correlation, mean_flipper_lengths_by_sex, max_body_mass_per_island, mean_body_mass_by_sex, mean_body_mass_by_species):
    print("Penguin Data Analysis Report")
    print("===================================")
    print("\nMean Bill Length by Species:")
    for species, mean_bill in mean_bill_lengths_by_species.items():
        print(f"{species}: {mean_bill} mm")

    print("\nCorrelation between Bill Length and Bill Depth:", correlation)

    print("\nMean Flipper Length by Sex:")
    for sex, mean_flipper in mean_flipper_lengths_by_sex.items():
        print(f"{sex}: {mean_flipper} mm")

    print("\nMaximum Body Mass per Island:")
    for island, max_mass in max_body_mass_per_island.items():
        print(f"{island}: {max_mass} g")

    print("\nMean Body Mass by Sex:")
    for sex, mean_mass in mean_body_mass_by_sex.items():
        print(f"{sex}: {mean_mass} g")

    print("\nMean Body Mass by Species:")
    for species, mean_mass in mean_body_mass_by_species.items():
        print(f"{species}: {mean_mass} g")
    print("\n===================================")

def main():
    csv_file = 'penguins.csv'
    penguin_data = load_data(csv_file)

    mean_body_mass_by_sex = calculate_mean_body_mass_by_sex(penguin_data)
    mean_body_mass_by_species = calculate_mean_body_mass_by_species(penguin_data)
    mean_bill_lengths_by_species = calculate_mean_bill_length_by_species(penguin_data)
    correlation = calculate_correlation_bill_length_and_depth(penguin_data)
    mean_flipper_lengths_by_sex = calculate_mean_flipper_length_by_sex(penguin_data)
    max_body_mass_per_island = calculate_max_body_mass_per_island(penguin_data)

    generate_report(mean_bill_lengths_by_species, correlation, mean_flipper_lengths_by_sex, max_body_mass_per_island, mean_body_mass_by_sex, mean_body_mass_by_species)

if __name__ == '__main__':
    main()