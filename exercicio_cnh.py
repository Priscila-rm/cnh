#voce foi contratado para criar um programa para uma autoescola, que deve verifica se a pessoa e maior ou tem 18 anos. Se ela tiver 18 ou mais, ela pode ter cnh, senão não pode digitar.

#1. receber o nome da pessoa 
nome = input('digite o seu nome : ')
#2. receber a idade da pessoa 
idade = int(input('digite a sua idade : '))
#3. possui cnh?
possui_cnh = input("voce possui a carteira de habilitação ? \n (1-sim / 2-nao):")

#4.verificar se a pessoa >=18
if idade  >= 18:
    #5.se ele ja é maior de idade, vou verificar se ele tem ou nao cnh 
    if possui_cnh == "1" :
        print('maior de 18 anos e pode dirigir!')
    else:
        print('nao pode dirigir, porque nao possui cnh')
else:
    print('menor de idade')