#Regex

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
IDENTIFIER="( "+LETTER+" | _ ) . ( "+LETTER+ " | "+DIGIT+" | _ ) . *" 
IF="i . f"
ELSE="e . l . s . e"
WHILE="w . h . i . l . e"
CLASS="c . l . a . s . s    "
RETURN="r .e . t . u .r  .n"
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

print(BOOLEAN_STRING)
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
        
def infixtopostfix(infixexpr):

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
    print(token_lst)
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


postfix = infixtopostfix(BOOLEAN_STRING) 
print(postfix)  

def make_input_symbol(postfix):
    op_lst=['(',')','.','*','|']
    input_symbol_lst=[]
    for symbol in postfix:
        if symbol not in op_lst and symbol not in input_symbol_lst:
            input_symbol_lst.append(symbol) 
    input_symbol_lst.append('eps')
    return input_symbol_lst   

regex=postfix
keys=make_input_symbol(postfix)        

table=[];stack=[];start_state=0;end_state=1

state_num=-1;new_state1=0;new_state2=0

for i in regex:
    if i in keys:
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
        if start_state==state1:
            start_state=new_state1 
        if end_state==state2:
            end_state=new_state2 
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
        if start_state==state1_1:
            start_state=state2_1 
        if end_state==state2_2:
            end_state=state1_2 
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
        if start_state==state1_1 or start_state==state2_1:
            start_state=new_state1 
        if end_state==state2_2 or end_state==state1_2:
            end_state=new_state2

print(keys)
print(start_state)
print(end_state)
print(table)
import pandas as pd
import numpy as np

arr_mat = np.full((end_state + 1, len(keys)), [-1])
df_trans = pd.DataFrame(arr_mat, columns = keys, index = range(0, end_state+1), dtype = 'object')
#print(df_trans)
i = 0   
for elem in table:
    for key, value in elem.items():
        #print(key, value)
        df_trans.at[i,key]=value
    i = i+1
print(df_trans)


#Convert NFA to DFA, get all the e-closures
# def get_e_closure(state):
#     stack_states = StackClass(list(state))
#     e_closure = state
#     #print(e_closure)
#     while not(stack_states.isEmpty()):
#         top_ele = stack_states.pop()
#         e_states = df_trans.at[top_ele, 'eps']
#         #print(isinstance(e_states, list))
#         if e_states != -1 and isinstance(e_states, list):
#             for e_state in e_states:
#                 #print(e_state)
#                 if e_state not in e_closure:
#                     e_closure.append(e_state)
#                     stack_states.push(e_state)
#         elif e_states!=-1:
#             if e_states not in e_closure:
#                 e_closure.append(e_states)
#                 stack_states.push(e_states)
#     print(e_closure)
#     return e_closure
# # get_e_closure([2,3])

# #Construct DFA from NFA, Procedure
# state0 = get_e_closure(list(map(int,str(start_state))))
# unmarked_states = []
# all_dfa_states = []
# all_dfa_states.append(state0)
# unmarked_states.append(state0)
# print(unmarked_states)
# keys_dfa=keys
# keys_dfa.remove('eps')
# print(keys_dfa)
# arr_mat = np.full((1, len(keys_dfa)), [-1])
# DFA_trans = pd.DataFrame(arr_mat, columns = keys_dfa) 


# index = -1
# while unmarked_states:
#     index = index + 1
#     s1 = unmarked_states.pop(0)
    
#     for key in keys_dfa:
#         inp_for_closure = []
#         for state in s1:
#             val_df = df_trans.at[state, key]
#             if val_df!=-1:
#                 if isinstance(val_df, list):
#                     for i in val_df:
#                         inp_for_closure.append(i)
#                 else:
#                     inp_for_closure.append(val_df)
#         #print(inp_for_closure)
#         s2 = get_e_closure(inp_for_closure)
    
#         if s2 not in all_dfa_states:
#             all_dfa_states.append(s2)
#             unmarked_states.append(s2)
#             DFA_trans = DFA_trans.append(pd.DataFrame(arr_mat, columns = keys_dfa), ignore_index = True)
#         DFA_trans.at[index, key]= all_dfa_states.index(s2)
# print(DFA_trans)
# print(all_dfa_states)