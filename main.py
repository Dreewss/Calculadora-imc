import tkinter as tk 
from tkinter import messagebox
# Bibliotecas que criam a interface e exibir mensagens para usuários

def calcular_imc():  #Lê os valores dos campos de entrada
    try:
        nome = entry_nome.get()
        idade = int(entry_idade.get())
        altura = float(entry_altura.get())
        peso = float(entry_peso.get())

        imc = peso / altura**2
        resultado = f"{imc:.2f} - Seu IMC é {imc:.2f}\n"

        if imc <= 18.10:
            resultado += "Você está abaixo do peso"
        elif imc > 18.10 and imc <= 24.9:
            resultado += "Você está no peso certo"
        elif imc > 24.9 and imc <= 29.9:
            resultado += "Você está acima do peso"
        elif imc > 29.9 and imc <= 39.9:
            resultado += "Você é obeso nível I"
        else:
            resultado += "Você é obeso nível II"

        messagebox.showinfo("Resultado do IMC", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Cria os widgets
label_nome = tk.Label(root, text="Nome:")
entry_nome = tk.Entry(root)

label_idade = tk.Label(root, text="Idade:")
entry_idade = tk.Entry(root)

label_altura = tk.Label(root, text="Altura (em m):")
entry_altura = tk.Entry(root)

label_peso = tk.Label(root, text="Peso (em kg):")
entry_peso = tk.Entry(root)

button_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)

# Organiza as caixas da janela 
label_nome.grid(row=0, column=0, padx=35, pady=10)
entry_nome.grid(row=0, column=1, padx=35, pady=10)

label_idade.grid(row=1, column=0, padx=35, pady=10)
entry_idade.grid(row=1, column=1, padx=35, pady=10)

label_altura.grid(row=2, column=0, padx=35, pady=10)
entry_altura.grid(row=2, column=1, padx=35, pady=10)

label_peso.grid(row=3, column=0, padx=35, pady=10)
entry_peso.grid(row=3, column=1, padx=35, pady=10)

button_calcular.grid(row=4, columnspan=2, pady=35)

# Inicia o loop da aplicação
root.mainloop()
