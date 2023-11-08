def adicionar_transacao():
    new_transacao = []
    tp_receita = input("Digite o tipo de transação (receita ou despesa): ")
    valor = float(input("Digite o valor: "))
    descricao = input("Descreva a receita: ")
    data = input("Digite a data da transação: ")

    new_transacao.append(tp_receita)
    new_transacao.append(valor)
    new_transacao.append(descricao)
    new_transacao.append(data)

    print("CONFIRMAÇÃO DOS DADOS")
    print(f"O tipo de receita é {tp_receita}.")
    print(f"O valor colocado é {valor}.")
    print(f"A descrição da transação é {descricao}")
    print(f"E a data é {data}.")

    resposta = input("Os dados estão corretos? (Responda com SIM ou NÃO)")
    resposta_caixa_alta = resposta.upper()
    if resposta_caixa_alta == "SIM":
        print ("Okay! Os dados foram confirmados!")
    else:
        return adicionar_transacao()


def remover_transacao ():
    descricao = 
    id = input(float("Qual o Id da transacao?"))
    del descricao [descricao]
   



adicionar_transacao()