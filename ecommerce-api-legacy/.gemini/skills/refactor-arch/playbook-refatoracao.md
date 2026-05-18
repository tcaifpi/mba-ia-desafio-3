# Playbook de Refatoração Arquitetural

Este guia detalha as estratégias de refatoração aplicadas para eliminar a dívida técnica e mitigar vulnerabilidades de segurança no sistema de e-commerce.

---

## 1. Isolamento de Credenciais (Secret Management)
**Resolve:** Credenciais Expostas (CRITICAL)
* **Antes:** As chaves de acesso e passwords eram declaradas diretamente no código.
    ```python
    def configurar_pagamento():
        api_key = "sk_live_51MZ2pL..." # Chave exposta no código
        gateway.init(api_key)
    ```
* **Depois:** Utilização de variáveis de ambiente via `.env`.
    ```python
    import os
    def configurar_pagamento():
        api_key = os.getenv("STRIPE_API_KEY")
        gateway.init(api_key)
    ```

## 2. Consultas Parametrizadas (Parameterized Queries)
**Resolve:** Injeção de SQL (CRITICAL)
* **Antes:** O input do utilizador era concatenado diretamente na query SQL.
    ```python
    def buscar_produto(nome):
        # Vulnerável a: ' OR '1'='1
        query = f"SELECT * FROM produtos WHERE nome = '{nome}'"
        return db.execute(query)
    ```
* **Depois:** Uso de placeholders (`?`) para garantir a sanitização.
    ```python
    def buscar_produto(nome):
        query = "SELECT * FROM produtos WHERE nome = ?"
        return db.execute(query, (nome,))
    ```

## 3. Modernização de Hashing (Security Update)
**Resolve:** Uso de APIs Deprecated (HIGH)
* **Antes:** Uso do algoritmo MD5 (obsoleto e vulnerável a colisões).
    ```python
    import hashlib
    hash_password = hashlib.md5(senha.encode()).hexdigest()
    ```
* **Depois:** Uso de `werkzeug.security` com algoritmos de derivação de chave robustos.
    ```python
    from werkzeug.security import generate_password_hash
    hash_password = generate_password_hash(senha, method='pbkdf2:sha256')
    ```

## 4. Implementação de Eager Loading
**Resolve:** Padrão N+1 Query (HIGH)
* **Antes:** Cada iteração de um loop disparava uma nova consulta individual ao banco.
    ```python
    pedidos = Pedido.query.all()
    for p in pedidos:
        print(p.itens) # Dispara N queries adicionais
    ```
* **Depois:** Uso de `joinedload` para carregar dados relacionados numa única query.
    ```python
    from sqlalchemy.orm import joinedload
    pedidos = Pedido.query.options(joinedload(Pedido.itens)).all()
    ```

## 5. Extração de Responsabilidade (SRP)
**Resolve:** Objeto Deus / God Class (MEDIUM)
* **Antes:** A classe `EncomendaManager` geria stock, calculava impostos e enviava e-mails.
* **Depois:** Divisão em serviços especializados: `StockService`, `TaxCalculator` e `NotificationProvider`.

## 6. Tratamento Granular de Erros
**Resolve:** Tratamento Genérico de Exceções (MEDIUM)
* **Antes:** Erros eram capturados e ignorados, dificultando o debug.
    ```python
    try:
        pagar()
    except Exception:
        pass # Falha silenciosa
    ```
* **Depois:** Captura de exceções específicas com log adequado.
    ```python
    try:
        pagar()
    except SaldoInsuficiente:
        log.warning("Cliente sem fundos")
    except GatewayError:
        log.error("Erro crítico no provedor de pagamento")
    ```

## 7. Refatoração de Lógica de Negócio (Extract Method)
**Resolve:** Método Longo (LOW)
* **Antes:** O método `finalizar_venda()` continha centenas de linhas com lógica misturada.
* **Depois:** O código foi dividido em métodos menores e coesos: `validar_carrinho()`, `reservar_stock()` e `gerar_fatura()`.

## 8. Encapsulamento de Parâmetros (Parameter Object)
**Resolve:** Aglomerados de Dados / Data Clumps (LOW)
* **Antes:** Métodos que recebiam longas listas de argumentos relacionados.
    ```python
    def enviar_envio(rua, numero, cidade, cp, pais):
        ...
    ```
* **Depois:** Agrupamento num objeto de valor (Value Object) ou Data Class.
    ```python
    from dataclasses import dataclass

    @dataclass
    class EnderecoEnvio:
        rua: str; numero: int; cidade: str; cp: str; pais: str

    def enviar_envio(endereco: EnderecoEnvio):
        ...
    ```