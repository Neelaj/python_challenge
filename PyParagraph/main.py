#PyPara_hw.py
import os
import csv
# file 

csv_path = os.path.join("Resources","paragraph_1.txt")
print("file path " + str(csv_path))

print("paragraph Analyis")
print(25*"-")

with open(csv_path, 'r') as file:
    for para in file:
        file.read()
        #print(para)        
        sp_words = para.split(" ")
        tot_words = len(sp_words)
        
    #print (sp_words)
    print("Approximate word count : " + str(tot_words))
    
with open (csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        sen_count = (len(row))
       
print ("approximate Sentence count: " + str(sen_count))

with open(csv_path, 'r') as file_letter:
    for letter in file_letter:
        file_letter.read()
        #print(para)        
        total_letters = len(letter)

#print(total_letters)

avg_lettercount = (total_letters/tot_words)
print ("Average Letter count : " + str(avg_lettercount))

avg_sentencecount = (tot_words/sen_count)
print ("Average Sentence Length : "+ str(avg_sentencecount))

