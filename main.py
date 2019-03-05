import prepare_data
import str_match

with open('prepared.csv', 'r') as f:
    in_list = f.read().strip(' ').replace(",", "").replace("\n", "").split(';')

with open('output.csv', 'r') as f:
    dam_list = f.read().strip(' ').replace(",", "").replace("\n", "").split(';')

def compare_list(pattern, damaged):     #WTF?!
    ls = []
    for index,word in enumerate(pattern) :
        ls.append(word == damaged[index])
    return ls

ls = compare_list(in_list,dam_list)

with open('ls.csv', 'w') as f:
    for item in ls:
        f.write("%s\n" % item)

zipped = zip(in_list,dam_list,ls)
all_lists = list(zipped)