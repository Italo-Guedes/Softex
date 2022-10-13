/*Crie dois códigos de sistema de notas para uma escola. O primeiro código deve ser um programa que informa se o aluno reprovou, ou não, com base nas três notas que ele adicionou ao programa. Utilize, no mínimo, um operador de atribuição e um operador ternário. 
O segundo código é um programa que o aluno deve escrever duas notas e o retorno informa a nota mínima que ele deve tirar na próxima prova para poder passar com nota sete.*/

/*1º Programa*/
let nota1 = parseFloat(prompt("Informe a sua primeira nota: "))
let nota2 = parseFloat(prompt("Informe a sua segunda nota: "))
let nota3 = parseFloat(prompt("Informe a sua terceira nota: "))

let media = (nota1 + nota2 + nota3)/3
let resposta = media >= 7 ? "APROVADO": "REPROVADO"
console.log("\nResultado:", resposta)

/*2º Programa*/

let prova1 = parseFloat(prompt("\nInforme a nota da primeira prova: "))
let prova2 = parseFloat(prompt("Informe a nota da segunda prova: "))
let media_prova = 21-(prova1+prova2)

console.log("Você precisa tirar ", media_prova, " na próxima prova para passar. ")

