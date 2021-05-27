from package.stackclass import StackClass
from package.cfg import *
import pandas as pd
import sys
table = pd.read_html('./table/table.html', header=2, encoding='utf-8')
del table[0]['State']
slr_table=table[0].transpose()

class Parser():
    
    def __init__(self,table,file_name,cfg):
        self.slr_table=table
        self.rf=open(file_name,'r')
        self.token_table=self.make_token_table()
        self.input_string=self.make_input_string()
        self.cfg=CfgList(cfg)
    def make_token_table(self):
       
        token_table=[]
        data=self.rf.readlines()
       
        for ele in data:
            
            token_input=dict()
            ele=ele.strip().lstrip('<').rstrip('>').split(',')
            ele[1]=ele[1].lower()
            if ele[1]=='op':
                if ele[2]=='+' or ele[2]=='-':
                    ele[1]=='addsub'    
                else:
                    ele[1]='muldiv'
            if ele[1]=='comma':
                ele[2]=','
            token_input["line"]=ele[0]
            token_input["token_name"]=ele[1]
            token_input["value"]=ele[2]
            token_table.append(token_input)
            
        return token_table

    def make_input_string(self):
        input_string=""
        for ele in self.token_table:
            input_string=input_string+ele["token_name"]+" "
        input_string+='$'
        return input_string
    def next(self,current_state,next_symbol):
        
        return self.slr_table[current_state][next_symbol]

    def check(self):
        stack=StackClass([0])
        current_state=stack.peek()
        left_string=""
        right_string=self.input_string
        next_symbol=right_string.split(" ",1)[0]
        idx=0
        next_action=self.next(current_state,next_symbol)
        while(True):
            next_action=self.next(current_state,next_symbol)
            try:
     
                if next_action[0]=='r':
                    rule_num=int(next_action[1:])
                    length=self.cfg.length_of_rhs(rule_num)
                    for i in range(length):
                        stack.pop()
                    current_state=stack.peek()
                    
                    left_string,reduced_result=self.cfg.reduce(left_string,rule_num)
                    left_string+=" " 
                    next_state=self.next(current_state,reduced_result)
                    stack.push(int(next_state))
                    current_state=stack.peek()
                    
                    
                elif next_action[0]=='s':
                    stack.push(int(next_action[1:]))
                    left_string=left_string+right_string.split(' ',1)[0]+' '
                    if right_string!='$':
                        right_string=right_string.split(' ',1)[1]
                    else:    
                        right_string=''               
                    current_state=stack.peek()
                    idx+=1
                    next_symbol=right_string.split(" ",1)[0]

                    

                elif next_action=='acc':
                    print("accept")
                    break
                else:
                    print("table error")
            except:
                print("Syntax error: '"+self.token_table[idx]["value"]+"' in line",self.token_table[idx]["line"])
               
                break
        
        

if __name__=='__main__':
    file_name="./test/"+sys.argv[1]
    parse=Parser(slr_table,file_name,cfg)
    parse.check()






        

    
