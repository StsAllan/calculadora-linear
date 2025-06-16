
# **Calculadora Linear**

Este projeto foi desenvolvido como parte da matéria de **Estruturas Matemáticas** da **Faculdade UNISUL - Pedra Branca**, com o objetivo de criar uma **calculadora** que resolve **equações lineares**.

## **Aplicação feita por:**
- Allan dos Santos
- Álvaro Wiggers Júnior

## **Conceito do Projeto**

A **Calculadora Linear** foi criada para fornecer uma ferramenta interativa e prática para a resolução de equações lineares. A aplicação permite que o usuário insira equações matemáticas e obtenha soluções com explicações detalhadas de cada etapa do cálculo.

## **Estrutura e Funcionalidade**

- **Interface Gráfica**: Desenvolvida com a biblioteca **Tkinter**, a interface é moderna e intuitiva, permitindo que o usuário interaja tanto com o mouse quanto com o teclado. A entrada de equações é facilitada por botões interativos, e o cálculo é feito ao pressionar `=` ou através do teclado.

- **Resolução de Equações Lineares**: A calculadora resolve equações do tipo \( ax + b = c \) e similares, exibindo o resultado final e explicando o passo a passo de cada operação, desde a expansão até a simplificação e solução final.

- **Passo a Passo**: O cálculo detalhado é mostrado em uma janela separada, permitindo que o usuário acompanhe o raciocínio por trás da resolução da equação.

- **Funcionalidades Extras**:
  - **Backspace**: O botão de **Backspace** permite apagar o último caractere inserido.
  - **Colar**: O usuário pode **colar** equações diretamente no campo de entrada usando `Ctrl + V`.
  - **Limpar**: A opção de **limpar** apaga toda a equação digitada, começando do zero.

## **Tecnologias Utilizadas**

- **Python 3**: Linguagem principal usada para desenvolver a calculadora.
- **Tkinter**: Biblioteca para a criação da interface gráfica.
- **SymPy**: Biblioteca matemática para resolução simbólica de equações lineares.

## **Como Funciona**

1. **Entrada**: O usuário insere uma equação linear usando os botões na interface ou digitando diretamente com o teclado.
2. **Processamento**: A equação é analisada e resolvida pela **SymPy**, que simbolicamente resolve a equação e apresenta o resultado.
3. **Saída**: O resultado da equação é exibido na tela. O passo a passo da resolução pode ser acessado ao clicar na opção **Passo a Passo**.

## **Desenvolvimento e Desafios**

O projeto foi desenvolvido para reforçar o aprendizado de **Estruturas Matemáticas** e a implementação de métodos computacionais para resolver problemas algébricos. Durante o desenvolvimento, desafios como a criação de uma interface intuitiva e a implementação do cálculo simbólico de equações foram superados com o uso das bibliotecas **Tkinter** e **SymPy**.

## **Como Usar**

1. **Instalar Dependências**:
   - Para rodar o projeto, é necessário ter o **Python 3** instalado em sua máquina.
   - Instalar as dependências com o seguinte comando:

   ```bash
   pip install sympy tkinter
   ```

2. **Executar o Programa**:
   - Execute o script Python `calculadora_linear.py` para iniciar a calculadora.

   ```bash
   python calculadora_linear.py
   ```

3. **Usar a Calculadora**:
   - Digite ou clique nos botões para inserir a equação.
   - Pressione o botão **`=`** para calcular a solução.
   - Utilize **`Esc`** para limpar a equação ou **Backspace** para apagar o último dígito.

