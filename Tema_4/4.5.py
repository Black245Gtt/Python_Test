lst1 = ['Санкт - Петербург', 'Москва', 'Казань' ]
lst2 = ['Воронеж', 'Санкт - Петербург','Иваново' ]
lst3 = []
print([i for i in lst1 if i in lst2])

for i in lst1:
    if i not in lst2:
      lst3.append(i)

for i in lst2:
    if i not in lst1:
      lst3.append(i)
print(lst3)