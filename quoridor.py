import pygame
import board
pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_h*0.9
screen = pygame.display.set_mode((screen_width, screen_width), pygame.RESIZABLE)
print(screen.get_size())

circle_color = (255, 0, 0)
circle_pos = [400, 300]
circle_radius = 30

board_cell_size = 100
board_cell_color = pygame.Color("darkslategrey")

board_wall_thickness = 20
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
        print(i+1)
        for j in range(board_size):
            x_position = i * (board_cell_size + board_wall_thickness)
            y_position = j * (board_cell_size + board_wall_thickness)
            board_cell = board.BoardCell(screen, [x_position, y_position],board_cell_size,board_cell_size, board_cell_color)
            board_cell.draw_self()


    
    #cursor circle
    pygame.draw.circle(screen,(255,0, 0), pygame.mouse.get_pos(),30)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(10)

pygame.quit()
