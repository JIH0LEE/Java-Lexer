#   Module for defining regular expression

#-------------Operator-------------
#   .   means concatenattion
#   *   means exponentiation 
#   |   means union


# -------------unique token-------------
# nl is '\n'
# tab is '\t'
# bl is ' '
# bar is '|'
# mul_op is '*'
# dot is '.'
# lp is '('
# rp is ')'

# These tokens are used to distinguish them from operators



WHITESPACE="( nl | tab | bl ) *"     

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

TERMINAL_SYMBOL="("                
for i in range(33,40):
    TERMINAL_SYMBOL+=" "+ chr(i)+ " |"
for i in range(43,46):
    TERMINAL_SYMBOL+=" "+ chr(i)+ " |"
for i in range(47,124):
    TERMINAL_SYMBOL+=" "+ chr(i)+ " |"
for i in range(125,127):
    TERMINAL_SYMBOL+=" "+ chr(i)+ " |"
TERMINAL_SYMBOL+=" lp | rp | dot | mul_op | bl | bar )"
    
INT="( i . n . t )"

CHAR="( c . h . a . r )"

BOOL="( b . o . o . l . e . a . n )"

STRING="( s . t . r . i . n . g ) "

VTYPE=INT+' | ' +CHAR+' | '+ BOOL + ' | ' + STRING

INTEGER="0 | ( ( - | eps ) . ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 ) . ( "+DIGIT+ " ) * )"            

CHARACTER="' . "+TERMINAL_SYMBOL+"  . '"

BOOLEAN="( t . r . u . e ) | ( f . a . l . s . e )"

STRING='" . '+TERMINAL_SYMBOL+ ' * . "'

ID="( "+LETTER+" | _ ) . ( "+LETTER+ " | "+DIGIT+" | _ ) *" 

IF="i . f"

ELSE="e . l . s . e"

WHILE="w . h . i . l . e"

CLASS="c . l . a . s . s"

RETURN="r . e . t . u . r  . n"

ADD_OP="+"

SUB_OP="-"

MUL_OP="mul_op"

DIV_OP="/"

OP=ADD_OP+' | '+SUB_OP+' | '+MUL_OP+' | '+DIV_OP

SEMI_COLON=";"

LPAREN="lp"

RPAREN="rp"

LBRACE="{"

RBRACE="}"

LBRACKET="["

RBRACKET="]"

COMMA=","

ASSIGN='='

LESS_THAN_OP='<'

GREATER_THAN_OP='>'

EQUAL_OP='( = . = )'

LESS_THAN_OR_EQUAL_OP='( < . = )'

GREATER_THAN_OR_EQUAL_OP='( > . = )'

NOT_EQUAL_OP='( ! . = )'

COM_OP=LESS_THAN_OP +' | '+GREATER_THAN_OP +' | '+EQUAL_OP+' | '+ LESS_THAN_OR_EQUAL_OP+' | '+ GREATER_THAN_OR_EQUAL_OP+' | '+ NOT_EQUAL_OP

#This function is changing unique symbol which has same form with operator of regular expression 
def make_key(symbol):
    
    if symbol =='nl':
        symbol='\n'
    elif symbol =='tab':
        symbol='\t'
    elif symbol =='bl':
        symbol=' '
    elif symbol=='lp':
        symbol='('
    elif symbol=='rp':
        symbol=')'
    elif symbol=="mul_op":
        symbol='*'
    elif symbol=="dot":
        symbol='.'
    elif symbol=="bar":
        symbol='|'
    return symbol