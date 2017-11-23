import matplotlib.pyplot as plt

#Vamos a mostraros una grafica circular



#Dibuja una grafica que nos muestre el porcentaje de mujeres, niños ,niñas y hombre que se encuentran en el parque:
#niños 20% niñas 30%  mujeres 10% hombre 20% ancianos 20% resaltando donde se encuentre mayor y menor porcentaje

#Nombres que vamos a mostrar en la gráfica circular
tipos= 'Niños', 'Niñas', 'Mujeres', 'Hombre','Ancianos'

#Cantidad  de tipos de personas ordenado correspondientemente en el mismo orden anteriormente escrito
cantidad = [20, 30, 10, 20,20]

#Nos muestra resaltado el tipo al que se refiera
sobresalto = (0, 0.05, 0, 0 , 0.05)

#Colores con los que quiero que se represente cada tipo en el mismo orden respectivamente
colores=['y','g','r','c','m']

#Figura que vamos a utilizar para representar
fig1, ax1 = plt.subplots()


plt.title("Cantidad de tipos de personas que se encuentran en el parque")

#A nuestra figura le vamos a dar una cantidad de caracteristicas que deseesmos en este caso le hemos dado la cantidad de cada tipo, que nos muestre el nombre de los diferentes tipos y dentro de el area
#que ocupan esos tipos le hemos insertado que nos muestre el porcentage ademas de que nos lo muestre en un angulo de 360º. Ademas de estas caracteristicas le podemos  cambiar  otro tipos de caracteristicas

ax1.pie(cantidad, explode=sobresalto,  labels=tipos, autopct='%1.1f%%', startangle=360, colors=colores)

#Mediante esta función conseguimos que no se nos deforme la figura y sea igual por todos los lados
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


#Nos muestra la figura
plt.show()