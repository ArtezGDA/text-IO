#EsmeeEllson
#Help

#Class Attributes
#You can instantiate with AsciiTable(table_data) or AsciiTable(table_data, 'Table Title'). 
#These are available after instantiating AsciiTable.

Name						Description/Notes
table_data					= List of list of strings. Same object passed to __init__().
title						= Table title string. Default is None for no title.
inner_column_border			= Default is True. Separates columns.
inner_heading_row_border	= Default is True. This is what makes the first row a “header row”.
inner_row_border			= Default is False. This adds lines between rows.
justify_columns				= Dictionary. Keys are column numbers (0 base), values are ‘left’, ‘right’, or ‘center’.
outer_border				= Default is True. Toggles the top, bottom, left, and right table borders.
padding_left				= Default is 1. Number of spaces to add to the left of the cell.
padding_right				= Default is 1. Number of spaces to add to the right of the cell.

#Class Methods
#These are regular methods available in either class.

Name						Description/Notes
column_max_width			= Takes one argument, column number (0 base). Returns The maximum size it will fit in the the 								therminal without breaking the table. Takes other columns into account.

#Class Properties
#These are read-only properties after you instantiate either class. They are “real-time”. You do not have to re-instantiate if you change any of the class attributes, including table_data.

Name						Description/Notes
column_widths				= Returns a list with the current column widths (one int per column) without padding.
ok							= Returns True if the table fits within the terminal width, False if the table breaks.
padded_table_data			= Returns the padding table data. With spaces and newlines. Does not include borders.
table						= Returns a large string, the whole table. This may be printed to the terminal.
table_width					= Returns the width of the table including padding and borders.