import numpy as np
import matplotlib.pyplot as plt

#Ahora veremos mediante una gráfica de barras la natalidad diferenciada entre niños y niñas en el Hospital Macarena
#mediante unos datos ficticios


#5 Meses en los que vamos a comparara la natalidad
meses = 5

#Cantidad de Niños nacidos en los ultimo 5 meses
natalidadDeNiños = (13, 20, 16, 17, 15)

#Cantidad de Niñas nacidos en los ultimos 5 meses
natalidadDeNiñas = (8, 10, 7, 10, 18)


#Creacion de la figura
fig, ax = plt.subplots()

#Anchura de la barra
anchoDeBarra = 0.3


#La funcion que utilizaremos pertenece a numpy que sirve para:
#Devolver valores espaciados uniformemente dentro de un intervalo dado.
#np.arange()

diagrama1 = ax.bar(np.arange(meses), natalidadDeNiños, anchoDeBarra,
                 color='b',label='Niños')

#Al sumarle al np.arange(meses) el ancho de Barra consigo que se nos posiciones al lado de la anterior barra en este caso de niños
diagrama2 = ax.bar(np.arange(meses) + anchoDeBarra, natalidadDeNiñas, anchoDeBarra,
                color='g',label='Niñas')

#Titulo de la gráfica
ax.set_title('Natalidad en el Hospital Macarena')
#Nombre que le vamos a poner en el eje x a la trabla
ax.set_xticklabels(('Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'))


#Devuelve los x tipos como una lista de ubicaciones
ax.set_xticks(np.arange(meses) + anchoDeBarra / 10)

#Nos muestra una leyenda en la gráfica donde nos viene el color que pertenece a cada tipo y el nombre de los diferentes tipos
ax.legend()


plt.show()