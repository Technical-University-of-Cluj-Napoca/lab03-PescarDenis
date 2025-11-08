import pygame

class Button:
    def __init__(self, x, y, width, height, text, action, win):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.win = win
        self.font = pygame.font.SysFont("Consolas", 20,bold = True)
        # Purple theme
        self.bg_color = (60, 50, 80)
        self.hover_color = (100, 80, 140)
        self.text_color = (230, 230, 255)

    def draw(self):
        mouse = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse) else self.bg_color

        pygame.draw.rect(self.win, color, self.rect, border_radius=6)
        text_surface = self.font.render(self.text, True, self.text_color)
        self.win.blit(text_surface, (self.rect.x + 12, self.rect.y + 8))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)