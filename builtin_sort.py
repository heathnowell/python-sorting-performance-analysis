import csv
import operator
from pathlib import Path
from time import perf_counter


INPUT_FILE = Path(__file__).with_name("Highest_Grossing_Movies.csv")
OUTPUT_FILE = Path(__file__).with_name("sorted_builtin.csv")
GROSS_COLUMN_INDEX = 5


def main():
    start_time = perf_counter()

    with INPUT_FILE.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        rows = list(reader)

    header = rows.pop(0)

    for row in rows:
        row[GROSS_COLUMN_INDEX] = float(row[GROSS_COLUMN_INDEX])

    rows.sort(
        key=operator.itemgetter(GROSS_COLUMN_INDEX),
        reverse=True,
    )

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    elapsed = perf_counter() - start_time
    print(f"Program took {elapsed:.10f} seconds to run")


if __name__ == "__main__":
    main()
