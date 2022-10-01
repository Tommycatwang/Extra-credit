text=open("book of John text.txt",'r')

d={'Father':0,'father':0,'God':0,'god': 0,'Christ':0,'christ':0,'Spirit':0,'spirit':0,'life':0,'Life':0,'Man':0,'man':0}


for line in text:
    line = line.strip()

    words = line.split(" ")

    for word in words:
        if word in d.keys():
            d[word]=d[word]+1

for key in list(d.keys()):
    if d[key]==0:
        del d [key]
    else:
        print(key,":",d[key])

text.close()
#del phonebook ['Chris']
#print(phonebook)