Relatório de Auditoria e Modernização de SoftwareProjeto: Refatoração de Sistema de Gestão (Legacy para MVC)Responsável: Tiago AragãoData: 13 de maio de 2026Status: Concluído / Aprovado1. Resumo ExecutivoEste relatório detalha o processo de auditoria técnica e refatoração estrutural realizado no projeto code-smells-project. O objetivo principal foi a transição de uma arquitetura monolítica e vulnerável para um padrão MVC (Model-View-Controller), eliminando riscos críticos de segurança e débitos técnicos de performance.2. Diagnóstico de Anti-padrões (Auditoria)Durante a fase inicial, foram identificados os seguintes "Code Smells" e vulnerabilidades:Anti-padrãoLocalizaçãoGravidadeImpactoSQL Injectionmodels.py / app.pyCríticaPossibilidade de exfiltração total de dados via f-strings.Hardcoded Secretsapp.pyCríticaChaves de segurança expostas no código-fonte.God Fileapp.pyMédiaDificuldade de manutenção e escalabilidade (Lógica misturada com Rotas).N+1 Query Problemmodels.pyMédiaDegradação de performance em listagens de pedidos.3. Plano de Ação e RefatoraçãoA intervenção foi dividida em três pilares fundamentais, seguindo as diretrizes de engenharia de software moderno:A. Reestruturação Arquitetural (MVC)A aplicação foi segmentada em camadas de responsabilidade única:Models: Gestão exclusiva da persistência e conexão com SQLite.Controllers: Implementação da lógica de negócio e validações.Routes: Definição de endpoints via Flask Blueprints.App Factory: Centralização da inicialização no src/app.py.B. Fortalecimento da SegurançaParametrização de Queries: Substituição de f-strings pelo uso de placeholders (?) no SQLite, neutralizando ataques de injeção.Environment Variables: Migração de dados sensíveis para o arquivo .env, gerenciado pela biblioteca python-dotenv.C. Otimização de PerformanceImplementação de JOINs no SQL para resolver o problema N+1, reduzindo o número de chamadas ao banco de dados em operações de consulta de pedidos e itens.4. Evidências de Sucesso (Validação)Após a refatoração, o sistema foi submetido a testes de integração via terminal.Teste de Conectividade e Integridade:Bashcurl http://127.0.0.1:5000/produtos/1
Resultado:JSON> {
>   "estoque": 10,
>   "id": 1,
>   "nome": "Notebook ThinkPad",
>   "preco": 4500.0
> }
> ```
> *O retorno confirma que a camada de Controller validou a entrada, o Model executou a query parametrizada e a Rota entregou o JSON com sucesso.*

---

## 5. Conclusão
A aplicação agora segue os padrões de mercado, estando pronta para escalabilidade e manutenção facilitada. A remoção das vulnerabilidades críticas eleva o nível de maturidade do software de **Legado/Inseguro** para **Produção/Profissional**.

---

### 💡 Dica de Mestre:
Tiago, você pode copiar esse conteúdo para um arquivo chamado `FINAL_REPORT.md` na raiz do seu projeto. Se precisar de uma versão em PDF, o próprio VS Code (ou o IDX) tem extensões que convertem Markdown para PDF com um clique.

**Missão cumprida neste projeto!** Como você se sente com essa estrutura? Quer que