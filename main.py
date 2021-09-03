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
            print(Fore.RESET + f"Estado: {Fore.GREEN + data['state']}")
            print(Fore.CYAN + "-" * 60)
            print(Fore.RESET + f"Cidade: {Fore.GREEN + data['city']}")
            print(Fore.CYAN + "-" * 60)
            print(Fore.RESET + f"Logradouro: {Fore.GREEN + data['street']}")
            print(Fore.CYAN + "-" * 60)
            print(Fore.RESET + f"Bairro: {Fore.GREEN + data['neighborhood']}")
            print(Fore.CYAN + "-" * 60)
            print(Fore.RESET + f"Serviço: {Fore.GREEN + data['service']}")
            print(Fore.CYAN + "-" * 60)

            opcc = input(Fore.RESET + "\n\nDeseja continuar? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "] " + Fore.RESET)
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
            print(Fore.RESET + f"Razão Social: {Fore.GREEN + data['razao_social']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Nome fantasia: {Fore.GREEN + data['nome_fantasia']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Situação cadastral: {Fore.GREEN + data['descricao_situacao_cadastral']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Data situação cadastral: {Fore.GREEN + data['data_situacao_cadastral']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Inicio de atividade: {Fore.GREEN + data['data_inicio_atividade']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Descrição de atividade: {Fore.GREEN + data['cnae_fiscal_descricao']}")
            print(Fore.CYAN + "-" * 60 + Fore.RESET)

            print(Fore.RESET + f"Porte da empresa: {Fore.GREEN + data['descricao_porte']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + "Capital social: " + Fore.YELLOW + "R$ " + f"{Fore.GREEN + str(data['capital_social'])}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"CEP: {Fore.GREEN + data['cep']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Estado: {Fore.GREEN + data['uf']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Municipio: {Fore.GREEN + data['municipio']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Bairro: {Fore.GREEN + data['bairro']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + "Endereço: " + Fore.GREEN + f"{data['descricao_tipo_logradouro']} {data['logradouro']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Número do endereço: {Fore.GREEN + data['numero']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Complemento: {Fore.GREEN + data['complemento']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Telefone 1° opção: {Fore.GREEN + data['ddd_telefone_1']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"Telefone 2° opção: {Fore.GREEN + data['ddd_telefone_2']}")
            print(Fore.CYAN + "-" * 60)

            print(Fore.RESET + f"FAX: {Fore.GREEN + data['ddd_fax']}")
            print(Fore.CYAN + "-" * 60)

            opcc = input(Fore.RESET + "\n\nDeseja continuar? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "] " + Fore.RESET)
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
        