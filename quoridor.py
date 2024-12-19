import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Pygame test")

circle_color = (255, 0, 0)
circle_pos = [400, 300]
circle_radius = 30
clock = pygame.time.Clock()

board_cell_size = 100
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a white background
    screen.fill((25, 25, 25))
    
    pygame.draw.circle(screen,(255,255,255), pygame.mouse.get_pos(),30)
    
    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(100)

pygame.quit()
