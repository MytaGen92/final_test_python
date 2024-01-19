import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10

columne_name_1 = lst[0]
columne_name_2 = lst[len(lst)-1]

random.shuffle(lst)

new_lst_1 = []
new_lst_2 = []

for item in lst:
    if item == lst[0]:
        new_lst_1.append(1)
        new_lst_2.append(0)
    else:
        new_lst_1.append(0)
        new_lst_2.append(1)

print(pd.DataFrame({columne_name_1: new_lst_1, columne_name_2: new_lst_2}))
