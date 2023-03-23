from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QApplication
from math import *
def premier(x):
    d=2
    while(d<x/2 and x%d!=0):
        d=d+1
    return d>x/2

def lisse(x):
    d=2
    max=2
    while(d<x/2):
        d=d+1
        if(premier(d) and x%d==0 ):
            max=d
    return max<=sqrt(x)


def play():
    ch=windows.n.text()
    if(int(ch)<1):
        windows.res.setText("introduire un nombre >1")
    elif(lisse(int(ch))==True):
        windows.res.setText( ch+ " est lisse")
    else:
        windows.res.setText( ch+ " n'est pas lisse")

app = QApplication([]) 
windows = loadUi ("InterfaceLisse.ui") 
windows.show() 
windows.verifier.clicked.connect(play) 
app.exec_()