#Aula 20-03-25
#Tema : Construtores de classes! O __init__ vai servir como interpretador para chamar os parâmetros atribuídos na classe- Exemplo, segue abaixo a criação da classe Pessoa


'''class Pessoa:
    def __init__(self, nome, cor= "Desconhecida"): #o init chama os parâmetros nome e cor para identificar as características da classe.
        self.nome = nome #Parâmetro nome para definir a pessoa
        self.cor = cor  #Parâmetro com valor de string embutido não sendo obrigatório o preenchimento do mesmo.

    def mostrar_info(self):
        print(f"Pessoa: {self.nome}, Cor: {self.cor}")

#Criando objetos da classe Animal
pessoa1= Pessoa("Ana") #Chamando a função Pessoa e atribuindo novo valor à ela.
pessoa2= Pessoa("Ana", "Branca") #Atribuindo cor de pele

pessoa1.mostrar_info()
pessoa2.mostrar_info()'''

#A seguir como convertemos blocos de código em tuplas ou dicionários afim de trazer praticidade para o código

'''class Produto:
    def __init__(self, nome, *args, **kwargs): #Chamando os conversores para o meu método 
        self.nome = nome #Crindo atributos para o método.
        self.caracteristicas = args #Atribuindo tupla
        self.detalhes = kwargs #Atribuindo dicionário

#Tupla = * , e, Dicionário = **
    def mostrar_info(self):   #Para chamar o método anterior
        print(f"Produto: {self.nome}")
        print("Características:", self.caracteristicas)
        print("Detalhes:", self.detalhes)

#Criando um objeto da classe Produto
produto1 = Produto("Notebook", "16GB RAM", "512GB SSD", marca="Dell", preco=5000) #Variável para chamar a classe 

produto1.mostrar_info() #Para exibir a variável'''


#Existem vários construtores que podem ser vistos em documentação
'''class ClassNew:
    def __new__(cls, *args, **kwargs ): #O new entra para a criação
        print("Criando uma nova instância")
        return super().__new__(cls)

    def __init__(self, valor): #O init inicia a classe que foi começada pelo método anterior.
        print("Inicializando a instância")
        self.valor = valor


#Criando um objeto da classe MinhaClasse
obj = ClassNew(666)
print(obj.valor)

#Classe del que serve para "destruir" a classe depois que ela é utiloizada no código afim de poupar espaço na memória que está a ser utilizada.

class ClassDel:
    def __init__(self, nome):
        self.nome = nome
        print(f"{self.nome} foi criado")

    def __del__(self):
        print(f"{self.nome} está sendo destruído.")

    #Criando um objeto da classe
    obj = ClassDel("Objeto1")

    #Deletando o objeto explicitamente
    del obj'''


#Método call = para chamar sua classe (objeto) como se fosse uma função
'''class CallableClass:
    def __init__(self, nome):
        self.nome = nome
    def __call__(self, *args, **kwds):
        print(f"{self.nome} foi chamado com argumento")

#Criando um objeto da classe CallableClass
obj = CallableClass("CallableObject")

#Chamando o objeto como uma função 
obj(1, 2, 3 chave="valor")'''
