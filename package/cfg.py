CFG=[
"CODE' -> CODE",
"CODE -> VDECL CODE", 
"CODE -> FDECL CODE", 
"CODE -> CDECL CODE",
"CODE -> ''",
"VDECL -> vtype id semi", 
"VDECL -> vtype ASSIGN semi",
"ASSIGN -> id assign RHS",
"RHS -> EXPR", 
"RHS -> literal", 
"RHS -> character", 
"RHS -> boolstr", 
"EXPR -> EXPR addsub EXPR_", 
"EXPR -> EXPR_",
"EXPR_ -> EXPR_ multdiv EXPR__",
"EXPR_ -> EXPR__",
"EXPR__ -> lparen EXPR___ rparen", 
"EXPR__ -> EXPR___",
"EXPR___ -> id", 
"EXPR___ -> num", 
"FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace", 
"ARG -> vtype id MOREARGS", 
"ARG -> ''", 
"MOREARGS -> comma vtype id MOREARGS", 
"MOREARGS -> ''", 
"BLOCK -> STMT BLOCK", 
"BLOCK -> ''", 
"STMT -> VDECL", 
"STMT -> ASSIGN semi", 
"STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE", 
"STMT -> while lparen COND rparen lbrace BLOCK rbrace",
"COND -> COND comp COND_", 
"COND_ -> boolstr",
"ELSE -> else lbrace BLOCK rbrace", 
"ELSE -> ''", 
"RETURN -> return RHS semi", 
"CDECL -> class id lbrace ODECL rbrace", 
"ODECL -> VDECL ODECL", 
"ODECL -> FDECL ODECL", 
"ODECL -> ''"
# CODE' -> CODE
# CODE -> VDECL CODE 
# CODE -> FDECL CODE 
# CODE -> CDECL CODE
# CODE -> ''
# VDECL -> vtype id semi 
# VDECL -> vtype ASSIGN semi
# ASSIGN -> id assign RHS
# RHS -> EXPR 
# RHS -> literal 
# RHS -> character 
# RHS -> boolstr 
# EXPR -> EXPR addsub EXPR_ 
# EXPR -> EXPR_
# EXPR_ -> EXPR_ multdiv EXPR__ 
# EXPR_ -> EXPR__
# EXPR__ -> lparen EXPR___ rparen 
# EXPR__ -> EXPR___
# EXPR___ -> id 
# EXPR___ -> num 
# FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace 
# ARG -> vtype id MOREARGS 
# ARG -> '' 
# MOREARGS -> comma vtype id MOREARGS 
# MOREARGS -> '' 
# BLOCK -> STMT BLOCK 
# BLOCK -> '' 
# STMT -> VDECL 
# STMT -> ASSIGN semi 
# STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE 
# STMT -> while lparen COND rparen lbrace BLOCK rbrace
# COND -> COND comp COND_ 
# COND_ -> boolstr
# ELSE -> else lbrace BLOCK rbrace 
# ELSE -> '' 
# RETURN -> return RHS semi 
# CDECL -> class id lbrace ODECL rbrace 
# ODECL -> VDECL ODECL 
# ODECL -> FDECL ODECL 
# ODECL -> ''

    
]
