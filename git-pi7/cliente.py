# cliente.py
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

    ("Rua Vidal Ramos, 829 - Centro", "Rua Caetano Costa, 1016 - Centro"): 0.6,
    ("Rua Vidal Ramos, 829 - Centro", "Rua Francisco de Paula Pereira, 494 - Centro"): 0.7,
    ("Rua Vidal Ramos, 829 - Centro", "Rua Felipe Schmidt, 507 - Centro"): 0.9,
    ("Rua Vidal Ramos, 829 - Centro", "Rua Duque de Caxias, 1420 - Alto das Palmeiras"): 2.5,

    ("Rua Caetano Costa, 1016 - Centro", "Rua Francisco de Paula Pereira, 494 - Centro"): 0.4,
    ("Rua Caetano Costa, 1016 - Centro", "Rua Felipe Schmidt, 507 - Centro"): 0.6,
    ("Rua Caetano Costa, 1016 - Centro", "Rua Duque de Caxias, 1420 - Alto das Palmeiras"): 2.0,

    ("Rua Duque de Caxias, 1420 - Alto das Palmeiras", "Rua Nazir Cordeiro, 791 - Campo d'Água Verde"): 2.2,
    ("Rua Nazir Cordeiro, 791 - Campo d'Água Verde", "Rua Reinoldo Hübner, 107 - Piedade"): 1.8,
    ("Rua Reinoldo Hübner, 107 - Piedade", "Rua Roberto Ehlke, 688 - Jardim Esperança"): 1.6,
    ("Rua Roberto Ehlke, 688 - Jardim Esperança", "Rua Henrique Sorg, 138 - Jardim Esperança"): 0.5,

    # Incluindo algumas distâncias diretas para farmácias
    ("Rua Francisco de Paula Pereira, 494 - Centro", "Rua Francisco de Paula Pereira, 564 - Centro"): 0.1,
    ("Rua Major Vieira, 505 - Centro", "Rua Getúlio Vargas, 57 - Centro"): 0.3,
    ("Rua Major Vieira, 505 - Centro", "Rua Vidal Ramos, 829 - Centro"): 0.7,
}

# Cria a chave com os dois endereços, de forma ordenada
        chave = (self.logradouro, outro_endereco.logradouro)
        chave_invertida = (outro_endereco.logradouro, self.logradouro)

        # Retorna a distância, se encontrada, caso contrário retorna 10.0 (valor padrão)
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
        self.data_emissao = datetime.now()  #Aqui usamos datetime.now()
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
    "6": Endereco("Rua Duque de Caxias, 1420 - Alto das Palmeiras"),
    "7": Endereco("Rua Nazir Cordeiro, 791 - Campo d'Água Verde"),
    "8": Endereco("Rua Reinoldo Hübner, 107 - Piedade"),
    "9": Endereco("Rua Roberto Ehlke, 688 - Jardim Esperança"),
    "0": Endereco("Rua Henrique Sorg, 138 - Jardim Esperança"),
}

    @staticmethod
    def obter_endereco(sus_numero: str):
        return SUS.enderecos_pacientes.get(
            sus_numero,
            Endereco("Endereço não cadastrado")  # Valor padrão se não encontrar
        )
    
    @staticmethod
    def verificar_entrega(paciente, farmacias):
        for farmacia in farmacias:
            distancia = paciente.endereco.calcular_distancia(farmacia.endereco)
            if distancia <= 3:  # Verifica farmácias a até 3 km
                return f"{farmacia.nome} a {distancia:.2f} km. Retirar na farmácia."
        return "Nenhuma farmácia próxima. SUS fará a entrega do medicamento."