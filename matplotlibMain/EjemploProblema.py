import matplotlib.pyplot as plt


#PLOT()


# Pondremos un ejemplo con un problema físico. Muestra mediante una grafica el movimiento especificado al final del enunciado
# para los 5 primeros segundo de trayectoria
#y=4*t +2

#Muestra los 5 primeros segundos de trayectoria EJE X
t=[1,2,3,4,5]


#Muestra el punto donde se encontrara el objeto cuando pasen los respectivos segundos EJE Y
y=[4*1+2   ,   4*2+2    ,  4*3+2   , 4*4+2   , 4*5+2  ]


#Nos muestra un encunciado para el EJE X
plt.xlabel('Tiempo (s)')

#Nos muestra un enunciado para el EJE Y
plt.ylabel('Trayectoria recorrida  (m)')

#Nos muestra un titulo de tabla
plt.title("Gráfica Ejercicio")



#Nos hace el trazado de line entre  t e y
plt.plot(t,y,)



plt.show()

