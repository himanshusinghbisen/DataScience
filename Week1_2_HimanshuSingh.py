#%% md
# ### Data Preperation
# ### Week 1 and 2
# ### Submitter - Himanshu Singh
# ### What is Data Wrangling?
#%% md
# Create a Jupyter notebook where you create a list, iterate over the list and sort your results, generate random numbers, add to the list, and then print your results.
# 
# 
#%% md
# Initializing a List and Generating Random Numbers
#%%
import random

# Initialize an empty list
my_list = []

# Generate and add 5 random numbers to the list
print("Adding random numbers to the list...")
for i in range(5):
    random_number = random.randint(1, 100)
    my_list.append(random_number)
    print(f"Added: {random_number}")

print("\nOriginal list:")
print(my_list)
#%% md
# Sorting the List
#%%
# Sort the list in ascending order
print("Sorting the list...")
my_list.sort()

print("\nSorted list (ascending):")
print(my_list)
#%% md
# Iterating Over the Sorted List and Printing
#%%
# Iterate through the sorted list and print each element
print("Iterating over the sorted list:")
for number in my_list:
    print(number)
#%%
# Add More Numbers to the List
print ("Do you want to add more numbers? Press 'N/n' at anytime to stop")
# Initialize a variable to control the loop
run_loop = True

while run_loop:
    # Ask the user for input
    user_input = input("Enter 'n' to stop the entering the numbers: ")

    # Check the user's input and exit if it's 'n'
    if user_input.lower() == 'n':
        run_loop = False # This will cause the loop condition to be False
        print("You entered 'n'. Exiting the loop.")
    elif user_input.isnumeric():
        my_list.append(int(user_input))
    else:
        print("Invalid entry")

print("Loop has been terminated.")

# Iterate through the list and print each number
print("Iterating over the list:")
for number in my_list:
    print(number)


#%% md
# Create a line chart with Matplotlib and the following data file.
# 
# 
# 
#      a. Data file: world-population.xlsm
# 
#      b. (Hint: Python for Data Analysis 2nd Edition: Page 19-50, Python for Data Analysis 3rd Edition: Page 281)
#%%
import pandas as pd

# Define the path to your .xlsm file
file_path = 'world-population.xlsm'

# Load the data into a pandas DataFrame
try:
    df = pd.read_excel(file_path)
    print("Data loaded successfully!")
    print(df.head()) # Print the first 5 rows of the DataFrame
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create the line chart from the DataFrame
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Population'], marker='o', linestyle='-', color='b')

# Add labels and a title
plt.title('Line Chart from a Pandas DataFrame')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a grid for readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Save the plot
plt.savefig('df_line_chart.png')
#%% md
# Activity 1.01: Handling Lists
# 			In this activity, you will generate a list of random numbers and then generate another list from the first one, which only contains numbers that are divisible by three. Repeat the experiment 10 times; you'll see that the output varies each time, given that a different set of random numbers will be generated each time. Then, you will calculate the average difference between the lengths of the two lists.
# 			These are the steps for completing this activity:
# 
# 				Create a list of 100 random numbers.
# 				Create a new list from this random list, with numbers that are divisible by 3.
# 				Calculate the length of these two lists and store the difference in a new variable.
# 				Using a loop, perform steps 1, 2, and 3, and find the difference variable 10 times.
# 				Find the arithmetic mean of these 10 difference values.
#%%


import statistics
# counter for running the loop 10 times
icount =0

# List to store the difference of length
difference_of_len=[]
# running the loop 10 times
while icount < 10:
    icount += 1
    # Getting the random list of numbers
    random_numbers = [random.randint(1, 1000) for _ in range(100)]
    # Getting the subset of divisible by 3 from the list
    divisible_by_3_list = [num for num in random_numbers if num % 3 == 0]
    # Calculating the length of difference of the list
    difference= len(random_numbers)-len(divisible_by_3_list)
    # print(difference)
    # adding the difference of list in the new list
    difference_of_len.append(difference)

# calculating the mean of of the difference of the length
statistics.mean(difference_of_len)


#%% md
# Activity 1.02: Analyzing a Multiline String and Generating the Unique Word Count
# 			In this activity, you will do the following:
# 
# 				Get multiline text and save it in a Python variable.
# 				Get rid of all new lines in it using string methods.
# 				Get all the unique words and their occurrences from the string.
# 				Repeat the steps to find all unique words and occurrences, without considering case sensitivity.
#%%
# Storing a multiline input in a variable in a way that NEWLINE is also captured in the input

