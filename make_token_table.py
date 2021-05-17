f=open("test.out",'r')
token_table=[]
data=f.readlines()

for ele in data:
    ele=ele.strip().lstrip('<').rstrip('>').split(',')
    ele[0]=ele[0].lower()
    token_table.append(ele)
