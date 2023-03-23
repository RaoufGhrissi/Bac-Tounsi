from PyQt5.uic import loadUi 
from PyQt5.QtWidgets import QApplication
def premier(x):
    d=2
    while(d<x//2+1 and x%d!=0):
        d+=1
    return d>x//2


def SemiPremier(N):
    d=2
    while(d<N//2+1):
        if(N%d==0 and premier(d) and premier(N//d)) :
            return True
        else:
            d=d+1
    return False

def play():
    ch=windows.nbr.text()
    if int(ch)<=2:
        mes="veuillez introduire un nombre>2"
    elif SemiPremier(int(ch))==False:
        mes=ch+"n'est pas semi-premier"
    else:
        mes=ch+"est semi-premier"
    windows.res.setText(mes)


app = QApplication([]) 
windows = loadUi ("InterfaceSemiPremier.ui") 
windows.show() 
windows.verif.clicked.connect(play) 
app.exec_()