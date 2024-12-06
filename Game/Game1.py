import pygame

# init
pygame.init()

isRun = True

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# Obejct Game
# Posisi
y = 250
x = 250

# ukuran 
panjang = 20
lebar = 20

# kecepatan gerak
speed = 0.2

while isRun:
    pygame.time.delay(2)
    # user input,database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    # keyboard action
    keys = pygame.key.get_pressed()
    
    # ke kiri
    if keys[pygame.K_a] and x > 0:
        x -= speed
        
    if keys[pygame.K_d] and x < window_lebar - lebar:
        x += speed
    
    if keys[pygame.K_w] and y > 0:
        y -= speed
    
    if keys[pygame.K_s] and y < window_panjang - panjang:
        y += speed
    
    # update asset
    window.fill((31, 209, 188))
    pygame.draw.rect(window,(209, 46, 31),(x,y,lebar,panjang))
    # render ke display
    pygame.display.update()
    
pygame.quit()





