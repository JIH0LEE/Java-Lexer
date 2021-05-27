cfg=[
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
"EXPR -> EXPR addsub EXPR`", 
"EXPR -> EXPR`",
"EXPR` -> EXPR` multdiv EXPR``",
"EXPR` -> EXPR``",
"EXPR`` -> lparen EXPR``` rparen", 
"EXPR`` -> EXPR```",
"EXPR``` -> id", 
"EXPR``` -> num", 
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
"COND -> COND comp COND`", 
"COND -> COND`",
"COND` -> boolstr",
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
# EXPR -> EXPR addsub EXPR` 
# EXPR -> EXPR`
# EXPR` -> EXPR` multdiv EXPR`` 
# EXPR` -> EXPR```
# EXPR`` -> lparen EXPR``` rparen 
# EXPR`` -> EXPR```
# EXPR``` -> id 
# EXPR``` -> num 
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
# COND -> COND comp COND` 
# COND -> COND`
# COND` -> boolstr
# ELSE -> else lbrace BLOCK rbrace 
# ELSE -> '' 
# RETURN -> return RHS semi 
# CDECL -> class id lbrace ODECL rbrace 
# ODECL -> VDECL ODECL 
# ODECL -> FDECL ODECL 
# ODECL -> ''

    
]

class Cfg():


    def __init__(self,rule_string):
        self.lhs,self.rhs=rule_string.split('->')
        self.lhs=self.lhs.strip()
        self.rhs=self.rhs.strip()
    def reduce(self,input): 
        if self.rhs=="''":
            rt=input+self.lhs
        else:
            idx=input.rfind(self.rhs) 
            rt=input[0:idx]+self.lhs  
        return rt,self.lhs
    def length_of_rhs(self):
        if self.rhs=="''":
            return 0
        rt_length=len(self.rhs.split(' '))    
        return rt_length
        
class CfgList():
    def __init__(self,rules):
        self.cfg_rules=[]
        for ele in rules:
            self.cfg_rules.append(Cfg(ele))
    def reduce(self,input,rule_num):
        rt=self.cfg_rules[rule_num].reduce(input)
        return rt
    def length_of_rhs(self,rule_num):
        return self.cfg_rules[rule_num].length_of_rhs()
