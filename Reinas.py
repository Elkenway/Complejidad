import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer

class Tablero:
    def __init__(self, tamano: int = 8):  # <-- CORREGIDO __init__
        self.tamano = tamano
        self.tablero = [['_' for _ in range(tamano)] for _ in range(tamano)]

    def reinas(self, posiciones: list[int]):
        self.tablero = [['_' for _ in range(self.tamano)] for _ in range(self.tamano)]
        for fila, col in enumerate(posiciones):
            self.tablero[fila][col] = 'R'

    def es_valido(self, posiciones, fila, col):
        for i in range(fila):
            if posiciones[i] == col or abs(posiciones[i] - col) == abs(i - fila):
                return False
        return True

class ReinaGUI(QWidget):
    def __init__(self): 
        super().__init__()  
        self.setWindowTitle("Problema de las 8 Reinas (Backtracking)")
        self.tamano = 8
        self.tablero = Tablero(self.tamano)
        self.solucion = None
        self.posiciones = []
        self.fila_actual = 0
        self.pila = [(0, [])]

        self.iteraciones = 0  # Contador de iteraciones

        self.layout_principal = QVBoxLayout()
        self.info_label = QLabel("Buscando solución con backtracking...")
        self.iter_label = QLabel("Iteraciones: 0")  # Etiqueta para iteraciones
        self.layout_principal.addWidget(self.info_label)
        self.layout_principal.addWidget(self.iter_label)

        self.grid = QGridLayout()
        self.botones = [[QPushButton('_') for _ in range(self.tamano)] for _ in range(self.tamano)]

        for i in range(self.tamano):
            for j in range(self.tamano):
                btn = self.botones[i][j]
                btn.setFixedSize(40, 40)
                self.grid.addWidget(btn, i, j)

        self.layout_principal.addLayout(self.grid)
        self.setLayout(self.layout_principal)

        self.timer = QTimer()
        self.timer.timeout.connect(self.backtracking_paso_a_paso)
        self.timer.start(10)

    def actualizar_tablero(self, posiciones):
        self.tablero.reinas(posiciones)
        for i in range(self.tamano):
            for j in range(self.tamano):
                simbolo = self.tablero.tablero[i][j]
                self.botones[i][j].setText(simbolo)

    def backtracking_paso_a_paso(self):
        if not self.pila:
            self.info_label.setText("No se encontró solución.")
            self.timer.stop()
            return

        fila, posiciones = self.pila.pop()
        self.iteraciones += 1
        self.iter_label.setText(f"Iteraciones: {self.iteraciones}")

        if fila == self.tamano:
            self.info_label.setText(f"¡Solución encontrada!: {posiciones}")
            self.actualizar_tablero(posiciones)
            self.timer.stop()
            return

        for col in range(self.tamano - 1, -1, -1):
            if self.tablero.es_valido(posiciones, fila, col):
                self.pila.append((fila + 1, posiciones + [col]))

        self.actualizar_tablero(posiciones)
        self.info_label.setText(f"Probando fila {fila}, posiciones: {posiciones}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ReinaGUI()
    ventana.show()
    sys.exit(app.exec_())
