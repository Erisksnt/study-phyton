maior_idade=18
idoso = 60
idade = int(input("Informe sua idade: "))

#if = condição se verdadeira
if idade >= idoso:
    print ("Inss ta chamado")
    
#elif = mais uma condição para verificar se é verdadeira
elif idade >= maior_idade:
    print ("adulto")

#else = após if/elif se condição for falsa
else:
    print ("menor de idade")
