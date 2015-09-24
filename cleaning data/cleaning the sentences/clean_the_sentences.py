import re,string
import scipy as sp
from textblob import TextBlob

def remove_non_ascii(s):
    return "".join(i for i in s if ord(i) < 128)


def create_new_file(file_name="../../data/train.csv"):
    lines=open(file_name,'r').readlines()
    total_lines=len(lines)
    new_file=open('cleaned_comments.csv','w')
    new_file.write(lines[0])
    for i in range(1,total_lines):
        x=lines[i].split('"""')
        new_file.write(x[0])
        line=x[1]
        line=remove_non_ascii(line)
        line=line.lower()
        t=[]
        for word in line.split(' '):
            if '?' not in word and ':' not in word and word!='':
                t+=[word]
        line=' '.join(t)
        line = re.sub(r'(\n|\\n|\\xc2|\\xa0|\\xe2|\\x80|\\xa6)', ' ',line)
        line = re.sub(r'(\\ | \\|")',' ',line)
        line = re.sub(r'(-{2,30})',' ',line)
        line = re.sub(r'(o{2,30})','oo',line)
        line = re.sub(r'(_)',' ',line)
        line=line.decode('unicode_escape').encode('ascii','replace')
        line=line.decode('unicode_escape').encode('ascii','ignore')
        line=line.replace('!',' ')
        line=line.replace('idi0t','idiot')
        line=line.replace('.',' ')
        line=line.replace(' (',' ')
        line=line.replace(') ',' ')
        line=line.replace(',',' ')
        line=line.replace(' -',' ')
        line=line.replace('- ',' ')
        line=line.replace("' ",' ')
        line=line.replace(" '",' ')
        line=re.sub(" \d+", " ", line)
        line=re.sub(" \d+th", " ", line)
        line=re.sub("u\d", " ", line)
        line=re.sub("\d+ ", " ", line)
        line=re.sub("\d+", " ", line)
        line=re.sub(r"<.>", " ", line)
        line=re.sub(r"<..>", " ", line)
        line=line.replace('?',' ')
        t=[]
        for k in emo_repl_order:
            line = line.replace(k, emo_repl[k])
        for r, repl in re_repl.iteritems():
            line = re.sub(r, repl, line)
        line=line.replace("'",' ')
        for word in line.split(' '):
            if word!='' and not(len(word)==1 and (word!='a' or word!='i')):
                if word.startswith('@'):
                    t+=['@name']
                else:
                    t+=[word]
        line=' '.join(t)
        new_file.write(line+'\n')
emo_repl = {
# positive emoticons
"&lt;3": " good ",
":d": " good ", # :D in lower case
":dd": " good ", # :DD in lower case
"8)": " good ",
":-)": " good ",
":)": " good ",
";)": " good ",
"(-:": " good ",
"(:": " good ",
# negative emoticons:
":/": " bad ",
":&gt;": " sad ",
":')": " sad ",
":-(": " bad ",
":(": " bad ",
":S": " bad ",
":-S": " bad ",
}

re_repl = {
r"\br\b": "are",
r"\bu\b": "you",
r"\bhaha\b": "ha",
r"\bhahaha\b": "ha",
r"\bdon't\b": "do not",
r"\bdoesn't\b": "does not",
r"\bdidn't\b": "did not",
r"\bhasn't\b": "has not",
r"\bhaven't\b": "have not",
r"\bhadn't\b": "had not",
r"\bwon't\b": "will not",
r"\bwouldn't\b": "would not",
r"\bcan't\b": "can not",
r"\bcannot\b": "can not",
r"\bwouldn't\b": "would not",
r"'re\b": " are",
r"'s\b": " is",
r"'ll\b": " will",
r"'ve\b": " have",
r"'m\b": " am",
r"'nt\b": " not",
r"&nbsp;": " ",

}
emo_repl_order = [k for (k_len,k) in reversed(sorted([(len(k),k) for k
in emo_repl.keys()]))]
create_new_file()
