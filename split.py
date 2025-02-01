def split_and_join(line):
    line=line.split(" ")
    return '-'.join(line)
line=input("enter value:")
result=split_and_join(line)
print(result)