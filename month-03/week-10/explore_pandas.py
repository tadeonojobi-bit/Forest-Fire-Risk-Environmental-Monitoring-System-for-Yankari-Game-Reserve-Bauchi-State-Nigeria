import pandas as pd

pop = pd.read_csv("Starterdata/raw/ward_population.csv")

print(pop.head())
print("shape:", pop.shape)
print("columns:", list(pop.columns))
print(pop.dtypes)
print(pop["population_2024"].describe())