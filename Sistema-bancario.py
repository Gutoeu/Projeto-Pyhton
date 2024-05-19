limite_saques = 3
limite_max = 500
extrato = ""
saldo_atual = 0
cont_saques = 0

while True:
    menu = int(input(f""" 
=====MENU=====
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
==============      
Digite:"""))
    if menu == 1:

        deposito = float(input("\n*Digite o valor que quer depositar:"))
        if deposito > 0:
            saldo_atual += deposito
            extrato += f"""Depósito: R${deposito:.2f}\n"""
        else:
        
            print("VALOR INVÁLIDO")
    elif menu == 2:

        saque = float(input("\n*Digite o valor que deseja sacar:"))

        excedeu_saques = cont_saques >= limite_saques
        excedeu_total = saque > limite_max
        excedeu_conta = saque > saldo_atual
        valor_invalido = saque < 0

        if excedeu_saques:
            print("\nVocê excedeu o limite de saques ")
        elif excedeu_total:
            print("\n*Você excedeu o limite possivel para sacar")
        elif excedeu_conta:
            print("\n*Você excedeu o limite total da sua conta")
        elif valor_invalido:
            print("\n*Valor inválido")
        else:
            saldo_atual -= saque
            cont_saques += 1
            extrato += f"""Saque: R${saque:.2f}\n"""
        
    elif menu == 3:
        print(f"""
=========EXTRATO=========
{extrato}
        
Saldo atual: R${saldo_atual:.2f}
=========================\n""")
  
    elif menu == 4:
        print("\n*Obrigado por utilizar o sistema!!")
        break
    else:
        print("\n*Valor inválido, tente novamente")

        