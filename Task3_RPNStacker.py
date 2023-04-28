import re # importa o módulo de expressões regulares

stack = [] # inicializa a pilha vazia

# duas classes para representar os diferentes tipos de tokens que podem ser reconhecidos pelo scanner
class TokenType:
    NUM = "NUM"
    OP = "OP"

# classe para expressões regulares
class Regex:
    NUM = r"\d+" # reconhece um ou mais dígitos
    OP = r"[\+\-\*/]" # reconhece um dos operadores "+", "-", "*" ou "/"

class Token:
    def __init__(self, type, lexeme):
        self.type = type
        self.lexeme = lexeme

def calculadora(operacao, numero1, numero2):
    if operacao == '+':
        return numero1 + numero2
    if operacao == '-':
        return numero1 - numero2
    if operacao == '*':
        return numero1 * numero2
    if operacao == '/':
        return numero1 / numero2

# função que lê uma linha de entrada e retorna uma lista de tokens
def scan_expression(expression):
    # a função vai ler cada linha do nosso arquivo 'Calc1.stk' e obter a lista dos tokens correspondentes

    tokens = []

    # encontra todos os tokens da expressão usando expressões regulares
    for match in re.finditer(f"{Regex.NUM}|{Regex.OP}", expression):
        lexeme = match.group(0) # pega o valor correspondente ao match encontrado

        # verifica se é um número
        if re.match(Regex.NUM, lexeme):
            tokens.append(Token(TokenType.NUM, lexeme))
        # verifica se é um operador
        elif re.match(Regex.OP, lexeme):
            tokens.append(Token(TokenType.OP, lexeme))
        else:
            # caractere inválido
            return f"Error: Unexpected character: {lexeme}"

    return tokens

with open('Calc1.stk', 'r') as exemplo_professor:  # puxa o arquivo, que no nosso caso é o exmeplo dado na task do clasroom

    for linha in exemplo_professor:
        # para cada linha do Calc1.stk:
        
        linha = linha.rstrip()   # remove todos os caracteres finais de uma string (espaço)
        tokens = scan_expression(linha)

        if isinstance(tokens, str):
            # ocorreu um erro no scanning
            print(tokens)
            break

        for token in tokens:
            if token.type == TokenType.NUM:
                stack.append(int(token.lexeme))

            elif token.type == TokenType.OP:
                operador2 = stack.pop()
                operador1 = stack.pop()
                resposta = calculadora(token.lexeme, operador1, operador2)
                stack.append(resposta)

final = stack.pop()

x = round(final)

print(x)
