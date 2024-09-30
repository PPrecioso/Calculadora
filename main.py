import sys
from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)

    # Aplica o tema customizado
    setupTheme(app)

    # Cria a janela principal
    window = MainWindow()

    # Define o ícone da janela
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Adiciona os componentes à janela
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Ajusta o tamanho da janela e exibe
    window.adjustFixedSize()
    window.show()

    # Executa a aplicação
    app.exec()
