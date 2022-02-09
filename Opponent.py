import pygame


class OpponentBehavior:
    WHITE = (255, 255, 255)
    opponent_y = None
    opponent_rect = None

    def __init__(self, screen):
        self.rect = None
        self.screen = screen
        self.velocity = 17
        OpponentBehavior.opponent_y = screen.get_height() / 2
        self.opponent_x = screen.get_width() * .95
        self.opponent_width = screen.get_width() / 100
        self.opponent_height = screen.get_height() / 15

    def draw_to_screen(self):
        self.opponent_rect = pygame.rect.Rect(self.opponent_x, OpponentBehavior.opponent_y, self.opponent_width, self.opponent_height)
        pygame.draw.rect(self.screen, OpponentBehavior.WHITE, self.opponent_rect)
        OpponentBehavior.opponent_rect = self.opponent_rect

    def move_opponent(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and OpponentBehavior.opponent_y > self.screen.get_height() / 10:
            OpponentBehavior.opponent_y -= self.velocity
        if keys[pygame.K_s] and OpponentBehavior.opponent_y < self.screen.get_height() - (self.screen.get_height() / 15 + 25):
            OpponentBehavior.opponent_y += self.velocity

