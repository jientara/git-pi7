import tkinter as tk
from tkinter import messagebox, ttk
import sistema

def centralizar_janela(janela, largura=300, altura=150):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

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

    window = tk.Tk()
    window.title("Menu Funcionário")
    centralizar_janela(window, 420, 400)
    style = ttk.Style(window)
    style.theme_use('clam')

    frame = ttk.Frame(window, padding=20)
    frame.grid(row=0, column=0, sticky="nsew")

    ttk.Label(frame, text="Nome do Paciente").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    nome_entry = ttk.Entry(frame)
    nome_entry.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame, text="CPF").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    cpf_entry = ttk.Entry(frame)
    cpf_entry.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(frame, text="Número SUS").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    sus_entry = ttk.Entry(frame)
    sus_entry.grid(row=2, column=1, padx=10, pady=5)

    ttk.Button(frame, text="Cadastrar Paciente", command=cadastrar_paciente).grid(row=3, column=0, columnspan=2, pady=10)

    ttk.Label(frame, text="Nome do Paciente (para consulta)").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    nome_consulta_entry = ttk.Entry(frame)
    nome_consulta_entry.grid(row=4, column=1, padx=10, pady=5)

    ttk.Label(frame, text="Medicamento").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    medicamento_entry = ttk.Entry(frame)
    medicamento_entry.grid(row=5, column=1, padx=10, pady=5)

    ttk.Label(frame, text="Doença").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    doenca_entry = ttk.Entry(frame)
    doenca_entry.grid(row=6, column=1, padx=10, pady=5)

    ttk.Label(frame, text="Observação").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    observacao_entry = ttk.Entry(frame)
    observacao_entry.grid(row=7, column=1, padx=10, pady=5)

    ttk.Button(frame, text="Registrar Consulta", command=registrar_consulta).grid(row=8, column=0, columnspan=2, pady=10)
    ttk.Button(frame, text="Listar Pacientes", command=listar_pacientes).grid(row=9, column=0, columnspan=2, pady=10)
    ttk.Button(frame, text="Sair", command=window.quit).grid(row=10, column=0, columnspan=2, pady=10)

    window.mainloop()

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
    centralizar_janela(window, 350, 220)
    style = ttk.Style(window)
    style.theme_use('clam')

    frame = ttk.Frame(window, padding=20)
    frame.grid(row=0, column=0, sticky="nsew")

    ttk.Label(frame, text="Nome do Paciente").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    nome_entry = ttk.Entry(frame)
    nome_entry.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame, text="CPF").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    cpf_entry = ttk.Entry(frame)
    cpf_entry.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(frame, text="Número SUS").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    sus_entry = ttk.Entry(frame)
    sus_entry.grid(row=2, column=1, padx=10, pady=5)

    ttk.Button(frame, text="Registrar Paciente", command=registrar_paciente).grid(row=3, column=0, columnspan=2, pady=10)
    ttk.Button(frame, text="Sair", command=window.quit).grid(row=4, column=0, columnspan=2, pady=10)

    window.mainloop()

def autenticar_usuario():
    def verificar_usuario():
        usuario = usuario_entry.get()
        senha = senha_entry.get()
        if usuario == "funcionario" and senha == "senha123":
            login_window.destroy()
            menu_funcionario()
        elif usuario == "paciente" and senha == "paciente":
            login_window.destroy()
            menu_paciente()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas.")

    login_window = tk.Tk()
    login_window.title("Login")
    centralizar_janela(login_window, 320, 180)
    style = ttk.Style(login_window)
    style.theme_use('clam')

    frame = ttk.Frame(login_window, padding=20)
    frame.grid(row=0, column=0, sticky="nsew")

    ttk.Label(frame, text="Usuário").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    usuario_entry = ttk.Entry(frame)
    usuario_entry.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame, text="Senha").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    senha_entry = ttk.Entry(frame, show="*")
    senha_entry.grid(row=1, column=1, padx=10, pady=5)

    ttk.Button(frame, text="Entrar", command=verificar_usuario).grid(row=2, column=0, columnspan=2, pady=15)

    login_window.mainloop()

if __name__ == "__main__":
    autenticar_usuario()