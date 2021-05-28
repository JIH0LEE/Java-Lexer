import pandas as pd
table = pd.read_html('table.html', header=2, encoding='utf-8')
del table[0]['State']

if __name__=="__main__":
    print(table)