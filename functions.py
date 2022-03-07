import random
from time import sleep

def menuInicial():
    print(" -------------BEM VINDO A CENTRAL DE MINI JOGOS ----------------------------")
    print(" -------------AQUI ESTÃO AS OPÇÕES: ----------------------------------------")
    print(" -------------DIGITE '1' para fazer um sorteio------------------------------")
    print(" -------------DIGITE '2'   para rodar os dados------------------------------")
    print(" -------------DIGITE '3'   para advinhar o número---------------------------")
    print(" -------------DIGITE '4'   para interagir com a bola de cristal-------------")
    print(" -------------DIGITE '5'   para jogar Pedra, Papel e Tesoura ---------------")
    print(" -------------DIGITE '6'   para jogar Forca --------------------------------")
    jogo = input("                      DIGITE AQUI: ")

    if jogo == '1':
        sorteio()
    elif jogo == '2':
        rodar_dado()
    elif jogo == '3':
        advinhe()
    elif jogo == '4':
        bolaDeCristal()
    elif jogo == '5':
        pedraPapelTesoura()
    elif jogo =='6':
        forca()

def rodar_dado():
    resposta = input("Vamos rodar o dado ? ").upper()
    try:
        if resposta == 'SIM':
            print(random.randint(1, 6))
            tryAgain = input("Gostaria de jogar novamente ? (S/N) ").upper()
            if tryAgain == 'S':
                rodar_dado()
            else:
                print("Obrigado pela sua participação !")
                menuInicial()
        elif resposta == 'NAO':
            print("Obrigado pela sua participação")
    except:
        print("OCORREU UM ERRO")
def sorteio():
    print("BEM VINDO AO JOGO DE SORTEIO")
    valorMinimo = int(input("Informe o valor mínimo a ser sorteado: "))
    valorMaximo = int(input("Informe o valor máximo a ser sorteado: "))

    while valorMinimo or valorMaximo == "":
        print("Favor inserir um valor mínimo! ")
        print("Favor inserir um valor máximo! ")

    checksorteio = input("VAMOS COMEÇAR ? \n Digite <S> para sim \n ou \n <N> para não: ")
    try:
        if checksorteio == 'S':
            print(random.randrange(valorMinimo, valorMaximo))
            tryAgain = input("Gostaria de jogar novamente ? (S/N) ").upper()
            if tryAgain == 'S':
                sorteio()
            else:
                print("Obrigado pela sua participação !")
                menuInicial()
        elif checksorteio == 'N':
            print("Obrigado pela sua participação")
    except:
        print("OCORREU UM ERRO AO RODAR O SORTEIO")
def advinhe():
    print("------------- VAMOS DETERMINAR A DIFICULDADE DO JOGO ? ---------------------")
    print(" -------------[1] -> FÁCIL (Sem limite de tentativas) ----------------------")
    print(" -------------[2] -> MÉDIO (Limite de 10 tentativas) -----------------------")
    print(" -------------[3] -> DIFÍCIL (Limite de 12 tentativas) ---------------------")
    print(" -------------[4] -> LENDÁRIO (Limite de 15 tentativas) --------------------")
    dificuldade = input("QUAL SERÁ A DIFICULDADE ?")

    if dificuldade == '1':
        aleatorioNumero = random.randint(1, 10)
        tentativas = 1000000000000000000000000000000000000000000000000000000000000000000000
        mecanicaAdvinhar(aleatorioNumero, tentativas)
    elif dificuldade == '2':
        aleatorioNumero = random.randint(1, 100)
        tentativas = 2
        mecanicaAdvinhar(aleatorioNumero, tentativas)
    elif dificuldade == '3':
        aleatorioNumero = random.randint(1, 1000)
        tentativas = 12
        mecanicaAdvinhar(aleatorioNumero, tentativas)
    elif dificuldade == '4':
        aleatorioNumero = random.randint(1, 10000)
        tentativas = 15
        mecanicaAdvinhar(aleatorioNumero, tentativas)
