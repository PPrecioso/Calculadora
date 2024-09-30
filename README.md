# *Descrição Geral do Projeto - Calculadora com PySide6*
Este projeto consiste em uma calculadora gráfica desenvolvida utilizando o PySide6, que é a biblioteca oficial do Qt para Python. A interface gráfica foi projetada para ser intuitiva e moderna, com suporte para temas personalizados (tema claro/escuro) e funcionalidades básicas de uma calculadora convencional.

# Principais Funcionalidades
- Interface gráfica amigável com botões dispostos em uma grade.
- Exibição clara das operações e resultados em uma tela dedicada (display).
- Botões especiais para operações matemáticas comuns.
- Personalização visual da interface com um tema customizado via QSS (Qt Style Sheets).

# *Detalhes Técnicos do Projeto*
# Ambiente de Desenvolvimento Virtual (env)
O projeto foi desenvolvido em um ambiente virtual Python (utilizando venv), onde foram instaladas todas as bibliotecas necessárias para a construção da interface e funcionalidades da calculadora.

# Bibliotecas Utilizadas
# 1. PySide6
Propósito: PySide6 é o binding oficial de Qt para Python, utilizado para criar a interface gráfica do usuário (GUI). Ele oferece uma ampla gama de widgets e funcionalidades, como layouts, botões, caixas de texto, entre outros.

Componentes Utilizados:
- QApplication: Gerencia o ciclo de vida da aplicação.
- QMainWindow: Janela principal da aplicação.
- QPushButton: Botões da calculadora.
- QGridLayout: Layout usado para organizar os botões.
- QIcon: Utilizado para definir ícones para a janela.

# 2. Python Standard Library
Propósito: A biblioteca padrão do Python foi usada para manipulação básica de arquivos, caminhos, e para interagir com o sistema operacional.

Componentes Utilizados:
os e sys: Utilizados para manipulação do sistema de arquivos e argumentos passados para a aplicação.

# 3. Git LFS (Large File Storage)
Propósito: O Git LFS foi usado para gerenciar arquivos grandes no repositório, como bibliotecas pesadas incluídas no projeto, por exemplo, arquivos .dll relacionados ao PySide6.
Descrição: Git LFS permite que arquivos grandes sejam armazenados fora do repositório principal, garantindo que o repositório Git se mantenha leve e eficiente para desenvolvimento colaborativo.

# 4. QSS (Qt Style Sheets)
Propósito: Utilizado para personalizar a aparência da interface. Com QSS, foi possível alterar cores, tamanhos de fontes, bordas e outros aspectos visuais dos botões e layouts da calculadora.

Componentes Utilizados:
Criação de temas personalizados para botões (QPushButton), como botões especiais que mudam de cor quando pressionados ou quando o mouse passa sobre eles.

# *Organização dos Arquivos*
# main.py:
Contém o código principal que inicializa a aplicação.
Gerencia a criação da janela principal e os componentes (display, botões, etc.).

# buttons.py:
Define a classe responsável pela criação dos botões da calculadora, organizados em uma grade (QGridLayout).

# display.py:
Responsável por exibir as operações e resultados na interface.
Utiliza widgets do PySide6 para criar uma interface clara e responsiva para o usuário.

# info.py:
Um widget adicional que exibe informações sobre a calculadora, como dicas de uso ou a operação atual que está sendo realizada.

# styles.py:
Contém a customização de estilos da interface usando QSS.
Define temas de cores e efeitos para os botões.

# variables.py:
Um arquivo dedicado a variáveis globais, como cores, tamanhos de fontes e caminhos de ícones. Permite centralizar configurações e facilita a manutenção de aspectos visuais e lógicos da aplicação.

![image](https://github.com/user-attachments/assets/a8a12720-fa1a-433d-be56-46a456e2268a)

![image](https://github.com/user-attachments/assets/f2cbbd57-4c0d-4cd4-a6a2-00e6b9c91235)

