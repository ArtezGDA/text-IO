>>> couses = ['Photography', 'Design Philosophy', 'Media Theory', 'Design Research', 'Digital Media', 'Computer Skills', 'Graphic Design', 'Typography']
>>> print len(couses)
8
>>> couses.append(Media Theory lecture series)
  File "<stdin>", line 1
    couses.append(Media Theory lecture series)
                             ^
SyntaxError: invalid syntax
>>> couses.append(9)
>>> 9=[Media Theory lecture series]
  File "<stdin>", line 1
    9=[Media Theory lecture series]
                  ^
SyntaxError: invalid syntax
>>> couses.append(Media Theory lecture series)
  File "<stdin>", line 1
    couses.append(Media Theory lecture series)
                             ^
SyntaxError: invalid syntax
>>> print len(couses)
9
>>> couses.pop(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> couses.pop()9
  File "<stdin>", line 1
    couses.pop()9
                ^
SyntaxError: invalid syntax
>>> couses.pop(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> len(couses)
9