import pandas as pd
import numpy as np
file_path = "wine.csv"
import os

# Task 1: Operations on a 1D array
array_1d = np.random.randint(1, 100, 10)  # Создание массива из 10 случайных целых чисел
mean = np.mean(array_1d)  # Cередне значение
median = np.median(array_1d)  # Медіана
std_dev = np.std(array_1d)  # Стандартне відхилення
array_even_replaced = np.where(array_1d % 2 == 0, 0, array_1d)  # Замена всех четных чисел на 0

print("Task 1:")
print("Original Array:", array_1d)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Array with evens replaced by 0:", array_even_replaced)

# Task 2: Indexing and slicing in a 2D array
matrix_2d = np.random.randint(1, 100, (3, 3))  # Создание 2D массива размером 3x3
first_row = matrix_2d[0, :]  # Перший ряд
last_column = matrix_2d[:, -1]  # Останній столбец
diagonal_elements = np.diag(matrix_2d)  # Диагональные элементы

print("\nTask 2:")
print("2D Matrix:\n", matrix_2d)
print("First Row:", first_row)
print("Last Column:", last_column)
print("Diagonal Elements:", diagonal_elements)

# Task 3: Broadcasting
matrix_2d_broadcast = np.random.randint(1, 10, (3, 3))  # 2D масив 3x3
array_1d_broadcast = np.random.randint(1, 10, 3)  # 1D масив 3
broadcast_result = matrix_2d_broadcast + array_1d_broadcast  # Broadcasting

print("\nTask 3:")
print("2D Matrix for Broadcasting:\n", matrix_2d_broadcast)
print("1D Array for Broadcasting:", array_1d_broadcast)
print("Broadcast Result:\n", broadcast_result)

# Task 4: Unique elements and row sums
matrix_5x5 = np.random.randint(1, 50, (5, 5))  # 2D массив 5x5
unique_elements = np.unique(matrix_5x5)  # Уникальные элементы
threshold = 100  # Пороговое значение для суммы
rows_above_threshold = matrix_5x5[np.sum(matrix_5x5, axis=1) > threshold]  # Ряды с суммой больше порога

print("\nTask 4:")
print("5x5 Matrix:\n", matrix_5x5)
print("Unique Elements:", unique_elements)
print("Rows with sum above threshold:", rows_above_threshold)

# Task 5: Reshaping a 1D array into 2D
array_1d_reshaped = np.arange(1, 21)  # 1D массив от 1 до 20
reshaped_2d = array_1d_reshaped.reshape(4, 5)  # Преобразование в 2D массив 4x5

print("\nTask 5:")
print("Original 1D Array:", array_1d_reshaped)
print("Reshaped 2D Array:\n", reshaped_2d)

# ----------------------------------------------
file_path = "wine.csv"
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    print(f"File found: {file_path}")

#  Створіть DataFrame Pandas із щонайменше 5 рядками та 3 стовпцями. Стовпці можуть представляти різні атрибути (наприклад, Ім'я, Вік, Місто).
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 22],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}
df = pd.DataFrame(data)

# Добавляем новый столбец с числовыми значениями
df["Score"] = [85, 92, 88, 79, 95]

# Встановлюємо поріг и фільтруем строки, де "Score" більше порога
threshold = 90
filtered_df = df[df["Score"] > threshold]

print("Part 1: Original DataFrame:")
print(df)
print("\nFiltered DataFrame (Score > 90):")
print(filtered_df)

#  Робота с даними wine.csv
file_path = "wine.csv"  # Замените на полный путь, если нужно

try:
    dataset = pd.read_csv(file_path)

    # перевірка, чи потрідно змінити назву стовпця
    if len(dataset.columns) == 14:  # Если в файле уже 14 столбцов
        column_names = [
            "Class", "Alcohol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium",
            "Total_Phenols", "Flavanoids", "Nonflavanoid_Phenols", "Proanthocyanins",
            "Color_Intensity", "Hue", "OD280_OD315", "Proline"
        ]
        dataset.columns = column_names
    else:
        print("Dataset columns do not match expected structure. Proceeding without renaming.")

    # вивід данних 5 перших строк
    print("\nPart 2: First 5 rows of the dataset:")
    print(dataset.head())

    # вивід статистики
    print("\nSummary statistics for numerical columns:")
    print(dataset.describe())

    # Пошук і вивід в категориальном столбце "Class"
    if "Class" in dataset.columns:
        unique_classes = dataset["Class"].unique()
        print("\nUnique values in the column 'Class':")
        print(unique_classes)
    else:
        print("\nColumn 'Class' not found in the dataset.")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty or cannot be read.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")