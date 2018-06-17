# John Giglio
# HW 3 PyBank
# Revised 6/17

# import packages

import csv


# three columns: `Voter ID`, `County`, and `Candidate`
# create empty lists to store columns

ID = []
country = []
candidate = []

# open and read csv file
with open('election_data.csv',encoding="utf8") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    # iterate through csvreader and append to ID country and candidate lists
    header = next(csvreader) #skip headers
   
    for row in csvreader:
        ID.append(row[0])
        country.append(row[1])
        candidate.append(row[2])

    """  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```"""
    print('  Election Results\n-------------------------')
#   * The total number of votes cast
    totalvotes = len(ID)
    print(f'Total Votes: {totalvotes}')
    print('-------------------------')
#   * A complete list of candidates who received votes
    candidates_list = set(candidate)

#   * The total number of votes each candidate won
    votes = [candidate.count(name) for name in candidates_list]

#   * The percentage of votes each candidate won
    votes_perc = [100*num/sum(votes) for num in votes]

    for cand, perc, vote in zip(candidates_list, votes_perc, votes):
        print(f'{cand}: {perc:.3f}% ({vote})')

#   * The winner of the election based on popular vote.
    print('-------------------------')
    winner = list(candidates_list)[votes.index(max(votes))]
    print(f'Winner: {winner}')
    print('-------------------------')

# write to csv
    with open('election_results.csv', 'w', newline='') as csvfile:

    # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows
        csvwriter.writerow(['  Election Results'])
        csvwriter.writerow(['-------------------------'])
        csvwriter.writerow(['Total Votes: ',str(totalvotes)])
        csvwriter.writerow(['-------------------------'])

        # iterate through candidates to print individual results
        for cand, perc, vote in zip(candidates_list, votes_perc, votes):
            csvwriter.writerow([str(cand) + ': ', f'{round(perc,3):.3f}%','="(' + str(vote) + ')"'])
        
        csvwriter.writerow(['-------------------------'])
        csvwriter.writerow(['Winner :', str(winner)])
        csvwriter.writerow(['-------------------------'])


