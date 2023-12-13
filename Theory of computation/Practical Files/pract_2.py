# Write a program for generating regular expressions for regular grammar

import re
S="A computer scienc portal for students"
match=re.search(r'portal',S)
print("Start index:",match.start())
print("End index:",match.end())
p=re.compile('ab*')
print(p.findall("ababbaabbb"))
string="""Hello my number is 123455 and my frnd number is 63742387"""
regex='\d+'
match=re.findall(regex,string)
print(match)
