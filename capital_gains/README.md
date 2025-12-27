# 📘 Capital Gains Calculator

## 📌 Visão Geral

Este projeto implementa uma calculadora de imposto sobre ganho de capital conforme as regras do desafio técnico.

O código foi desenvolvida com foco em:

- **Simplicidade** → projeto pequeno, direto e fácil de entender
- **Elegância** → separação clara das responsabilidades + domínio limpo
- **Operacionalidade** → cobre casos de borda, perdas acumuladas, isenção e arredondamento
- **Qualidade** → testes unitários e testes de integração
- **Robustez** → validações e exceções específicas para erros de domínio
- **Extensibilidade** → fácil adicionar novas regras e operações
- **Boas práticas** → estrutura modular e extensível

---

# 🧱 Arquitetura & Decisões Técnicas

A arquitetura combina princípios leves de DDD e Hexagonal Architecture. 
- Domínio fiscal isolado e independente de entrada/saída.
- As regras de negócio são organizadas em serviços de domínio e modelos que refletem diretamente a linguagem do problema.
- O CLI e a formatação do output atuam como adapters, seguindo o padrão Ports & Adapters.

Essa separação garante baixo acoplamento, alta coesão e facilita testes unitários.
O resultado é uma solução modular, extensível e alinhada a boas práticas de engenharia modernas.


### Estrutura do Projeto
```
src/
├─ domain/
│   ├─ exceptions/
│   │   └─ exceptions.py          → PositionState (estado da carteira)
│   ├─ models/
│   │   ├─ money.py          → classe Money (Decimal + arredondamento)
│   │   ├─ operation.py      → operação (buy/sell)
│   │   └─ result.py         → resultado com imposto
│   ├─ rules/
│   │   ├─ base.py
│   │   ├─ buy_rule.py
│   │   └─ sell_rule.py
│   ├─ position/
│   │   └─ state.py          → PositionState (estado da carteira)
│   ├─ services/
│   │   └─ tax_calculator.py      → cálculo de imposto e dedução de perdas
│   │   └─ calculator.py      → CapitalGainsCalculator (validação + orquestração)
├─ infra/
│   ├─ cli.py                → executável via stdin/stdout
│   └─ jsonio.py             → parser + MoneyEncoder
└─ app.py                    → main entry point

```
## 💡 Principais decisões arquiteturais

### ✔ 1. Classe `Money`
- Envolve `Decimal` padronizando para **2 casas decimais**
- Todas operações retornam outro `Money` já arredondado
- Garante precisão em todos os cálculos financeiros
- Evita erros de `float`

---

### ✔ 2. Regras separadas (`BuyRule` e `SellRule`)
- Cada operação tem uma regra isolada
- Fácil adicionar novas operações no futuro
- Evita “ifs” espalhados pelo projeto

---

### ✔ 3. `PositionState` como estado único
- Mantém quantidade total, custo total e perda acumulada
- Facilita o cálculo do PMP
- Permite que regras sejam puras e independentes

---

### ✔ 4. Integração via JSON + stdin/stdout
- Atende ao formato exigido no desafio. 
- Permite que o domínio opere sem depender do 
- Isso também torna o projeto *unix-friendly*, podendo ser encadeado em pipelines.

---

### ✔ 5. Testes
- **Testes unitários** validam domínio e regras
- **Testes de integração** validam o comportamento real da CLI
- Casos fornecidos no desafio foram mapeados em `/tests/integration/cases`


###  6. TaxCalculator isolado e extensível
-	Aplica perda acumulada, isenção e imposto
-	Lógica tributária 100% separada das regras
-	Permite  implementar novos modelos

### 7. Camada de validação

- Validações feitas antes de aplicar regras:
-	quantidade deve ser positiva
-	preço unitário deve ser positivo
-	operação desconhecida lança InvalidOperationError
---

# 🧰 Bibliotecas e justificativas

### ✔ `Decimal` (nativo)
- Necessário para cálculos monetários
- Evita problemas de precisão de `float`

### ✔ `unittest` (nativo)
- Framework simples e eficiente
- Sem dependências externas
- Atende perfeitamente ao tamanho do projeto

### ❌ Nenhum framework externo foi utilizado

---

# ▶️ Como executar o projeto

- Este projeto foi desenvolvido e validado utilizando Python 3.9.5.
- Para garantir compatibilidade total, recomenda-se utilizar pyenv.

## 🐍 Configurar o Python 3.9.5 (usando pyenv)
```
pyenv install 3.9.5
pyenv local 3.9.5
```
---

## ▶️ Executar a aplicação:

A aplicação lê entrada JSON via stdin e escreve o resultado no stdout.

### Forma direta:
```
python app.py
```
Depois digite ou cole o texto no terminal:

```
[{"operation":"buy","unit-cost":10,"quantity":100}]
```
### Usando pipe:
```
echo '[{"operation":"sell","unit-cost":20,"quantity":10}]' | python src/infra/cli.py
```

## 🧪  Como executar os testes:

### Teste unitário específico:
```
 python -m unittest -v tests/test_calculator.py 
```
### Testes de integração:
```
python -m unittest discover -s tests/integration
```
### TODOS os testes:
```
python -m unittest -v
```
