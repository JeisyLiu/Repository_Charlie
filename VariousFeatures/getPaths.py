import os
tstr1=os.path.abspath(__file__)
tstr2=os.path.dirname(os.path.abspath(__file__))
tstr3=os.getcwd()
print("include this file"+tstr1)
print("without this file"+tstr2)
print(tstr3)