import pandas as pd

data = {
        'Yes': [50,21],
        'No': [131,2]
        }

dat = pd.DataFrame(data)

print(dat)

data1 = {'Bob': ['I liked it.', 'It was awful.'],
         'Sue': ['Pretty good.', 'Bland.']
         }

dat1 = pd.DataFrame(data1, index=['Product A','Product B'])
print(dat1)

serie = [30,35,40]
item = pd.Series(serie, index=['2015 Salees','2016 Sales','2017 Sales'], name= 'Product A')
print(item)
