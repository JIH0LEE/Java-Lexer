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
BOOLEAN_STRING="( t . r . u . e | f . a . l . s . e)"
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

print(SINGLE_CHARACTER)
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
    prec['*']=3
    prec['|']=2
    prec['.']=1
    prec['(']=1
    op_lst=['*','|','.']

    tokenlst=infixexpr.split()
    for token in tokenlst:
       
            
        if token == '(':
            stack.push(token)

        elif token == ')':
            topToken=stack.pop()
            while topToken != '(':
                return_lst.append(topToken)
                topToken=stack.pop()
        elif token in op_lst:
            while (not stack.isEmpty()) and (prec[stack.peek()] >= prec[token]):
                #print token
                return_lst.append(stack.pop())
            stack.push(token)
                #print return_lst
        else:
            return_lst.append(token)

            
           

    while not stack.isEmpty():
        opToken=stack.pop()
        return_lst.append(opToken)
        #print return_lst
    return return_lst


postfix = infixtopostfix(INT) 
print(postfix)  

def make_input_symbol(postfix):
    op_lst=['(',')','.','*','|']
    input_symbol_lst=[]
    for symbol in postfix:
        if symbol not in op_lst:
            input_symbol_lst.append(symbol) 
    input_symbol_lst.append('eps')
    return input_symbol_lst   

regex=postfix
keys=make_input_symbol(postfix)        

s=[];stack=[];start=0;end=1

counter=-1;c1=0;c2=0

for i in regex:
    if i in keys:
        counter=counter+1
        c1=counter
        counter=counter+1
        c2=counter
        s.append({})
        s.append({})
        stack.append([c1,c2])
        
        s[c1][i]=c2
    elif i=='*':
        r1,r2=stack.pop()
        counter=counter+1
        c1=counter
        counter=counter+1
        c2=counter
        s.append({})
        s.append({})
        stack.append([c1,c2])
        s[r2]['eps']=[r1,c2]
        s[c1]['eps']=[r1,c2]
        if start==r1:
            start=c1 
        if end==r2:
            end=c2 
    elif i=='.':
        r11,r12=stack.pop()
        r21,r22=stack.pop()
        r12 = r11
        r11 = r22
        stack.append([r21,r12])
        elem = s[r12]
        del s[r12]
        for key in elem.keys():
            s[r11][key] = elem.get(key)-1
        counter = counter - 1
        if start==r11:
            start=r21 
        if end==r22:
            end=r12 
    else:
        counter=counter+1
        c1=counter
        counter=counter+1
        c2=counter
        s.append({})
        s.append({})
        r11,r12=stack.pop()
        r21,r22=stack.pop()
        stack.append([c1,c2])
        s[c1]['eps']=[r21,r11]
        s[r12]['eps']=c2
        s[r22]['eps']=c2
        if start==r11 or start==r21:
            start=c1 
        if end==r22 or end==r12:
            end=c2

print(keys)
print(start)
print(end)
print(s)
import pandas as pd
import numpy as np

arr_mat = np.full((end + 1, len(keys)), [-1])
df_trans = pd.DataFrame(arr_mat, columns = keys, index = range(0, end+1), dtype = 'object')
#print(df_trans)
i = 0   
for elem in s:
    for key, value in elem.items():
        #print(key, value)
        df_trans.at[i,key]=value
    i = i+1
print(df_trans)