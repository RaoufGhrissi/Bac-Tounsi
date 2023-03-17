from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QApplication

def ondulant(ch):
    a=ch[0]
    b=ch[1]
    i=0
    test=True
    while( test==True and  i<len(ch)):
        if(i%2==1 and ch[i]!=b):
            test=False
        elif(i%2==0 and ch[i]!=a):
            test=False
        else:
            i+=1
    return test


def play():
    ch=windows.n.text()
    if int(ch)<100:
        mes="veuiller introduire un nombre>100"
    elif ondulant(ch)==False:
        mes=ch+" n'est pas ondulant"
    else:
        mes=ch+" est ondulant"
    
    windows.res.setText(mes)
    
app = QApplication([]) 
windows=loadUi("nombreOndulant.ui") 
windows.show() 
windows.verifier.clicked.connect(play)
app.exec_()