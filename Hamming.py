# Exercicio Adicional - OAC
# Codigo para deteccao de erro - Paridade
# Jaciane de Oliveira Cruz - 118110412
# Nayara Silva Pereira de Souza - 118110390


#### DETECÇÃO DO ERRO ####
            
# Metodo que detecta o erro (Complemento do metodo detectaErroHamming)
def detectaErro(binarioParidade, acumulo):
    if (binarioParidade == 0) and (acumulo % 2 == 0):
        return False
    if (binarioParidade == 1) and (acumulo % 2 == 1):
        return False
    return True

#### CORREÇÃO DO ERRO ####
def corrigeErro(paridadesErradas, sequencia):
    sequencia = list(map(int, sequencia))
    
    if (len(paridadesErradas) % 2 == 0):
        count = 0

        for i in paridadesErradas:
            count += int(i)

        if (count < len(sequencia)):
            if (sequencia[count] == 0):
                sequencia[count] = 1
            else:
                sequencia[count] = 0

        sequencia = list(map(str, sequencia))

        print('A sequencia de bits corrigida eh: ' + ''.join(sequencia))
    else:
        print('A correção nao foi possivel, pois o numero de paridades incorretas eh impar')
    

#### DETECÇÃO E CORREÇÃO DO ERRO ####
def detectaErroHamming(sequencia):
    
    existeErro = False
    paridadesErradas = []

    for i in range(len(sequencia)):
        potenciaNumero = pow(2,i)

        temp = []

        if (potenciaNumero < len(sequencia)):
            acumulo = 0
            inicioAcumulo = potenciaNumero + 1
            deveAcumular = True
            qntAcumulada = 1

            temp.append(potenciaNumero)

            while (inicioAcumulo < len(sequencia)):
                if (qntAcumulada == potenciaNumero):
                    deveAcumular = False

                if (qntAcumulada == 0):
                    deveAcumular = True

                if (deveAcumular == True):
                    acumulo += int(sequencia[inicioAcumulo])
                    qntAcumulada += 1
                    temp.append(inicioAcumulo)

                else:
                    qntAcumulada -= 1

                inicioAcumulo += 1
            
            if (detectaErro(int(sequencia[potenciaNumero]),acumulo)):
                existeErro = True
                paridadesErradas.append(potenciaNumero)

    if (existeErro == True):
        print('A sequencia possui erros')
        corrigeErro(paridadesErradas, sequencia)
    else:
        print('A sequencia nao possui erros')


### TESTES (Exemplos) ###
# Para a detecção de erros, o codigo deve desconsiderar a posição 0 da sequencia

# Teste 1 - Nao possui erros
sequencia1 = '00011001'
print('Teste 1 -> 00011001')
detectaErroHamming(sequencia1)

# Teste 2 - Possui erros corrigiveis
sequencia2 = '00001001'
print('\nTeste 2 -> 00001001')
detectaErroHamming(sequencia2)

# Teste 3 - Possui erros incorrigiveis
sequencia3 = '01111001111'
print('\nTeste 2 -> 01111001111')
detectaErroHamming(sequencia3)