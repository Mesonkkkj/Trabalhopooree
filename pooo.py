medicos = []
pacientes = []
convenios = []
agenda = []

ere = True
#ps: emerson, regilane e evillin
while ere:
   lang = input("1 - Cadastrar Médico\n"
                "2 - Cadastrar Paciente\n"
                "3 - Cadastrar Convênio\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer?\n")
   
   def cadastrarMedicos():
         #Aqui vai seu codigo 
       print("Você deseja cadastar um médico? (sim/não)")
       rm=input("")
       if rm=="sim":
        print("Nome do médico:")
        Mnome=input("")
        print("CPF do medico:")
        Mcpf= input("")
        print("RG do medico:")
        Mrg= input("")
        print("CRM do medico:")
        Mcrm= input("")
        print("Telefone do medico:")
        Mtele= input("")
        print("Endereço do medico:")
        Mende= input("")
        print("Senha do medico:")
        Msenha= input("")
        print("Sexo do medico:")
        Msexo=input("")
        print("Deseja salvar as informaçoes? (sim/não)")
        input()
        print("Médico cadastrado com sucesso!")
        medicos.append({"nome": Mnome,
                    "cpf": Mcpf,
                    "rg": Mrg,
                    "crm": Mcrm,
                    "telefone": Mtele,
                    "endereco": Mende,
                    "sexo": Msexo,
                    "senha": Msenha})
        print(medicos)
       else:
          print("Programa encerrado!")
          breakpoint
#-#
   def cadastrarPacientes():
    
       print("Você deseja cadastar um paciente? (sim/não)")
       rp=input("")
       if rp=="sim":
        print("Nome do paciente:")
        Pnome= input("")
        print("Endereço do paciente:")
        Pende= input("")
        print("Telefone do paciente:")
        Ptele= input("")
        print("CPF do paciente:")
        Pcpf= input("")
        print("RG do paciente:")
        Prg= input("")
        print("Sexo do paciente:")
        Psexo= input("")
        print("Convenio do paciente:")
        Pconv = input("")
        print("Deseja salvar as informaçoes? (sim/não)")
        input()
        print("Paciente cadastrado com sucesso!")
        pacientes.append({
    
                "nome": Pnome,
                "endereco": Pende,
                "telefone": Ptele,
                "cpf": Pcpf,
                "rg": Prg,
                "sexo": Psexo,
                "convenio": Pconv
        })
 
        print(pacientes)
       else:
          print("Programa encerrado!")
          breakpoint
       
   def cadastrarConvenios():
     
       print("Você deseja cadastar um convênio? (sim/não)")
       rc=input(" ")
       if rc=="sim":
        print("Nome do convênio:")
        Cnome= input(" ")
        print("Telefone para contato:")
        Ctele= input(" ")
        print("Seu endereço:")
        Cende= input(" ")
        print("CNPJ do convênio:")
        Ccnpj= input(" ")
        print("Planos disponíveis: ")
        Cplanos = input(" ")
        print("Deseja salvar as informaçoes? (sim/não) " )
        input()
        print("Convenio cadastrado com sucesso!")
        convenios.append({
    
                "nome": Cnome,
                "endereco": Cende,
                "telefone": Ctele,
                "palnos": Cplanos,
                "cnpj": Ccnpj
        })
        print(convenios)
       else:
          print("Programa Encerrado!")
          breakpoint
#-#
   def buscarMedicos():
   
       print("Informe o nome ou CRM do médico:")
       busm = input("")
       resultados = [medico for medico in medicos if busm in medico['nome'] or busm in medico['crm']]
       if resultados:
           for resultado in resultados:
               print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CRM: {resultado['crm']}")
       else:
           print("Nenhum médico encontrado.")

   def buscarPacientes():
   
       print("Informe o nome ou CPF do paciente:")
       busp = input("")
       resuls = [paciente for paciente in pacientes if busp in paciente['nome'] or busp in paciente['cpf']]
       if resuls:
           for resultado in resuls:
               print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CPF: {resultado['cpf']}")
       else:
           print("Nenhum paciente encontrado.")

   def buscarConvenios():
     
       print("Informe o nome ou CNPJ do convênio")
       busc = input("")
       resultados = [convenio for convenio in convenios if busc in convenio['nome'] or busc in convenio['cnpj']]
       if resultados:
           for resultado in resultados:
               print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CNPJ: {resultado['cnpj']}")
       else:
           print("Nenhum convênio encontrado.")
   
