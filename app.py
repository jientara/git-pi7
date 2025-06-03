import tkinter as tk
from tkinter import messagebox
import sistema

# Função para exibir o menu de funcionário
def menu_funcionario():
    def cadastrar_paciente():
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        sus_num = sus_entry.get()
        endereco = sistema.SUS.obter_endereco(sus_num)
        paciente = sistema.Paciente(nome, cpf, sus_num, endereco)
        sistema.pacientes.append(paciente)
        messagebox.showinfo("Cadastro", "Paciente cadastrado com sucesso!")
    
    def listar_pacientes():
        pacientes_lista = ""
        for p in sistema.pacientes:
            pacientes_lista += f"{p.nome} - CPF: {p.cpf} - SUS: {p.sus_numero}\n"
        messagebox.showinfo("Lista de Pacientes", pacientes_lista)

    def registrar_consulta():
        nome = nome_consulta_entry.get()
        paciente = next((p for p in sistema.pacientes if p.nome.lower() == nome.lower()), None)
        if paciente:
            medico = sistema.Medico("Dr. Jacinto", "12345")
            medicamento = medicamento_entry.get()
            doenca = doenca_entry.get()
            observacao = observacao_entry.get()
            receita = sistema.Receita(paciente, medico, medicamento, doenca, observacao)
            medico.autorizar_receita(receita)
            messagebox.showinfo("Receita", receita.gerar_receita())
            farmacia = sistema.SUS.verificar_entrega(paciente, sistema.farmacias)
            messagebox.showinfo("Farmácias", f"Farmácias próximas: {farmacia}")
        else:
            messagebox.showwarning("Erro", "Paciente não encontrado.")
    
    # Criando a janela do funcionário
    window = tk.Tk()
    window.title("Menu Funcionário")

    tk.Label(window, text="Nome do Paciente").grid(row=0, column=0)
    nome_entry = tk.Entry(window)
    nome_entry.grid(row=0, column=1)

    tk.Label(window, text="CPF").grid(row=1, column=0)
    cpf_entry = tk.Entry(window)
    cpf_entry.grid(row=1, column=1)

    tk.Label(window, text="Número SUS").grid(row=2, column=0)
    sus_entry = tk.Entry(window)
    sus_entry.grid(row=2, column=1)

    tk.Button(window, text="Cadastrar Paciente", command=cadastrar_paciente).grid(row=3, column=0, columnspan=2)

    tk.Label(window, text="Nome do Paciente (para consulta)").grid(row=4, column=0)
    nome_consulta_entry = tk.Entry(window)
    nome_consulta_entry.grid(row=4, column=1)

    tk.Label(window, text="Medicamento").grid(row=5, column=0)
    medicamento_entry = tk.Entry(window)
    medicamento_entry.grid(row=5, column=1)

    tk.Label(window, text="Doença").grid(row=6, column=0)
    doenca_entry = tk.Entry(window)
    doenca_entry.grid(row=6, column=1)

    tk.Label(window, text="Observação").grid(row=7, column=0)
    observacao_entry = tk.Entry(window)
    observacao_entry.grid(row=7, column=1)

    tk.Button(window, text="Registrar Consulta", command=registrar_consulta).grid(row=8, column=0, columnspan=2)

    tk.Button(window, text="Listar Pacientes", command=listar_pacientes).grid(row=9, column=0, columnspan=2)

    tk.Button(window, text="Sair", command=window.quit).grid(row=10, column=0, columnspan=2)

    window.mainloop()

# Função para exibir o menu de paciente
def menu_paciente():
    def registrar_paciente():
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        sus_num = sus_entry.get()
        endereco = sistema.SUS.obter_endereco(sus_num)
        paciente = sistema.Paciente(nome, cpf, sus_num, endereco)
        sistema.pacientes.append(paciente)
        messagebox.showinfo("Cadastro", "Paciente registrado com sucesso!")

    window = tk.Tk()
    window.title("Menu Paciente")

    tk.Label(window, text="Nome do Paciente").grid(row=0, column=0)
    nome_entry = tk.Entry(window)
    nome_entry.grid(row=0, column=1)

    tk.Label(window, text="CPF").grid(row=1, column=0)
    cpf_entry = tk.Entry(window)
    cpf_entry.grid(row=1, column=1)

    tk.Label(window, text="Número SUS").grid(row=2, column=0)
    sus_entry = tk.Entry(window)
    sus_entry.grid(row=2, column=1)

    tk.Button(window, text="Registrar Paciente", command=registrar_paciente).grid(row=3, column=0, columnspan=2)

    tk.Button(window, text="Sair", command=window.quit).grid(row=4, column=0, columnspan=2)

    window.mainloop()

# Função de autenticação para selecionar o tipo de usuário
def autenticar_usuario():
    def verificar_usuario():
        usuario = usuario_entry.get()
        senha = senha_entry.get()

        if usuario == "funcionario" and senha == "senha123":
            menu_funcionario()
            login_window.destroy()
        elif usuario == "paciente" and senha == "paciente":
            menu_paciente()
            login_window.destroy()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas.")

    # Criando a janela de login
    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Usuário").grid(row=0, column=0)
    usuario_entry = tk.Entry(login_window)
    usuario_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Senha").grid(row=1, column=0)
    senha_entry = tk.Entry(login_window, show="*")
    senha_entry.grid(row=1, column=1)

    tk.Button(login_window, text="Entrar", command=verificar_usuario).grid(row=2, column=0, columnspan=2)

    login_window.mainloop()

# Iniciar a aplicação
if __name__ == "__main__":
    autenticar_usuario()