#import csv
import random
import string
from str_match import StrMatch

with open('prepared.csv', 'r') as f:
    in_list=f.read().strip(' ').replace(",","").replace("\n","").split(';')

#    ******** BIBLIOTEKA CSV ******* 
#    
#    coś nie chciało siąść - nie rozpoznawał listy
#
#def get_csv_lines():
 #  with open('prepared.csv') as csv_file:
  #      csv_reader = csv.reader(csv_file, delimiter=',')
   #     for row in csv_reader:
    #        yield row 
#in_list = list(get_csv_lines())

# **********************************

#for i in range (0,len(your_list)):
 #  print(in_list[i])



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

difflist_delate_spaces(your_list,5)
difflist_delete_random_letter(your_list,5)
difflist_uppercase(your_list,5)
difflist_lowercase(your_list,5)
difflist_title(your_list,5)
difflist_insert_random_letter(your_list,5)



#with open("output.csv",'w') as resultFile:
 #   wr = csv.writer(resultFile, dialect='excel')
  #  wr.writerows(your_list)


def compare_list(pattern, damaged):     #WTF?!
    ls = []
    for index,word in enumerate(pattern) :       
        ls.append(word == damaged[index])
    return ls

with open('output.csv', 'w') as f:
    for item in your_list:
        f.write("%s\n" % item)

ls = compare_list(in_list,your_list)

with open('ls.csv', 'w') as f:
    for item in ls:
        f.write("%s\n" % item)

zipped = zip(in_list,your_list,ls)
all_lists = list(zipped)

#with open('all_lists.csv', 'w') as f:
#  for item in all_lists:
#     f.write("%s\n" % item)

print(79*'*')
for i in range(60):    
   print(all_lists[i])

#StrMatch.first_algorithm()