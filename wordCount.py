"""
wordCount.py: Counts the frequency of each distinct word in a file.

This script reads words from a specified file, counting the frequency of each distinct word using
basic algorithms without relying on specialized libraries or functions. It handles invalid data,
continuing execution without interruption. The results, including the count of each
distinct word and the elapsed time for processing, are printed to the console and saved in
WordCountResults.txt. The script can process files containing hundreds to thousands of words and
is compliant with PEP8 guidelines.

Usage:
    python wordCount.py fileWithData.txt
"""

import argparse
import time

def parse_arguments():
    """Parse command-line arguments for the file name."""
    parser = argparse.ArgumentParser(description="Count word frequencies in a file.")
    parser.add_argument("filename", help="The file containing the words.")
    return parser.parse_args()

def count_words(filename):
    """Read the file and count the frequency of each distinct word."""
    word_count = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    if word.isalpha():  # Consider a word valid if it's purely alphabetical
                        word = word.lower()  # Case-insensitive counting
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
                    else:
                        print(f"Invalid data encountered and skipped: {word}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except UnicodeDecodeError:
        print(f"Error: The file '{filename}' contains characters that this script cannot decode.")
    except IOError as ioerror:
        print(f"Error: An IO error occurred while processing the file '{filename}': {ioerror}")
    return word_count


def display_and_save_results(word_count, elapsed_time):
    """Display and save the word counts and elapsed time."""
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)  # Sort by frequency
    output_lines = ["WORD | FREQ"]
    for word, frequency in sorted_words:
        output_lines.append(f"{word} | {frequency}")
    output_lines.append(f"Elapsed Time: {elapsed_time} seconds")

    output_str = "\n".join(output_lines)
    print(output_str)

    with open('WordCountResults.txt', 'w', encoding='utf-8') as file:
        file.write(output_str)

def main():
    """Main function to orchestrate argument parsing, word counting, and result presentation."""
    args = parse_arguments()
    start_time = time.time()
    word_count = count_words(args.filename)
    elapsed_time = time.time() - start_time
    display_and_save_results(word_count, elapsed_time)

if __name__ == "__main__":
    main()
