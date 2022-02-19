import pygame
from Ball import BallBehavior

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

    # "A.I"
    def move_opponent(self):
        if BallBehavior.ball_x > self.screen.get_width() / 2:
            if BallBehavior.ball_y > OpponentBehavior.opponent_y:
                if BallBehavior.ball_x < self.screen.get_width() * .75 and BallBehavior.ball_y > self.screen.get_height() * .75 and OpponentBehavior.opponent_y < self.screen.get_height() * .5:
                    OpponentBehavior.opponent_y += BallBehavior.opponent_speed * 1.75
                if BallBehavior.ball_x > self.screen.get_width() * .8 and abs(BallBehavior.ball_y - OpponentBehavior.opponent_y) > self.screen.get_height() * .05:
                    OpponentBehavior.opponent_y += BallBehavior.opponent_speed * 1.75
                elif BallBehavior.ball_x < self.screen.get_width() * .75:
                    OpponentBehavior.opponent_y += BallBehavior.opponent_speed * .8
                else:
                    OpponentBehavior.opponent_y += BallBehavior.opponent_speed
            elif BallBehavior.ball_y < OpponentBehavior.opponent_y:
                if BallBehavior.ball_x < self.screen.get_width() * .75 and BallBehavior.ball_y < self.screen.get_height() * .25 and OpponentBehavior.opponent_y > self.screen.get_height() * .5:
                    OpponentBehavior.opponent_y -= BallBehavior.opponent_speed * 1.75
                if BallBehavior.ball_x > self.screen.get_width() * .8 and abs(BallBehavior.ball_y - OpponentBehavior.opponent_y) > self.screen.get_height() * .05:
                    OpponentBehavior.opponent_y -= BallBehavior.opponent_speed * 1.75
                elif BallBehavior.ball_x < self.screen.get_width() * .75:
                    OpponentBehavior.opponent_y -= BallBehavior.opponent_speed * .8
                else:
                    OpponentBehavior.opponent_y -= BallBehavior.opponent_speed
        elif BallBehavior.ball_x < self.screen.get_width() * .33:
            if BallBehavior.ball_y > OpponentBehavior.opponent_y:
                OpponentBehavior.opponent_y += BallBehavior.opponent_speed
            elif BallBehavior.ball_y < OpponentBehavior.opponent_y:
                OpponentBehavior.opponent_y -= BallBehavior.opponent_speed



