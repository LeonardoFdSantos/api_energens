# API para Energens.

Vou explicar primeiro, o que é Energens. A Energens, empresa de engenharia, trabalha com serviços de engenharia em geral, instalação de energia fotovoltaica. Temos um problema envolvendo sistemas solares, que é monitorar várias usinas, criar um banco de dados enorme, com registros, dependendo do nome, cliente, tamanho do sistema, parte de previsão de dados. Por isso resolvi criar uma API para ajudar no processo de automação de funções e cálculos automáticos, criados pelo front-end, que serão desenvolvidos posteriormente.

## Arquivos que compõem o sistema para Recursos e Modelos

1. [Modelo de senhas de Acesso](models/accessPassword.py) e [Recursos da senhas de Acesso](resources/accessPassword.py)

2. [Modelo de Limpezas](models/cleanings.py) e [Recursos da Limpeza](resources/cleanings.py)

3. [Modelo do consolidados](models/consolidated.py) e [Recursos do consolidados](resources/consolidated.py)

4. [Modelo de Registro de Cliente](models/customerRegistration.py) e [Recursos do registro de clientes](resources/customerRegistration.py)

5. [Modelo de registros de senhas da Internet](models/internetPasswords.py) e [Recursos do registros de senhas da Internet](resources/internetPasswords.py)

6. [Modelo de registro de Inversores](models/inverter.py) e [Recursos de registro de Inversores](resources/inverter.py)

7. [Modelo de Irradiação local](models/localIrradiation.py) e [Recursos do Irradiação local](resources/localIrradiation.py)

8. [Modelo da previsão de geração](models/predicted.py) e [Recursos da previsão de geração](resources/predicted.py)

