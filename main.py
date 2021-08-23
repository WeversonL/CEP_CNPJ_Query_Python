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

            cepUser = input("Informe o CEP: \033[1;32m")
            cepUser = cepUser.replace("-","")
            cepUser = cepUser.replace(".","")
            cepUser = cepUser.replace("/","")

            data = consultCep(cepUser)
            print("\033[0m\033[1;36m-\033[0m"*60)
            print(f"Estado: \033[1;32m{data['state']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Cidade: \033[1;32m{data['city']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Logradouro: \033[1;32m{data['street']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Bairro: \033[1;32m{data['neighborhood']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Serviço: \033[1;32m{data['service']}\033[0m")
            print("\033[1;36m-\033[0m"*60)

            opcc = input("\n\nDeseja continuar? [\033[1;32mY\033[0m/\33[1;35mN\033[0m] ")
            if opcc == "Y" or opcc == "y":
                os.system('clear')
                continue
            else:
                os.system('clear')
                break
        
        except:
            print("\033[1;35mCEP não localizado\033[0m")
            print("\033[1;36m-\033[0m"*60)

    elif opc == "2":

        try:

            cnpj = input("Informe o CNPJ: \033[1;32m")
            cnpj = cnpj.replace("-","")
            cnpj = cnpj.replace(".","")
            cnpj = cnpj.replace("/","")

            data = consultaCpnj(cnpj)
            print("\033[0m\033[1;36m-\033[0m"*60)
            print(f"Razão Social: \033[1;32m{data['razao_social']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Nome fantasia: \033[1;32m{data['nome_fantasia']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Situação cadastral: \033[1;32m{data['descricao_situacao_cadastral']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Data situação cadastral: \033[1;32m{data['data_situacao_cadastral']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Inicio de atividade: \033[1;32m{data['data_inicio_atividade']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Descrição de atividade: \033[1;32m{data['cnae_fiscal_descricao']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Porte da empresa: \033[1;32m{data['descricao_porte']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Capital social: \033[1;32mR$ {data['capital_social']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Estado: \033[1;32m{data['uf']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Municipio: \033[1;32m{data['municipio']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Bairro: \033[1;32m{data['bairro']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Endereço: \033[1;32m{data['descricao_tipo_logradouro']} {data['logradouro']}\033[0m")
            print("\033[1;36m-\033[0m"*60)
            print(f"Número do endereço: \033[1;32m{data['numero']}\033[0m")
            print("\033[1;36m-\033[0m"*60)

            opcc = input("\n\nDeseja continuar? [\033[1;32mY\033[0m/\33[1;35mN\033[0m] ")
            if opcc == "Y" or opcc == "y":
                os.system('clear')
                continue
            else:
                os.system('clear')
                break
        
        except:
            print("\033[1;35mCNPJ não localizado\033[0m")
            print("\033[1;36m-\033[0m"*60)

    else:
        print("\033[1;36m-\033[0m"*60)
        print("\033[1;35mDigite uma opção válida\033[0m")
        print("\033[1;36m-\033[0m"*60)
        