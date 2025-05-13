
# 📘 Anotações de Python

Este documento contém um resumo dos principais comandos e funcionalidades do Python que você pode usar como referência rápida no seu dia a dia.

---

## 🔍 Comandos Básicos

```python
dir()      # Mostra os atributos e métodos de um objeto
help()     # Mostra a ajuda interativa no terminal
print()    # Exibe mensagens/valores na tela
input()    # Solicita entrada do usuário (retorna string)
```

---

## 📌 Tipos de Dados

```python
int     # Números inteiros (ex: 10)
float   # Números decimais (ex: 3.14)
bool    # Booleano (True ou False)
str     # Texto (ex: "Olá mundo")
```

---

## 🔁 Estruturas de Controle

### Condicionais

```python
if condicao:
    # código

elif outra_condicao:
    # código

else:
    # código
```

### Laços de Repetição

```python
while condicao:
    # repete enquanto a condição for verdadeira

for item in lista:
    # percorre a lista
```

### Operadores

```python
# Operadores Lógicos
and, or, not

# Operadores de Comparação
==, !=, <, >, <=, >=

# Operadores matematicos
+=, -=, /=, //, *=, %=, **,

# Outros operadores
in, not in, is, is not
```

---

## 🧮 Funções

```python
def nome_da_funcao():
    print("Olá mundo!")
```

---

## 📚 Listas

```python
frutas = ["maçã", "banana", "laranja"]
```

### Métodos de Lista

```python
frutas.append("uva")               # Adiciona item ao final
frutas.clear()                     # Limpa todos os itens
frutas.copy()                      # Retorna cópia da lista
frutas.count("maçã")               # Conta quantas vezes aparece
frutas.extend(["pera"])            # Junta outra lista
frutas.index("banana")             # Retorna índice
frutas.pop()                       # Remove o último item
frutas.remove("laranja")           # Remove o item especificado
frutas.reverse()                   # Inverte a lista
frutas.sort()                      # Ordena em ordem crescente
frutas.sort(key=lambda x: len(x))  # Ordena por tamanho dos itens
```

---

## 🔢 Matrizes (Listas dentro de Listas)

```python
matriz = [
    [1, 2],
    [3, 4]
]
```

---

## 📐 Tuplas

```python
cores = ("vermelho", "azul", "verde",)  # Estrutura imutável (utilizasse virgula ao final como boa pratica)
```
## 🔢 Matrizes (Listas dentro de Tuplas)

```python
matriz = [
    (1, 2),
    (3, 4),
]
```

---

## 🧰 Funções Úteis

```python
len(objeto)   # Retorna o tamanho do objeto
type(objeto)  # Mostra o tipo do objeto
```

---

> ⚙️ Atualizado por Erick — Aprendizado contínuo em Python 💻
