from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QApplication
from math import *
def verif(ch):
    i=0
    while(i<len(ch) and int(ch[i])%2==0):
        i+=1
    return i==len(ch)
def diviseur(x):
    d=2
    test=True
    while(d<x/2 and test):
        if(x%d==0 and d%2==1):
            test=False
        d+=1
    return test
def super_pairPlus(ch):
    if(verif(ch) and diviseur(int(ch)) and int(ch)%2==0 ):
        return True
    else:
        return False
def play():
    ch=windows.n.text()
    if(int(ch)<0):
        windows.res.setText("introduire un nombre >0")
    elif(super_pairPlus(ch)==True):
        windows.res.setText( ch+ " est super pair plus")
    else:
        windows.res.setText( ch+ " n'est pas super pair plus")

app = QApplication([]) 
windows = loadUi ("superPairPlus.ui") 
windows.show() 
windows.verifier.clicked.connect(play) 
app.exec_()