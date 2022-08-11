#Desenvolva um código que simule uma eleição com três candidatos.
#- candidato_X => 889
#- candidato_Y => 847
#- candidato_Z => 515
#- branco => 0

#O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente.

#Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a quantidade de votos de cada candidato, os brancos e nulos 





print("Eleições\n\n")

candidato_x = 0
candidato_y = 0
candidato_z = 0
brancos     = 0
nulos       = 0


try:
    while True:
        print("Escolha seu candidato:\n\nCandito X => 889 \nCandidato Y => 847 \nCandidato Z => 515 \nBranco => 0")
        voto = input("\nDigite seu voto: ")

        if voto.isalpha():
          print("Você não digitou um número válido! Por favor, tente novamente.")
          pass
        else:
          if voto == "889":
            candidato_x += 1
          if voto == "847":
            candidato_y +=1
          if voto == "515":
            candidato_z += 1
          else:
            nulos += 1

          fim = input("Obrigado, por votar! Digite '1' para votar novamente ou digite qualquer tecla para finalizar.")           
          if fim != "1":
            break            
          else:
             print("\nOk, vote novamente. \n")

except:
  pass


candidatos = ["candidato_X", "canditato_Y", "candidato_Z", "Brancos", "Nulos"]
apuracao = [candidato_x, candidato_y, candidato_z, brancos, nulos]
vencedor = candidatos[apuracao.index(max(apuracao))]


print(f"\nO resultado foi: \nCandidato_x: {candidato_x} voto(s), Candidato_Y: {candidato_y} voto(s), Candidato_Z: {candidato_z} voto(s), votos brancos: {brancos}, votos nulos: {nulos}")

if candidato_x == 0 and candidato_y == 0 and candidato_z == 0:
  print("Não houve vencedor!")
else:  
  print(f"\nO vencedor da eleição é: {vencedor}")





