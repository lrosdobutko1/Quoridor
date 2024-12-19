import pygame
import board
pygame.init()

screen = pygame.display.set_mode((500, 500))
print(screen.get_size())

circle_color = (255, 0, 0)
circle_pos = [400, 300]
circle_radius = 30
board_cell_size = 100
board_wall_thickness = 10
board_wall_length = board_cell_size + (2*board_wall_thickness)
clock = pygame.time.Clock()

board_size = 9

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a white background
    screen.fill((25, 25, 25))
    
    for i in range(board_size):
        for j in range(board_size):
            x_position = screen.get_size()[0]*0.01 + i*screen.get_size()[0]*0.11
            y_position = screen.get_size()[0]*0.01 + j*screen.get_size()[1]*0.11
            board_cell = board.BoardCell([x_position, y_position],screen.get_size()[0]/10,screen.get_size()[0]/10,(0,255,0))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x_position, y_position, board_cell.height, board_cell.width))


    
    #cursor circle
    pygame.draw.circle(screen,(255,0, 0), pygame.mouse.get_pos(),30)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(100)

pygame.quit()
