import os
import csv

# Set the path for the CSV file
election_csv = os.path.join('Desktop', 'Starter_Code', 'PyPoll', 'Resources', 'election_data.csv')

# Initialize variables to track election data
total_num_votes_cast = 0  # Total number of votes cast
candidate_list_options = []  # List of all unique candidates
candidates_vote_total = {}  # Dictionary to hold vote count for each candidate was the best option
Election_winner_candidate = ""  # Picked this to hold the name of the winning candidate
winning_count = 0  # This is to track the highest vote count
percentage_winning_votes = 0  # This is to track the highest vote percentage

# Open and read the CSV file
with open(election_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
     # Skip the header row
    csvheader = next(csvreader) 

    for row in csvreader:
        # need to increase the total vote count by 1 for each row
        total_num_votes_cast += 1
        candidate_name = row[2]

        # If the candidate is not already in the list, add them
        if candidate_name not in candidate_list_options:
            candidate_list_options.append(candidate_name)
             # This will start their vote count
            candidates_vote_total[candidate_name] = 0 

        # Increase the vote count for the candidate by 1
        candidates_vote_total[candidate_name] += 1

# Present the election results in the gitbash/coder
election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_num_votes_cast}\n"
    f"-------------------------\n"
)
print(election_results)

# Will all me to store candidate results
candidate_vote_percentages = []

for candidate_name in candidates_vote_total:
    votes = candidates_vote_total[candidate_name]
    candidate_vote_percentage = (votes / total_num_votes_cast) * 100
    candidate_results = f"{candidate_name}: {candidate_vote_percentage:.1f}% ({votes})\n"
    print(candidate_results)
    
    candidate_vote_percentages.append(candidate_vote_percentage)

    # This will figure out the winning candidate based on highest vote count and percentage
    if (votes > winning_count) and (candidate_vote_percentage > percentage_winning_votes):
        winning_count = votes
        Election_winner_candidate = candidate_name
        percentage_winning_votes = candidate_vote_percentage

# Display the winning candidate's results
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {Election_winner_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {percentage_winning_votes:.1f}%\n"
    f"-------------------------\n"
)
print(winning_candidate_summary)

# Create an output text file to save the results
output_file = os.path.join("election_analysis.txt")
with open(output_file, 'w') as datafile:
    datafile.write("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write(f"Total Votes: {total_num_votes_cast}\n")
    datafile.write("-------------------------\n")
    
    for candidate_name, votes in candidates_vote_total.items():
        percentage = (votes / total_num_votes_cast) * 100
        datafile.write(f"{candidate_name}: {percentage:.1f}% ({votes})\n")

    datafile.write("-------------------------\n")
    datafile.write(f"Winner: {Election_winner_candidate}\n")
    datafile.write(f"Winning Vote Count: {winning_count}\n")
    datafile.write(f"Winning Percentage: {percentage_winning_votes:.1f}%\n")
    datafile.write("-------------------------\n")
