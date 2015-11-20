```
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> serie = {'totel': "Homeland", 'main character': "Carrie Matheson"}
>>> 
>>> serie
{'main character': 'Carrie Matheson', 'totel': 'Homeland'}
>>> serie['seizoenen']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'seizoenen'
>>> serie ['serizoenen'] = []
>>> serie
{'serizoenen': [], 'main character': 'Carrie Matheson', 'totel': 'Homeland'}
>>> serie['seizoenen'].append("s01")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'seizoenen'
>>> serie['seizoenen'].append("s01")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'seizoenen'
>>> serie
{'serizoenen': [], 'main character': 'Carrie Matheson', 'totel': 'Homeland'}
>>> serie['serizoenen'].append("s01")
>>> serie['serizoenen'].append("s02")
>>> serie['serizoenen'].append("s03")
>>> serie['serizoenen'].append("s04")
>>> serie
{'serizoenen': ['s01', 's02', 's03', 's04'], 'main character': 'Carrie Matheson', 'totel': 'Homeland'}
>>> 
```