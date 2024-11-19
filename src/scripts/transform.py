import sys
import pandas as pd


def modify_dataset(input_path, output_path):
    # Читаем входной CSV-файл
    df = pd.read_csv(input_path)
    # Умножаем значения столбца 'weight' на 2
    df["weight"] = df["weight"] * 2
    # Сохраняем обновлённый DataFrame с кавычками
    df.to_csv(output_path, index=False, quoting=1)  # quoting=1 == csv.QUOTE_ALL


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python transform.py <input_path> <output_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    modify_dataset(input_file, output_file)
