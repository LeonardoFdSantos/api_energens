# API para Energens.

Vou explicar primeiro, o que é Energens. A Energens, empresa de engenharia, trabalha com serviços de engenharia em geral, instalação de energia fotovoltaica. Temos um problema envolvendo sistemas solares, que é monitorar várias usinas, criar um banco de dados enorme, com registros, dependendo do nome, cliente, tamanho do sistema, parte de previsão de dados. Por isso resolvi criar uma API para ajudar no processo de automação de funções e cálculos automáticos, criados pelo front-end, que serão desenvolvidos posteriormente.

## Arquivos que compõem o sistema para Recursos e Modelos

### Explicação dos modelos utilizados

Estes campos do banco de dados, vão se localizar dentro da tabela. O "id" e "customer" serão as chaves primárias, para buscas feitas.
O método "__init__()" instância o banco de dados e seus recursos serializados, o método "json()" cria a exibição dos dados por meio de JSON para facilitar a visualização da API, qual o padrão de API hoje é utilizar o JSON para envio das informações seriais.
Assim entramos no métodos de classes qual funcionam da mesma forma em todos os modelos, seriam eles os:

   - find
   - save
   - update
   - delete
  
Esses métodos são básicos de todos os modelos, será abordado uma breve explicação deles.
"Find": Método de procurar, ele é utilizado para procurar um "id" ou "city" no banco de dados e retornar o valor ou não retornar nada para o JSON.
"Save": Método de salvar no banco de dados, ele adiciona a informação e faz o salvamento da informação no banco de dados.
"Update": Método de atualizar o banco de dados, passando informações igual qual vão ser modificadas.
"Delete": Método de deletar uma informação pelo "id" ou "city" no banco de dados.


### Explicação dos recursos

#### Get
        
O "get" tem por função retornar um "id" ou "city" especifico com todo conjunto de informações.

#### Post

O "post" tem por meio, postar uma nova requisição no sistema, seguindo seus parametros de "JSON", neste caso sem utilizar o id novamente, pois esse vai por metodo serial já incluido, caso aquele id já esteja ocupado ele envia a mensagem para o cliente, dizendo que o id já existe.

#### Put

O "put" tem a função de atulizar um "id" ou "city" já existente.

#### Delete

O "delete" tem a função de deletar a "id" ou "city" selecionada.

1. [Modelo de senhas de Acesso](models/accessPassword.py) e [Recursos da senhas de Acesso](resources/accessPassword.py)
    
#### Modelo

O modelo, cria o banco de dados de nome, "accessPassword" com os seguintes campos:

   - id
   - customer
   - portal
   - user
   - password

#### Recursos

A classe "AccessPasswords" com a sua única função "get", busca toda a tabela e retorna por separação em formato JSON.

A classe "AccessPassword" possui as funções "get", "post", "put" e "delete", qual representa o CRUD deste banco de dados.
   
2. [Modelo de Limpezas](models/cleanings.py) e [Recursos da Limpeza](resources/cleanings.py)

3. [Modelo do consolidados](models/consolidated.py) e [Recursos do consolidados](resources/consolidated.py)

4. [Modelo de Registro de Cliente](models/customerRegistration.py) e [Recursos do registro de clientes](resources/customerRegistration.py)

5. [Modelo de registros de senhas da Internet](models/internetPasswords.py) e [Recursos do registros de senhas da Internet](resources/internetPasswords.py)

6. [Modelo de registro de Inversores](models/inverter.py) e [Recursos de registro de Inversores](resources/inverter.py)

7. [Modelo de Irradiação local](models/localIrradiation.py) e [Recursos do Irradiação local](resources/localIrradiation.py)

8. [Modelo da previsão de geração](models/predicted.py) e [Recursos da previsão de geração](resources/predicted.py)



