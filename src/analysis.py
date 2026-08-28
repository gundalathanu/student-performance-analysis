import pandas as pd

# Load the dataset
data = pd.read_csv("data/students.csv")

print("Original Data:")
print(data)

# 1. Handle missing values
data["Attendance"] = data["Attendance"].fillna(data["Attendance"].mean())

# 2. Remove duplicate rows
data = data.drop_duplicates()

# 3. Categorical encoding
data["Gender"] = data["Gender"].map({
    "Male": 0,
    "Female": 1
})

print("\nAfter Preprocessing:")
print(data)

print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate rows:")
print(data.duplicated().sum())

# Save processed data
data.to_csv("data/processed_students.csv", index=False)
print("\nPreprocessing completed successfully.")