from .nfa import NFA
from .stackclass import StackClass
from .regex import make_key

class DFA:
    def __init__(self,nfa_object):

        self.nfa_table=nfa_object.nfa_table()
        self.nfa_start_state=nfa_object.start_state()
        self.nfa_end_state=nfa_object.end_state()
        self.keys=self.change_key_form(nfa_object.keys())
        self.dfa_table=self.nfa_to_dfa()


    def change_key_form(self,nfa_keys):

        rt_key=[]
        for i in nfa_keys:
            rt_key.append(make_key(i))
        rt_key.remove('eps')
        return rt_key
        

    def get_e_closure(self,state):

        states_stack = StackClass(list(state))
        e_closure = state
        while not(states_stack.isEmpty()):
            top_ele = states_stack.pop()
            e_states = self.nfa_table[top_ele]['eps']
            if e_states != -1 and isinstance(e_states, list):
                for e_state in e_states:
                    if e_state not in e_closure:
                        e_closure.append(e_state)
                        states_stack.push(e_state)
            elif e_states!=-1:
                if e_states not in e_closure:
                    e_closure.append(e_states)
                    states_stack.push(e_states)
        return e_closure
    

    def nfa_to_dfa(self):
       
        state0 = self.get_e_closure([self.nfa_start_state])
        unmarked_states = []
        self.all_dfa_states = []
        self.all_dfa_states.append(state0)
        unmarked_states.append(state0)
        table_list=[] 
        temp_dict=dict()
        for i in self.keys:
            temp_dict[i]=-1       
        table_list.append(temp_dict)
        index = -1
        while unmarked_states:
            index = index + 1
            unmarked_state = unmarked_states.pop(0)
            for key in self.keys:
                inp_for_closure = []
                for state in unmarked_state:
                    val_df = self.nfa_table[state][key]
                    if val_df!=-1:
                        if isinstance(val_df, list):
                            for i in val_df:
                                inp_for_closure.append(i)
                        else:
                            inp_for_closure.append(val_df)
                new_state = self.get_e_closure(inp_for_closure)
                if new_state not in self.all_dfa_states:
                    self.all_dfa_states.append(new_state)
                    unmarked_states.append(new_state)
                    temp_dict=dict()
                    for i in self.keys:
                        temp_dict[i]=-1
                    table_list.append(temp_dict)
                table_list[index][key]= self.all_dfa_states.index(new_state)
        return table_list


    def check(self,input):
        current_state=0
        for ch in input:
            if ch not in self.keys:
                return False
            current_state=self.dfa_table[current_state][ch]
        final_state=self.all_dfa_states[current_state]
        if self.nfa_end_state in final_state:
            return True
        else:
            return False