#PyBank_hw.py
import os
import csv
import operator as op

#set the file path
csv_path = os.path.join("Resources", "budget_data_1.csv")
print("The file path " + csv_path)

print("Financial Analysis")
print(25*"-")
#open csv file
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #first line 
    header = next(csvreader)  
        
    data = []
    for row in csvreader:
        # row = [Date , Revenue]
        bug_date = row[0]
        bugRevenue = int(row[1])

        data.append([bug_date,bugRevenue])
        
    #print(data[0])
    #print(bug_date)
    #print(bugRevenue)  

#commpute
tot_revenue = 0
tot_chareveue = 0

for i in range(len(data)):  
    tot_month = len(list(data))    
    cal_revenue = data[i]
    tot_revenue = tot_revenue + float(cal_revenue[1])
    
     
avg_revenue = round(tot_revenue / tot_month)
#print (avg_revenue)
print("Total months: "+ str(tot_month) )    
print ("Total Revenue: $" + str(tot_revenue))  
#print ("Average Revenue change $" + str(avg_revenue))

#The average change in revenue between months over the entire period
charevenuelist = []

with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #first line 
    header = next(csvreader) 
    for row in csvreader:
        charevenuelist.append(int(row[1]) - tot_chareveue)
        tot_chareveue = int(row[1])

charevenue = []
for k in charevenuelist:
    charevenue.append(abs(k))

avgchange = sum(charevenue) / len(charevenuelist)
print ("Average Revenue change $" + str(avgchange))

#max Revenue    
#max_revenue = max(list(data))
#print(" Greatest Incresase in Revenue " + str(max_revenue[0]) +  " ($" +str(max_revenue[1])+")")  

with open(csv_path) as csvfile:
    next(csvfile) # discard first row from file -- see notes
    max_value = max(row for row in csv.reader(csvfile))
     
#print(max_value)
print(" Greatest Incresase in Revenue " + str(max_value[0]) +  " ($" +str(max_value[1])+")")  

#min value 
with open(csv_path) as csvfile:
    next(csvfile) # discard first row from file -- see notes
    min_row = min(csv.reader(csvfile), key=op.itemgetter(1))
#print(min_row)    
print(" Greatest Decrease in Revenue " + str(min_row[0]) +  " ($" +str(min_row[1])+")")  


#or i in range(len(total_revenue)):
 #      if i < (len(total_revenue)-1):
  #         avg_rev.append(int(total_revenue[i+1])-int(total_revenue[i]))
   #    y = sum(avg_rev)/int(len(avg_rev))
   #print("Average Change in Revenue: ${:.0f}".format(y))
