'''
      program:Magical Calculator
      Author:Rahul Aggarwal
      copyright:2018
'''
import re
print("Our Magical Calculator:")
print("Type 'quit' to exit")
run=True
previous=0
def performMath():
    global run
    global previous
    equation=""
    if previous==0:
        equation=input("enter a equation:")
    else:
        equation=input(str(previous))
    if equation=="quit":
        run=False
        print('Good bye::::')
    else:
        equation=re.sub('[a-zA-Z,:,;]','',equation)
        if previous==0:
            previous=eval(equation)

        else:
            previous=eval(str(previous)+equation)

while run:
    performMath()