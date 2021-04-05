import pandas as pd
import numpy as np  
WHITESPACE="( \n | \t | bl ) *"

DIGIT="("
for i in range(48,58):
    if i!=57:
        DIGIT+=" "+ chr(i)+ " |"
    else:
        DIGIT+=" "+ chr(i)
DIGIT+=" )"


LETTER="("
for i in range(65,91):
    if i!=90:
        LETTER+=" "+ chr(i)+ " |"
        LETTER+=" "+ chr(i+32)+ " |"
    else:
        LETTER+=" "+ chr(i)+" |"
        LETTER+=" "+ chr(i+32)
LETTER+=" )"


INT="i . n . t"
CHAR="c . h . a . r"
BOOLEAN="b . o . o . l . e . a . n"
STRING="s . t . r . i . n . g"
SIGNED_INTEGER="( - | eps ) . ( "+DIGIT+ " ) . ( "+DIGIT+ " ) *"
SINGLE_CHARACTER="sq . ( "+LETTER+" ) . sq"
BOOLEAN_STRING="( t . r . u . e ) | ( f . a . l . s . e )"
LITERAL_STRING="dq . ( "+LETTER+" | "+DIGIT+"  | bl ) * . dq"
IDENTIFIER="( "+LETTER+" | _ ) . ( "+LETTER+ " | "+DIGIT+" | _ ) *" 
IF="i . f"
ELSE="e . l . s . e"
WHILE="w . h . i . l . e"
CLASS="c . l . a . s . s    "
RETURN="r .e . t . u . r  .n"
ADD_OP="+"
SUB_OP="-"
MUL_OP="mul_op"
DIV_OP="/"
SEMI_COLON=";"
LPAREN="lp"
RPAREM="rp"
LBRACE="{"
RBRACE="}"
LBRACKET="["
RBRACKET="]"
COMMA=","
class StackClass:

    def __init__(self, itemlist=[]):
        self.items = itemlist

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[-1:][0]

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)
        
class NFA:

    def make_input_symbol(self,postfix):
        op_lst=['(',')','.','*','|']
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
        # this is the precedence order
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
                    #print token
                    return_lst.append(stack.pop())
                stack.push(token)
                    #print return_lst
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
                temp_dict[i]=-1
            
            table_list.append(temp_dict)
        
        i = 0   
        
            
        for elem in table:
            
            for key, value in elem.items():
                
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

class DFA:
    def __init__(self,nfa_object):
        self.nfa_table=nfa_object.nfa_table()
        self.nfa_start_state=nfa_object.start_state()
        self.nfa_end_state=nfa_object.end_state()
        self.keys=nfa_object.keys()
        self.keys.remove('eps')
        self.dfa_table=self.nfa_to_dfa()
       
    def get_e_closure(self,state):
        stack_states = StackClass(list(state))
        e_closure = state
        #print(e_closure)
        while not(stack_states.isEmpty()):
            top_ele = stack_states.pop()
            e_states = self.nfa_table[top_ele]['eps']
            #print(isinstance(e_states, list))
            if e_states != -1 and isinstance(e_states, list):
                for e_state in e_states:
                    #print(e_state)
                    if e_state not in e_closure:
                        e_closure.append(e_state)
                        stack_states.push(e_state)
            elif e_states!=-1:
                if e_states not in e_closure:
                    e_closure.append(e_states)
                    stack_states.push(e_states)
       
        return e_closure
    

    #Construct DFA from NFA, Procedure
    def nfa_to_dfa(self):
       
        state0 = self.get_e_closure([self.nfa_start_state])
        
       
        unmarked_states = []
        self.all_dfa_states = []
        self.all_dfa_states.append(state0)
        unmarked_states.append(state0)
        
        table_list=[] 
        temp_dict=dict()
        for i in self.keys:
            temp_dict[i]=-1
                    
        table_list.append(temp_dict)


        index = -1
        while unmarked_states:
            index = index + 1
            s1 = unmarked_states.pop(0)
            
            for key in self.keys:
                inp_for_closure = []
                for state in s1:
                    val_df = self.nfa_table[state][key]
                    if val_df!=-1:
                        if isinstance(val_df, list):
                            for i in val_df:
                                inp_for_closure.append(i)
                        else:
                            inp_for_closure.append(val_df)
                
                s2 = self.get_e_closure(inp_for_closure)
            
                if s2 not in self.all_dfa_states:
                    self.all_dfa_states.append(s2)
                    unmarked_states.append(s2)
                    
                    temp_dict=dict()
                    for i in self.keys:
                        temp_dict[i]=-1
                    
                    table_list.append(temp_dict)
                    
                table_list[index][key]= self.all_dfa_states.index(s2)
        return table_list
    def check(self,input):
        current_state=0
        for ch in input:
            if ch not in self.keys:
                return False
            current_state=self.dfa_table[current_state][ch]
        final_state=self.all_dfa_states[current_state]
        if self.nfa_end_state in final_state:
            return True
        else:
            return False
test_nfa=NFA(IDENTIFIER)
test_dfa=DFA(test_nfa)

