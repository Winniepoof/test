file=open('c.txt','r')

file.seek(3)

print(file.read())
print(file.tell())
file.close()