a=[["1","2","3"], "456"]
a=[";".join(i) if isinstance(i,list) else i for i in a]
print(a)