import os 
import csv

#Path to collect data from the resources folder
budget_csv= os.path.join("Resources","budget_data.csv")

#  The total number of months included in the dataset
# with open (budget_csv,newline="") as csvFile:
#     csvReader = csv.reader(csvFile,delimiter=",")
#     csvHeader=next(csvReader)
# # print (sumcolumn)
with open("budget_data.csv") as csvFile:
    csvReader=csv.reader(csvFile,delimiter=",")
    csvHeader=next(csvReader)
    #  headerline = fin.next()
    totalMonth=0
    Sums=0
    Max=0
    Min=0
    maxchange=0
    minchange=0
    Change=0
    Lastprofit=0
    maxdate=0
    mindate=0

    for row in csvReader:
        totalMonth= totalMonth+1
        Sums=int(row[1])+Sums
        Change=int(row[1])-Lastprofit
        if Change > maxchange:
            maxchange=Change
            maxdate=row[0]
            # maxchange=int(row[1])
            # maxdate=row[0]

        if Change < minchange:
            minchange=Change
            mindate=row[0]

        Lastprofit=int(row[1])
    AveCh= Sums/totalMonth
        # if Min > int(row[1]): 
        #     Min=int(row[1])

        # if Max < int(row[1]):
        #     Max=int(row[1])



print('```text')       
print('Financial Analysis')
print('------------------')
print("Total Months: " + str(totalMonth))
print("Total: $"+ str(Sums))
print('Average Change: $'+str(round(AveCh,3)))
print('Greatest Increase in Profits: '+str(maxdate)+" ($"+ str(maxchange) +")")
print("Greatest Decrease in Profits: "+str(mindate)+" ($"+ str(minchange)+")")
print("```")

output_path = os.path.join(r'C:\Users\Owner\Desktop\python-challenge\PyBank\Resources', 'pyBankResult1.txt')

with open (output_path,'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['```text'])       
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(["Total Months: " + str(totalMonth)])
    csvwriter.writerow(["Total: $"+ str(Sums)])
    csvwriter.writerow(['Average Change: $'+str(round(AveCh,3))])
    csvwriter.writerow(['Greatest Increase in Profits: '+str(maxdate)+" ($"+ str(maxchange) +")"])
    csvwriter.writerow(["Greatest Decrease in Profits: "+str(mindate)+" ($"+ str(minchange)+")"])
    csvwriter.writerow(["```"])

# The net total amount of "Profit/Losses" over the entire period


#   * The average of the changes in "Profit/Losses" over the entire period

#   * The greatest increase in profits (date and amount) over the entire period
# incr_P=max()

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.