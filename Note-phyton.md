
# 📘 Anotações de Python

## 🛠️ Comandos Básicos

- `dir` — Verifica a estrutura e os atributos disponíveis de um objeto.
- `help()` — Ajuda interativa dentro do próprio Python.
- `input()` — Solicita uma entrada do usuário.
- `print()` — Exibe valores na tela.

## 📌 Tipos de Dados

- `int` — Número inteiro.
- `float` — Número com casas decimais.
- `bool` — Booleano (True ou False, 1 ou 0).
- `str` — Texto (string/caractere).

## 🧠 Operadores Lógicos

- `and` — E lógico.
- `or` — Ou lógico.
- `not` — Negação lógica.
- `in`, `is`, `is not` — Operadores de comparação e identidade.

## 🔁 Estruturas de Repetição

- `while` — Executa enquanto a condição for verdadeira.
- `for` — Loop com controle de condição ou intervalo.

## ✅ Estruturas Condicionais

- `if` — Se a condição for verdadeira, executa o bloco.
- `elif` — Caso contrário, se essa outra condição for verdadeira.
- `else` — Executado se nenhuma condição for satisfeita.

## 🧩 Funções

- `def` — Define uma função.
  
```python
def minha_funcao():
    print("Olá!")
```

## 📚 Listas

- `list` — Estrutura para armazenar múltiplos valores mutáveis.

```python
minha_lista = [1, 2, 3]
```

### Métodos de Lista

- `.append(x)` — Adiciona um item ao final.
- `.clear()` — Limpa todos os itens da lista.
- `.copy()` — Cria uma cópia da lista.
- `.count(x)` — Conta quantas vezes um item aparece.
- `.extend(lista2)` — Junta duas listas.
- `.index(x)` — Retorna o índice do item.
- `.pop()` — Remove e retorna o último item.
- `.remove(x)` — Remove um item específico.
- `.reverse()` — Inverte a ordem dos elementos.
- `.sort()` — Ordena em ordem crescente.
- `.sort(key=lambda x: len(x))` — Ordena com base no comprimento dos itens.
- `len(lista)` — Retorna o número de elementos.

## 📐 Tuplas

- `tuple` — Estrutura imutável.

```python
tupla = ("a", "b", "c")
```

## 🎯 Sets (Conjuntos)

- `set` — Estrutura de dados sem elementos duplicados.

```python
meu_set = {"a", "b", "c"}
```

## ⏳ Datas e Horas

> É necessário importar a biblioteca:

```python
from datetime import date, datetime, time, timedelta
```

- `date` — Representa uma data.
- `time` — Representa um horário.
- `datetime` — Representa data e hora.
- `datetime.today()` — Retorna a data e hora atual.
- `datetime.timedelta()` — Faz operações com datas.
- `strftime()` — Converte objeto `datetime` em string com formato.
- `strptime()` — Converte string formatada em objeto `datetime`.
