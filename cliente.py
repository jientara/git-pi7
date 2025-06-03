from datetime import datetime  # Adicionando a importação do datetime

class Endereco:
    def __init__(self, logradouro: str):
        self.logradouro = logradouro

    def calcular_distancia(self, outro_endereco) -> float:
        # Dicionário de distâncias simuladas
        distancias_simuladas = {
    ("Rua Getúlio Vargas, 57 - Centro", "Rua Vidal Ramos, 829 - Centro"): 0.5,
    ("Rua Getúlio Vargas, 57 - Centro", "Rua Caetano Costa, 1016 - Centro"): 1.2,
    ("Rua Getúlio Vargas, 57 - Centro", "Rua Francisco de Paula Pereira, 494 - Centro"): 0.8,
    ("Rua Getúlio Vargas, 57 - Centro", "Rua Felipe Schmidt, 507 - Centro"): 1.0,
    ("Rua Getúlio Vargas, 57 - Centro", "Rua Duque de Caxias, 1420 - Alto das Palmeiras"): 2.8,
    ("Rua Getúlio Vargas, 57 - Centro", "Rua Nazir Cordeiro, 791 - Campo d'Água Verde"): 3.0,
    ("Rua Getúlio Vargas, 57 - Centro", "Rua Reinoldo Hübner, 107 - Piedade"): 2.4,
    ("Rua Getúlio Vargas, 57 - Centro", "Rua Roberto Ehlke, 688 - Jardim Esperança"): 3.2,
    ("Rua Getúlio Vargas, 57 - Centro", "Rua Henrique Sorg, 138 - Jardim Esperança"): 3.4,
    }

        chave = (self.logradouro, outro_endereco.logradouro)
        chave_invertida = (outro_endereco.logradouro, self.logradouro)

        return distancias_simuladas.get(chave, distancias_simuladas.get(chave_invertida, 10.0))

class Paciente:
    def __init__(self, nome, cpf, sus_numero, endereco):
        self.nome = nome
        self.cpf = cpf
        self.sus_numero = sus_numero
        self.endereco = endereco

class Medico:
    def __init__(self, nome, crm):
        self.nome = nome
        self.crm = crm

    def autorizar_receita(self, receita):
        receita.autorizada = True
        return True

class Farmacia:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Receita:
    def __init__(self, paciente, medico, medicamento, doenca, observacao):
        self.paciente = paciente
        self.medico = medico
        self.medicamento = medicamento
        self.doenca = doenca
        self.observacao = observacao
        self.data_emissao = datetime.now()
        self.autorizada = False

    def gerar_receita(self):
        if not self.autorizada:
            return "Receita não autorizada."
        return (f"\nReceita Médica\n"
                f"Paciente: {self.paciente.nome}\n"
                f"Médico: {self.medico.nome} (CRM: {self.medico.crm})\n"
                f"Medicamento: {self.medicamento}\n"
                f"Doença: {self.doenca}\n"
                f"Observações: {self.observacao}\n"
                f"Data: {self.data_emissao.strftime('%d/%m/%Y')}\n")

class SUS:
    enderecos_pacientes = {
        "1": Endereco("Rua Getúlio Vargas, 57 - Centro"),
        "2": Endereco("Rua Vidal Ramos, 829 - Centro"),
        "3": Endereco("Rua Caetano Costa, 1016 - Centro"),
        "4": Endereco("Rua Francisco de Paula Pereira, 494 - Centro"),
        "5": Endereco("Rua Felipe Schmidt, 507 - Centro"),
    }

    @staticmethod
    def obter_endereco(sus_num):
        """Retorna o endereço do paciente pelo número SUS, ou None se não encontrado."""
        endereco = SUS.enderecos_pacientes.get(sus_num)
        if not endereco:
            print(f"Endereço não encontrado para SUS: {sus_num}")
        return endereco

    @staticmethod
    def verificar_entrega(paciente, farmacias):
        """Retorna a farmácia mais próxima do paciente."""
        if not farmacias:
            return "Nenhuma farmácia cadastrada."
        farmacia_mais_proxima = min(
            farmacias, key=lambda f: paciente.endereco.calcular_distancia(f.endereco)
        )
        return (
            f"A farmácia mais próxima para o paciente {paciente.nome} é {farmacia_mais_proxima.nome}, "
            f"localizada em {farmacia_mais_proxima.endereco.logradouro}."
        )