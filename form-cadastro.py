## Documentação KTINTER - https://docs.python.org/pt-br/3.13/library/tk.html

import tkinter as tk
from tkinter import ttk, messagebox

# Função para verificar se a pessoa é maior de idade
def verificar_maioridade(idade):
# Tratamento de dado com try except para evitar erros no código no campo da idade
    try:
        idade = int(idade)
        #Adiciona String "Maior" ou "Menor" com relação a idade informada
        if idade >= 18:
            return "Maior"
        else:
            return "Menor"
    except ValueError:
        return "Idade inválida"

# Função que será chamada ao clicar em "Cadastrar"
def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    telefone = entry_telefone.get()
    parentesco = entry_parentesco.get()
    time = entry_time.get() # Adicionei o campo de time como campo opinional do form
    info_idade = verificar_maioridade(idade)
    
    familiar = f"Nome: {nome} | Idade: {idade} | Telefone: {telefone} | Parentesco: {parentesco} | Time: {time} | {info_idade}"
    #O tk.END vai adicionar a nova pessoa no ultimo campo da listagem
    lista_familiares.insert(tk.END, familiar)

# Configurações de tela inicial
tela = tk.Tk()
tela.title("Cadastro de Pessoas")
tela.geometry("850x650")
tela.configure(bg="white")
# Configura o style para a tela do sistema (fica um pouquinho mais bonito)
style = ttk.Style()
style.theme_use("clam")

# Definição dos componentes utilizados na tela
style.configure("TLabel", background="white", foreground="black", font=("Arial", 11, "bold"))
style.configure("TButton", background="#00e600", foreground="black", font=("Arial", 11, "bold"), padding=6)

# Título
titulo = tk.Label(tela, text="Cadastro de Familiares", bg="white", fg="blue", font=("Arial", 22, "bold"))
titulo.grid(row=0, column=0, columnspan=2, pady=15)

# Labels e campos de entrada dos dados
ttk.Label(tela, text="Nome: ").grid(row=1, column=0, sticky="e")
entry_nome = ttk.Entry(tela, width=40)
entry_nome.grid(row=1, column=1, pady=5)

ttk.Label(tela, text="Idade: ").grid(row=2, column=0, sticky="e")
entry_idade = ttk.Entry(tela, width=40)
entry_idade.grid(row=2, column=1, pady=5)

ttk.Label(tela, text="Telefone: ").grid(row=3, column=0, sticky="e")
entry_telefone = ttk.Entry(tela, width=40)
entry_telefone.grid(row=3, column=1, pady=5)

ttk.Label(tela, text="Parentesco: ").grid(row=4, column=0, sticky="e")
entry_parentesco = ttk.Entry(tela, width=40)
entry_parentesco.grid(row=4, column=1, pady=5)

ttk.Label(tela, text="Time: ").grid(row=5, column=0, sticky="e")
entry_time = ttk.Entry(tela, width=40)
entry_time.grid(row=5, column=1, pady=5)

# Botão de cadastrar
btn_cadastrar = ttk.Button(tela, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=6, column=0, columnspan=2, pady=15)

# Lista para mostrar familiares
lista_familiares = tk.Listbox(tela, width=100, height=12, bg="white", fg="black", font=("Courier New", 10))
lista_familiares.grid(row=7, column=0, columnspan=2, pady=10)

# Dados iniciais da minha família
familiares_iniciais = [
    {"nome": "Odilon", "idade": 62, "telefone": "91234-1234", "parentesco": "Pai", "time": "Santos"},
    {"nome": "Leonice", "idade": 42, "telefone": "99292-5678", "parentesco": "Tia", "time": "Flamengo"},
    {"nome": "Bruno", "idade": 25, "telefone": "98888-1221", "parentesco": "Primo", "time": "Corinthians"},
    {"nome": "Tânia", "idade": 71, "telefone": "99877-2112", "parentesco": "Avó", "time": "Sem time"},
    {"nome": "Maycon", "idade": 18, "telefone": "99222-1111", "parentesco": "Primo", "time": "São Paulo"}
]

#For de f (uma pessoa) para todas as cadastradas
#Usado para mostrar na tela todos os familiares já cadastrados no sistema
for f in familiares_iniciais:
    info_idade = verificar_maioridade(f["idade"])
    familiar = f"Nome: {f['nome']} | Idade: {f['idade']} | Telefone: {f['telefone']} | Parentesco: {f['parentesco']} | Time: {f['time']} | {info_idade}"
    lista_familiares.insert(tk.END, familiar)

tela.mainloop()
