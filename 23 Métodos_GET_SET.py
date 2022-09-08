#Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter um método acessor (get) e um método modificador (set) para cada. Defina um objeto para cada atributo e elabore um construtor para criar alguma regra.

#A atividade pode ser realizada em qualquer linguagem de programação ou apenas utilizando algoritmos.

class Pessoa:
  def __init__(self, nome, idade):
    if len(nome)>0:
      self.__nome = nome
    else:
      print("Este nome é inváido.")
    if idade>=0 and idade<=120:
      self.__idade = idade
    else:
      print("Esta idade é inválida.")

  def getNome(self):
    return self.__nome
  def setNome(self, newNome):
    if len(newNome)>0:
      self.__nome = newNome
      print(f"Nome alterado pelo método SET para '{self.__nome}'.")

  
  def getIdade(self):
    return self.__idade
  def setIdade(self, newIdade):
    if newIdade>=0 and newIdade<=120:
      self.__idade = newIdade
      print(f"Idade alterada pelo método SET para {self.__idade}anos.")
    else:
      print("Esta idade é inválida.")

primeiraPessoa = Pessoa("Maria", 35)
segundaPessoa = Pessoa("João", 33)

print("O nome de 1ª pessoa é ", primeiraPessoa.getNome())
print("A idade de 2ª pessoa é ", segundaPessoa.getIdade(), "anos.\n")

primeiraPessoa.setNome("Tadeu")
segundaPessoa.setIdade(43)
