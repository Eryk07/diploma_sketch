#import csv
import random
import string
#from str_match import StrMatch

with open('prepared.csv', 'r') as f:
    in_list=f.read().strip(' ').replace(",","").replace("\n","").split(';')

your_list = in_list.copy()

def difflist_delate_spaces(ls, percentage=5):
   for x in range (0,int(percentage/100*len(ls)) ):
       lsindex = random.randrange(0, len(ls));
       ls[lsindex] = ls[lsindex].replace(" ","");
   return ls

def difflist_delete_random_letter(ls, percentage=5):
   for x in range (0,int(percentage/100*len(ls)) ):
       lsindex = random.randrange(0, len(ls));
       index = random.randint(0, len(ls[lsindex])-1)
       ls[lsindex] = ls[lsindex][:index] + ls[lsindex][index+1:]
   return ls

def difflist_uppercase(ls, percentage=5):
   for x in range (0,int(percentage/100*len(ls)) ):
       lsindex = random.randrange(0, len(ls));
       ls[lsindex] = ls[lsindex].upper();
   return ls

def difflist_lowercase(ls, percentage=5):
   for x in range (0,int(percentage/100*len(ls)) ):
       lsindex = random.randrange(0, len(ls));
       ls[lsindex] = ls[lsindex].lower();
   return ls

def difflist_title(ls, percentage=5):
   for x in range (0,int(percentage/100*len(ls)) ):
       lsindex = random.randrange(0, len(ls));
       ls[lsindex] = ls[lsindex].title();
   return ls

def difflist_insert_random_letter(ls, percentage=5):
   for x in range (0,int(percentage/100*len(ls)) ):
       lsindex = random.randrange(0, len(ls))
       index = random.randint(0, len(ls[lsindex])-1)
       letter = random.choice(string.ascii_letters)
       ls[lsindex] = ls[lsindex][:index] + letter + ls[lsindex][index:]
   return ls

#for i in range (0,len(your_list)):
#   print(your_list[i])
#print(79*'*')

difflist_delate_spaces(your_list,10)
difflist_delete_random_letter(your_list,5)
difflist_uppercase(your_list,5)
difflist_lowercase(your_list,5)
difflist_title(your_list,5)
difflist_insert_random_letter(your_list,5)

#with open("output.csv",'w') as resultFile:
 #   wr = csv.writer(resultFile, dialect='excel')
  #  wr.writerows(your_list)

with open('output.csv', 'w') as f:
   for item in your_list:
        f.write("%s;\n" % item)
