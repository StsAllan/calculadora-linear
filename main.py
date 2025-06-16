import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import sympy as sp
from datetime import datetime

equacao_atual = ""
historico = []

def atualizar_display():
    display_var.set(equacao_atual)

def adicionar_caractere(c):
    global equacao_atual
    equacao_atual += c
    atualizar_display()

def limpar():
    global equacao_atual
    equacao_atual = ""
    display_var.set("")
    resultado_var.set("")

def backspace():
    global equacao_atual
    equacao_atual = equacao_atual[:-1]
    atualizar_display()

def calcular():
    global equacao_atual
    try:
        if "=" not in equacao_atual:
            resultado_var.set("Erro: Equação inválida")
            return

        lhs_str, rhs_str = equacao_atual.split('=')
        lhs = sp.sympify(lhs_str)
        rhs = sp.sympify(rhs_str)

        variaveis = lhs.free_symbols.union(rhs.free_symbols)
        var_principal = list(variaveis)[0]
        passos = []

        eq = sp.Eq(lhs, rhs)
        passos.append("1. Equação original:")
        passos.append(str(eq))

        lhs_exp = sp.expand(lhs)
        rhs_exp = sp.expand(rhs)
        passos.append("2. Expandindo os dois lados:")
        passos.append(f"LHS: {lhs_exp}")
        passos.append(f"RHS: {rhs_exp}")

        expressao_final = lhs_exp - rhs_exp
        passos.append("3. Subtraindo RHS de LHS:")
        passos.append(f"{expressao_final} = 0")

        simplificada = sp.simplify(expressao_final)
        passos.append("4. Simplificando:")
        passos.append(f"{simplificada} = 0")

        solucoes = sp.solve(simplificada, var_principal)
        passos.append("5. Solução:")
        for sol in solucoes:
            passos.append(f"{var_principal} = {sol}")
            resultado_var.set(f"{var_principal} = {sol}")

        historico.append((equacao_atual, resultado_var.get()))
        return passos

    except Exception as e:
        resultado_var.set("Erro")
        return ["Erro ao resolver a equação."]

def mostrar_passos():
    passos = calcular()
    if not passos:
        return
    passo_janela = tk.Toplevel(root)
    passo_janela.title("Passo a Passo")
    passo_janela.geometry("400x300")
    passo_text = ScrolledText(passo_janela, font=("Consolas", 10), bg="#111", fg="#eee")
    passo_text.pack(fill="both", expand=True, padx=10, pady=10)
    passo_text.insert(tk.END, "\n".join(passos))

def mostrar_historico():
    passo_janela = tk.Toplevel(root)
    passo_janela.title("Histórico")
    passo_janela.geometry("400x300")
    passo_text = ScrolledText(passo_janela, font=("Consolas", 10), bg="#111", fg="#eee")
    passo_text.pack(fill="both", expand=True, padx=10, pady=10)
    passo_text.insert(tk.END, "Histórico de Cálculos:\n\n")
    for eq, res in historico[-10:][::-1]:
        passo_text.insert(tk.END, f"{eq}  →  {res}\n")

def key_press(event):
    tecla = event.char
    if tecla in "0123456789+-*/x()":
        adicionar_caractere(tecla)
    elif tecla == "=" or event.keysym == "Return":
        calcular()
    elif tecla == "Escape":
        limpar()
    elif event.keysym == "BackSpace":
        backspace()

def colar(event):
    global equacao_atual
    texto_colado = root.clipboard_get()
    equacao_atual += texto_colado
    atualizar_display()

root = tk.Tk()
root.title("Calculadora Linear")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

style = ttk.Style(root)
style.theme_use("clam")

display_var = tk.StringVar()
resultado_var = tk.StringVar()

# Layout com grid geral
for i in range(4):
    root.grid_columnconfigure(i, weight=1, uniform="col")

for i in range(3, 8):
    root.grid_rowconfigure(i, weight=1)

display = tk.Label(root, textvariable=display_var, font=("Segoe UI", 20), bg="#1e1e1e", fg="white", anchor="e")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=(8, 4), sticky="nsew")

resultado = tk.Label(root, textvariable=resultado_var, font=("Segoe UI", 16, "bold"), bg="#1e1e1e", fg="#00ffcc", anchor="e")
resultado.grid(row=1, column=0, columnspan=4, padx=5, pady=(0, 8), sticky="nsew")

top_botoes = [
    ("🧠 Passo a Passo", mostrar_passos),
    ("🕘 Histórico", mostrar_historico),
    ("🔄 Limpar", limpar),
    ("⌫", backspace)  # Botão Backspace
]

for idx, (txt, cmd) in enumerate(top_botoes):
    b = ttk.Button(root, text=txt, command=cmd)
    b.grid(row=2, column=idx, padx=2, pady=2, sticky="nsew")

botoes = [
    ("7", "8", "9", "+"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "*"),
    ("0", "x", "y", "/"),
    ("(", ")", "=", "⏎"),
]

for i, linha in enumerate(botoes):
    for j, texto in enumerate(linha):
        if texto == "⏎":
            action = calcular
            cor = "#ff00cc"
            label = "="
        else:
            action = lambda c=texto: adicionar_caractere(c)
            cor = "#2e2e2e"
            label = texto
        btn = tk.Button(root, text=label, font=("Segoe UI", 16), width=6, height=3,
                  bg=cor, fg="white", bd=2, relief="solid")
        btn.grid(row=i+3, column=j, padx=2, pady=2, sticky="nsew")
        btn.configure(command=action)

# Configurar para capturar entradas do teclado e colar (Ctrl + V)
root.bind("<Key>", key_press)
root.bind("<Control-v>", colar)

root.mainloop()