def mecanicaAdvinhar(aleatorioNumero, tentativas):
    print("BEM VINDO AO JOGO DE ADVINHAR, ESTÁ PRONTO ?")
    palpite = input("ADVINHE O NÚMERO: ")
    while palpite == "" or palpite == " " or palpite is None:
        print("ERRO")
        palpite = input("DIGITE UM NÚMERO VÁLIDO:")
    try:
        if int(palpite) != aleatorioNumero:
            for x in range(int(tentativas)):
                if int(palpite) == aleatorioNumero:
                    print("PARABÉNS, VOCÊ ACERTOU")
                    break
                elif int(palpite) > aleatorioNumero:
                    palpite = int(input("Chute um número menor: "))
                elif int(palpite) < aleatorioNumero:
                    palpite = int(input("Chute um número maior: "))

            print("Suas tentativa se esgotaram infelizmente :(")
            tryAgain = input("Gostaria de jogar novamente ? (S/N) ").upper()
            if tryAgain == 'S':
                advinhe()
            else:
                print("Obrigado pela sua participação !")
                menuInicial()

    except:
        print("Isso não é um número")
        sleep(5)
        menuInicial()
def bolaDeCristal():
    ready = input("OLÁ, SOU A BOLA DE CRISTAL E LHE DIREI TODA A VERDADE, ESTÁ PRONTO ?").upper()
    while ready == 'SIM' or ready == 'S':
        perguntaUsuario = input("Perfeito, faça-me uma pergunta: ")
        opcoes = ["SIM", "NÃO", "TALVEZ", "OLHA, SINCERAMENTE NÃO SEI", "É PROVÁVEL"]
        print(random.choice(opcoes))

        ready = input("Gostaria de continuar perguntando ?").upper()

    if ready != 'SIM' or ready != 'S':
        print("Obrigado pela sua participação ! ")
def forca():
    print("VAMOS JOGAR FORCA ? ")
    print("Você vai jogar com alguém localmente ou contra o computador ? ")
    qtdJogadores = input("Sua opção (LOCAL/COMP): ").upper()
    if qtdJogadores == "LOCAL":
        forcaSingle()
    elif qtdJogadores == "COMP":
        forcaMulti()
def forcaSingle():
    print("VAMOS JOGAR FORCA ! ")
    print("       -------- \n"
          "       |      | \n"
          "       O      | \n"
          "      /|\     | \n"
          "       |      | \n"
          "      / \     | \n"
          "______________|_\n")
    print("------------- QUAL SERÁ A CATEGORIA ? -------------------------")
    print(" -------------[1] -> ANIMAL -----------------------------------")
    print(" -------------[2] -> OBJETOS ----------------------------------")
    print(" -------------[3] -> PAÍSES -----------------------------------")
    print(" -------------[4] -> PARTE DO CORPO HUMANO --------------------")
    categoriaForca = input("QUAL SERÁ A CATEGORIA ? ")
    if categoriaForca == '1':
        palarvrasAnimal = ["ONCA", "LEAO", "GIRAFA","ELEFANTE", "MAMUTE", "CACHORRO","GATO", "PASSARO", "PORCO","CARNEIRO", "TIGRE", "LEMURE","ARANHA", "COBRA", "LAGARTO"]
        palavra_comp = random.choice(palarvrasAnimal)
        print("A palavra escolhida tem {} letras".format(len(palavra_comp)))
        forcaMecanismo(palavra_comp)

    elif categoriaForca == '2':
        palavrasObjetos = ["TESOURA", "TECLADO", "MESA", "COMPUTADOR", "CARRO", "PORTA", "DINHEIRO", "TENIS", "CADERNO", "FONE DE OUVIDO", "BORRIFADOR", "QUADRO", "VIDEO-GAME", "CELULAR", "SOFA"]
        palavra_comp = random.choice(palavrasObjetos)
        print("A palavra escolhida tem {} letras".format(len(palavra_comp)))
        forcaMecanismo(palavra_comp)

    elif categoriaForca == '3':
        palavraPaises = ["BRASIL", "NORUEGA", "SUIÇA", "URUGUAI", "ESTADOS UNIDOS", "CANADA", "HONDURAS", "VATICANO", "ITALIA","ESLOVAQUIA", "IRAQUE", "RUSSIA", "AUSTRALIA", "INDIA", "JAPAO"]
        palavra_comp = random.choice(palavraPaises)
        print("A palavra escolhida tem {} letras".format(len(palavra_comp)))
        forcaMecanismo(palavra_comp)

    elif categoriaForca == '4':
        palavraParteDoCorpoHumano = ["BRACO" , "ORELHA", "PE", "PERNA", "UNHA", "BARRIGA", "CABEÇA", "QUADRIL", "DEDOS", "GARGANTA", "OLHO", "OUVIDO", "ANTE-BRAÇO", "FALANGE", "COXA"]
        palavra_comp = random.choice(palavraParteDoCorpoHumano)
        print("A palavra escolhida tem {} letras".format(len(palavra_comp)))
        forcaMecanismo(palavra_comp)
