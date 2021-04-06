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

INT="i . n . t"

CHAR="c . h . a . r"

BOOLEAN="b . o . o . l . e . a . n"

STRING="s . t . r . i . n . g"

SIGNED_INTEGER="0 | ( ( - | eps ) . ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 ) . ( "+DIGIT+ " ) * )"

SINGLE_CHARACTER="sq . ( "+LETTER+" ) . sq"

BOOLEAN_STRING="( t . r . u . e ) | ( f . a . l . s . e )"

LITERAL_STRING="dq . ( "+LETTER+" | "+DIGIT+"  | bl ) * . dq"

IDENTIFIER="( "+LETTER+" | _ ) . ( "+LETTER+ " | "+DIGIT+" | _ ) *" 

IF="i . f"

ELSE="e . l . s . e"

WHILE="w . h . i . l . e"

CLASS="c . l . a . s . s"

RETURN="r . e . t . u . r  . n"

ADD_OP="+"

SUB_OP="-"

MUL_OP="mul_op"

DIV_OP="/"

SEMI_COLON=";"

LPAREN="lp"

RPAREN="rp"

LBRACE="{"

RBRACE="}"

LBRACKET="["

RBRACKET="]"

COMMA=","

ASSIGNMENT_OP='='

LESS_THAN_OP='<'

GREATER_THAN_OP='>'

EQUAL_OP='= . ='

LESS_THAN_OR_EQUAL_OP='< . ='

GREATER_THAN_OR_EQUAL_OP='> . ='

NOT_EQUAL_OP='! . ='


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
    elif symbol=='dq':
        symbol='\"'
    elif symbol=='sq':
        symbol='\''   
    elif symbol=="mul_op":
        symbol='*'
    return symbol