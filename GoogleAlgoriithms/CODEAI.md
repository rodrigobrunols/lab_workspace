# GoogleAlgoriithms - Repositório de Estudos de Algoritmos

## Visão Geral do Projeto

Este é um repositório pessoal de estudos focado em algoritmos, estruturas de dados e conceitos de programação. O projetoserve como um laboratório para implementação de soluções para problemas técnicos, exercícios de algoritmia e desenvolvimento de sistemas OO.

### Principais Tecnologias
- **Python 3.x** - Linguagem principal
- **Unittest** - Framework de testes
- **Estruturas de dados nativas** - collections, heapq, bisect, etc.
- **Enum** - Para definições de tipos
- **Threading** - Para sistemas concorrentes
- **Datetime** - Para sistemas de agendamento

### Arquitetura do Projeto

O código está organizado em módulos temáticos:

#### 🧮 Algoritmos e Estruturas de Dados (Ada)
- **Localização**: `ada/`
- **Conteúdo**: Implementações de algoritmos clássicos do LeetCode
- **Arquivos principais**:
  - `arrays.py` - Problemas com arrays (LIS, sliding window)
  - `graphs/` - Algoritmos de grafos:
    - Dijkstra para menor caminho
    - Algoritmo de Prim para MST
    - Detecção de ciclos
    - Busca de pontes
  - `minBridgesToConnectIslands.py` - Conectar ilhas
  - `LengthOfLis.py` - Subsequência crescente mais longa
  - `1136 - Parallel Courses.py` - Ordenação topológica

#### 🏗️ Princípios de Programação OO
- **Localização**: `ooprincipals/`
- **Conteúdo**: Implementações de sistemas complexos seguindo princípios OO
- **Exemplos**:
  - `TicTacToe.py` - Jogo da velha completo
  - `ElevatorSystem.py` - Sistema de elevadores
  - `parking_lot.py` - Sistema de estacionamento
  - `TicTacToe_LowLevelDesign.py` - Design detalhado

#### 📊 Estruturas de Dados Customizadas
- **Localização**: `datastructures/`
- **Conteúdo**: Implementações manuais de estruturas fundamentais
- **Arquivos**:
  - `Tree.py` - Árvores binárias
  - `LinkedList.py` - Listas encadeadas
  - `DoublyLinkedList.py` - Listas duplamente encadeadas
  - `Array.py` - Implementações de arrays dinâmicos

#### 🔄 Algoritmos de Grafos
- **Localização**: `graph_traversal/`
- **Conteúdo**: BFS, DFS e algoritmos relacionados
- **Funcionalidades**:
  - Contar componentes conectados
  - Encontrar todos os caminhos
  - Menor caminho em grafos

#### ⏰ Sistemas de Agendamento
- **Localização**: `meeting_scheduler/`
- **Conteúdo**: Sistema completo de agendamento de reuniões
- **Componentes**:
  - Participants (participantes)
  - Meeting (reuniões)
  - MeetingRoom (salas)
  - MeetingScheduler (agendador)

#### 🎯 Sandbox de Experimentos
- **Localização**: `playground/`
- **Conteúdo**: Exercícios, protótipos e experimentos
- **Sistemas implementados**:
  - `VisitorTracker.py` - Rastreamento de visitantes
  - `LockerSystem.py` - Sistema de lockers com enum
  - `MessageStream.py` - Stream de mensagens
  - `TimeMap.py` - Mapeamento temporal
  - `WordProcessor.py` - Processamento de texto
  - `loadbalancer/` - Múltiplos algoritmos de load balancing

#### 🧪 Testes (TDD)
- **Localização**: `tdd/`
- **Conteúdo**: Testes unitários seguindo TDD
- **Exemplo**: `TestStringUtils.py` - Testes para MyStringUtils

#### 🏢 Aplicações Corporativas
- **Localização**: `quinto_andar/` e `amazon_locker/`
- **Conteúdo**: Implementações inspiradas em problemas reais
- **Sistemas**:
  - Quinto Andar: Inspeções, agendamento, otimização de rotas
  - Amazon Locker: Sistema de gestão de lockers

## Convenções de Desenvolvimento

### Estrutura de Classes
```python
class MinhaClasse:
    def __init__(self, parametros):
        pass
    
    def metodo_principal(self):
        pass
```

### Testes
- Uso de `unittest` para testes unitários
- Estrutura: `test_[nome_do_modulo].py` para cada módulo
- Nomenclatura: `Test[NomeDaClasse]` para classes de teste

### Documentação
- Comentários técnicos em inglês na implementação
- Docstrings ausentes - código autoexplicativo
- Prints para debug em código de experiments

### Importações
- Importações sempre no topo do arquivo
- Bibliotecas Python nativas priorizadas
- Uso de `from typing import` para type hints

## Execução e Testes

### Executar arquivos individuais
```bash
python3 <caminho_do_arquivo>
```

### Executar testes
```bash
python3 -m unittest discover -s . -p "Test*.py"
```

### Exemplos de execução
```bash
# Executar sistema de elevadores
python3 ooprincipals/ElevatorSystem.py

# Executar jogo da velha
python3 ooprincipals/TicTacToe.py

# Executar algoritmo de Dijkstra
python3 ada/graphs/Dijkstra.py

# Executar playground principal
python3 playground/Main.py
```

### Executar TDD
```bash
# Executar todos os testes
python3 -m unittest tdd/TestStringUtils.py

# Executar testes específicos
python3 tdd/TestStringUtils.py
```

## Casos de Uso Comuns

### 🔍 Estudar algoritmos
1. Navegar para `ada/` para ver implementações
2. Executar arquivos para observar comportamento
3. Modificar parâmetros para experimentar

### 🧪 Experimentar conceitos
1. Usar `playground/` para protótipos rápidos
2. Adicionar novos experimentos conforme necessário
3. Testar ideias antes de consolidar

### 🏗️ Desenvolver sistemas
1. Seguir padrão de `ooprincipals/` para sistemas OO
2. Usar `meeting_scheduler/` como referência para sistemas complexos
3. Implementar testes em `tdd/`

### 📝 Análise de dados
1. Usar `text_analyzer/` para processamento de texto
2. Implementar novas análises seguindo o padrão
3. Adicionar testes unitários

## Pontos de Atenção

### 🔧 Desenvolvimento Futuro
- **Expansão de testes**: Adicionar cobertura de testes mais abrangente
- **Documentação**: Implementar docstrings para classes e métodos principais
- **Padronização**: Uniformizar convenções de nomenclatura
- **Performance**: Otimizar algoritmos onde necessário

### 📋 Manutenção
- **Organização**: Manter a estrutura modular
- **Qualidade**: Seguir padrões estabelecidos
- **Compatibilidade**: Manter compatibilidade com Python 3.8+

### 🚀 Melhorias Sugeridas
- Interface CLI para alguns sistemas
- GUI para jogos e sistemas visuais
- API para sistemas corporativos
- Integração com frameworks de logging

---

**Importante**: Este é um **repositório de estudos pessoais** onde o foco está na **aprendizado prático** de algoritmos e conceitos de programação. O código serve como referência para entender implementações e pode ser.expandido conforme novos conceitos sejam estudados.