from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QApplication
from math import *
def premier(x):
    d=2
    while(d<x/2 and x%d!=0):
        d+=1
    return d>x/2
def lisse(x):
    if(premier(x)==True):
        return False
    d=2
    max=0
    while(d<=x/2):
        if(x%d==0 and premier(d)):
            max=d
        d+=1
    return max<=sqrt(x)
def play():
    n=windows.n.text()
    if(int(n)<1):
        windows.res.setText("veuillez saisir un nombre >1")
    elif(lisse(int(n))):
        windows.res.setText(n+" est lisse")
    else:
        windows.res.setText(n+" n'est pas lisse")

app = QApplication([]) 
windows = loadUi ("InterfaceLisse.ui") 
windows.show() 
windows.verifier.clicked.connect(play) 
app.exec_()