def forcaMecanismo(palavra_comp):
    letras_chutadas = []
    letras_acertadas = []
    print("       -------- \n"
          "       |      | \n"
          "       O      | \n"
          "      /|\     | \n"
          "       |      | \n"
          "      / \     | \n"
          "              | \n")
    print("_" * len(palavra_comp))

    print("Chute uma letra: ")
    letrachute = input("Letra: ").upper()
    membrosBoneco = 0
    acertos = 0

    letras_chutadas.append(letrachute)
    print("Letras já tentadas: ", letras_chutadas)

    while membrosBoneco <= 8:
        if letrachute in palavra_comp:
            print("Você acertou uma letra")
            acertos = acertos + 1
            letras_acertadas.append(letrachute)
            print("Letras acertadas: ", letras_acertadas)
            print("VOCÊ TEM {} ACERTOS".format(acertos))
            letrachute = input("Letra: ").upper()

        elif acertos == len(palavra_comp):
            print("PARABÉS VOCE GANHOU!!")
            break

        if letrachute not in palavra_comp:
            membrosBoneco = membrosBoneco + 1
            print("Conferencia: ", membrosBoneco)
            print("Essa não. Vamos la!")
            if membrosBoneco == 2:
                print("       -------- \n"
                      "       |      | \n"
                      "       O      | \n"
                      "       |      | \n"
                      "              | \n"
                      "              | \n"
                      "______________|_\n")
            elif membrosBoneco == 3:
                print("       -------- \n"
                      "       |      | \n"
                      "       O      | \n"
                      "       |\     | \n"
                      "              | \n"
                      "              | \n"
                      "______________|_\n")
            elif membrosBoneco == 4:
                print("       -------- \n"
                      "       |      | \n"
                      "       O      | \n"
                      "      /|\     | \n"
                      "              | \n"
                      "              | \n"
                      "______________|_\n")
            elif membrosBoneco == 5:
                print("       -------- \n"
                      "       |      | \n"
                      "       O      | \n"
                      "      /|\     | \n"
                      "       |      | \n"
                      "              | \n"
                      "______________|_\n")
            elif membrosBoneco == 6:
                print("       -------- \n"
                      "       |      | \n"
                      "       O      | \n"
                      "      /|\     | \n"
                      "       |      | \n"
                      "              | \n"
                      "______________|_\n")
            elif membrosBoneco == 7:
                print("       -------- \n"
                      "       |      | \n"
                      "       O      | \n"
                      "      /|\     | \n"
                      "       |      | \n"
                      "      /       | \n"
                      "______________|_\n")
            elif membrosBoneco == 8:
                print("       -------- \n"
                      "       |      | \n"
                      "       O      | \n"
                      "      /|\     | \n"
                      "       |      | \n"
                      "      / \     | \n"
                      "______________|_\n")
                print("VOCE PERDEU")
                sleep(3)
                retornoForca = input("Você deseja jogar novamente? (S/N) ").upper()
                if retornoForca == 'S':
                    forca()
                elif retornoForca == 'N':
                    print("Obrigado pela jogatina")
                    sleep(1)
                    menuInicial()

            print("Você tem {} erros".format(membrosBoneco))
            letrachute = input("Letra: ").upper()
