from StickyDicT import *
from time import sleep
# Create Sticky Dict called todo-list
SD = Sticky('todo-list')
# Make our Dict a list
SD.Dict = list()
# Add grocery shopping to the todo list
SD.Dict.append("grocery shopping")
# Verify todo list is in the cloud
todo = OrmanNameSpace().sync()["stickies"]["todo-list"]
print(todo)
# Add haircut = to the todo list
SD.Dict.append("haircut")
# 
# Dont forget to walk the dog
SD.Dict.append("walk dog")
# Nevermind on the haircut
SD.Dict.remove("haircut")
#
sleep(1)
#
# Quit python and see how quick you could get that list again in a pinch
quit()
#
#
#
from StickyDicT import Sticky
print( Sticky('todo-list').Dict )
