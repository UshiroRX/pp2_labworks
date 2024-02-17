import re

pattern1 = r"ab*"   #Ex1
pattern2 = r"ab{2,3}"   #Ex2
pattern3 = r"[a-z]+_[a-z]+" #Ex3
pattern4 = r"[A-Z][a-z]+"   #Ex4
pattern5 = r"a.*\b" #Ex5 

def match(pattern):

    with open("row.txt", "r", encoding="utf-8") as s:
        text = s.read()
        matches = re.findall(pattern, text)
        return matches

print(match(pattern1))

