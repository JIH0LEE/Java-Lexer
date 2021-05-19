from table.slr_table import slr_table;
from package.stackclass import StackClass
class Cfg():
    def __init__(self,rule_string):
        self.lhs,self.rhs=rule_string.split('->')
        self.lhs=self.lhs.strip()
        self.rhs=self.rhs.strip()
    def reduce(self,input):
        
        idx=self.rhs.rfind(input)
        rt=input[0:idx]+self.rhs
        return rt

class CfgList():
    def __init__(self,rules):
        self.cfg_rules=[]
        for ele in rules:
            self.cfg_rules.append(Cfg(ele))
    def reduce(self,input,rule_num):
        rt=self.cfg_rules[rule_num].reduce(input)
        return rt

class Parser():
    
    def __init__(self,table,file_name,cfg):
        self.slr_table=table
        
        self.rf=open(file_name,'r')
        self.token_table=self.make_token_list()
        self.input_string=self.input_string()
        self.cfg=CfgList(["test","test1"])
        
        

    def make_token_list(self):
        token_table=[]
        data=self.rf.readlines()

        for ele in data:
            ele=ele.strip().lstrip('<').rstrip('>').split(',')
            ele[0]=ele[0].lower()
            token_table.append(ele)
        return token_table

    def make_input_string(self):
        input_string=""
        for ele in self.token_table:
            input_string+=ele
        return input_string+'$'
    def next(self,current_state,next_symbol):
        return self.slr_table[current_state][next_symbol]

    def check(self):
        stack=StackClass([0])
        current_state=stack.peek()
        left_string=""
        right_string=self.input_string
        next_symbol=right_string.split(" ",1)[0]
        next_action=next(current_state,next_symbol)
        while(True):
            if next_action==None:
                print('error')
            elif next_action[0]=='r':
                rule_num=int(next_action[1:])
                stack.pop()
                current_state=stack.peek()
                left_string=self.cfg.reduce(left_string,rule_num)
                next_state=next(current_state,left_string)
                stack.push(int(next_state))
                current_state=stack.peek()
                
            elif next_action[0]=='s':
                stack.push(int(next_action[1:]))
                left_string=left_string+right_string.split(' ',1)[0]
                right_string=right_string.split(' ',1)[1]
            elif next_action=='acc':
                print("accept")
                break
            else:
                print("table error")

if __name__=='__main__':
    parse=Parser(slr_table,"test.out")


            



        

    