print("Enter your text (type 'END' on a new line to finish):")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

multiline_text = "\n".join(lines)
print(multiline_text)

#%%

# Getting length of the text
print(len(multiline_text))
multiline_text = multiline_text.replace('\n', "")


#%%
import re
from collections import Counter

# Convert the entire text to lowercase to handle case insensitivity.
# The findall() method with regex pattern r'\b\w+\b' finds all "word boundaries" and extracts the words, ignoring punctuation.
words = re.findall(r'\b\w+\b', multiline_text.lower())

# Use collections.Counter to efficiently count the occurrences of each word.
word_counts = Counter(words)

word_counts
#%% md
# In this activity, we will be using permutations to generate all possible three-digit numbers that can be generated using 0, 1, and 2. A permutation is a mathematical way to represent all possible outcomes. Then, we'll loop over this iterator and also use isinstance and assert to make sure that the return types are tuples. Use a single line of code involving dropwhile and lambda expressions to convert all the tuples to lists while dropping any leading zeros (for example, (0, 1, 2) becomes [1, 2]). Finally, we will write a function that takes a list like before and returns the actual number contained in it.
#%%
import itertools
from itertools import dropwhile

# Declaring the digits which combination needs to be created
digits = [0, 1, 2]
all_permutations = itertools.permutations(digits, 3)
final_numbers = []
for perm in all_permutations:
        #Using isinstance and assert to verify that the return types are tuples.
        assert isinstance(perm, tuple)

        # Using dropwhile and lambda expressions to convert all the tuples to lists while dropping any leading zeros.
        # dropwhile continues to drop elements as long as the lambda condition is true.
        # list() then converts the dropwhile iterator to a list.
        list_without_leading_zeros = list(dropwhile(lambda x: x == 0, perm))

        # If the list is empty after dropping zeros (e.g., all zeros),
        # add a single zero to represent the number 0.
        if not list_without_leading_zeros:
            list_without_leading_zeros = [0]

        # Converts a list of digits into a single integer number. For example, [1, 2, 0] becomes 120.
        final_number = int("".join(map(str, list_without_leading_zeros)))
        final_numbers.append(final_number)

print(f"\nAll generated numbers: {final_numbers}")


#%% md
# Activity 2.02: Designing Your Own CSV Parser
# 			A CSV file is something you will encounter a lot in your life as a data practitioner. A CSV file is a comma-separated file where data from a tabular format is generally stored and separated using commas, although other characters can also be used,such as tab or *. Here's an example CSV file:
# 
#             Figure 2.12: Partial output of a CSV file
# 			In this activity, we will be tasked with building our own CSV reader and parser. Although it is a big task if we try to cover all use cases and edge cases, along with escape characters, for the sake of this short activity, we will keep our requirements small. We will assume that there is no escape character—meaning that if you use a comma at any place in your row, you are starting a new column. We will also assume that the only function we are interested in is to be able to read a CSV file line by line, where each read will generate a new dictionary with the column names as keys and row names as values.
#%%
import csv

def parse_csv_data(data):

    if not data:
        return

    header = data[0]

    # Process the remaining lists as data rows. Taken only first few rows to process.
    # In order to process complete file remove 5
    for row_values in data[1:5]:
        # Create a dictionary for the current row using the header as keys
        # The zip() function pairs the header keys with the row values
        row_dict = dict(zip(header, row_values))

        # Use yield to return the dictionary, allowing for line-by-line processing
        yield row_dict


if __name__ == "__main__":
    try:
        # open the downloaded .csv file
        with open('sales_record.csv', 'r') as file:

            # To confirm the file is open, you can print a message.
            print("File 'sales_record.csv' has been opened successfully.")

            # Use csv.reader to parse the data
            csv_reader = csv.reader(file)

            # Convert the reader object to a list to store all data in a variable
            csv_data = list(csv_reader)

            #print(csv_data)

    except FileNotFoundError:
        print("Error: The file 'sales_record.csv' was not found in the directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Parsing CSV data and printing each row as a dictionary:")
    print("-" * 50)

    # Iterate through the generator created by the parse_csv_data function
    for row in parse_csv_data(csv_data):
        print(row)

#%%

#%%
