# app.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from cliente import Paciente, Medico, Farmacia, Receita, SUS, Endereco

# Lista de pacientes e farmácias
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

# Funções da interface
def cadastrar_paciente():
    nome = simpledialog.askstring("Cadastro", "Nome do paciente:")
    cpf = simpledialog.askstring("Cadastro", "CPF:")
    sus_num = simpledialog.askstring("Cadastro", "Número do SUS:")

    if not nome or not cpf or not sus_num:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    endereco = SUS.obter_endereco(sus_num)
    paciente = Paciente(nome, cpf, sus_num, endereco)
    pacientes.append(paciente)
    messagebox.showinfo("Cadastro", "Paciente cadastrado com sucesso!")

def listar_pacientes():
    if not pacientes:
        messagebox.showinfo("Lista", "Nenhum paciente cadastrado.")
        return
    texto = ""
    for p in pacientes:
        texto += f"{p.nome} - CPF: {p.cpf} - SUS: {p.sus_numero}\nEndereço: {p.endereco.logradouro}\n\n"
    mostrar_janela("Pacientes Cadastrados", texto)

def registrar_consulta():
    nome = simpledialog.askstring("Consulta", "Nome do paciente:")
    paciente = next((p for p in pacientes if p.nome.lower() == nome.lower()), None)
    if not paciente:
        messagebox.showerror("Erro", "Paciente não encontrado.")
        return

    medicamento = simpledialog.askstring("Consulta", "Medicamento:")
    doenca = simpledialog.askstring("Consulta", "Doença:")
    observacao = simpledialog.askstring("Consulta", "Observações:")

    if not medicamento or not doenca:
        messagebox.showerror("Erro", "Campos obrigatórios faltando!")
        return

    medico = Medico("Dr. Jacinto", "12345")
    receita = Receita(paciente, medico, medicamento, doenca, observacao)
    medico.autorizar_receita(receita)
    resultado = receita.gerar_receita()
    entrega = SUS.verificar_entrega(paciente, farmacias)

    mostrar_janela("Receita", f"{resultado}\n{entrega}")

def mostrar_janela(titulo, mensagem):
    janela = tk.Toplevel(root)
    janela.title(titulo)
    janela.geometry("500x400")
    texto = tk.Text(janela, wrap=tk.WORD)
    texto.insert(tk.END, mensagem)
    texto.config(state=tk.DISABLED)
    texto.pack(expand=True, fill=tk.BOTH)

# Construção da interface principal
root = tk.Tk()
root.title("Sistema SUS")
root.geometry("400x350")

titulo = tk.Label(root, text="Sistema SUS - Receitas e Consultas", font=("Helvetica", 14, "bold"))
titulo.pack(pady=20)

btn_cadastrar = tk.Button(root, text="📋 Cadastrar Paciente", width=30, command=cadastrar_paciente)
btn_listar = tk.Button(root, text="📄 Listar Pacientes", width=30, command=listar_pacientes)
btn_consulta = tk.Button(root, text="💊 Registrar Consulta", width=30, command=registrar_consulta)
btn_sair = tk.Button(root, text="❌ Sair", width=30, command=root.destroy)

btn_cadastrar.pack(pady=5)
btn_listar.pack(pady=5)
btn_consulta.pack(pady=5)
btn_sair.pack(pady=20)

root.mainloop()