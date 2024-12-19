import pygame

class BoardCell:
    
    
    def __init__(self, screen, top_left, width, height, color):
        self.screen = screen
        self.top_left = top_left
        self.width = width
        self.height = height
        self.center = [self.top_left[0]+(width/2),self.top_left[1]+(height/2)]
        self.color = color
        self.is_empty = True
        self.is_cell = True

    def can_move(self) -> bool:
        # Method to check if the cell is empty and can be moved to
        return self.is_empty
    
    def draw_self(self):
        pygame.draw.rect(self.screen,self.color,pygame.Rect(self.top_left[0],self.top_left[1],self.width,self.height))
