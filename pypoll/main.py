import csv
from collections import Counter
import os

# Get the directory path of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Path to the CSV file containing poll data
file_path = os.path.join(script_dir, "Resources", "election_data.csv")

# Read poll data from CSV file
with open(file_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip header row
    
    # Initialize variables
    total_votes = 0
    votes_per_candidate = Counter()
    
    # Collect votes data
    for row in csv_reader:
        try:
            total_votes += 1
            votes_per_candidate[row[2]] += 1
        except IndexError:
            print("Error: Row doesn't contain expected data.")
            continue

if total_votes == 0:
    print("Error: No votes recorded.")
else:
    # Calculate the percentage of votes each candidate won
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}

    # Determine the winner based on the candidate with the most votes
    winner = max(votes_per_candidate, key=votes_per_candidate.get)

    # Print the analysis results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in votes_per_candidate.items():
        print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    