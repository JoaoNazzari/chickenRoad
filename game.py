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