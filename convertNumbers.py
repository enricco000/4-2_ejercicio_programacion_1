"""
convertNumbers.py: Converts numbers from a file to their binary and hexadecimal representations.

This script reads numbers from a specified file, converts each number to binary and hexadecimal
using basic algorithms (without relying on built-in conversion functions), and handles invalid data.
It prints the conversion results to the console and saves them in ConversionResults.txt,
including the elapsed time for processing. The script is designed to process files with hundreds to
thousands of numbers and is compliant with PEP8 guidelines.

Usage:
    python convertNumbers.py fileWithData.txt
"""

import argparse
import time

def parse_arguments():
    """Parse command-line arguments for the file name."""
    parser = argparse.ArgumentParser(description="Convert numbers to binary and hexadecimal.")
    parser.add_argument("filename", help="The file containing the list of numbers.")
    return parser.parse_args()

def to_binary(number):
    """Convert a decimal number to binary using a basic algorithm."""
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary or '0'

def to_hexadecimal(number):
    """Convert a decimal number to hexadecimal using a basic algorithm."""
    hex_chars = '0123456789ABCDEF'
    hexadecimal = ''
    while number > 0:
        hexadecimal = hex_chars[number % 16] + hexadecimal
        number = number // 16
    return hexadecimal or '0'

def process_file(filename):
    """Read and convert numbers from the file, handling invalid data."""
    start_time = time.time()
    results = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line.isdigit():
                number = int(stripped_line)
                binary = to_binary(number)
                hexadecimal = to_hexadecimal(number)
                results.append((number, binary, hexadecimal))
            else:
                print(f"Invalid data encountered and skipped: {stripped_line}")

    elapsed_time = time.time() - start_time
    return results, elapsed_time

def display_and_save_results(results, elapsed_time):
    """Display and save the conversion results, including the elapsed time."""
    output_lines = ["NUM | BIN | HEX"]
    for number, binary, hexadecimal in results:
        output_lines.append(f"{number} | {binary} | {hexadecimal}")
    output_lines.append(f"Elapsed Time: {elapsed_time} seconds")

    output_str = "\n".join(output_lines)
    print(output_str)
    
    with open('ConversionResults.txt', 'w', encoding='utf-8') as file:
        file.write(output_str)

def main():
    """Main function to orchestrate argument parsing, file processing, and result presentation."""
    args = parse_arguments()
    results, elapsed_time = process_file(args.filename)
    display_and_save_results(results, elapsed_time)

if __name__ == "__main__":
    main()
