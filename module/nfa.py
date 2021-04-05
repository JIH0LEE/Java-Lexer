from stackclass import StackClass
import pandas as pd
import numpy as np


class NFA:

    def make_input_symbol(self,postfix):
        op_lst=['(',')','.','*','|']
        input_symbol_lst=[]
        for symbol in postfix:
            if symbol not in op_lst:
                input_symbol_lst.append(symbol) 
        input_symbol_lst.append('eps')
        return input_symbol_lst 


    def infixtopostfix(self,infixexpr):

        stack=StackClass()
        return_lst=[]
        prec={}
        # this is the precedence order
        prec['*']=3
        prec['|']=2
        prec['.']=1
        prec['(']=1
        op_lst=['*','|','.']

        token_lst=infixexpr.split()
        for token in token_lst:
        
                
            if token == '(':
                stack.push(token)

            elif token == ')':
                top_token=stack.pop()
                while top_token != '(':
                    return_lst.append(top_token)
                    top_token=stack.pop()
            elif token in op_lst:
                while (not stack.isEmpty()) and (prec[stack.peek()] >= prec[token]):
                    #print token
                    return_lst.append(stack.pop())
                stack.push(token)
                    #print return_lst
            else:
                return_lst.append(token)
            
        while not stack.isEmpty():
            op_token=stack.pop()
            return_lst.append(op_token)
        #print return_lst
        return return_lst



    def __init__(self,regex):
        postfix = self.infixtopostfix(regex)
        self.__regex=postfix
        self.__keys=self.make_input_symbol(postfix)
        self.__nfa_table=self.regex_to_nfa()

        
    def regex_to_nfa(self):
        table=[]
        stack=[]
        self.__start_state=0
        self.__end_state=1
        state_num=-1;new_state1=0;new_state2=0
         
        for i in self.__regex:
            if i in self.__keys:
                state_num=state_num+1
                new_state1=state_num
                state_num=state_num+1
                new_state2=state_num
                table.append({})
                table.append({})
                stack.append([new_state1,new_state2])
                
                table[new_state1][i]=new_state2
            elif i=='*':
                state1,state2=stack.pop()
                state_num=state_num+1
                new_state1=state_num
                state_num=state_num+1
                new_state2=state_num
                table.append({})
                table.append({})
                stack.append([new_state1,new_state2])
                table[state2]['eps']=[state1,new_state2]
                table[new_state1]['eps']=[state1,new_state2]
                if self.__start_state==state1:
                    self.__start_state=new_state1 
                if self.__end_state==state2:
                    self.__end_state=new_state2 
            elif i=='.':
                state1_1,state1_2=stack.pop()
                state2_1,state2_2=stack.pop()
                state1_2 = state1_1
                state1_1 = state2_2
                stack.append([state2_1,state1_2])
                elem = table[state1_2]
                del table[state1_2]
                for key in elem.keys():
                    table[state1_1][key] = elem.get(key)-1
                state_num = state_num - 1
                if self.__start_state==state1_1:
                    self.__start_state=state2_1 
                if self.__end_state==state2_2:
                    self.__end_state=state1_2 
            else:
                state_num=state_num+1
                new_state1=state_num
                state_num=state_num+1
                new_state2=state_num
                table.append({})
                table.append({})
                state1_1,state1_2=stack.pop()
                state2_1,state2_2=stack.pop()
                stack.append([new_state1,new_state2])
                table[new_state1]['eps']=[state2_1,state1_1]
                table[state1_2]['eps']=new_state2
                table[state2_2]['eps']=new_state2
                if self.__start_state==state1_1 or self.__start_state==state2_1:
                    self.__start_state=new_state1 
                if self.__end_state==state2_2 or self.__end_state==state1_2:
                    self.__end_state=new_state2

        # print(keys)
        # print(self.__start_state)
        # print(self.__end_state)
        # print(table)

        arr_mat = np.full((self.__end_state + 1, len(self.__keys)), [-1])
        nfa_table = pd.DataFrame(arr_mat, columns = self.__keys, index = range(0, self.__end_state+1), dtype = 'object')
        
        i = 0   
        for elem in table:
            for key, value in elem.items():
                #print(key, value)
                nfa_table.at[i,key]=value
            i = i+1
        return nfa_table
       

    def keys(self):
        return self.__keys
    def nfa_table(self):
        return self.__nfa_table
    def regex(self):
        return self.__regex   
    def start_state(self):
        return self.__start_state
    def end_state(self):
        return self.__end_state    

print(1)