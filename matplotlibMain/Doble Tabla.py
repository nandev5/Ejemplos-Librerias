import numpy as np
import matplotlib.pyplot as plt


#SUBPLOT()

#En este ejemplo vamos a plantear un problema de movimiento curvilineo uniforme
#Para ello vamos a plasmar una funcion tal que f(x)=sen(3*x+10)+3 y otr tal que f(x)=cos(2*x+5)+10
#Nos tiene que mostrar en dos graficas el desplazamiento que se produce en 5(s)

#Funcion de numpy que nos sirve para hacer un
#Domininio de tiempo (empezar,terminar)
t1= np.linspace(0.0, 5.0)



#Funciones que queremos resolver la t1 es todos los numeros desde el timpo de empezar el tiempo de terminar
y1 = np.sin( 3 * t1+10)+3
y2 = np.cos(2 * t1 +5 )*np.exp(-t1+54)


#Datos de la primera tabla
plt.subplot(2, 1, 1)
#Trazado de puntos
plt.plot(t1, y1,'g')
#Descripcion del eje y
plt.ylabel('Metro(m)')

#Titulo de la gráfica
plt.title('Funciones del movimiento')

#Datos de la segunda tabla
plt.subplot(2, 1, 2)
plt.plot(t1, y2,'y')
plt.ylabel('Metro(m)')

#Como podeis comprobar en el subplot() tienen diferentes el ultimo termino que se refiere al posicionamiento esto es asi para que se produzca
#  la creacion de dos tablas

plt.xlabel('Tiempo (s)')

plt.show()