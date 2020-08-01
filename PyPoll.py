import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter - variable
total_votes = 0
# Candidates option and candidate votes - list
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # pring each row in the CSV file.
    headers = next(file_reader)

    # print each row in the csv file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # print the candidates name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1

#Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list
    for  candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.") 
        # votes to the terminal

        #determing winning vote count and candidate
        #determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning percentage = voter_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # and, set the winning_candidate equal to the candidates name
            winning_candidate = candidate_name
        # to do: print out the winning candidate, vote count and percentage to terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary =(
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)

   
# 1. Find to total number of votes cast
# 2. List all the candidates that received a vote
# 3. Find the total numbe of votes each candidate received 
# 4. Find the percentage of votes each candidate won
# 5. Find the winner of of the election based on the popular vote

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

#close the file unless the above is updated to the with funtion
# outfile.close()

# PRACTICING
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:
    #write some data to the file.
    #txt_file.write("Counties in the Election\n------------\n")
    # write three counties to the file
    #txt_file.write("Arapahoe\nDenver\nJefferson")

#close the file
# outfile.close()