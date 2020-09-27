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

#### Modelo

O modelo, cria o banco de dados de nome, "cleanings" com os seguintes campos:

   - id
   - customer
   - date
   - nextDate
   - maximumTime

#### Recursos

A classe "Cleanings" com a sua única função "get", busca toda a tabela e retorna por separação em formato JSON.

A classe "Cleaning" possui as funções "get", "post", "put" e "delete", qual representa o CRUD deste banco de dados.

3. [Modelo do consolidados](models/consolidated.py) e [Recursos do consolidados](resources/consolidated.py)

O modelo, cria o banco de dados de nome, "consolidated" com os seguintes campos:

   - id
   - customer
   - projectNumber
   - modulesNumber
   - modulesPower
   - powerTotal
   - effectiveness
   - delivered
   - local

#### Recursos

A classe "Consolidated" com a sua única função "get", busca toda a tabela e retorna por separação em formato JSON.

A classe "Funded" possui as funções "get", "post", "put" e "delete", qual representa o CRUD deste banco de dados.

4. [Modelo de Registro de Cliente](models/customerRegistration.py) e [Recursos do registro de clientes](resources/customerRegistration.py)

O modelo, cria o banco de dados de nome, "customerRegistration" com os seguintes campos:

   - id
   - customer
   - typeCustomer
   - CPF_CNPJ
   - code

#### Recursos

A classe "CustomerRegistrations" com a sua única função "get", busca toda a tabela e retorna por separação em formato JSON.

A classe "CustomerRegistration" possui as funções "get", "post", "put" e "delete", qual representa o CRUD deste banco de dados.

5. [Modelo de registros de senhas da Internet](models/internetPasswords.py) e [Recursos do registros de senhas da Internet](resources/internetPasswords.py)

O modelo, cria o banco de dados de nome, "internetPasswords" com os seguintes campos:

   - id
   - customer
   - ssid
   - password

#### Recursos

A classe "InternetPasswords" com a sua única função "get", busca toda a tabela e retorna por separação em formato JSON.

A classe "InternetPassword" possui as funções "get", "post", "put" e "delete", qual representa o CRUD deste banco de dados.

6. [Modelo de registro de Inversores](models/inverter.py) e [Recursos de registro de Inversores](resources/inverter.py)

O modelo, cria o banco de dados de nome, "inverters" com os seguintes campos:

   - id
   - customer
   - numberInverters
   - inverter01
   - inverter02
   - inverter03
   - inverter04
   - inverter05

#### Recursos

A classe "Inverters" com a sua única função "get", busca toda a tabela e retorna por separação em formato JSON.

A classe "Inverter" possui as funções "get", "post", "put" e "delete", qual representa o CRUD deste banco de dados.

7. [Modelo de Irradiação local](models/localIrradiation.py) e [Recursos do Irradiação local](resources/localIrradiation.py)

O modelo, cria o banco de dados de nome, "localIrradiation" com os seguintes campos:

   - city
   - january
   - february
   - march
   - april
   - may
   - june
   - july
   - august
   - september
   - october
   - november
   - december
   - average

#### Recursos

A classe "LocationsIrradiation" com a sua única função "get", busca toda a tabela e retorna por separação em formato JSON.

A classe "LocalIrradiation" possui as funções "get", "post", "put" e "delete", qual representa o CRUD deste banco de dados.

8. [Modelo da previsão de geração](models/predicted.py) e [Recursos da previsão de geração](resources/predicted.py)

O modelo, cria o banco de dados de nome, "provided" com os seguintes campos:

   - id
   - customer
   - effectiveness
   - powerTotal
   - local
   - january
   - february
   - march
   - april
   - may
   - june
   - july
   - august
   - september
   - october
   - november
   - december
   - average

#### Recursos

A classe "Predicted" com a sua única função "get", busca toda a tabela e retorna por separação em formato JSON.

A classe "Provided" possui as funções "get", "post", "put" e "delete", qual representa o CRUD deste banco de dados.



