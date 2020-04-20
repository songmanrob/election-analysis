# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis_challenge.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Create a list for the counties
counties = []

# Create a dictionary where the county is the key and the votes cast for each county in the election are the values
votes_by_county = {}

# Create an empty string that will hold the county name that had the largest turnout
largest_turnout = ""

# Declare a variable that represents the number of votes that a county received
county_votes = 0

county_percentage = 0



# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        # Hint: Inside a for loop, add an if statement to check if the county name has already been recorded.
        # If not, add it to the list of county names.
        county_name = row[1]
        if county_name not in counties:
            counties.append(county_name)
            votes_by_county[county_name] = 0
        votes_by_county[county_name] += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    
    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
    
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the county votes and percentages
        txt_file.write(f"\nCounty Results:\n")
        for county in votes_by_county:
            c_votes = votes_by_county[county]
            c_percentage = float(c_votes) / float(total_votes) * 100
            county_results = (f"{county}: {c_percentage:.1f}% ({c_votes:,})\n")
            print(county_results)
            txt_file.write(county_results)
            if (c_votes > county_votes) and (c_percentage > county_percentage):
                county_votes = c_votes
                county_percentage = c_percentage
                largest_turnout = county
        largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")
        txt_file.write(largest_county_summary)
        # Determine the percentage of votes for each candidate by looping through the counts.
        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate      
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        txt_file.write(winning_candidate_summary)

        # Create three if statements to print out the voter turnout results similar to the results shown above.
        # Add the results to the output file.
        # Print the results to the command line.
