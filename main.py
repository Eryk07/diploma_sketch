#import prepare_data
import str_match as sm
#import pandas as pd
from CRecord import CRecord

with open('prepared.csv', 'r') as f:
    in_list = f.read().strip(' ').replace(",", "").replace("\n", "").split(';')
    #in_list = pd.read_

with open('output1.csv', 'r') as f:
    dam_list = f.read().strip(' ').replace(",", "").replace("\n", "").split(';')

ls = [] #lista czy równe czy nie
ls_ham = [] #lista współczynników Hamminga
ls_lev = [] #lista współczynników Levensteina
ls_jar = [] #lista współczynników Jaro
ls_jar_wi = [] #lista współczynników Jaro-Winklera
ls_rat_ob = [] #lista współczynników Ratcliffa-Obershelpa

cr = CRecord()
def compare_list(pattern, damaged):     #WTF?!

    if(len(pattern)==len(damaged)):
        for index, word in enumerate(pattern):
            ls.append(word == damaged[index])
            ls_ham.append(sm.distance_Hamming(word,damaged[index]))
            ls_lev.append(sm.distance_Levenshtein(word,damaged[index]))
            ls_jar.append(sm.distance_Jaro(word,damaged[index]))
            ls_jar_wi.append(sm.distance_Jaro_Winkler(word,damaged[index]))
            ls_rat_ob.append(sm.distance_Ratcliff_Obershelp(word, damaged[index]))

    else:
        print("Listy nie są równe! " + str(len(pattern)) +" i " + str(len(damaged)))
    return ls

ls = compare_list(in_list,dam_list)

with open('ls.csv', 'w') as f:
    for item in ls:
        f.write("%s\n" % item)




zipped = zip(in_list,dam_list,ls,ls_ham,ls_lev,ls_jar,ls_jar_wi,ls_rat_ob)
all_lists = list(zipped)
print(all_lists)

with open('all_lists.csv', 'w') as f:
    for item in all_lists:
        f.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % item)

print("Hamming: " + str(sm.distance_Hamming("INFORMACJA","INFORMATYKA")))
print("Levenshtein: " + str(sm.distance_Levenshtein("INFORMACJA","INFORMATYKA")))
print("Jaro: " + str(sm.distance_Jaro("INFORMACJA","INFORMATYKA")))
print("Jaro Winkler: " + str(sm.distance_Jaro_Winkler("INFORMACJA","INFORMATYKA")))
print("Ratcliff Obershelp: " + str(sm.distance_Ratcliff_Obershelp("INFORMACJA","INFORMATYKA")))