from PyQt5.QtWidgets import *
import sys

class VentanaPrincipal(QMainWindow):
    def saludar(self, e):
        ventanaSaludo = QMessageBox()
        nombre = self.textoNombre.text()
        ventanaSaludo.setText("¡Hola, " + nombre + "!")
        ventanaSaludo.setWindowTitle("Mensaje de saludo")
        ventanaSaludo.exec_()

    def textoNombre_changed(self, e):
        nombre = self.textoNombre.text()
        if(nombre == ""):
            self.botonSaludar.setEnabled(False)
        else:
            self.botonSaludar.setEnabled(True)

    def sumarClicks(self, e):
        cantidad = int(self.labelCantidad.text())
        cantidad = cantidad + 1
        self.labelCantidad.setText(str(cantidad))

    def restarClicks(self, e):
        cantidad = int(self.labelCantidad.text())
        cantidad = cantidad - 1
        self.labelCantidad.setText(str(cantidad))

    def __init__(self):
        super().__init__()
        self.title = 'Mi programa genial'
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 480

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QVBoxLayout()

        saludadorLayour = QHBoxLayout()
        
        self.textoNombre = QLineEdit()
        self.textoNombre.textChanged.connect(self.textoNombre_changed)
        saludadorLayour.addWidget(self.textoNombre)
        self.botonSaludar = QPushButton()
        self.botonSaludar.setText("Saludar")
        self.botonSaludar.setEnabled(False)
        self.botonSaludar.clicked.connect(self.saludar)
        saludadorLayour.addWidget(self.botonSaludar)

        layout.addLayout(saludadorLayour)

        contadorLayout = QHBoxLayout()
        label = QLabel()
        label.setText("Número de clicks: ")
        contadorLayout.addWidget(label)

        self.labelCantidad = QLabel()
        self.labelCantidad.setText("0")

        contadorLayout.addWidget(self.labelCantidad)
        buttonRestar = QPushButton("Restar")
        buttonRestar.clicked.connect(self.restarClicks)
        contadorLayout.addWidget(buttonRestar)

        buttonSumar = QPushButton("Sumar")
        buttonSumar.clicked.connect(self.sumarClicks)
        contadorLayout.addWidget(buttonSumar)

        layout.addLayout(contadorLayout)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    codigoDeFinalizacion = app.exec_()
    sys.exit(codigoDeFinalizacion)