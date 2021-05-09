import os
import csv

bankanalysis = os.path.join("Resources", "budget_data.csv")

with open(bankanalysis) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    print("Bank Financial Analysis")
    print("------------------------------------")


    RowNum = 0
    NetTol = []
    MonthList = []
   
    for row in csv_reader:
        RowNum = RowNum + 1
   

        Profit = int(row[1])
        NetTol.append(Profit)
        Month = row[0]
        MonthList.append(Month)
       
    subtractlist = [NetTol[i+1] - NetTol[i] for i in range(len(NetTol) - 1)]
    average = sum(subtractlist) / len(subtractlist)


    greatestincrease = subtractlist[0]
    greatestdecrease = subtractlist[0]

    for j in range(len(subtractlist)):
        if subtractlist[j] > greatestincrease:
            greatestincrease = subtractlist[j]
            increasemonth = MonthList[j+1]
        if subtractlist[j] < greatestdecrease:
            greatestdecrease = subtractlist[j]
            decreasemonth = MonthList[j+1]

   
   
    print(f"Total months: {RowNum}")
    print(f"Net Total: {sum(NetTol)}")
    print(f"Average Change: {average}")
    print(f"Greatest Increase in Profit: {increasemonth} (${greatestincrease})")
    print(f"Greatest Decrease in Profit: {decreasemonth} (${greatestdecrease})")
       