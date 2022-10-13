<meta charset="UTF-8">
<script>
let prompt = require('prompt-sync')();

let num1 = parseFloat(prompt("Informe o primeiro número: "))
let num2 = parseFloat(prompt("Informe o segundo número: "))

console.log("Escolha a operação:\n")

console.log("Digite + para Adição.")
console.log("Digite - para Subtração.")
console.log("Digite * para Multiplicação.")
console.log("Digite / para Divisão.")

let op = prompt()

switch (op) {
  case '+':
    console.log(num1+num2)
    break
  case '-':
    console.log(num1-num2)
    break
  case '*':
    console.log(num1*num2)
    break
  case '/':
    if (num2 == 0) {
      console.log("Impossível dividir por zero.")
      break }
    else if((num1%num2)!=0){
      	console.log("Resultado:",parseInt(num1/num2), "Resto:", num1%num2) }
    else
        console.log(num1/num2)
  }
</script>