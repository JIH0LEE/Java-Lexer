from package import *

INT_dfa=DFA(NFA(INT))

CHAR_dfa=DFA(NFA(CHAR))
   
BOOLEAN_dfa=DFA(NFA(BOOLEAN))

STRING_dfa=DFA(NFA(STRING))

SIGNED_INTEGER_dfa=DFA(NFA(SIGNED_INTEGER))

SINGLE_CHARACTER_dfa=DFA(NFA(SINGLE_CHARACTER))

BOOLEAN_STRING=DFA(NFA(BOOLEAN_STRING))

LITERAL_STRING_dfa=DFA(NFA(LITERAL_STRING)) 

IDENTIFIER_dfa=DFA(NFA(IDENTIFIER))

IF_dfa=DFA(NFA(IF))

ELSE_dfa=DFA(NFA(ELSE))

WHILE_dfa=DFA(NFA(WHILE))

CLASS_dfa=DFA(NFA(CLASS))

RETURN_dfa=DFA(NFA(RETURN))

ADD_OP_dfa=DFA(NFA(ADD_OP))

SUB_OP_dfa=DFA(NFA(SUB_OP))

MUL_OP_dfa=DFA(NFA(MUL_OP))

DIV_OP_dfa=DFA(NFA(DIV_OP))

SEMI_COLON_dfa=DFA(NFA(SEMI_COLON))

LPAREN_dfa=DFA(NFA(LPAREN))

RPAREN_dfa=DFA(NFA(RPAREN))

LBRACE_dfa=DFA(NFA(LBRACE))

RBRACE_dfa=DFA(NFA(RBRACE))

LBRACKET_dfa=DFA(NFA(LBRACKET))

RBRACKET_dfa=DFA(NFA(RBRACKET))

COMMA_dfa=DFA(NFA(COMMA))

WHITESPACE_dfa=DFA(NFA(WHITESPACE))

ASSIGNMENT_OP_dfa=DFA(NFA(ASSIGNMENT_OP))

LESS_THAN_OP_dfa=DFA(NFA(LESS_THAN_OP))

GREATER_THAN_OP_dfa=DFA(NFA(GREATER_THAN_OP))

EQUAL_OP_dfa=DFA(NFA(EQUAL_OP))

LESS_THAN_OR_EQUAL_OP_dfa=DFA(NFA(LESS_THAN_OR_EQUAL_OP))

GREATER_THAN_OR_EQUAL_OP_dfa=DFA(NFA(GREATER_THAN_OR_EQUAL_OP))

NOT_EQUAL_OP_dfa=DFA(NFA(NOT_EQUAL_OP))


