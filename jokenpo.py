import random

def obter_escolha_usuario():
 print("Olá! Bem Vindo JANGEKU! O nosso jogo de Jokenpo!")
 escolha_user = input("Digite a sua escolha (pedra, papel ou tesoura):")
 escolha_caixa_alta = escolha_user.upper()

 while True:
  if escolha_caixa_alta == "TESOURA" or escolha_caixa_alta == "PAPEL" or escolha_caixa_alta == "PEDRA":
    print(f"A sua escolha foi {escolha_caixa_alta}.")
    break 
  else:
    print("Confirme se a digitação está correta e tente novamente")
    return obter_escolha_usuario
 
 return escolha_caixa_alta
    

def gerar_escolha_computador():
    opcoes = ["PEDRA", "PAPEL", "TESOURA"]
    escolha_computador = random.choice(opcoes)
    print (f"O computador escolheu {escolha_computador}")
    return escolha_computador


      

def determinar_vencedor(escolha_caixa_alta, escolha_computador):
    if escolha_caixa_alta == escolha_computador:
        print("Empate")
    elif escolha_caixa_alta == "PEDRA" and escolha_computador == "TESOURA" or \
         escolha_caixa_alta == "PAPEL" and escolha_computador == "PEDRA" or \
         escolha_caixa_alta == "TESOURA" and escolha_computador == "PAPEL":
        print("Parabéns, Você venceu!")
    else:
       print("O computador ganhou, tente novamente!")



def jogar_novamente():
    resposta = input("Deseja jogar novamente? (S/N): ")
    resposta = resposta.upper()
    if resposta == "S":
        return True
    else:
        print("Obrigado pela partida! Mal vejo a hora de jogarmos de novo!")
        return False

def main():
    escolha_user = obter_escolha_usuario()
    escolha_computador = gerar_escolha_computador()
    print("______________________________________________________")
    determinar_vencedor(escolha_user, escolha_computador)
    print("______________________________________________________")
    while jogar_novamente():
        escolha_user = obter_escolha_usuario()
        escolha_computador = gerar_escolha_computador()
        determinar_vencedor(escolha_user, escolha_computador)

if __name__ == "__main__":
    main()




















   
