import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("musica.mp3") 

# Toca o arquivo
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
input("Pressione Enter para parar a reprodução...")
pygame.mixer.music.stop()
