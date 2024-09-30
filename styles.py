# Estilos do QT for Python usando QSS diretamente
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR)

# Definindo o QSS diretamente para o estilo
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
        padding: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
    QWidget {{
        background-color: #2b2b2b;
        color: #fff;
    }}
    QMainWindow {{
        background-color: #2b2b2b;
    }}
    QLabel {{
        color: #fff;
    }}
    QLineEdit {{
        background-color: #1e1e1e;
        color: #fff;
        border: 1px solid {PRIMARY_COLOR};
        padding: 5px;
    }}
    QPushButton {{
        background-color: {PRIMARY_COLOR};
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
    }}
    QPushButton:hover {{
        background-color: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton:pressed {{
        background-color: {DARKEST_PRIMARY_COLOR};
    }}
"""

# Função para aplicar o tema
def setupTheme(app):
    """Aplica o tema escuro ao aplicativo."""
    app.setStyleSheet(qss)
