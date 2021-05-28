from .nfa import NFA
from .stackclass import StackClass
from .regex import make_key

class DFA:
    def __init__(self,nfa_object):

        self.nfa=nfa_object
        self.keys=self.__change_key_form(self.nfa.keys())
        self.__make_e_closure_each_State()
        self.__dfa_table=self.__nfa_to_dfa()

    #function: make nfa keys to dfa keys by removing epsilon
    def __change_key_form(self,nfa_keys):

        rt_key=[]
        for i in nfa_keys:
            if i!='eps':
                rt_key.append(make_key(i))
        
        return rt_key
        

    def __make_e_closure_each_State(self):
        self.__e_closure=list()
        for i in range(0,self.nfa.end_state()+1):
            self.__e_closure.append(set())
        for i in range(0,self.nfa.end_state()+1):
            e_closure=set()
            checked=set()
            e_closure.add(i)
            while True:
                temp=e_closure-checked
                for j in temp:

                    if self.nfa.nfa_table()[j]['eps'] !=-1:
                        if not isinstance(self.nfa.nfa_table()[j]['eps'],list):
                            e_closure=e_closure | set([self.nfa.nfa_table()[j]['eps']])
                        else:
                            e_closure=e_closure | set(self.nfa.nfa_table()[j]['eps'])
                    checked.add(j)

                if e_closure==checked:
                    break

            self.__e_closure[i]=set(sorted(list(e_closure)))

        return self.__e_closure
    #function: get states with epsilon move
    def __get_e_closure(self,state):

        states_stack = StackClass(list(state))
        e_closure =set()
        while not(states_stack.isEmpty()):
            top_ele = states_stack.pop()

            e_closure=e_closure|self.__e_closure[top_ele]
        return list(e_closure)

    
    # #function: make nfa to dfa with Subset construct algorithm
    def __nfa_to_dfa(self):
        
        # state0 = self.__get_e_closure([self.nfa.start_state()])
        state0 = self.__e_closure[self.nfa.start_state()]
        unmarked_states = []
        self.all_dfa_states = []
        self.all_dfa_states.append(state0)
        unmarked_states.append(state0)
        table_list=[] 
        temp_dict=dict()
        for i in self.keys:
            temp_dict[i]=-1       
        table_list.append(temp_dict)
        state_num = -1
        while unmarked_states:
            state_num = state_num + 1
            unmarked_state = unmarked_states.pop(0)
            for key in self.keys:
                lst_for_e_closure = []
                for state in unmarked_state:
                    value = self.nfa.nfa_table()[state][key]
                    if value!=-1:
                        if isinstance(value, list):
                            for i in value:
                                lst_for_e_closure.append(i)
                        else:
                            lst_for_e_closure.append(value)
                new_state = self.__get_e_closure(lst_for_e_closure)
                if new_state==[]:
                    new_state=-1
                    
                if new_state not in self.all_dfa_states:
                    if new_state!=-1:
                        self.all_dfa_states.append(new_state)
                        unmarked_states.append(new_state)
                        temp_dict=dict()
                        for i in self.keys:
                            temp_dict[i]=-1
                        table_list.append(temp_dict)
                if new_state!=-1:
                    table_list[state_num][key]= self.all_dfa_states.index(new_state)
                else:
                    table_list[state_num][key]= -1

        return table_list

    #function:check is true when final state has end state
    #If state is empty set return false
    def check(self,input):
        current_state=0
        for ch in input:
            if ch not in self.keys:
                return False
            current_state=self.__dfa_table[current_state][ch]
            if current_state==-1:
                return False
        final_state=self.all_dfa_states[current_state]
        if self.nfa.end_state() in final_state:
            return True
        else:
            return False
        
    def table(self):
        return self.__dfa_table
        
    def getkeys(self):
        return self.keys