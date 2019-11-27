import numpy as np                                     #импортируем библитеки 
import matplotlib.pyplot as plt
G=6.6743*10**(-11)
R=np.arange(2*10**4, 10**9, 2*10**5)
c=299792458
M=2.464*10**31
#нейтронная звезда
def grafic(M=2.464*10**31):
    x=np.linspace(19*10**3, 5*10**4, 10**3)
    y = (4*G*M)/(x*c**2)                      #функция графика                                  #пространство                #линия X
    plt.plot(x,y,color='y', label = 'Нейтронная звезда')
    plt.xlabel('Прицельное расстояние')
    plt.ylabel('Угол отклонения')#вызов графика
    plt.legend()
    plt.show()
grafic(M=2.464*10**31)
#СОЛНЦЕ
def grafic1(M=2*10**30): 
    x=np.linspace(696*10**6, 696*10**7, 10**4)
    y = (4*G*M)/(x*c**2)                      #функция графика                                   #пространство              #линия X 
    plt.plot(x,y,color='r',label = 'Cолнце')
    plt.xlabel('Прицельное расстояние')
    plt.ylabel('Угол отклонения')  
    plt.legend()                            #вызов графика
    plt.show()
grafic1(M=2*10**30)
                             
def grafic2(M=3.381*10**31):                           #функция графика                                 #пространство
    x=np.arange(9.8789*10**11, 9.8789*10**12, 10**6) 
    y = (4*G*M)/(x*c**2)     #линия X
    plt.plot(x,y, color='b',label='Большой песссс')
    plt.xlabel('Прицельное расстояние')
    plt.ylabel('Угол отклонения') 
    plt.legend()                           #вызов графика
    plt.show()
    
grafic2(M=3.381*10**31)