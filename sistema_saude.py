nomes = []
unidades = []
historicos = []   # cada paciente tem a sua própria lista de registos

opcao = ""

while opcao != "0":
    print("\n=== SISTEMA INTEGRADO DE SAÚDE - UÍGE ===")
    print("1 - Registar paciente")
    print("2 - Adicionar consulta ao histórico")
    print("3 - Consultar histórico clínico")
    print("4 - Transferir paciente para outra unidade")
    print("5 - Listar pacientes")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do paciente: ")
        unidade = input("Unidade de saúde: ")
        nomes.append(nome)
        unidades.append(unidade)
        historicos.append([])
        print("Paciente registado com o número", len(nomes))

    elif opcao == "2":
        numero = int(input("Número do paciente: "))
        if numero >= 1 and numero <= len(nomes):
            i = numero - 1
            unidade = input("Unidade onde foi a consulta: ")
            data = input("Data (dd/mm/aaaa): ")
            diagnostico = input("Diagnóstico: ")
            historicos[i].append(data + " | " + unidade + " | " + diagnostico)
            print("Consulta adicionada ao histórico.")
        else:
            print("Paciente não encontrado.")

    elif opcao == "3":
        numero = int(input("Número do paciente: "))
        if numero >= 1 and numero <= len(nomes):
            i = numero - 1
            print("\nPaciente:", nomes[i])
            print("Unidade atual:", unidades[i])
            if len(historicos[i]) == 0:
                print("Sem registos clínicos.")
            else:
                print("Histórico:")
                for registo in historicos[i]:
                    print("-", registo)
        else:
            print("Paciente não encontrado.")

    elif opcao == "4":
        numero = int(input("Número do paciente: "))
        if numero >= 1 and numero <= len(nomes):
            i = numero - 1
            nova = input("Nova unidade de saúde: ")
            historicos[i].append("Transferido de " + unidades[i] + " para " + nova)
            unidades[i] = nova
            print("Paciente transferido para", nova)
        else:
            print("Paciente não encontrado.")

    elif opcao == "5":
        if len(nomes) == 0:
            print("Sem pacientes registados.")
        else:
            for i in range(len(nomes)):
                print(i + 1, "-", nomes[i], "-", unidades[i])

    elif opcao == "0":
        print("Sistema encerrado.")

    else:
        print("Opção inválida.")
