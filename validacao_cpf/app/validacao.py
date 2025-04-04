import re
import tkinter as tk
from tkinter import messagebox

def validar_cpf(cpf: str) -> bool:
    if not isinstance(cpf, str):
        return False

    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

def verificar_cpf():
    cpf = entrada_cpf.get()
    if validar_cpf(cpf):
        messagebox.showinfo("Resultado", "✅ CPF VÁLIDO!")
    else:
        messagebox.showerror("Resultado", "❌ CPF INVÁLIDO!")

def mostrar_saudacao(event):
    saudacao_var.set("Bom dia, Boa tarde, Boa noite meu povo")

# Criando a janela principal
janela = tk.Tk()
janela.title("Validador de CPF")
janela.geometry("330x220")
janela.resizable(False, False)

# Saudação no topo
saudacao_var = tk.StringVar()
saudacao_label = tk.Label(janela, textvariable=saudacao_var, font=("Arial", 11, "bold"), fg="blue")
saudacao_label.pack(pady=(15, 5)) 

# Rótulo
rotulo = tk.Label(janela, text="Digite o CPF:", font=("Arial", 12))
rotulo.pack(pady=5)

# Campo de entrada
entrada_cpf = tk.Entry(janela, font=("Arial", 12), justify='center')
entrada_cpf.pack(pady=5)
entrada_cpf.bind("<KeyRelease>", mostrar_saudacao)

# Botão de validar
botao_validar = tk.Button(janela, text="Validar CPF", command=verificar_cpf, font=("Arial", 12), bg="#4CAF50", fg="white")
botao_validar.pack(pady=15)

# Rodar a interface
janela.mainloop()