def lex(input_str):

    rt_token=dict()
    if INT_dfa.check(input_str):
        rt_token['name']='INT'
        rt_token['value']=input_str
        return rt_token
    if CHAR_dfa.check(input_str):
        rt_token['name']='CHAR'
        rt_token['value']=input_str
        return rt_token
    if BOOLEAN_dfa.check(input_str):
        rt_token['name']='BOOLEAN'
        rt_token['value']=input_str
        return rt_token
    if STRING_dfa.check(input_str):
        rt_token['name']='STRING'
        rt_token['value']=input_str
        return rt_token
    if WHILE_dfa.check(input_str):
        rt_token['name']='WHILE'
        rt_token['value']=input_str
        return rt_token
    if IF_dfa.check(input_str):
        rt_token['name']='IF'
        rt_token['value']=input_str
        return rt_token
    if ELSE_dfa.check(input_str):
        rt_token['name']='ELSE'
        rt_token['value']=input_str
        return rt_token
    if CLASS_dfa.check(input_str):
        rt_token['name']='CLASS'
        rt_token['value']=input_str
        return rt_token 
    if RETURN_dfa.check(input_str):
        rt_token['name']='RETURN'
        rt_token['value']=input_str
        return rt_token     
    if WHITESPACE_dfa.check(input_str):
        rt_token['name']='WHITESPACE'
        rt_token['value']=input_str
        return rt_token 
    if IDENTIFIER_dfa.check(input_str):
        rt_token['name']='IDENTIFIER'
        rt_token['value']=input_str
        return rt_token
    if SUB_OP_dfa.check(input_str):
        rt_token['name']='SUB_OP'
        rt_token['value']=input_str
        return rt_token 
    if SIGNED_INTEGER_dfa.check(input_str):
        if input_str[0]=='-' and token_lst[-1]['name'] in ['RPAREN','IDENTIFIER','SIGNED_INTEGER','RBRACKET','RBRACE']:
            return None
        rt_token['name']='SIGNED_INTEGER'
        rt_token['value']=input_str
        return rt_token
    if LITERAL_STRING_dfa.check(input_str):
        rt_token['name']='LITERAL_STRING'
        rt_token['value']=input_str
        return rt_token        
    if SINGLE_CHARACTER_dfa.check(input_str):
        rt_token['name']='SINGLE_CHARACTER'
        rt_token['value']=input_str
        return rt_token
    if ADD_OP_dfa.check(input_str):
        rt_token['name']='ADD_OP'
        rt_token['value']=input_str
        return rt_token  
    if MUL_OP_dfa.check(input_str):
        rt_token['name']='MUL_OP'
        rt_token['value']=input_str
        return rt_token 
    if DIV_OP_dfa.check(input_str):
        rt_token['name']='DIV_OP'
        rt_token['value']=input_str
        return rt_token 
    if SEMI_COLON_dfa.check(input_str):
        rt_token['name']='SEMICOLON'
        rt_token['value']=input_str
        return rt_token 
    if LPAREN_dfa.check(input_str):
        rt_token['name']='LPAREN'
        rt_token['value']=input_str
        return rt_token 
    if RPAREN_dfa.check(input_str):
        rt_token['name']='RPAREN'
        rt_token['value']=input_str
        return rt_token 
    if LBRACE_dfa.check(input_str):
        rt_token['name']='LBRACE'
        rt_token['value']=input_str
        return rt_token 
    if RBRACE_dfa.check(input_str):
        rt_token['name']='RBRACE'
        rt_token['value']=input_str
        return rt_token 
    if LBRACKET_dfa.check(input_str):
        rt_token['name']='LBRACKET'
        rt_token['value']=input_str
        return rt_token 
    if RBRACKET_dfa.check(input_str):
        rt_token['name']='RBRACKET'
        rt_token['value']=input_str
        return rt_token 
    if COMMA_dfa.check(input_str):
        rt_token['name']='COMMA'
        rt_token['value']=input_str
        return rt_token 
    if LESS_THAN_OP_dfa.check(input_str):
        rt_token['name']='LESS_THAN_OP'
        rt_token['value']=input_str
        return rt_token 
    if GREATER_THAN_OP_dfa.check(input_str):
        rt_token['name']='GREATER_THAN_OP'
        rt_token['value']=input_str
        return rt_token 
    if EQUAL_OP_dfa.check(input_str):
        rt_token['name']='EQAUL_OP'
        rt_token['value']=input_str
        return rt_token 
    if ASSIGNMENT_OP_dfa.check(input_str):
        rt_token['name']='ASSIGNMENT_OP'
        rt_token['value']=input_str
        return rt_token 
    if NOT_EQUAL_OP_dfa.check(input_str):
        rt_token['name']='NOT_EQAUL_OP'
        rt_token['value']=input_str
        return rt_token 
    if GREATER_THAN_OR_EQUAL_OP_dfa.check(input_str):
        rt_token['name']='GREATER_THAN_OR_EQUAL_OP'
        rt_token['value']=input_str
        return rt_token 
    if LESS_THAN_OR_EQUAL_OP_dfa.check(input_str):
        rt_token['name']='LESS_THAN_OR_EQUAL_OP'
        rt_token['value']=input_str
        return rt_token 
    else:
        return None




f=open('test.txt','r')
data=f.read()
token_lst=[]
token_str=''
temp_token=dict()
for ch in data:
    token_str+=ch
    token_to_add=temp_token
    temp_token=lex(token_str)
    if temp_token==None:
        token_lst.append(token_to_add)  
        token_str=ch
        temp_token=lex(token_str)
print(token_lst)
    

