import pygame

pygame.joystick.init()

class PlayerBehavior:
    WHITE = (255, 255, 255)
    player_y = None
    player_rect = None

    def __init__(self, screen):
        self.player_rect = None
        self.screen = screen
        self.velocity = 17
        PlayerBehavior.player_y = screen.get_height() / 2
        self.player_x = screen.get_width() * .05
        self.player_width = screen.get_width() / 100
        self.player_height = screen.get_height() / 15

    def draw_to_screen(self):
        self.player_rect = pygame.rect.Rect(self.player_x, PlayerBehavior.player_y, self.player_width, self.player_height)
        PlayerBehavior.player_rect = self.player_rect
        pygame.draw.rect(self.screen, PlayerBehavior.WHITE, self.player_rect)

    def move_player(self):
        joystick_count = pygame.joystick.get_count()
        if joystick_count >= 1:
            joystick = pygame.joystick.Joystick(0)
            hat = joystick.get_hat(0)
            if hat == (0, 1) and PlayerBehavior.player_y > self.screen.get_height() / 10:
                PlayerBehavior.player_y -= self.velocity
            if hat == (0, -1) and PlayerBehavior.player_y < self.screen.get_height() - (self.screen.get_height() / 15 + 25):
                PlayerBehavior.player_y += self.velocity

        keys = pygame.key.get_pressed()
        print(keys)
        if keys[pygame.K_UP] and PlayerBehavior.player_y > self.screen.get_height() / 10:
            PlayerBehavior.player_y -= self.velocity
        if keys[pygame.K_DOWN] and PlayerBehavior.player_y < self.screen.get_height() - (self.screen.get_height() / 15 + 25):
            PlayerBehavior.player_y += self.velocity
