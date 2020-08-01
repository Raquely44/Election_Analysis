import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # pring each row in the CSV file.
    headers = next(file_reader)
    print(headers)

# 1. Find to total number of votes cast
# 2. List all the candidates that received a vote
# 3. Find the total numbe of votes each candidate received 
# 4. Find the percentage of votes each candidate won
# 5. Find the winner of of the election based on the popular vote

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

#close the file unless the above is updated to the with funtion
# outfile.close()

# PRACTICING
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    #write some data to the file.
    txt_file.write("Counties in the Election\n------------\n")
    # write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")

#close the file
# outfile.close()