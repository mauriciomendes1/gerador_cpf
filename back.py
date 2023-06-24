from random import randint

def validar_cpf(cpf):
    nove_digitos = []
    primeiro_digito = 0
    verificador1 = cpf[9:10]
    verificador2 = cpf[10:11]
    seq = 11
    soma = 10

    while seq > 2:
        nove_digitos.append(int(cpf[-seq]))
        seq -= 1

    for i in nove_digitos:
        primeiro_digito += i * soma
        soma -= 1
    resto = primeiro_digito % 11

    if resto == 0 or resto == 1:
        digito1 = 0
    else:
        digito1 = 11 - resto


    segundo_digito = 0
    soma = 10
    nove_digitos += str(digito1)
    for i in nove_digitos[1:]:
        segundo_digito += int(i) * soma
        soma -= 1

    resto2 = segundo_digito % 11

    if resto2 == 0 or resto2 == 1:
        digito2 = 0
    else:
        digito2 = 11 - resto2

    if digito1 == int(verificador1) and digito2 == int(verificador2):
        return True
    else:
        return False

def gerar_cpf():
    CPF = ''
    cpf_primeiroDigito = ''
    cpf_gerado = ''
    soma = 10
    total = 0
    
    digito1 = ''

    for i in range(9):
        i = randint(0, 9)
        CPF += str(i)
    
    for i in CPF:
        total += int(i) * soma
        soma -= 1
    
    resto = total % 11

    if resto == 0 or resto == 1:
        digito1 = 0
        
    else:
        digito1 = 11 - resto

    cpf_primeiroDigito = str(CPF) + str(digito1)


    total2 = 0
    soma = 10
    digito2 = 0
    for i in cpf_primeiroDigito[1:]:
        total2 += int(i) * soma
        soma -= 1

    resto2 = total2 % 11

    if resto2 == 0 or resto2 == 1:
        digito2 = 0
    else:
        digito2 = 11 - resto2
    
    cpf_gerado = cpf_primeiroDigito + str(digito2)

    return cpf_gerado