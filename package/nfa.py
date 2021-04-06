from .stackclass import StackClass
from .regex import make_key


class NFA:

    def make_input_symbol(self,postfix):
        op_lst=['.','*','|']
        input_symbol_lst=[]
        for symbol in postfix:  
            if symbol not in op_lst and symbol not in input_symbol_lst:
                input_symbol_lst.append(symbol) 
        input_symbol_lst.append('eps')
        
        return input_symbol_lst 


    def infixtopostfix(self,infixexpr):

        stack=StackClass()
        return_lst=[]
        prec={}
        prec['*']=4
        prec['|']=3
        prec['.']=2
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
                    return_lst.append(stack.pop())
                stack.push(token)
            else:
                return_lst.append(token)        
        while not stack.isEmpty():
            op_token=stack.pop()
            return_lst.append(op_token)     
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
                i=make_key(i)
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
                stack.append([state2_1,state1_2])
                table[state2_2]['eps']=state1_1
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
        table_list=[]
        for i in range(0,self.__end_state+1):
            temp_dict=dict()
            for i in self.__keys:
                i=make_key(i)
                temp_dict[i]=-1
            table_list.append(temp_dict)        
        i = 0    
        for elem in table:
            for key, value in elem.items():
                key=make_key(key)
                (table_list[i])[key]=value
            i = i+1
        return table_list
       

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
