stack = []

def calculadora(operacao, numero1, numero2):
    if operacao == '+':
        return numero1 + numero2
    if operacao == '-':
        return numero1 - numero2
    if operacao == '*':
        return numero1 * numero2
    if operacao == '/':
        return numero1 / numero2

with open('Calc1.stk', 'r') as exemplo_professor:  #puxa o arquivo, que no nosso caso é o exmeplo dado na task do clasroom
    
    for linha in exemplo_professor:
        #para cada linha do Calc1.stk:
      linha = linha.rstrip()   #remove todos os caracteres finais de uma string(espaço))

      if linha.isnumeric():   #verifica se todos os caracteres são numéricos ou é algum operador/caracter
        stack.append(linha)

    #se a linha tiver um operador e não um número:
      else:
        operador2 = stack.pop()
        operador1 = stack.pop()
        resposta = eval(f"{operador1} {linha} {operador2}")
        stack.append(resposta)

final = stack.pop()

x = round(final)

print(x)
