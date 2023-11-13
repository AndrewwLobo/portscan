import socket

most_ports = [20,21,22,23,25]

#Caso o arguemento 'porta' seja str, informa que deve ser int.
def obter_porta():
    while True:
        porta = input("Informe a porta: ")

        if porta.isdigit():
            return int(porta)
        else:
            print("Insira número inteiro.")
            print("Exemplo: 22")

#Realiza a conexão na porta e valida se está aberta ou não.
def meusocket_connection(ip, porta):

    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resultado = meusocket.connect_ex((ip,porta))

    if resultado == 0:
        print (f"Porta {porta} aberta.")
    else:
        print (f"Porta {porta} fechada.")



print ("##########################################\n"
       "Para scannear aperas uma porta digite: 1\n"
       "Para full scan, digite: 2\n"
       "Para scannear top 20 portas, digite: 3\n"
       "##########################################")
escolha = input("Informe sua escolha: ")


if escolha == '1':
    print("")
    ip = input("informe o domínio: ")
    porta = obter_porta()
    meusocket_connection(ip, porta)

elif escolha == '2':
    ip = input("informe o domínio: ")
    for porta in range(1,5000):
        meusocket_connection(ip, porta)

elif escolha == '3':
    ip = input("informe o domínio: ")
    for porta in most_ports:
        meusocket_connection(ip, porta)

    print("Deseja realizar um banner gabbring em alguma porta ?\n"
        "S = SIM \n"
        "N = NÃO \n")
    res = input("S OU N:")

    if res == "S":
        print ("Qual porta deseja realizar o bannergrabing ?")
        res_1 = input("Informe a porta: ")
        res_1 = int(res_1)
        meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = meusocket.connect_ex((ip,res_1))
        banner = meusocket.recv(1024)
        print(banner)
        



