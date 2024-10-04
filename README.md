Programa Bancário Utilizando Conceitos de POO em Python
Este repositório contém um programa em Python que permite ao usuário realizar operações bancárias básicas utilizando os conceitos de Programação Orientada a Objetos (POO). As operações disponíveis são:

Criar conta
Verificar saldo
Depositar dinheiro
Sacar dinheiro
Encerrar o atendimento
O programa armazena as informações das contas bancárias em um dicionário e utiliza classes para representar as contas e as operações, demonstrando na prática os princípios da POO.

🎯 Objetivos
Aplicar os conceitos de POO em Python:
Implementação de classes, objetos, atributos e métodos.
Uso de encapsulamento para proteger os dados das contas.
Criar um menu interativo para o usuário:
Interface simples no terminal para interação com o sistema bancário.
📋 Descrição do Projeto
O programa simula um sistema bancário básico, onde o usuário pode criar uma conta e realizar operações financeiras. Cada conta bancária é representada por um objeto da classe ContaBancaria, que encapsula os dados e fornece métodos para interagir com a conta.

Funcionalidades:
Criar Conta: O usuário pode criar uma nova conta fornecendo um número de conta e o nome do titular.

Verificar Saldo: Permite ao usuário verificar o saldo atual de sua conta.

Depositar Dinheiro: O usuário pode depositar um valor em sua conta, aumentando o saldo disponível.

Sacar Dinheiro: Permite ao usuário sacar um valor de sua conta, com verificação de saldo suficiente.

Encerrar Atendimento: Finaliza o programa.

🛠️ Tecnologias Utilizadas
Python 3.x: Linguagem de programação utilizada para desenvolver o programa.
Paradigma POO: Aplicação dos conceitos de Programação Orientada a Objetos.

🚀 Como Executar o Programa
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Navegue até o diretório do projeto:

bash
Copiar código
cd seu-repositorio
Execute o programa:

bash
Copiar código
python programa_bancario.py
Certifique-se de ter o Python 3 instalado em seu ambiente.

📖 Instruções de Uso
Ao executar o programa, um menu interativo será exibido no terminal:

markdown
Copiar código
=== Banco POO ===
1. Criar conta
2. Verificar saldo
3. Depositar dinheiro
4. Sacar dinheiro
5. Encerrar atendimento
Escolha uma opção:
Digite o número correspondente à operação que deseja realizar e siga as instruções apresentadas.
Exemplo de Uso:
Criar Conta:

Informe o número da nova conta.
Informe o nome do titular da conta.
A conta será criada e armazenada no sistema.
Depositar Dinheiro:

Informe o número da sua conta.
Informe o valor para depósito.
O saldo da conta será atualizado.
Sacar Dinheiro:

Informe o número da sua conta.
Informe o valor para saque.
O programa verificará se há saldo suficiente e realizará a operação.
🧩 Conceitos de POO Aplicados
Classes e Objetos: A classe ContaBancaria define o modelo para as contas, e cada conta criada é um objeto dessa classe.

Atributos e Métodos:

Atributos: numero_conta, titular, __saldo (privado).
Métodos:
verificar_saldo()
depositar(valor)
sacar(valor)
encerrar_conta()
Encapsulamento:

Uso de atributos privados (__saldo) para proteger os dados internos.
Implementação de getters e setters com o decorador @property para acessar e modificar os atributos de forma controlada.
📝 Código Fonte
O código completo está disponível no arquivo programa_bancario.py.

📚 Aprendizados
Este projeto reforça a compreensão dos conceitos fundamentais da POO em Python, incluindo:

Criação e uso de classes e objetos.
Encapsulamento e proteção de dados sensíveis.
Implementação de métodos e propriedades com validações.
Interação com o usuário através de um menu em linha de comando.
📌 Observações
Validações Simples: O programa inclui validações básicas para as operações financeiras, mas não cobre todos os cenários possíveis.

Melhorias Futuras:

Implementação de persistência de dados (salvar informações das contas em um arquivo ou banco de dados).
Desenvolvimento de uma interface gráfica para melhor experiência do usuário.
Ampliação das funcionalidades bancárias (transferências, extratos, etc.).

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

📄 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

📞 Contato
Autor: Carlos Celestino
E-mail: carloscelestino.pydev@gmail.com
LinkedIn: https://www.linkedin.com/in/carloscelestinosf1/
Obrigado por visitar este projeto!
