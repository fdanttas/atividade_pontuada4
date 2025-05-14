import csv
import time
import os
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome = str
    cpf = int
    cargo = str
    salario = int

    def exibir_dados(self):
        print("\nExibindo dados:")
        print(f"Nome: {self.nome}, CPF: {self.cpf}, Cargo: {self.cargo}, Salário: {self.salario}")

# Lista para armazenar os funcionários
funcionarios = []

# Função para exibir o menu
def exibir_menu():
    print("\n--- MENU ---")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Salvar em CSV")
    print("6. Sair")

# Cadastrar
def cadastrar():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")
    salario = input("Salário: ")
    funcionarios.append([nome, cpf, cargo, salario])
    print("Funcionário cadastrado!")

# Listar
def listar():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        for f in funcionarios:
            print(f"Nome: {f[0]}, CPF: {f[1]}, Cargo: {f[2]}, Salário: {f[3]}")

# Atualizar
def atualizar():
    cpf = input("Digite o CPF do funcionário a atualizar: ")
    for f in funcionarios:
        if f[1] == cpf:
            f[0] = input("Novo nome: ")
            f[2] = input("Novo cargo: ")
            f[3] = input("Novo salário: ")
            print("Funcionário atualizado!")
            return
    print("Funcionário não encontrado.")

# Excluir
def excluir():
    cpf = input("Digite o CPF do funcionário a excluir: ")
    for f in funcionarios:
        if f[1] == cpf:
            funcionarios.remove(f)
            print("Funcionário excluído!")
            return
    print("Funcionário não encontrado.")

# Salvar CSV
def salvar():
    with open("funcionarios.csv", "w", newline="") as arq:
        writer = csv.writer(arq)
        writer.writerow(["Nome", "CPF", "Cargo", "Salario"])
        writer.writerows(funcionarios)
    print("Dados salvos no arquivo funcionarios.csv!")



# Programa principal
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        salvar()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")

if opcao != 1:
    time.sleep(5)
os.system("cls|| clear")

     