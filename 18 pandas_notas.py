#Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:

#aluno: Nome do aluno;
#nota_1: Primeira nota;
#nota_2: Segunda nota;
#faltas: Número de faltas;

#O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

#O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

#Por fim, o programa deverá mostrar na tela:
#- o maior número de faltas;
#- a média geral das notas dos alunos;
#- e a maior média.



from ast import If
import pandas as pd


df = pd.read_csv("notas_alunos.csv")

media = (df["nota_1"] + df["nota_2"])/2
df["media"] = media


df.loc[(df["media"] < 7) | (df["faltas"] > 5), "situacao"] = "REPROVADO"
df.loc[(df["media"] >= 7) & (df["faltas"] <= 5), "situacao"] = "APROVADO"

df.to_csv('alunos_situacao.csv', index = False)

max_faltas = df["faltas"].max()
media_notas = df["media"].median()
maior_media = df["media"].max()

print(f"\nO maior número de faltas é: {max_faltas}")
print(f"\nA média geral das notas é: {media_notas}")
print(f"\nA maior média é: {maior_media}\n")