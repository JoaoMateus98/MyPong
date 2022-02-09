import pygame
import random
import Score
from Score import ScoreTracker


def move_ball(go_to):
    if go_to == "go_top_left":
        BallBehavior.ball_x -= 50
        BallBehavior.ball_y -= 50
    if go_to == "go_top_right":
        BallBehavior.ball_x += 50
        BallBehavior.ball_y -= 50
    if go_to == "go_bottom_left":
        BallBehavior.ball_x -= 50
        BallBehavior.ball_y += 50
    if go_to == "go_bottom_right":
        BallBehavior.ball_x += 50
        BallBehavior.ball_y += 50


class BallBehavior:
    score = Score

    WHITE = (255, 255, 255)

    ball_x = None
    ball_y = None

    # go_to top/bottom right/left
    go_to = ""

    rand_pos = None

    def __init__(self, screen):
        self.circle = None
        self.screen = screen
        BallBehavior.ball_x = self.screen.get_width() / 2
        BallBehavior.ball_y = self.screen.get_height() / 2
        self.radius = 10
        self.velocity = 17
        self.screen_top = self.screen.get_height() / 10
        self.screen_bottom = self.screen.get_height() - 12
        self.new_round = True
        self.player_rect = None
        self.opponent_rect = None

    def draw_ball(self, player_rect, opponent_rect):
        score_tracker = ScoreTracker(self.screen)
        score_tracker.draw_to_screen()
        self.player_rect = player_rect
        self.opponent_rect = opponent_rect

        print("player pos = ", BallBehavior.ball_y, "top = ", self.screen_top, "bottom =", self.screen_bottom)

        ball_rect = pygame.draw.circle(self.screen, BallBehavior.WHITE, (BallBehavior.ball_x, BallBehavior.ball_y),
                                       self.radius)

        # call random initial path
        if self.new_round:
            BallBehavior.start_ball(self)

        # check next ball path
        if ball_rect.colliderect(
                opponent_rect) and BallBehavior.go_to == "go_top_right" or BallBehavior.ball_y > self.screen_bottom and BallBehavior.go_to == "go_bottom_left":
            BallBehavior.go_to = "go_top_left"
        if ball_rect.colliderect(
                opponent_rect) and BallBehavior.go_to == "go_bottom_right" or BallBehavior.ball_y < self.screen_top and BallBehavior.go_to == "go_top_left":
            BallBehavior.go_to = "go_bottom_left"
        if ball_rect.colliderect(
                player_rect) and BallBehavior.go_to == "go_top_left" or BallBehavior.ball_y > self.screen_bottom and BallBehavior.go_to == "go_bottom_right":
            BallBehavior.go_to = "go_top_right"
        if ball_rect.colliderect(
                player_rect) and BallBehavior.go_to == "go_bottom_left" or BallBehavior.ball_y < self.screen_top and BallBehavior.go_to == "go_top_right":
            BallBehavior.go_to = "go_bottom_right"

        # call movement function
        if BallBehavior.go_to == "go_top_left":
            move_ball("go_top_left")
        if BallBehavior.go_to == "go_top_right":
            move_ball("go_top_right")
        if BallBehavior.go_to == "go_bottom_left":
            move_ball("go_bottom_left")
        if BallBehavior.go_to == "go_bottom_right":
            move_ball("go_bottom_right")

        BallBehavior.restart(self)

    # give ball's initial trajectory
    def start_ball(self):
        self.new_round = False
        rand_pos = random.randint(1, 4)
        if rand_pos == 1:
            BallBehavior.go_to = "go_top_left"
        if rand_pos == 2:
            BallBehavior.go_to = "go_top_right"
        if rand_pos == 3:
            BallBehavior.go_to = "go_bottom_left"
        if rand_pos == 4:
            BallBehavior.go_to = "go_bottom_right"

    def restart(self):
        # opponent scored
        if BallBehavior.ball_x < 0:
            BallBehavior.score.update_opponent_score()
            self.new_round = True

        # player scored
        if BallBehavior.ball_x > self.screen.get_width():
            BallBehavior.score.update_player_score()
            self.new_round = True

        if self.new_round:
            BallBehavior.__init__(self, self.screen)
