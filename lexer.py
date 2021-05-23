import sys
from package.dfa_object import *


#function:find token with given input
#keyword and vtype have higher precedence

def lex(input_str):

	# requirement1: If input_string satisfy DFA, do not check other DFA and return 	token name and value

	# requirement2: KEYWORDS DFAs and VtTYPE DFA must take precedence over 	other 	DFAs.

	# requirement3: When input_string starts with '-' and satisfies both INTERGER 	DFA and SUB_OP DFA, check top of token_lst and get suitable token.
    rt_token=dict()
    if VTYPE_dfa.check(input_str):
        rt_token['name']='VTYPE'
        rt_token['value']=input_str
        return rt_token
    if BOOLEAN_dfa.check(input_str):
        rt_token['name']='BOOLSTR'
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
    if SEMI_COLON_dfa.check(input_str):
        rt_token['name']='SEMI'
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

    if COM_OP_dfa.check(input_str):
        rt_token['name']='COMP'
        rt_token['value']=input_str
        return rt_token 
    if ASSIGN_dfa.check(input_str):
        rt_token['name']='ASSIGN'
        rt_token['value']=input_str        
        return rt_token 

    if OP_dfa.check(input_str):
        rt_token['name']='OP'
        rt_token['value']=input_str
        return rt_token      
    if WHITESPACE_dfa.check(input_str):
        rt_token['name']='WHITESPACE'
        rt_token['value']=input_str
        return rt_token 
    if ID_dfa.check(input_str):
        rt_token['name']='ID'
        rt_token['value']=input_str
        return rt_token
    #by peeking token list, choose '-' is signed integer or minus operator
    if INTEGER_dfa.check(input_str):
        if input_str[0]=='-' and token_lst[-1]['name'] in ['RPAREN','ID','INTEGER','RBRACKET','RBRACE']:
            return None
        rt_token['name']='NUM'
        rt_token['value']=input_str
        return rt_token
    if STRING_LITERAL_dfa.check(input_str):
        rt_token['name']='STRING'
        rt_token['value']=input_str
        return rt_token        
    if CHARACTER_dfa.check(input_str):
        rt_token['name']='CHARACTER'
        rt_token['value']=input_str
        return rt_token
    if COMMA_dfa.check(input_str):
        rt_token['name']='COMMA'
        rt_token['value']=input_str
        return rt_token    
    else:
        return None

#print output in file
def print_token(token_list,file):

    for elem in token_list:
        if elem['name']!='WHITESPACE':
            if elem['name'] in ['VTYPE','ID','CHARACTER','BOOLEAN','STRING','INTEGER','OP','COM_OP']: 
                file.write('<'+elem['name']+","+elem['value']+'>\n')
            else:
                file.write('<'+elem['name']+'>\n')




if __name__ == "__main__":
    	# 1. Get symbol from input_string until lex() returns nothing.
		# 2. Add the most recent return token from lexer(). 
		# 3. Then restart to make new token.
		# 4. If the file is read to the end and there is no suitalbe token, an error ocuurs.


    file_name=sys.argv[1]
    try:
        readfile=open(file_name,'r')
    except:
        sys.stderr.write("No file: %s\n" % file_name)
        exit(1)
    data=readfile.read()
    readfile.close()
    token_lst=[]
    token_str=''
    temp_token=None
    token_to_add=None

    for i in range(len(data)):
        token_str+=data[i]
        temp_token=lex(token_str)
        if temp_token!=None:                        
            token_to_add=temp_token    
            if(i==len(data)-1):
                token_lst.append(token_to_add)
            
        else:
            if token_to_add ==None:
                if(i==len(data)-1):
                    sys.exit('Error!!  Invalid token value:'+token_str)
                continue   
            else: 
                token_lst.append(token_to_add)
                token_str=data[i]
                temp_token=lex(token_str)
                token_to_add=temp_token
                if i== len(data)-1:         
                    token_lst.append(token_to_add)

    writefile=open(file_name.split('.')[0]+".out",'w')
    print_token(token_lst,writefile)
    writefile.close()   