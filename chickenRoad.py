import pygame

from funcoes import limparTela, lerTexto, lerArquivo, salvarArquivo

limparTela()
nome = lerTexto("DIGITE O SEU NOME: ")
email = lerTexto("DIGITE O SEU E-MAIL: ")

dados = lerArquivo()
dados.append("\n" + "NOME: " +nome+ "\n" + "E-MAIL: " + email)
salvarArquivo(dados)


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
carAzul2 = pygame.image.load("assets/carroRoxo.png")
carAzul3 = pygame.image.load("assets/carroAzul.png")
carAzul4 = pygame.image.load("assets/carroAzul.png")
carAzul5 = pygame.image.load("assets/carroRoxo.png")
carAzul6 = pygame.image.load("assets/carroAzul.png")  

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
    larguraCar2 = 203                                                      
    alturaCar2 = 94      
    posicaoCarX2 = 400
    posicaoCarY2 = -203
    velocidadeCar2 = 15
    larguraCar3 = 203                                                       
    alturacar3 = 94                                                         
    posicaoCarX3 = 1400                                                    
    posicaoCarY3 = -203                                                     
    velocidadeCar3 = 15
    larguraCar4 = 203                                                       
    alturaCar4 = 94                                                         
    posicaoCarX4 = 2000                                                     
    posicaoCarY4 = -203                                                     
    velocidadeCar4 = 15 
    larguraCar5 = 203                                                       
    alturaCar5 = 94                                                         
    posicaoCarX5 = 600                                                 
    posicaoCarY5 = -203                                                     
    velocidadeCar5 = 15
    larguraCar6 = 203                                                       
    alturaCar6 = 94                                                         
    posicaoCarX6 = 100                                                     
    posicaoCarY6 = -203                                                     
    velocidadeCar6 = 15   
           
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

            if posicaoCarX2 > largura:
                posicaoCarX2 = -203
                posicaoCarY2 = 760
                pygame.mixer.Sound.play(carSound)
            else:
                posicaoCarX2 =posicaoCarX2 + velocidadeCar2

            if posicaoCarX3 > largura:
                posicaoCarX3 = -203
                posicaoCarY3 = 550
                pygame.mixer.Sound.play(carSound)
            else:
                posicaoCarX3 =posicaoCarX3 + velocidadeCar3

            if posicaoCarX4 > largura:
                posicaoCarX4 = -203
                posicaoCarY4 = 450
                pygame.mixer.Sound.play(carSound)
            else:
                posicaoCarX4 =posicaoCarX4 + velocidadeCar4
            
            if posicaoCarX5 > largura:
                posicaoCarX5 = -203
                posicaoCarY5 = 340
                pygame.mixer.Sound.play(carSound)
            else:
                posicaoCarX5 =posicaoCarX5 + velocidadeCar5

            if posicaoCarX6 > largura:
                posicaoCarX6 = -203
                posicaoCarY6 = 240
                pygame.mixer.Sound.play(carSound)
            else:
                posicaoCarX6 =posicaoCarX6 + velocidadeCar6

            if galinhaX + movimentoGalinhaX + larguraGalinha < largura and galinhaX + movimentoGalinhaX > 0:
                galinhaX = galinhaX + movimentoGalinhaX

            if galinhaY + movimentoGalinhaY + alturaGalinha < altura and galinhaY + movimentoGalinhaY > 0:
                galinhaY = galinhaY + movimentoGalinhaY
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(galinha, (galinhaX,galinhaY))
            
            gameDisplay.blit(carAzul, (posicaoCarX,posicaoCarY))
            gameDisplay.blit(carAzul2, (posicaoCarX2,posicaoCarY2))
            gameDisplay.blit(carAzul3, (posicaoCarX3,posicaoCarY3))
            gameDisplay.blit(carAzul4, (posicaoCarX4,posicaoCarY4))
            gameDisplay.blit(carAzul5, (posicaoCarX5,posicaoCarY5))
            gameDisplay.blit(carAzul6, (posicaoCarX6,posicaoCarY6))
            escreverTexto("Pontos: "+str(pontos))

            pixelXGalinha = list(range(galinhaX, galinhaX+larguraGalinha))
            pixelYGalinha = list(range(galinhaY, galinhaY+alturaGalinha))

            pixelXCar = list(range(posicaoCarX, posicaoCarX+larguraCar))
            pixelYCar = list(range(posicaoCarY, posicaoCarY+alturaCar))
            pixelXCar2 = list(range(posicaoCarX2, posicaoCarX2+larguraCar2))
            pixelYCar2 = list(range(posicaoCarY2, posicaoCarY2+alturaCar2))
            pixelXcar3 = list(range(posicaoCarX3, posicaoCarX3+larguraCar3))                    
            pixelYcar3 = list(range(posicaoCarY3, posicaoCarY3+alturacar3))      
            pixelXcar4 = list(range(posicaoCarX4, posicaoCarX4+larguraCar4))                    
            pixelYcar4 = list(range(posicaoCarY4, posicaoCarY4+alturaCar4))            
            pixelXcar5 = list(range(posicaoCarX5, posicaoCarX5+larguraCar5))                   
            pixelYcar5 = list(range(posicaoCarY5, posicaoCarY5+alturaCar5))        
            pixelXcar6 = list(range(posicaoCarX6, posicaoCarX6+larguraCar6))                   
            pixelYcar6 = list(range(posicaoCarY6, posicaoCarY6+alturaCar6)) 

            colisaoY = len(list(set(pixelYCar) & set(pixelYGalinha) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXCar) & set(pixelXGalinha) ))
                print(colisaoX)
                if colisaoX > 60:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(batidaSound)

            colisaoY2 = len(list(set(pixelYCar2) & set(pixelYGalinha) ))
            if colisaoY2 > 0:
                colisaoX2 = len(list(set(pixelXCar2) & set(pixelXGalinha) ))
                print(colisaoX2)
                if colisaoX2 > 60:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(batidaSound)

            colisaoY3 = len(list(set(pixelYcar3) & set(pixelYGalinha) ))                        
            if colisaoY3 > 0:
                colisaoX3 = len(list(set(pixelXcar3) & set(pixelXGalinha) ))                    
                print(colisaoX3)
                if colisaoX3 > 60:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(batidaSound)
            
            colisaoY4 = len(list(set(pixelYcar4) & set(pixelYGalinha) ))                       
            if colisaoY4 > 0:
                colisaoX4 = len(list(set(pixelXcar4) & set(pixelXGalinha) ))                    
                print(colisaoX4)
                if colisaoX4 > 60:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(batidaSound)

            colisaoY5 = len(list(set(pixelYcar5) & set(pixelYGalinha) ))                        
            if colisaoY5 > 0:
                colisaoX5 = len(list(set(pixelXcar5) & set(pixelXGalinha) ))                    
                print(colisaoX5)
                if colisaoX5 > 60:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(batidaSound)

            colisaoY6 = len(list(set(pixelYcar6) & set(pixelYGalinha) ))                        
            if colisaoY6 > 0:
                colisaoX6 = len(list(set(pixelXcar6) & set(pixelXGalinha) ))                    
                print(colisaoX6)
                if colisaoX6 > 60:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(batidaSound)

            if galinhaY < 65 and galinhaX < 1040  and  galinhaX > 860 :
                pontos += 1
                velocidadeCar += 3
                velocidadeCar2 += 3
                velocidadeCar3 += 3
                velocidadeCar4 += 3
                velocidadeCar5 += 3
                velocidadeCar6 += 3
                galinhaX = 940
                galinhaY = 1010

        pygameDisplay.update()
        clock.tick(60)

jogar()