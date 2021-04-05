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