a = [1,2,3,4,5]
b =[1,2,3,4,5]
mydict = {i[0] : i[1] for i in zip(a,b)}
print{i for i in mydict.items()}
