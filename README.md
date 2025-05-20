Sistema de Saúde
Este projeto é um sistema de gerenciamento de saúde que permite o cadastro de pacientes, registro de consultas e gerenciamento de farmácias. A interface gráfica foi construída usando a biblioteca Tkinter, proporcionando uma interação mais amigável e intuitiva com o usuário.

Estrutura do Projeto
O projeto contém os seguintes arquivos:

cliente.py: Define várias classes relacionadas ao sistema de saúde, como Endereco, Paciente, Medico, Farmacia, Receita e SUS. Também contém métodos para calcular distâncias entre endereços e gerenciar dados de pacientes e médicos.

sistema.py: Contém a lógica principal da aplicação, fornecendo funções para cadastrar pacientes, listar pacientes, registrar consultas e verificar farmácias próximas. Este arquivo é utilizado pelo app.py para realizar as operações de backend.

app.py: Este é o arquivo que deve ser executado para iniciar a interface gráfica. Ele utiliza a biblioteca Tkinter para criar janelas de login e menus de navegação, onde o usuário pode se identificar como paciente ou funcionário e realizar ações específicas de acordo com o tipo de usuário.

Como Configurar
1. Instalar o Python
Certifique-se de que o Python está instalado na sua máquina. Você pode verificar se o Python está instalado executando o seguinte comando no terminal:

bash
Copiar
Editar
python --version
2. Instalar as Dependências
Se o seu projeto tiver dependências, instale-as utilizando o pip. Para isso, basta executar o seguinte comando:

bash
Copiar
Editar
pip install -r requirements.txt
Se não houver o arquivo requirements.txt, o único pré-requisito é o Tkinter, que é geralmente pré-instalado no Python.

3. Baixar ou Clonar o Repositório
Clone ou baixe os arquivos do projeto para a sua máquina:

bash
Copiar
Editar
git clone https://github.com/seu_usuario/seu_repositorio.git
4. Navegar até o Diretório do Projeto
Use o terminal para acessar o diretório onde os arquivos do projeto foram baixados:

bash
Copiar
Editar
cd nome_do_projeto
Como Usar
1. Executar o Sistema
Para iniciar o sistema, execute o arquivo app.py:

bash
Copiar
Editar
python app.py
Ao rodar o script, uma janela de login será exibida. O sistema suporta dois tipos de usuários:

Paciente

Funcionário (Admin)

2. Tela de Login
Na tela de login, você será solicitado a fornecer as credenciais:

Usuário: Para o paciente, use "paciente". Para o funcionário, use "funcionario".

Senha: A senha para o paciente é "paciente", e para o funcionário é "senha123".

Após inserir as credenciais corretas, o sistema abrirá a interface correspondente (paciente ou funcionário).

3. Menu do Paciente
Após um paciente logar com sucesso, a interface será direcionada para o menu de paciente, onde ele poderá:

Registrar Paciente: O paciente poderá se registrar no sistema inserindo seu nome, CPF e número do SUS.

Após o registro, o paciente não terá outras opções de interação no sistema.

4. Menu do Funcionário (Admin)
Após um funcionário logar com sucesso, a interface será direcionada para o menu de funcionário, onde ele terá mais opções disponíveis, como:

Cadastrar Paciente: O funcionário pode cadastrar novos pacientes fornecendo o nome, CPF e número do SUS.

Listar Pacientes: O funcionário pode visualizar todos os pacientes cadastrados no sistema.

Registrar Consulta: O funcionário pode registrar uma consulta médica para um paciente já cadastrado, fornecendo informações como medicamento, doença e observações do médico.

Essas opções estarão disponíveis em uma janela com campos de entrada e botões específicos para cada ação.

5. Funções Específicas
Cadastrar Paciente
Ao escolher a opção de Cadastrar Paciente, o usuário será solicitado a preencher um formulário com os seguintes dados:

Nome do paciente

CPF

Número do SUS

Após o cadastro, uma mensagem será exibida informando que o paciente foi registrado com sucesso.

Listar Pacientes
Se o funcionário escolher Listar Pacientes, uma lista com os dados dos pacientes cadastrados será exibida em uma janela pop-up.

Registrar Consulta
Para Registrar Consulta, o funcionário deverá fornecer:

Nome do paciente (para localizar o paciente no banco de dados)

Medicamento prescrito

Doença diagnosticada

Observações adicionais

Após o registro da consulta, o sistema irá gerar uma receita médica com as informações inseridas e mostrar quais farmácias estão próximas ao paciente para entrega de medicamentos.

6. Interface Gráfica
Toda a interação com o sistema se dá por meio de uma interface gráfica desenvolvida com Tkinter. O sistema abrirá novas janelas conforme o tipo de usuário, e em cada janela estarão disponíveis os campos e botões para realizar as ações desejadas.

Fluxo de Funcionalidade
Paciente:
Login: O paciente faz login com o usuário e senha "paciente".

Cadastrar Paciente: Após o login, o paciente pode se cadastrar no sistema, fornecendo suas informações.

Após Cadastro: O paciente não terá mais opções após o registro.

Funcionário:
Login: O funcionário faz login com o usuário e senha "senha123".

Cadastrar Paciente: O funcionário pode cadastrar novos pacientes.

Listar Pacientes: O funcionário pode visualizar todos os pacientes cadastrados no sistema.

Registrar Consulta: O funcionário pode registrar uma consulta para um paciente, gerando uma receita médica.