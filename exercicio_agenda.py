import json
import os

agenda = "agenda_cabeleireiro.json"

def carregar_dados():
    if os.path.exists(agenda):
        with open(agenda, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
def obter_dados():
    Nome_do_cliente =input( "Informe seu nome:")
    Servico =input("Informe o serviço desejado:")
    Data =input("Informe a data:")
    Horario =input("Informe o horario:")
    Observacoes =input("Informe observações (se houver):")
    
    data_agenda ={
        "nome_do_cliente": Nome_do_cliente,
        "servico": Servico,
        "data": Data,
        "observacoes": Observacoes
    }

def cadastrar_agenda(receber_agendamentos):
    db_agendamentos = carregar_dados()
    db_agendamentos.append(receber_agendamentos)

    with open(agenda, "w", encoding="utf-8") as arq_json:
        json.dump(db_agendamentos, arq_json, indent=4, ensure_ascii=False)

def mostrar_agendamentos(agendamentos):
    if agendamentos:
        for agenda in agendamentos:
            print(f"""
                  Nome do cliente {agenda["nome_do_cliente"]}
                  Serviço {agenda["servico"]}
                  Data {agenda["data"]}
                  Horario {agenda["horario"]}
                  Observacoes {agenda["observacoes"]}
            """)

def iniciar_sistema():
    db_agendamentos = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar agenda completa")
        print("Opção 2 - Cadastrar novo agendamento")
        print("Opção 3 - Sair do sistema")
        print("="*80)

        opcao = input("Escolha uma das opções do menu: ")

        if opcao == "1":
            mostrar_agendamentos(db_agendamentos)
        elif opcao == "2":
            cadastrar_agenda(obter_dados())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção invalida, escolha uma das opções do menu.")

iniciar_sistema()