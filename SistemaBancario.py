menu = """
[1] Depositar
[2] Sacar
[3] extrato
[4] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saq = 0
LIMITE_SAQ = 3


while True:
    opcao = input(menu)
    
    if opcao == "1":
       S = float(input("valor a ser inserido: "))
       if S > 0:
            saldo+=S
            print(f"Saldo Atual R${saldo:.2f}") 
            extrato += f"Deposito: R$ {S:.2f}\n"
       else:
           print("valor invalido")
    elif opcao == "2":
        S = float(input('Valor para saque: '))
        if (S > saldo) or (numero_saq == LIMITE_SAQ) or (S > limite):
            print('Operação invalida!!!')
        else:
            saldo -= S
            numero_saq+=1
            extrato += f"Saque: R$ {S:.2f}\n"
        print(f"Saldo Atual R${saldo:.2f}")   
    elif opcao == "3":
        print(extrato)
    elif opcao == "4":
        break
    else:  
        break
