# ![Vote-Counting](Images/Vote_counting.png)
import os
import csv
# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
election_data= os.path.join("Resources","election_data.csv")
# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
with open("election_data.csv") as csvFile:
    csvReader=csv.reader(csvFile,delimiter=",")
    csvHeader=next(csvReader)

with open (election_data,newline='') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=',')
    csvHeader=next(csvReader)
    tot=0
    khanc=[]
    correy=[]
    li=[]
    oley=[]
    for i in csvReader:
        tot=tot+1
        if i[2]=="Khan":
            khanc.append(i[2])
        if i[2]=="Correy":
            correy.append(i[2])
        if i[2]=="Li":
            li.append(i[2])
        if i[2]=="O'Tooley":
            oley.append(i[2])
    tots=tot-1
    x1=len(khanc)
    x2=len(correy)
    x3=len(li)
    x4=len(oley)
    y1=round(x1/tots*100,3)
    y2=round(x2/tots*100,3)
    y3=round(x3/tots*100,3)
    y4=round(x4/tots*100,3)
    if y1==max(y1,y2,y3,y4):
        winner="Khan"
    elif y2==max(y1,y2,y3,y4):
        winner="Correy"
    elif y3==max(y1,y2,y3,y4):
        winner="Li"
    elif y4==max(y1,y2,y3,y4):
        winner="O'Tooley"
    print('Election Results')
    print('----------------------')
    print('Total Votes: '+ str(tots))
    print('----------------------')
    print('Khan: '+str(y1)+'% ' + '('+ str(x1)+')')
    print('Correy: '+str(y2)+'% ' + '('+ str(x2)+')')
    print('Li: '+str(y3)+'% ' + '('+ str(x3)+')')
    print("O'Tooley: "+str(y4)+'% ' + '('+ str(x4)+')')
    print("Winner: " + winner)
    output_path =os.path.join(r'C:\Users\Owner\Desktop\python-challenge\PyPoll\Resources','pyPollResult.txt')
    with open(output_path, 'w') as newFile:
        newf=csv.writer(newFile)
        newf.writerow(['Election Results'])
        newf.writerow(['----------------------'])
        newf.writerow(['Total Votes: '+ str(tots)])
        newf.writerow(['----------------------'])
        newf.writerow(['Khan: '+str(y1)+'% ' + '('+ str(x1)+')'])
        newf.writerow(['Correy: '+str(y2)+'% ' + '('+ str(x2)+')'])
        newf.writerow(['Li: '+str(y3)+'% ' + '('+ str(x3)+')'])
        newf.writerow(["O'Tooley: "+str(y4)+'% ' + '('+ str(x4)+')'])
        newf.writerow(['----------------------'])
        newf.writerow(["Winner: " + winner])
        
#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.