# cliente.py
from datetime import datetime  # Adicionando a importação do datetime

class Endereco:
    def __init__(self, logradouro: str):
        self.logradouro = logradouro

    def calcular_distancia(self, outro_endereco) -> float:
        # Dicionário de distâncias simuladas
        distancias_simuladas = {
            ("Rua Francisco de Paula Pereira, 685", "Rua Vidal Ramos, 404"): 1.2,
            ("Rua Francisco de Paula Pereira, 685", "Rua Caetano Costa, 1016"): 2.5,
            ("Rua Francisco de Paula Pereira, 685", "Rua Francisco de Paula Pereira, 560"): 0.2,
            ("Rua Francisco de Paula Pereira, 685", "Rua Getúlio Vargas, 57"): 3.0,
            ("Rua Vidal Ramos, 404", "Rua Caetano Costa, 1016"): 1.5,
            ("Rua Vidal Ramos, 404", "Rua Francisco de Paula Pereira, 560"): 0.8,
            ("Rua Vidal Ramos, 404", "Rua Getúlio Vargas, 57"): 2.5,
            ("Rua Caetano Costa, 1016", "Rua Francisco de Paula Pereira, 560"): 1.7,
            ("Rua Caetano Costa, 1016", "Rua Getúlio Vargas, 57"): 2.0,
            ("Rua Francisco de Paula Pereira, 560", "Rua Getúlio Vargas, 57"): 2.3,
        }
        chave = (self.logradouro, outro_endereco.logradouro)
        chave_invertida = (outro_endereco.logradouro, self.logradouro)
        return distancias_simuladas.get(chave) or distancias_simuladas.get(chave_invertida, 10.0)  # Valor default caso não ache a chave


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
        self.data_emissao = datetime.now()  # Aqui usamos datetime.now()
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
    @staticmethod
    def obter_endereco(sus_numero: str):
        return Endereco("Rua Francisco de Paula Pereira, 685")  # Exemplo de endereço fixo para o paciente

    @staticmethod
    def verificar_entrega(paciente, farmacias):
        for farmacia in farmacias:
            distancia = paciente.endereco.calcular_distancia(farmacia.endereco)
            if distancia <= 3:  # Verifica farmácias a até 3 km
                return f"{farmacia.nome} a {distancia:.2f} km. Retirar na farmácia."
        return "Nenhuma farmácia próxima. SUS fará a entrega do medicamento."