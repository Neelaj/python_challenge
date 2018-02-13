#PyPoll.py
import os
import csv

from pprint import pprint
import collections

# file 

csv_path = os.path.join("Resources","election_data_1.csv")
csv_path_wr = os.path.join("Resources","election1.csv")
print(csv_path)

fo= open("test.txt", "w")
print (fo.name)

print("Election Results")
print(25*"-")

fo.write("Election Results \n--------------------------------\n")


#open
with open(csv_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ',')

    #first line 
    header = next(csv_reader)
    #print(header) 
    tot_voters = 0

    data = []
    can_list = []

    #candidate list total
    for row in csv_reader:
        tot_voters = tot_voters + 1 
        vote_id = row[0]
        county = row[1]
        candidate = row[2]
        data.append([vote_id, county, candidate])
        if not can_list:
            can_list.append(candidate)
        else:          
            thing_index = can_list.index(candidate) if candidate in can_list else -1
            
            #0() means existed and -1 means ned to add the element.
            if( thing_index == -1):
                can_list.append(candidate)


    fo.write("total votes : " + str(tot_voters) + "\n----------------------------\n")
    print("total votes :" + str(tot_voters))         
    print(25*"-")
    print(can_list) 
    per_win = 0

    for can in can_list:
        #print (can)
        tot_can = 0        
        for i in range(tot_voters):
            if (can == data[i][2]):
                tot_can = tot_can + 1 

          
        per_can = ((tot_can/tot_voters)* 100)   
        fo.write("candidate name : " + str(can) + ": " + str(per_can) +"% (" + str(tot_can) + ")" )
        fo.write("\n")            
        print ("candidate name :"+str(can)  + ": " + str(per_can) +"% (" + str(tot_can) + ")" )    
        if (per_can > per_win):
            per_win = per_can
            winner_Can = can  
            #print (per_win)

        #print("Winner :" + str(can))
    print(25*"-") 
    
    print("Winner :" + str(winner_Can))
    fo.write("---------------------\n")
    fo.write("Winner :" +str(winner_Can))
    fo.write("\n---------------------")    
    print(25*"-")               # data.append([vote_id, county, candidate])



    
 
    