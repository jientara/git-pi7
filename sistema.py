# sistema.py
from cliente import Paciente, Medico, Farmacia, Receita, SUS, Endereco
from datetime import datetime

# Banco de dados em memória
pacientes = []
farmacias = [
    Farmacia("Farmácia Preço Baixo", Endereco("Rua Major Vieira, 505 - Centro")),
    Farmacia("Farmácia Genérica", Endereco("Rua Getúlio Vargas, 57 - Centro")),
    Farmacia("Farmácia Trevisani", Endereco("Rua Vidal Ramos, 829 - Centro")),
    Farmacia("Farmácia Ideal", Endereco("Rua Caetano Costa, 1016 - Centro")),
    Farmacia("Farmácia Vital", Endereco("Rua Francisco de Paula Pereira, 564 - Centro")),
    Farmacia("Farmácia Preço Popular", Endereco("Rua Francisco de Paula Pereira, 494 - Centro")),
    Farmacia("Farmácia Nativa Farma", Endereco("Rua Duque de Caxias, 1420 - Alto das Palmeiras")),
    Farmacia("Farmácia ForteFarma", Endereco("Rua Nazir Cordeiro, 791 - Campo d'Água Verde")),
    Farmacia("Farmácia Santa Helena", Endereco("Rua Reinoldo Hübner, 107 - Piedade")),
    Farmacia("Farmácia Jardim", Endereco("Rua Roberto Ehlke, 688 - Jardim Esperança")),
]

def cadastrar_paciente():
    nome = input("Nome do paciente: ")
    cpf = input("CPF: ")
    sus_num = input("Número do SUS: ")
    endereco = SUS.obter_endereco(sus_num)
    paciente = Paciente(nome, cpf, sus_num, endereco)
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!\n")

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
    else:
        for p in pacientes:
            print(f"{p.nome} - CPF: {p.cpf} - SUS: {p.sus_numero}")
            print(f"Endereço: {p.endereco.logradouro}")
            print("-" * 30)

def registrar_consulta():
    nome = input("Digite o nome do paciente: ").lower()
    paciente = next((p for p in pacientes if p.nome.lower() == nome), None)
    if not paciente:
        print("Paciente não encontrado.\n")
        return

    medico = Medico("Dr. Jacinto", "12345")
    medicamento = input("Medicamento: ")
    doenca = input("Doença: ")
    observacao = input("Observações: ")

    receita = Receita(paciente, medico, medicamento, doenca, observacao)
    medico.autorizar_receita(receita)

    print("\n" + receita.gerar_receita())
    print(SUS.verificar_entrega(paciente, farmacias))

def menu():
    while True:
        print("=== MENU SUS ===")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Registrar consulta")
        print("4 - Sair")
        try:
            opcao = input("Escolha uma opção: ")
        except EOFError:
            break

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            listar_pacientes()
        elif opcao == "3":
            registrar_consulta()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()