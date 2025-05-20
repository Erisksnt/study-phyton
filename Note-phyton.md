
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

# 📘 Programacao Orientada a Objetos (POO)

A Programacao Orientada a Objetos é um paradigma de programação que se baseia no uso de **classes** e **objetos**. Com ela, conseguimos organizar o código de forma mais modular e reutilizável.

---

## 🔹 Conceitos Iniciais

### ✅ Atributos

Atributos são **características** ou **propriedades** de uma classe. Exemplo:

```python
class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
```

---

## 💠 Método Construtor (`__init__`)

O método construtor é usado para **inicializar os atributos** do objeto assim que ele é criado.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

---

## 🧹 Método Destrutor (`__del__`)

Executado automaticamente quando o objeto é destruído. Pode ser usado para liberar recursos.

```python
class Pessoa:
    def __del__(self):
        print("Objeto destruído")
```

---

## 🧬 Herança

Permite que uma classe **filha** herde atributos e métodos de uma **classe pai**.

```python
class Animal:
    def falar(self):
        print("Som genérico")

class Cachorro(Animal):
    pass

dog = Cachorro()
dog.falar()  # Saída: Som genérico
```

---

## ✅ Benefícios da Herança

- Representa relações do **mundo real**;
- **Reutilização de código** (evita duplicacoes);
- Permite **extensão de funcionalidades** sem modificar a classe original;
- **Transitividade**: se B herda de A, e C herda de B, então C também herda de A.

```python
class A: pass
class B(A): pass
class C(B): pass
```

---

## 🔀 Herança Múltipla

Quando uma classe **herda de duas ou mais** classes ao mesmo tempo.

```python
class Mamifero:
    def andar(self):
        print("Andando")

class Aquatico:
    def nadar(self):
        print("Nadando")

class Onitorrinco(Mamifero, Aquatico):
    pass

bicho = Onitorrinco()
bicho.andar()
bicho.nadar()
```

---

## 🔑 `**kwargs`

`**kwargs` permite passar um número variável de argumentos nomeados (chave=valor) para uma função.

```python
def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_info(nome="Erick", idade=23)
```

---

## 📚 `__mro__` (Method Resolution Order)

Mostra a ordem de busca dos métodos na hierarquia de herança. Útil para entender como Python resolve métodos em herança múltipla.

```python
class A: pass
class B(A): pass
class C(B): pass

print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

---

📌 **Resumo:**\
POO é fundamental para a construção de sistemas organizados e reutilizáveis. Os conceitos de atributos, métodos, herança, e funcionalidades como `**kwargs` e `__mro__` tornam o código mais flexível e poderoso.