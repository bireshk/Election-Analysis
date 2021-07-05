
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []

# County Options
county_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Declare the empty dictionary.
county_votes = {}


# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Winning County and Winning County Tracker
winning_county_name = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load, "r") as election_data:

    # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # Print the header row.
     headers = next(file_reader)
     #print(headers)
     # Print each row in the CSV file.
     for row in file_reader:
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        # Print the candidate name from each row.
        county_name = row[1]

        # If the county name does not match any existing county...
        if county_name not in county_options:
            # Add it to the list of counties.
            county_options.append(county_name)
            # Begin tracking that county's vote count.
            county_votes[county_name] = 0
        # Add a vote to that candidate's count.
        county_votes[county_name] += 1





        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the county list.
    for county_name in county_votes:
        # Retrieve vote count of a county.
        county_vote_count = county_votes[county_name]
        # Calculate the percentage of votes.
        county_vote_percentage = float(county_vote_count) / float(total_votes) * 100

        # Wrie county results        
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        #  Save the candidate results to our text file.
        print(county_results)
        txt_file.write(county_results)

        # Determine winning vote count based on county
        # Determine if the vote count are greater than the winning county.
        if (county_vote_count > winning_county_count) and (county_vote_percentage > winning_county_percentage):
        
            # If true then set winning_county = county_vote_count and winning_percent =
            # vote_percentage.
            winning_county_count = county_vote_count
            winning_county_percentage = county_vote_percentage
            # Set the winning_county equal to the county's name.
            winning_county_name = county_name
            # Print the winning county name to the terminal.
    write_winning_county_name = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county_name}\n"
        f"-------------------------\n\n")

    print(write_winning_county_name)
    # Save the winning county name to the text file.
    txt_file.write(write_winning_county_name)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Wrie candidate results        
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #  Save the candidate results to our text file.
        print(candidate_results)
        txt_file.write(candidate_results)





        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)