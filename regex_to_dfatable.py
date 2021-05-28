import sys
import pandas as pd
import numpy as np
from module.regex import *
from module.dfa_object import *




if __name__ =="__main__":

        dfa=DFA(NFA('( a | b ) *'))
        _data=dfa.table()
        DFA_trans = pd.DataFrame(_data, columns = dfa.getkeys(), index = range(0, len(_data)), dtype = 'object')
        print(DFA_trans)