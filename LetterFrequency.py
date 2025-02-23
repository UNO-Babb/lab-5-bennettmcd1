#LetterFrequency.py
#Name:
#Date:
#Assignment:

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os
import csv

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # The alphabet to map letter frequencies
    message = message.upper()  # Convert the message to uppercase to ignore case

    # Initialize frequency array for each letter (A-Z), 26 letters total.
    freq = [0] * 26  # This will count occurrences of each letter from A to Z

    # Loop through each letter in the message
    for letter in message:
        if letter.isalpha():  # Only count alphabetic characters (skip punctuation/numbers)
            index = alpha.find(letter)  # Find the letter's position in the alphabet (0 = A, 1 = B, etc.)
            freq[index] += 1  # Increase the count at the position for that letter

    # Prepare the output in CSV format (letter, frequency)
    output = []
    for i in range(26):
        line = [alpha[i], freq[i]]  # Create a row with letter and its frequency
        output.append(line)  # Add it to the output list

    writeToFile(output)  # Call the function to write the data to a file

def writeToFile(data):
    # Determine the current directory of the script to save the file correctly
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    # Open (or create) a CSV file to write the frequencies
    with open('letter_frequency.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Letter", "Frequency"])  # Write the header row
        writer.writerows(data)  # Write the data rows

    print("Frequency data saved to 'letter_frequency.csv'")

def main():
    msg = input("Enter a message: ")  # Prompt the user to enter a message
    countLetters(msg)  # Call the function to count letter frequencies

if __name__ == '__main__':
    main()  # Run the main function when the script is executed