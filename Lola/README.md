# Lola's work for Text IO 

## Homework
[collections]() (python code)

## Concept

Het concept van mijn script is dat als je een letter invoert er een andere letter of symbool uitkomt. Zo kan je een tekst in code taal schrijven. Het idee is een beetje zoals rot 13. 

Origineel:  	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z

Vervanging:  	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m


## Prototype: working demo

def karakters (n):
    o=""
    key = {'a':'@', 'b':'!!', 'c':'>', 'd':'<', 'e':'?', 'f':'/', 'g':'=', 'h':'+', 
       'i':')', 'j':'(', 'k':'#', 'l':'$', 'm':'%', 'n':'^', 'o':'&', 'p':'*', 
       'q':'[', 'r':']', 's':'{', 't':'}', 'u':';', 'v':'~', 'w':',', 'x':'.',
       'y':'//', 'z':'...', 'A':'<>', 'B':'**', 'C':'$$', 'D':'>@', 'E':'2', 'F':'#_', 
       'G':'-', 'H':'_', 'I':'__', 'J':'±', 'K':'++', 'L':'7', 'M':'{}', 'N':'11', 
       'O':'?', 'P':'66', 'Q':'``', 'R':'+--', 'S':'oo', 'T':'1234', 'U':'+++++', 'V':'xx', 
       'W':'xy', 'X':'Kkk', 'Y':'0_', 'Z':'))'}
    for x in n:
        v = x in key.keys()
        if v==True:
            o+=(key[x])   
        else:
            o+=x
    return o
type= karakters("hier type je de tekst die moet vertaald worden")
print(type)



``de uitkomst zou dan zijn: +)?] }//*? (? <? }?#{} <)? %&?} ~?]}@@$< ,&]<?^

## Design the flow of the program

## How to use the script

## PDF format 
			
