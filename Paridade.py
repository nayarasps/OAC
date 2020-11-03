# Exercicio Adicional - OAC
# Codigo para deteccao de erro - Paridade
# Jaciane de Oliveira Cruz - 118110412
# Nayara Silva Pereira de Souza - 118110390

# Metodo que identifica o bit de paridade
def paridade(sequencia):
    
    count = 0
    
    for i in sequencia:
        if i == "1":
            count += 1

    if count % 2 == 0:
        return '0'
    
    return '1'

# Metodo que checa se a mensagem transmitida e recebida possuem o mesmo bit de paridade.
# Se possuem bits iguais, existe erro
# Se possuem bits diferentes, nao existe erro
def checaErro(original, enviado):
    
    if (paridade(original) == paridade(enviado)):
        print('Erro de Paridade encontrado')
    else:
        print('Erro de Paridade nao encontrado')

### TESTES (Exemplos) ###

# Teste 1
print('Teste 1 -> 0100101')
transmissor1 = '0100101'
receptor1correto = '01001011'
receptor1errado = '01001010'

checaErro(transmissor1, receptor1correto) # Retorna mensagem sem erro
checaErro(transmissor1, receptor1errado) # Retorna mensagem com erro

# Teste 2
print('\nTeste 2 -> 001111')
transmissor2 = '001111'
receptor2correto = '0011110'
receptor2errado = '0011111'

checaErro(transmissor2, receptor2correto) # Retorna mensagem sem erro
checaErro(transmissor2, receptor2errado) # Retorna mensagem com erro

# Teste 3
# Neste exemplo temos um erro de verificacao usando paridade.
print('\nTeste 3 -> 00011')
transmissor3 = '00011'
receptor3correto = '000110'
receptor3errado = '000111'

checaErro(transmissor3, receptor3correto) # Retorna mensagem com erro
checaErro(transmissor3, receptor3errado) # Retorna mensagem sem erro





