import re

s='hello python'
a='hello'
b='python'
o=re.match(a,s)
p=re.search(b,s)
q=re.sub(b,'java',s,1)
print(o)
print(p)
print(q)