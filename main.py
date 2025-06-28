import os
import random

answer = '1'

print("=====================")
print("Seja bem-vindo(a)!")

while answer == '1' or answer == '2':
    print("=====================")
    print("      < Menu >")
    print("=====================")
    answer = input("Você gostaria de:\n[1] Gerar um cpf\n[2] Verificar a validade de um cpf\n[Qualquer outra Tecla] Sair\n")
    if answer == '1':
        generatedCpf = ''
        nineDigits = ''
        tenDigits = 0
        result = 0
        times = 10
        for i in range(9): # gerando os 9 digitos iniciais
            nineDigits += str(random.randint(0,9))

        for i in range(9): # calculando o primeiro digito validador
            result += int(nineDigits[i]) * times
            times -= 1
        result = (result * 10) % 11
        firstDigitValidated = result if result <= 9 else 0
        tenDigits = nineDigits + str(result)
        
        times = 11
        result = 0
        for i in range(10): # etapas para calcular o segundo dígito validador
            result += int(tenDigits[i]) * times
            times -= 1
        result = (result * 10) % 11
        secondDigitValidated = 0 if result > 9 else result
        generatedCpf = tenDigits + str(result)
        cpfFormated = f'{generatedCpf[:3]}.{generatedCpf[3:6]}.{generatedCpf[6:9]}-{generatedCpf[9:]}'
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'Cpf gerado: {''.join(cpfFormated)}')
        answer = input("Você gostaria de:\n[1] Voltar ao Menu [Qualquer outra Tecla] Sair\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    elif answer == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("===== Validador de cpf =====")
        cpf = input("->Digite o cpf: na seguinte formatação:\n 000.000.000-00: ")
        cpfNumbers = '' # resetando as variáveis para cada loop
        result = 0
        times = 10
        cpfList = []
        firstDigitValidated = 0
        secondDigitValidated = 0

        for digit in cpf: # pega apenas os numeros digitados
            if digit.isdigit():
                cpfNumbers += digit
                cpfList.append(digit)
            continue

        # validação do que foi digitado
        if cpf == '':
            input("Por favor, digite algo!\n\nPressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if len(cpfNumbers) != 11:
            input("Digite o cpf na formatação pedida: 000.000.000-00!\n\nPressione Enter para contiinuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        if cpfNumbers[0] * len(cpfNumbers) == cpfNumbers:
            input("Cpf inválido")
            continue

        # contas para validar o primeiro digito validador
        for i in range(9):
            result += int(cpfNumbers[i]) * times
            times -= 1
        result = (result * 10) % 11
        firstDigitValidated = result if result <= 9 else 0
        if firstDigitValidated != int(cpfList[-2]):
            print("O cpf é inválido")
            input("\nPressione Enter para continuar")
            continue
        times = 11
        result = 0
        # etapas para verificar o segundo dígito validador
        for i in range(10):
            result += int(cpfNumbers[i]) * times
            times -= 1
        result = (result * 10) % 11
        secondDigitValidated = 0 if result > 9 else result
        os.system('cls' if os.name == 'nt' else 'clear')
        if secondDigitValidated == int(cpfList[-1]):
            print("O cpf é valido")
        else:
            print("O cpf é inválido")
        input("\nPressione Enter para continuar")
    else:
        break
