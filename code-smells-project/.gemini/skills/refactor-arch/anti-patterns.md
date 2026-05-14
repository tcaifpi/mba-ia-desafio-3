Catálogo de Anti-padrões e Heurísticas de Auditoria
Este catálogo é utilizado para identificar vulnerabilidades de segurança, falhas estruturais e débitos técnicos nos projetos auditados.

1. Segurança e Integridade de Dados
SQL Injection [CRITICAL]: Uso de f-strings ou concatenação direta de entradas de usuários em consultas SQL, permitindo a execução de comandos maliciosos no banco de dados.

Insecure Hashing / Deprecated APIs [CRITICAL]: Uso de algoritmos de criptografia obsoletos e vulneráveis, como MD5 ou SHA1, para o armazenamento de senhas.

Hardcoded Secrets [CRITICAL]: Armazenamento de chaves de API, senhas de banco de dados ou tokens de acesso diretamente no código-fonte, em vez de utilizar variáveis de ambiente (.env).

Exposição de Informações Sensíveis [HIGH]: Tratamento de erros que retorna stack traces ou logs detalhados para o usuário final, expondo a estrutura interna da aplicação.

2. Arquitetura e Design (Code Smells)
God Class / God File [HIGH]: Arquivos ou classes que concentram múltiplas responsabilidades (ex: rotas, lógica de negócio e persistência em um único arquivo), violando o Princípio de Responsabilidade Única (SRP).

Fat Routes [MEDIUM]: Endpoints de API que contêm lógica de negócio complexa ou processamento de dados que deveria estar isolado em Controllers ou Services.

Acoplamento Forte [MEDIUM]: Dependência direta entre módulos que dificulta a testabilidade e a manutenção, impedindo a substituição de componentes (ex: banco de dados).

3. Performance e Manutenibilidade
N+1 Query Problem [HIGH]: Execução de múltiplas consultas ao banco de dados dentro de loops, causando degradação severa de performance conforme o volume de dados cresce.

Código Morto e Inconsistência [LOW]: Presença de funções não utilizadas, variáveis com nomes genéricos (ex: data, var1) e falta de padronização entre CamelCase e snake_case.