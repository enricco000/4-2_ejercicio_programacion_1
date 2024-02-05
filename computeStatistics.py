"""
This script computes descriptive statistics (mean, median, mode, variance, and standard deviation) 
for a list of numbers provided in a file. It handles invalid data gracefully, calculates statistics 
using basic algorithms, and reports both the results and the execution time.
"""

import argparse
import time

def compute_mean(data):
    """Calculate and return the mean of the data."""
    return sum(data) / len(data) if data else 0

def compute_median(data):
    """Calculate and return the median of the data."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    midpoint = n // 2
    if n % 2 == 0:
        return (sorted_data[midpoint - 1] + sorted_data[midpoint]) / 2
    else:
        return sorted_data[midpoint]

def compute_mode(data):
    """Calculate and return the mode of the data."""
    frequency = {}
    for number in data:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values(), default=0)
    modes = [key for key, val in frequency.items() if val == max_frequency]
    return modes[0] if len(modes) == 1 else '#N/A'

def compute_variance(data, mean):
    """Calculate and return the variance of the data."""
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1) if len(data) > 1 else 0

def compute_statistics(data):
    """
    Compute and return all descriptive statistics for the data.
    This includes mean, median, mode, variance, and standard deviation.
    """
    mean = compute_mean(data)
    median = compute_median(data)
    mode = compute_mode(data)
    variance = compute_variance(data, mean)
    std_deviation = variance ** 0.5
    return mean, median, mode, variance, std_deviation

def display_and_save_results(results, elapsed_time):
    """
    Display the calculated statistics and elapsed time on the console and save them to a file.
    """
    output = (
        f"Mean: {results[0]}\n"
        f"Median: {results[1]}\n"
        f"Mode: {results[2]}\n"
        f"Variance: {results[3]}\n"
        f"Standard Deviation: {results[4]}\n"
        f"Elapsed Time: {elapsed_time} seconds\n"
    )
    print(output)
    with open('StatisticsResults.txt', 'w', encoding='utf-8') as file:
        file.write(output)

def parse_arguments():
    """
    Parse command-line arguments. Expects a filename as an argument.
    """
    parser = argparse.ArgumentParser(description="Compute Descriptive Statistics from a file.")
    parser.add_argument("filename", help="The file containing the list of numbers.")
    return parser.parse_args()

def main():
    """
    Main function. Parses arguments, reads data, computes statistics, and handles errors.
    """
    args = parse_arguments()
    start_time = time.time()
    try:
        with open(args.filename, 'r', encoding='utf-8') as file:
            data = [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
    except FileNotFoundError:
        print(f"Error: The file {args.filename} does not exist.")
        return
    except ValueError as e:
        print(f"Error: An error occurred while processing the file: {e}")
        return
    
    results = compute_statistics(data)
    elapsed_time = time.time() - start_time
    display_and_save_results(results, elapsed_time)

if __name__ == "__main__":
    main()
