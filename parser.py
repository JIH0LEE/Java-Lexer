class Cfg():
    def __init__(self,rule_string):
        self.lhs,self.rhs=rule_string.split('->')
        self.lhs=self.lhs.strip()
        self.rhs=self.rhs.strip()
    def printf(self):
        print(self.lhs,self.rhs)
    def reduce(self,input_string):
        if input_string == self.rhs:
            return self.lhs
        else:
            return None
def parser():
    