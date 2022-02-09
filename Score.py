import pygame


def update_player_score():
    ScoreTracker.player_score += 1


def update_opponent_score():
    ScoreTracker.opponent_score += 1


class ScoreTracker:
    WHITE = (255, 255, 255)
    player_score = 0
    opponent_score = 0

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Times New Roman", int(screen.get_height() / 15))
        self.player_score_surface = self.font.render(str(ScoreTracker.player_score), True, ScoreTracker.WHITE)
        self.opponent_score_surface = self.font.render(str(ScoreTracker.opponent_score), True, ScoreTracker.WHITE)

    def draw_to_screen(self):
        self.screen.blit(self.player_score_surface, (self.screen.get_width() / 5, self.screen.get_height() / 50))
        self.screen.blit(self.opponent_score_surface,
                         (self.screen.get_width() / 1.33333, self.screen.get_height() / 50))
