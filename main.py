from package import *

test_nfa=NFA(IDENTIFIER)
test_dfa=DFA(test_nfa)
print(test_dfa.check('_abd'))

