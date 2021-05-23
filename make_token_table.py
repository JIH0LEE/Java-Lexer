f=open("test.out",'r')
token_table=[]
data=f.readlines()

for ele in data:
    ele=ele.strip().lstrip('<').rstrip('>').split(',')
    ele[0]=ele[0].lower()
    if ele[0]=='op':
        
        if ele[1]=='+' or ele[1]=='-':
            ele[0]=='addsub'    
        else:
            ele[0]='muldiv'
         
    token_table.append(ele)

if __name__=="__main__":
    print(token_table)
