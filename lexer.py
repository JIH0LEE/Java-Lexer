import sys
from package.dfa_object import *


#function:find token with given input
#keyword and vtype have higher precedence

def lex(input_str,line_num):

	# requirement1: If input_string satisfy DFA, do not check other DFA and return 	token name and value

	# requirement2: KEYWORDS DFAs and VtTYPE DFA must take precedence over 	other 	DFAs.

	# requirement3: When input_string starts with '-' and satisfies both INTERGER 	DFA and SUB_OP DFA, check top of token_lst and get suitable token.
    rt_token=dict()
    rt_token['value']=input_str
    rt_token['line_num']=line_num
    if VTYPE_dfa.check(input_str):
        rt_token['name']='VTYPE'
        
        return rt_token
    if BOOLEAN_dfa.check(input_str):
        rt_token['name']='BOOLSTR'
        
        return rt_token
    if WHILE_dfa.check(input_str):
        rt_token['name']='WHILE'
        
        return rt_token
    if IF_dfa.check(input_str):
        rt_token['name']='IF'
        
        return rt_token
    if ELSE_dfa.check(input_str):
        rt_token['name']='ELSE'
        
        return rt_token
    if CLASS_dfa.check(input_str):
        rt_token['name']='CLASS'
        
        return rt_token 
    if RETURN_dfa.check(input_str):
        rt_token['name']='RETURN'
        
        return rt_token
    if SEMI_COLON_dfa.check(input_str):
        rt_token['name']='SEMI'
        
        return rt_token 
    if LPAREN_dfa.check(input_str):
        rt_token['name']='LPAREN'
        
        return rt_token 
    if RPAREN_dfa.check(input_str):
        rt_token['name']='RPAREN'
        
        return rt_token 
    if LBRACE_dfa.check(input_str):
        rt_token['name']='LBRACE'
        
        return rt_token 
    if RBRACE_dfa.check(input_str):
        rt_token['name']='RBRACE'
        
        return rt_token 
    if LBRACKET_dfa.check(input_str):
        rt_token['name']='LBRACKET'
        
        return rt_token 
    if RBRACKET_dfa.check(input_str):
        rt_token['name']='RBRACKET'
        
        return rt_token 

    if COM_OP_dfa.check(input_str):
        rt_token['name']='COMP'
        
        return rt_token 
    if ASSIGN_dfa.check(input_str):
        rt_token['name']='ASSIGN'
                
        return rt_token 

    if OP_dfa.check(input_str):
        rt_token['name']='OP'
        
        return rt_token      
    if WHITESPACE_dfa.check(input_str):
        rt_token['name']='WHITESPACE'
        
        return rt_token 
    if ID_dfa.check(input_str):
        rt_token['name']='ID'
        
        return rt_token
    #by peeking token list, choose '-' is signed integer or minus operator
    if INTEGER_dfa.check(input_str):
        if input_str[0]=='-' and token_lst[-1]['name'] in ['RPAREN','ID','INTEGER','RBRACKET','RBRACE']:
            return None
        rt_token['name']='NUM'
        
        return rt_token
    if STRING_LITERAL_dfa.check(input_str):
        rt_token['name']='STRING'
        
        return rt_token        
    if CHARACTER_dfa.check(input_str):
        rt_token['name']='CHARACTER'
        
        return rt_token
    if COMMA_dfa.check(input_str):
        rt_token['name']='COMMA'
        
        return rt_token    
    else:
        return None

#print output in file
def print_token(token_list,file):

    for elem in token_list:
        if elem['name']!='WHITESPACE':
            if elem['name'] in ['VTYPE','ID','CHARACTER','BOOLEAN','STRING','INTEGER','OP','COM_OP']: 
                file.write('<'+str(elem['line_num'])+","+elem['name']+","+elem['value']+'>\n')
            else:
                file.write('<'+str(elem['line_num'])+","+elem['name']+","+elem['value']+'>\n')




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
    lines=readfile.readlines()
    readfile.close()
    token_lst=[]
    token_str=''
    temp_token=None
    token_to_add=None
    line_num=1
    for data in lines:     
        for i in range(len(data)):
            token_str+=data[i]       
            temp_token=lex(token_str,line_num)
            if temp_token!=None:                        
                token_to_add=temp_token    
                if(i==len(data)-1):
                    token_lst.append(token_to_add)
            else:
                if token_to_add ==None:
                    if(i==len(data)-1):
                        sys.exit('Error!!  Invalid token value:'+token_str+ "in line",line_num)
                    continue   
                else: 
                    token_lst.append(token_to_add)
                    token_str=data[i]
                    temp_token=lex(token_str,line_num)
                    token_to_add=temp_token
                    if i== len(data)-1:         
                        token_lst.append(token_to_add)
        line_num+=1
    writefile=open(file_name.split('.')[0]+".out",'w')
    print_token(token_lst,writefile)
    writefile.close()   