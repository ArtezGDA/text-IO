#EsmeeEllson
#AsciiTable
#In this file you can make your own Aspace Leaflet table. 
#The below usage information is for AsciiTable which uses simple ASCII characters for the table (e.g. -+|). 

from terminaltables import AsciiTable
table_data = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2 column1', 'row2 column2']
]
table = AsciiTable(table_data)
print table.table

+--------------+--------------+
| Heading1     | Heading2     |
+--------------+--------------+
| row1 column1 | row1 column2 |
| row2 column1 | row2 column2 |
+--------------+--------------+

# table_data is a list of lists of strings. 
#The outer list represents the whole table, while the inner lists represents rows. 
#Each row-list holds strings which are the cells of that row.

#The first row can be though of the heading, but it doesn’t have to be. 
#You can turn off the heading separator (the only thing that makes the first row a “heading” row) by setting table.inner_heading_row_border = False.

table.inner_heading_row_border = False
print table.table
+--------------+--------------+
| Heading1     | Heading2     |
| row1 column1 | row1 column2 |
| row2 column1 | row2 column2 |
+--------------+--------------+