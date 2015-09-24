import re
from textblob import TextBlob
###reading lines
lines=open('../data/train.csv','r').readlines()[1:]
###number of lines
number_of_lines=len(lines)
###finding the actual sentences
###saving polarity in a new file
polarity=open("polarity.txt","w")
polarity.write('Insult,Polarity\n')
for i in range(number_of_lines):
    x=lines[i].split('"""')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    lines[i]=x[1]
    insult=x[0].split(',')[0]
    lines[i] = re.sub(r'(\n|\\n|\\xc2|\\xa0|\\xe2|\\x80|\\xa6)', ' ', lines[i])
    lines[i] = re.sub(r'(\\ | \\|")',' ',lines[i])
    lines[i] = lines[i].decode('unicode_escape').encode('ascii','ignore')
    polar = TextBlob(lines[i]).sentiment.polarity
    polarity.write(insult+','+str(polar)+'\n')
polarity.close()
