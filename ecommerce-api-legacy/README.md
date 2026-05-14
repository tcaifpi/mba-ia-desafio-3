# Ecommerce API Legacy - Modernização de Sistemas

**Responsável:** Tiago Aragão (Analista de TI)  
**Projeto:** Refatoração e Migração de API de E-commerce  
**Tecnologias:** Node.js, Express, JavaScript (ES6+).

## 🚀 Visão Geral
Este repositório contém a camada de API de um sistema de e-commerce legado. O objetivo deste projeto foi realizar o saneamento de débitos técnicos, melhorar a estrutura de rotas e preparar a aplicação para uma futura migração para microsserviços, garantindo que as regras de negócio essenciais fossem preservadas.

## 🛠️ Intervenções Técnicas Realizadas

1. **Padronização de Endpoints:** Reestruturação das rotas para seguir o padrão RESTful, utilizando nomes de recursos claros e métodos HTTP corretos (GET, POST, PUT, DELETE).
2. **Separação de Preocupações (SoC):** Organização do diretório `src` para separar a lógica de roteamento, controladores de requisição e serviços de dados.
3. **Gerenciamento de Dependências:** Limpeza do `package.json` e atualização de pacotes críticos para evitar vulnerabilidades de segurança conhecidas.
4. **Documentação de Interface:** Criação do arquivo `api.http` para permitir testes rápidos de integração e documentar o comportamento esperado de cada endpoint.

## 📂 Estrutura do Projeto

- `src/`: Contém todo o código-fonte da aplicação.
- `node_modules/`: Dependências externas do projeto.
- `api.http`: Arquivo de teste de requisições (compatível com REST Client).
- `package.json`: Manifesto do projeto e scripts de execução.

## 🚦 Como Executar

1. **Instalar Dependências:**
   ```bash
   npm install