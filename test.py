
DIGIT="("
for i in range(48,58):
    if i!=57:
        DIGIT+=" '"+ chr(i)+ "' |"
    else:
        DIGIT+=" '"+ chr(i)+"'"
DIGIT+=" )"
LETTER="("
for i in range(65,91):
    if i!=91:
        LETTER+=" '"+ chr(i)+ "' |"
        LETTER+=" '"+ chr(i+32)+ "' |"
    else:
        LETTER+=" '"+ chr(i)+"' |"
        LETTER+=" '"+ chr(i+32)+"'"
LETTER+=" )"
IDENTIFIER="( "+LETTER+" | '_' ) ( "+LETTER+ " | "+DIGIT+" | '_' ) *" 
print(IDENTIFIER)

