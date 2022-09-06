#Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento.
#Depois, desenvolva três ou mais objetos para testar o código.

class Funcionario:
  def __init__(self, nome, cargo, salario):
      self.nome = nome
      self.cargo = cargo
      self.salario = salario

  def dados(self):
    print(f"Funcionário de nome {self.nome}, cargo: {self.cargo}")

  def promocao(self, salario = 1500):
    self.salario += salario
    print(f"Com a promoção o salário de {self.nome} passou de R$1500 para R${self.salario}.")

funcionario1 = Funcionario("João", "supervisor", 3500)
funcionario2 = Funcionario("Maria", "Gerente", 5500)
funcionario3 = Funcionario("Pedro", "Técnico_Pleno", 2500)


funcionario1.dados()
funcionario3.promocao()
print(f"O maior aumento de salário foi de {funcionario2.nome}, aumento de R${funcionario2.salario}")
