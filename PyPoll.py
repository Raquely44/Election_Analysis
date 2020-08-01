import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter - variable
total_votes = 0
# Candidates option and candidate votes - list
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Winning candidate, vote count, and percentage
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the first row as
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
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

#save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal.
    election_results= (
        f'\nElection Results\n'
        f'-----------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-----------------------\n')
    print(election_results, end= "")
    # save the final vote count to the text file.
    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for  candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")
        
        #print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        #save the candidate results to our text file
        txt_file.write(candidate_results)

        #determing winning vote count and candidate
        #determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning percentage = voter_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # and, set the winning_candidate equal to the candidates name
            winning_candidate = candidate_name
    # print the winning candidate's results to the terminal.
    winning_candidate_summary =(
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)
    #save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)