import sys
import pandas as pd
import numpy as np
from package.regex import *
from package import *




if __name__ =="__main__":
    for elem in regex_lst:
       
        dfa=DFA(NFA(elem))
        _data=dfa.table()
    
        DFA_trans = pd.DataFrame(_data, columns = dfa.getkeys(), index = range(0, len(_data)), dtype = 'object')
        print(DFA_trans)