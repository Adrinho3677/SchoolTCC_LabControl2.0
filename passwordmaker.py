import random
import string

def gerar_senha(comprimento):
    # Definir os conjuntos de caracteres possíveis
    caracteres_maiusculos = string.ascii_uppercase
    caracteres_minusculos = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?/`~"
    
    # Garantir que a senha tenha exatamente 2 caracteres especiais
    senha = [
        random.choice(caracteres_especiais),
        random.choice(caracteres_especiais)
    ]
    
    # Preencher a senha com caracteres aleatórios, exceto especiais
    senha += random.choices(caracteres_maiusculos + caracteres_minusculos + numeros, k=comprimento - 2)
    
    # Embaralhar a senha para garantir que os caracteres especiais não fiquem em posições fixas
    random.shuffle(senha)
    
    # Converter a lista de caracteres para uma string
    return ''.join(senha)

# Exemplo de uso:

comprimento=14

senha_gerada = gerar_senha(comprimento)
print(f'Senha gerada: {senha_gerada}')

senha_simplificada = '123456789'

lista_senhas = {
    'senha_simplificada':senha_simplificada
    }

print(lista_senhas)
