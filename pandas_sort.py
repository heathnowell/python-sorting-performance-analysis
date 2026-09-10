from pathlib import Path
from time import perf_counter

import pandas as pd


INPUT_FILE = Path(__file__).with_name("Highest_Grossing_Movies.csv")
OUTPUT_FILE = Path(__file__).with_name("sorted_pandas.csv")
SORT_COLUMN = "Gross (In Millions)"


def main():
    start_time = perf_counter()

    data_frame = pd.read_csv(INPUT_FILE)
    data_frame[SORT_COLUMN] = pd.to_numeric(
        data_frame[SORT_COLUMN], errors="raise"
    )
    data_frame.sort_values(
        SORT_COLUMN,
        ascending=False,
        inplace=True,
    )
    data_frame.to_csv(OUTPUT_FILE, index=False)

    elapsed = perf_counter() - start_time
    print(f"Program took {elapsed:.10f} seconds to run")


if __name__ == "__main__":
    main()
