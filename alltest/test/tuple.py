t=(10,[50,61],20,'张海盐')
print(t,type(t))
print(t[0],type(t[0]))
print(t[1],type(t[1]))
print(t[2],type(t[2]))
t[1].append(86)
print(t)
t[1].insert(1,520)
print(t)

for i in t:
    print(i,end='\t')

