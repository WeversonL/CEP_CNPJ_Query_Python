from colorama import Fore
import requests
import os

os.system('clear')

def consultCep(cep):
    r = requests.get(f"https://brasilapi.com.br/api/cep/v2/{cep}")
    data = r.json()
    return data

def consultaCpnj(cnpj):
    r = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")
    data = r.json()
    return data

while True:
    opc = input("1 - Consultar CEP\n2 - Consultar CNPJ\n")

    os.system('clear')
    
    if opc == "1":
        try:

            cepUser = input("Informe o CEP: " + Fore.GREEN)
            cepUser = cepUser.replace("-","")
            cepUser = cepUser.replace(".","")
            cepUser = cepUser.replace("/","")

            data = consultCep(cepUser)
            print(Fore.CYAN + "-" * 60)
            print(Fore.WHITE + f"Estado: {Fore.GREEN + data['state']}")
            print(Fore.CYAN + "-" * 60)
            print(Fore.WHITE + f"Cidade: {Fore.GREEN + data['city']}")
            print(Fore.CYAN + "-" * 60)
            print(Fore.WHITE + f"Logradouro: {Fore.GREEN + data['street']}")
            print(Fore.CYAN + "-" * 60)
            print(Fore.WHITE + f"Bairro: {Fore.GREEN + data['neighborhood']}")
            print(Fore.CYAN + "-" * 60)
            print(Fore.WHITE + f"Serviço: {Fore.GREEN + data['service']}")
            print(Fore.CYAN + "-" * 60)

            opcc = input(Fore.WHITE + "\n\nDeseja continuar? [" + Fore.GREEN + "Y" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE + "] " + Fore.RESET)
            if opcc == "Y" or opcc == "y":
                os.system('clear')
                continue
            else:
                os.system('clear')
                break
        
        except:
            print(Fore.RED + "CEP não localizado")
            print(Fore.CYAN + "-" * 60 + Fore.RESET)

    elif opc == "2":

        try:

            cnpj = input("Informe o CNPJ: " + Fore.GREEN)
            cnpj = cnpj.replace("-","")
            cnpj = cnpj.replace(".","")
            cnpj = cnpj.replace("/","")

            data = consultaCpnj(cnpj)
            print(Fore.CYAN + "-" * 60)
            print(Fore.WHITE + f"Razão Social: {Fore.GREEN + data['razao_social']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Nome fantasia: {Fore.GREEN + data['nome_fantasia']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Situação cadastral: {Fore.GREEN + data['descricao_situacao_cadastral']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Data situação cadastral: {Fore.GREEN + data['data_situacao_cadastral']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Inicio de atividade: {Fore.GREEN + data['data_inicio_atividade']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Descrição de atividade: {Fore.GREEN + data['cnae_fiscal_descricao']}")
            print(Fore.CYAN + "-" * 60 + Fore.RESET)

            print(Fore.WHITE + f"Porte da empresa: {Fore.GREEN + data['descricao_porte']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Capital social: R$ {Fore.GREEN + str(data['capital_social'])}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Estado: {Fore.GREEN + data['uf']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Municipio: {Fore.GREEN + data['municipio']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Bairro: {Fore.GREEN + data['bairro']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + "Endereço: " + Fore.GREEN + f"{data['descricao_tipo_logradouro']} {data['logradouro']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.WHITE + f"Número do endereço: {Fore.GREEN + data['numero']}")
            print(Fore.CYAN + "-" * 60)

            opcc = input(Fore.WHITE + "\n\nDeseja continuar? [" + Fore.GREEN + "Y" + Fore.WHITE + "/" + Fore.RED + "N" + Fore.WHITE + "] " + Fore.RESET)
            if opcc == "Y" or opcc == "y":
                os.system('clear')
                continue
            else:
                os.system('clear')
                break
        
        except:
            print(Fore.RED + "CNPJ não localizado")
            print(Fore.CYAN + "-" * 60 + Fore.RESET)

    else:
        print(Fore.CYAN + "-" * 60)
        print(Fore.RED + "Digite uma opção válida")
        print(Fore.CYAN + "-" * 60 + Fore.RESET)
        