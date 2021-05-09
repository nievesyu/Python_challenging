import os
import csv

pollanalysis = os.path.join("Resources", "election_data.csv")

with open(pollanalysis) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)


    Total_Votes = []
    Candidate_List = []
    Vote_Count = []
    Percentage = []
    Percent_Final = []
   


    for row in csv_reader:
        Total_Votes.append(row[2])

        DupCan = False
        for candidate in Candidate_List:
            if candidate == row[2]:
                DupCan = True
       
        if DupCan == False:
            Candidate_List.append(row[2])

    for person in Candidate_List:
        Vote_Count.append(Total_Votes.count(person))
   
    for count in Vote_Count:
        Percentage.append(count/int(len(Total_Votes))*100)

    for item in Percentage:
        Percent_Final.append(round(item, 2))

    results = dict()
    Final_Results = []

    for i in range(len(Candidate_List)):
        results = {f"{Candidate_List[i]}: {Percent_Final[i]}% ({Vote_Count[i]})"}
        Final_Results.append(results)

    MaxVote = Vote_Count[0]
    Winner = Candidate_List[0]

    for j in range(len(Vote_Count)):
        if Vote_Count[j] > MaxVote:
            MaxVote = Vote_Count[j]
            Winner = Candidate_List[j]

   
    print("Election Results")
    print("---------------------------------------")
    print(f"Total Votes: {len(Total_Votes)}")
    print("---------------------------------------")
    print(Final_Results)
    print("---------------------------------------")
    print(f"Winner: {Winner}")
    print("---------------------------------------")