f=open("test.out",'r')
token_table=[]
data=f.readlines()

for ele in data:
    token_input=dict()
    ele=ele.strip().lstrip('<').rstrip('>').split(',')
    ele[1]=ele[1].lower()
    if ele[1]=='op':
        if ele[2]=='+' or ele[2]=='-':
            ele[0]=='addsub'    
        else:
            ele[0]='muldiv'
    
    token_input["line"]=ele[0]
    token_input["token_name"]=ele[1]
    token_input["value"]=ele[2]
    token_table.append(token_input)

if __name__=="__main__":
    print(token_table)
