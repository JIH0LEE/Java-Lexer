from nfa import NFA
from StackClass import StackClass
import pandas as pd
import numpy as np


class DFA:

    def __init__(self,nfa_object):
        self.nfa_table=nfa_object.nfa_table()
        self.nfa_start_state=nfa_object.start_state()
        self.nfa_end_state=nfa_object.end_state()
        self.keys=nfa_object.keys()
        self.keys.remove('eps')
        self.dfa_table=self.nfa_to_dfa()
    def get_e_closure(self,state):
        stack_states = StackClass(list(state))
        e_closure = state
        #print(e_closure)
        while not(stack_states.isEmpty()):
            top_ele = stack_states.pop()
            e_states = self.nfa_table.at[top_ele, 'eps']
            #print(isinstance(e_states, list))
            if e_states != -1 and isinstance(e_states, list):
                for e_state in e_states:
                    #print(e_state)
                    if e_state not in e_closure:
                        e_closure.append(e_state)
                        stack_states.push(e_state)
            elif e_states!=-1:
                if e_states not in e_closure:
                    e_closure.append(e_states)
                    stack_states.push(e_states)
        print(e_closure)
        return e_closure
    # get_e_closure([2,3])

    #Construct DFA from NFA, Procedure
    def nfa_to_dfa(self):

        state0 = self.get_e_closure(list(map(int,str(self.nfa_start_state))))
        unmarked_states = []
        self.all_dfa_states = []
        self.all_dfa_states.append(state0)
        unmarked_states.append(state0)
        print(unmarked_states)
        print(self.keys)
        arr_mat = np.full((1, len(self.keys)), [-1])
        DFA_trans = pd.DataFrame(arr_mat, columns = self.keys) 


        index = -1
        while unmarked_states:
            index = index + 1
            s1 = unmarked_states.pop(0)
            
            for key in self.keys:
                inp_for_closure = []
                for state in s1:
                    val_df = self.nfa_table.at[state, key]
                    if val_df!=-1:
                        if isinstance(val_df, list):
                            for i in val_df:
                                inp_for_closure.append(i)
                        else:
                            inp_for_closure.append(val_df)
                #print(inp_for_closure)
                s2 = self.get_e_closure(inp_for_closure)
            
                if s2 not in self.all_dfa_states:
                    self.all_dfa_states.append(s2)
                    unmarked_states.append(s2)
                    DFA_trans = DFA_trans.append(pd.DataFrame(arr_mat, columns = self.keys), ignore_index = True)
                DFA_trans.at[index, key]= self.all_dfa_states.index(s2)
        return DFA_trans
    def check(self,input):
        current_state=0
        for ch in input:
            if ch not in self.keys:
                return False
            current_state=self.dfa_table[current_state,ch]
        final_state=self.all_dfa_states[current_state]
        if self.nfa_end_state in final_state:
            return True
        else:
            return False

