from .stackclass import StackClass
from .regex import make_key


class NFA:
    #function: change infix of regular expression to postfix 
    def __infixtopostfix(self,infixexpr):

        stack=StackClass()  #stack for operand
        return_lst=[]       #return list of postfix of regular expression (Each symbol is splited into list) 
        
        #precedence of operation
        prec={}
        prec['*']=4
        prec['.']=3
        prec['|']=2
        prec['(']=1

        #operator
        op_lst=['*','|','.']

        token_lst=infixexpr.split()     #infix of regular expression are split with ' '
        
        
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
    
    
    #function: make keys for nfa
    def __make_inpit_symbol(self,postfix):
        op_lst=['.','*','|']
        input_symbol_lst=[]
        for symbol in postfix:  
            if symbol not in op_lst and symbol not in input_symbol_lst:
                input_symbol_lst.append(symbol) 
        input_symbol_lst.append('eps')
        
        return input_symbol_lst 




    #function: make postfix of regularexpression to nfa table 
    def __regex_to_nfa(self):
        table=[]        #idx of this list is state number and each have dictionary whose keys are route for other state.
                        #([{key1:state3,key2:state},{key1:state1,..}...])       
        
        stack=[]        #stack for getting operand states ([start,end]) 
        self.__start_state=0
        self.__end_state=1
        state_num=-1;new_state1=0;new_state2=0


        #get a token from postfix of regular expression 
        for i in self.__regex:

            #case key: make 2 new states each are start and end 
            #ex)i='a',newstate1=2,newstate2=3 table[newstate1]={'a':3}
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


            #case operator *: get 1 table from stack for using operand 
            #make 2 new states with epsilon move to make exponentiation
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
            
            #case operator .: get 2 tables from stack for using operand 
            #concatenate 2 tables
            #ex) [1,3],[4,10] => [1,10]
            elif i=='.':
                state1_1,state1_2=stack.pop()
                state2_1,state2_2=stack.pop()
                stack.append([state2_1,state1_2])
                table[state2_2]['eps']=state1_1
                if self.__start_state==state1_1:
                    self.__start_state=state2_1 
                if self.__end_state==state2_2:
                    self.__end_state=state1_2

            #case operator |: get 2 tables from stack for using operand 
            #make 2 new states which would be each start and end.
            #connect 2 tables and new states with epsilon

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


        #make full dictionary with all keys.         
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
       
    def __init__(self,regex):
        postfix = self.__infixtopostfix(regex)
        self.__regex=postfix
        self.__keys=self.__make_inpit_symbol(postfix)
        self.__nfa_table=self.__regex_to_nfa()

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
