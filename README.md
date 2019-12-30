# PyEditplusCodeTips
An code tips tools for editplus code with python.

open editplus tools -> configure user tools
add new tool with program, input tool name as you want, input python path in command textbox, in arguments textbox input :
path\to\tiplist.py "$(FileDir)" "$(CurWord)"

action combobox select the Run as text filter(replace).

press ok

add Tips.dat file to edit file path, and put tips in it, one tip per line. save it.

in edit window, press ctrl+num , no text input will show all list, if has chars before cursor, will filter all tips prefix with chars.