def forcaMulti():
    pass
    print("VAMOS JOGAR FORCA ! ")
    palavraUsuario = input("Escreva uma palavra para o outro jogador advinhar:")
    palavra_comp = random.choice(palavraUsuario)
    print("A palavra escolhida tem {} letras".format(len(palavra_comp)))
    forcaMecanismo(palavra_comp)
def pedraPapelTesoura():
    print("Vamos jogar Pedra Papel e Tesoura!")
    usuario = input("Sua vez: ").upper()

    if usuario != "PEDRA" or usuario != "PAPEL" or usuario == "TESOURA":
        print("Jogada Inválida. As opções são: Pedra, Papel ou Tesoura")
        usuario = input("Qual você escolhe ? ").upper()
        condicoesPedraPapelTesoura(usuario)
def condicoesPedraPapelTesoura(usuario):
    opcoesjogo = ['PEDRA', 'PAPEL', 'TESOURA']
    print("Computador: ", random.choice(opcoesjogo))

    if random.choice(opcoesjogo) == usuario:
        print("É um empate!! \n Vamos de novo ? ")
        usuario = input("Sua vez: ").upper()
        print("Computador: ", random.choice(opcoesjogo))

    elif usuario == "PEDRA" and random.choice(opcoesjogo) == "PAPEL":
        print("VOCÊ PERDEU :(")
        comecarDenovo = input("Vamos de novo ? (S/N) ").upper()
        if comecarDenovo == 'S':
            pedraPapelTesoura()
        else:
            print("Obrigado por jogar conosco!")
            sleep(5)
            menuInicial()

    elif usuario == "PAPEL" and random.choice(opcoesjogo) == "TESOURA":
        print("VOCÊ PERDEU :(")
        comecarDenovo = input("Vamos de novo ? (S/N) ").upper()
        if comecarDenovo == 'S':
            pedraPapelTesoura()
        else:
            print("Obrigado por jogar conosco!")
            sleep(5)
            menuInicial()

    elif usuario == "TESOURA" and random.choice(opcoesjogo) == "PEDRA":
        print("VOCÊ PERDEU :(")
        comecarDenovo = input("Vamos de novo ? (S/N) ").upper()
        if comecarDenovo == 'S':
            pedraPapelTesoura()
        else:
            print("Obrigado por jogar conosco!")
            sleep(5)
            menuInicial()

    elif usuario == "TESOURA" and random.choice(opcoesjogo) == "PAPEL":
        print("VOCÊ GANHOU :)")
        comecarDenovo = input("Vamos de novo ? (S/N) ").upper()
        if comecarDenovo == 'S':
            pedraPapelTesoura()
        else:
            print("Obrigado por jogar conosco!")
            sleep(5)
            menuInicial(),

    elif usuario == "PEDRA" and random.choice(opcoesjogo) == "TESOURA":
        print("VOCÊ GANHOU :)")
        comecarDenovo = input("Vamos de novo ? (S/N) ").upper()
        if comecarDenovo == 'S':
            pedraPapelTesoura()
        else:
            print("Obrigado por jogar conosco!")
            sleep(5)
            menuInicial()

    elif usuario == "PAPEL" and random.choice(opcoesjogo) == "PEDRA":
        print("VOCÊ GANHOU :)")
        comecarDenovo = input("Vamos de novo ? (S/N) ").upper()
        if comecarDenovo == 'S':
            pedraPapelTesoura()
        else:
            print("Obrigado por jogar conosco!")
            sleep(5)
            menuInicial()