#-#   

   def alterarMedicos():
     
     print("Informe o CRM do médico a ser alterado")
     crm = input("")
     medico = next((medico for medico in medicos if medico['crm'] == crm), None)
     if medico:
           print(f"Dados atuais: {medico}")
           print("Forneça os novos dados (deixe em branco para manter o valor atual):")
           nome = input(f"Nome ({medico['nome']}): ") or medico['nome']
           cpf = input(f"CPF ({medico['cpf']}): ") or medico['cpf']
           rg = input(f"RG ({medico['rg']}): ") or medico['rg']
           telefone = input(f"Telefone ({medico['telefone']}): ") or medico['telefone']
           endereco = input(f"Endereço ({medico['endereco']}): ") or medico['endereco']
           sexo = input(f"Sexo ({medico['sexo']}): ") or medico['sexo']
           senha = input(f"Senha ({medico['senha']}): ") or medico['senha']
           medico.update({
               "nome": nome,
               "cpf": cpf,
               "rg": rg,
               "telefone": telefone,
               "endereco": endereco,
               "sexo": sexo,
               "senha": senha
           })
           print("Dados do médico atualizados.")
           print(medicos)
     else:
           print("Médico não encontrado.")

   def alterarPacientes():
   
       print("Informe o CPF do paciente a ser alterado")
       cpf = input("")
       paciente = next((paciente for paciente in pacientes if paciente['cpf'] == cpf), None)
       if paciente:
           print(f"Dados atuais: {paciente}")
           print("Forneça os novos dados (deixe em branco para manter o valor atual):")
           nome = input(f"Nome ({paciente['nome']}): ") or paciente['nome']
           rg = input(f"RG ({paciente['rg']}): ") or paciente['rg']
           telefone = input(f"Telefone ({paciente['telefone']}): ") or paciente['telefone']
           endereco = input(f"Endereço ({paciente['endereco']}): ") or paciente['endereco']
           sexo = input(f"Sexo ({paciente['sexo']}): ") or paciente['sexo']
           convenio = input(f"Convênio ({paciente['convenio']}): ") or paciente['convenio']
           paciente.update({
               "nome": nome,
               "rg": rg,
               "telefone": telefone,
               "endereco": endereco,
               "sexo": sexo,
               "convenio": convenio
           })
           print("Dados do paciente atualizados.")
       else:
           print("Paciente não encontrado.")
 #-#  

   def marcarCompromisso():
     
     print("Deseja marcar um compromisso? (sim/não)")
     com=input("")
     if com=="sim":
         print("Data do compromisso: (formato: DD/MM/AAAA):")
         data=input("")
         print("Hora do compromisso: (formato: HH:MM - HH:MM):")
         horai=input("")
         print("Descreva o seu compromisso")
         descC=input("")
         print("Você deseja salvar essas informações? (sim/não)")
         rc=input("")
         print(f"Seu compromisso foi marcado!")
        
     else:
         print("Programa Encerrado")
         breakpoint   

   def marcarConsulta():
       print("Você deseja marcar uma consulta? (sim/não)")
       mc = input("")
       if mc == "sim":
           print("Informe o nome do médico:")
           nm = input("")
           mencontrado = next((medico for medico in medicos if medico['nome'] == nm), None)
           if mencontrado:
               print("Nome do paciente:")
               pnome = input("")
               pencontrado = next((paciente for paciente in pacientes if paciente['nome'] == pnome), None)
               if pencontrado:
                   print("Data da consulta (formato: DD/MM/AAAA):")
                   data = input("")
                   print("Horário da consulta (formato: HH:MM - HH:MM):")
                   horario = input("")
                   print("Consulta marcada com sucesso!")
                   agenda.append({
                       "data": data,
                       "horario": horario,
                       "medico": nm,
                       "paciente": pnome
                   })
               else:
                   print("Paciente não encontrado.")
           else:
               print("Médico não encontrado.")
       else:
           print("Programa Cancelado.")

   def emitirRelatorio():
    print("Qual relatório você deseja emitir?")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas realizadas em um intervalo de data")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"Nome: {medico['nome']}, CPF: {medico['cpf']}, CRM: {medico['crm']}, Telefone: {medico['telefone']}")
    elif escolha == "2":
        print("Pacientes cadastrados:")
        for paciente in pacientes:
            print(f"Nome: {paciente['nome']}, CPF: {paciente['cpf']}, Telefone: {paciente['telefone']}")
    elif escolha == "3":
        print("Convênios:")
        for convenio in convenios:
            print(f"Nome: {convenio['nome']}, CNPJ: {convenio['cnpj']}, Telefone: {convenio['telefone']}")
    elif escolha == "4":
        print("Informe a data de início (formato DD/MM/AAAA):")
        data_inicio = input("")
        data_fim = input("Informe a data de fim (formato DD/MM/AAAA): ")
        print(f"Consultas de {data_inicio} a {data_fim}:")
       
        for consulta in agenda:
            data_consulta = consulta.get("data", "")
            if data_inicio <= data_consulta <= data_fim:
                print(f"Data: {consulta['data']}, Horário: {consulta.get('horario', consulta.get('hora inicial', ''))}-{consulta.get('hora final', '')}, Médico: {consulta.get('medico', '')}, Paciente: {consulta.get('paciente', '')}, Descrição: {consulta.get('descrição', '')}")
    else:
        print("Opção inválida.")

   match lang:
       case "1":
           cadastrarMedicos()
       case "2":
           cadastrarPacientes()
       case "3": 
           cadastrarConvenios()
       case "4":
           buscarMedicos()        
       case "5":
          buscarPacientes()           
       case "6":
           buscarConvenios()        
       case "7":
           alterarMedicos()         
       case "8":
           alterarPacientes()          
       case "9":
           marcarCompromisso()          
       case "10":
           marcarConsulta()          
       case "11":
           emitirRelatorio()             
       case "12":
           ere = False
          
       case _:
           print("Escolha uma opção válida")
           lang = input("1 - Cadastrar Médico\n"
                "2 - Cadastrar Paciente\n"
                "3 - Cadastrar Convênio\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer?\n")