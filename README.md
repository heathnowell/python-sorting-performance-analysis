# Python Sorting Performance Analysis

A Python science fair project comparing the runtime of three different approaches for sorting a dataset of 950 high-grossing movies by gross income.

I originally built this project to explore how the choice of Python libraries and implementation approach can affect execution time for a small dataset.

## Project Overview

The experiment compares three implementations:

1. **pandas** using `DataFrame.sort_values()`
2. Python's built-in **csv/list sorting** using `list.sort()` and `operator.itemgetter()`
3. **natsort** using `natsorted()`

Each program:

- Reads the same CSV dataset
- Sorts the movies by `Gross (In Millions)` from highest to lowest
- Writes the sorted data to a new CSV file
- Measures and prints total execution time

## Original Experiment

The original science fair experiment used a dataset containing the top 950 highest-grossing movies and ran each implementation three times.

Original average runtimes recorded in the project:

| Approach | Average Runtime |
| --- | ---: |
| pandas | 0.0480766295 s |
| Built-in csv/list sorting | 0.016045014 s |
| natsort | 0.046794335 s |

On the machine and dataset used for the original experiment, the built-in approach produced the lowest measured runtime.

These measurements include file I/O and were collected on one computer, so they should be treated as the results of the original learning experiment rather than a general-purpose benchmark.

## Repository Structure

```text
python-sorting-performance-analysis/
├── pandas_sort.py
├── builtin_sort.py
├── natsort_sort.py
├── Highest_Grossing_Movies.csv
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3
- pandas
- natsort

Install the third-party dependencies with:

```bash
pip install -r requirements.txt
```

## Running the Programs

Run each implementation separately from the repository folder.

### pandas

```bash
python pandas_sort.py
```

Creates:

```text
sorted_pandas.csv
```

### Built-in Python libraries

```bash
python builtin_sort.py
```

Creates:

```text
sorted_builtin.csv
```

### natsort

```bash
python natsort_sort.py
```

Creates:

```text
sorted_natsort.csv
```

Each script prints the total runtime after it finishes.

## What I Learned

This project helped me practice:

- Reading and writing CSV data
- Sorting structured datasets
- Comparing multiple implementation approaches
- Measuring program runtime
- Working with third-party Python libraries
- Collecting repeated experimental results
- Analyzing and documenting performance differences

## Notes on Benchmarking

This was an early programming and science fair project. A stronger future benchmark could improve the methodology by:

- Separating file I/O time from sorting time
- Running many more trials
- Using `timeit` or `time.perf_counter()` consistently
- Testing multiple dataset sizes
- Controlling background processes and hardware conditions
- Comparing the scaling behavior of each approach

## Background

This project was originally completed as a science fair experiment while I was learning Python. The goal was to investigate whether different coding approaches and libraries noticeably changed runtime when sorting a relatively small dataset.
