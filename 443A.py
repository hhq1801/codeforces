data=input()
data=data.replace('{','')
data=data.replace('}','')
data=data.replace(', ',' ')
data=data.split()
data = list(set(data))
print(len(data))