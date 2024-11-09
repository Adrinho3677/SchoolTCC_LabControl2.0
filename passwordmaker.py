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



lucio = '}udy=4PmQtWTlz'
maria_jesus = 'cpF5LHQ:5KOiI%'
leandro = '_sld8ZYxP}gYMv'
glecio = 'MIq8lH63H{%kpM'
nilo = 'E+EOhB6Yl8OJ<D'
lorena_silva = 'REpw#URL4?1qj6'
maria_cristina = 'SDarF9$todcW#j'
lorena_azevedo = 'ze[fSc3@paxr4c' #Faltam informações: CPF
thiago = 'B.IvRvVyRmBj-A'

senha_simplificada = '123456789'

lista_senhas = {
    'lucio':lucio,
    'maria_jesus':maria_jesus,
    'leandro':leandro,
    'glecio':glecio,
    'nilo':nilo,
    'lorena_silva':lorena_silva,
    'maria_cristina':maria_cristina,
    'lorena_azevedo':lorena_azevedo,
    'thiago':thiago,
    'senha_simplificada':senha_simplificada
    }

print(lista_senhas)