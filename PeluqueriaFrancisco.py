#Francisco tiene una peluquería y actualmente realiza todos los cobros con una calculadora vieja,
#lo que le quita tiempo por la gran cantidad de clientes que atiende.
#El precio de los servicios es el siguiente:

# *Personas mayores de 15 años: cada servicio (corte de cabello, barba o cejas) 
# cuesta $5.30. Si el cliente solicita los tres servicios, el total es $15.90.

# *Personas mayores de 60 años: se aplica un 30% de descuento sobre el Total.

# *Niños y adolescentes menores de 14 años: cada servicio cuesta $4.25. Si se solicitan dos servicios, el total es $8.50.

#Francisco necesita un programa donde pueda ingresar los datos del cliente (Nombre, edad y servicios solicitados), 
# y que automáticamente calcule el cobro correspondiente de manera rápida y sencilla.

# Importamos lo necesario para hacer ventanas con PyQt5
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QVBoxLayout,QLabel,QLineEdit,QMessageBox,QCheckBox)
from PyQt5.QtGui import QIcon
import sys


# Creamos la aplicación principal
app = QApplication(sys.argv)

# ---- FUNCIÓN QUE HACE EL CÁLCULO DEL TOTAL ----
def calcular():
    try:
        # Guardamos lo que escribe el usuario en las cajas de texto
        nombre = entrada_nombre.text()
        #convertimos el texto a numero
        edad = int(entrada_edad.text())

        # Servicios seleccionados
        servicios = []
        if chk_cabello.isChecked(): servicios.append("Cabello")
        if chk_barba.isChecked(): servicios.append("Barba")
        if chk_cejas.isChecked(): servicios.append("Cejas")
        cantidad = len(servicios) # cantidad de servicios seleccionados

        if cantidad == 0:
            QMessageBox.warning(ventana, "Atención", "Debe seleccionar al menos un servicio.")
            return
        

        # Aquí calculamos el precio según la edad del cliente
        total = 0.0

        # Reglas de precios
        if edad >= 15 and edad < 60:
            total = cantidad * 5.30
        elif edad >= 60:
            total = cantidad * 5.30
            total -= total * 0.30
        elif edad < 14:
            if cantidad == 1:
                total = 4.25
            elif cantidad == 2:
                total = 8.50
            else:
                total = cantidad * 4.25
        
        # Convertimos los servicios seleccionados en un texto
        servicios_str = ", ".join(servicios)
        #mostramos la informacion al cliente
        QMessageBox.information(
            ventana,
            "Total a Cobrar",
            f"Cliente: {nombre}\nEdad: {edad}\nServicios: {servicios_str}\n\nTotal: ${total:.2f}"
        )
        # Si la edad no es un número, mostramos un error
    except ValueError:
        QMessageBox.warning(ventana, "Error", "Por favor ingrese una edad válida.")


# ---- DISEÑO DE LA VENTANA ----

# Creamos la ventana principal
ventana = QWidget()
ventana.setWindowTitle("Peluquería Francisco")
ventana.setGeometry(500, 200, 400, 400)
ventana.setWindowIcon(QIcon("Peluqueria.ico"))

layout = QVBoxLayout()

# Widgets
# Creamos los textos y cajas donde el cliente pondrá datos
texto = QLabel("Bienvenido a la Peluquería Francisco")
entrada_nombre = QLineEdit()
nombre = QLabel("Ingresa el Nombre del cliente:")


entrada_edad = QLineEdit()
edad = QLabel("Ingresa la Edad del cliente:")


# Opciones de servicios con casillas para marcar
lbl_servicios = QLabel("Seleccione los servicios:")
chk_cabello = QCheckBox("Corte de Cabello")
chk_barba = QCheckBox("Corte de Barba")
chk_cejas = QCheckBox("Corte de Cejas")

# Botón que hace el cálculo al dar clic
boton = QPushButton("Calcular Total")
boton.clicked.connect(calcular) # conecta el botón con la función calcular

# Ponemos todos los elementos en la ventana
# Agregar widgets
widgets = [texto, nombre, entrada_nombre, edad, entrada_edad, lbl_servicios, chk_cabello, chk_barba, chk_cejas, boton]
for w in widgets:
    layout.addWidget(w)

ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())