import pygame

from funcoes import limparTela, lerTexto, lerArquivo, salvarArquivo

pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Por que a galinha atravessou a rua?")  
altura = 1080                                                    
largura = 1920                                                        
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
fundo = pygame.image.load("assets/fundoRodovia.png")                    
galinha = pygame.image.load("assets/galinha.png")                   
carAzul = pygame.image.load("assets/carroAzul.png")   

limparTela()
nome = lerTexto("DIGITE O SEU NOME: ")
email = lerTexto("DIGITE O SEU E-MAIL: ")

dados = lerArquivo()
dados.append("\n" + "NOME: " +nome+ "\n" + "E-MAIL: " + email)
salvarArquivo(dados)

def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",25)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (920,110))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("Game Over",True,branco)
    textoDisplay3 = fonte2.render("press enter to continue!",True,branco)
    gameDisplay.blit(textoDisplay, (695,450))  
    gameDisplay.blit(textoDisplay3, (695,570))
    pygameDisplay.update()

def jogar():
    jogando = True
    galinhaX = 940
    galinhaY = 1010
    movimentoGalinhaY = 0
    movimentoGalinhaX = 0
    larguraGalinha = 64                                                 
    alturaGalinha = 58
    larguraCar = 203                                                      
    alturaCar = 94      
    posicaoCarX = 1000
    posicaoCarY = -203
    velocidadeCar = 15

                   
    pontos = 0
    pygame.mixer.music.load("assets/chickenThemeSong.mp3")                             
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

    carSound = pygame.mixer.Sound("assets/carSound.mp3")                       
    carSound.set_volume(1)
    pygame.mixer.Sound.play(carSound)

    batidaSound = pygame.mixer.Sound("assets/batidaSound.wav")                     
    batidaSound.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:                                       
                    movimentoGalinhaX = -6                                     
                elif event.key == pygame.K_RIGHT:
                    movimentoGalinhaX = 6
                elif event.key == pygame.K_UP:
                    movimentoGalinhaY = -6
                elif event.key == pygame.K_DOWN:
                    movimentoGalinhaY = 6
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoGalinhaY = 0
                movimentoGalinhaX = 0
            
        if jogando:
            if posicaoCarX > largura:
                posicaoCarX = -203
                posicaoCarY = 860
                pygame.mixer.Sound.play(carSound)
            else:
                posicaoCarX =posicaoCarX + velocidadeCar