import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag

dane = pd.read_csv(r"C:\Users\Adrian Szczeszek\Desktop\HCI\sub-02_trial-04.csv",
 delimiter=',', engine='python',
 names=['kolejnosc','ch1','ch2','ch3','ch4','bodziec'])

#zmienne
mojeDane = dane['ch1']
czestProbkowania=200
czas=len(mojeDane)/czestProbkowania
czas=int(czas) #zaokraglanie
t= np.linspace(0,czas,czas*czestProbkowania)
poprzedni=0
probka=0
kod=[]

#filtracja
przefiltrowany1= ag.pasmowozaporowy(mojeDane, czestProbkowania, 49, 51)
przefiltrowany2= ag.pasmowoprzepustowy(przefiltrowany1, czestProbkowania, 1, 50)

#bezfiltracji
plt.subplot(2, 1, 1)
plt.plot(t, mojeDane[0:czas*czestProbkowania])
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [mV]")
plt.title("a")

#przefiltrowany
plt.subplot(2, 1, 2)
plt.plot(t, przefiltrowany2[0:czas*czestProbkowania])
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [mV]")
plt.title("b")

#odstepy miedzy wykresami
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

#wyswietlanie
plt.show()

#szukanie mrugnięć
for i in przefiltrowany2:
    if i>=0.15 and poprzedni<0.15:
        kod.append(dane['bodziec'][probka])
    poprzedni=i
    probka+=1

#generowanie wymruganego kodu
print("Kod:",kod)
