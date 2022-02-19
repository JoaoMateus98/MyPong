import pygame
import random
import Score
from Score import ScoreTracker
from pygame import mixer

mixer.init()


def change_opponent_speed():
    BallBehavior.opponent_speed = random.randint(9, 11)
    return BallBehavior.opponent_speed


def move_ball(go_to):
    if go_to == "go_top_left":
        BallBehavior.ball_x -= 10
        BallBehavior.ball_y -= 10
    if go_to == "go_top_right":
        BallBehavior.ball_x += 10
        BallBehavior.ball_y -= 10
    if go_to == "go_bottom_left":
        BallBehavior.ball_x -= 10
        BallBehavior.ball_y += 10
    if go_to == "go_bottom_right":
        BallBehavior.ball_x += 10
        BallBehavior.ball_y += 10


class BallBehavior:
    score = Score

    opponent_speed = random.randint(9, 11)

    WHITE = (255, 255, 255)

    ball_x = None
    ball_y = None

    # go_to top/bottom right/left
    go_to = ""

    rand_pos = None

    pong_paddle = mixer.Sound('PongPaddleBounce.wav')
    pong_wall_bounce = mixer.Sound('PongWallBounce.wav')
    score_sound = mixer.Sound('PongScored.wav')
    game_over_sound = mixer.Sound('PongGameOver.wav')

    def __init__(self, screen):
        self.circle = None
        self.screen = screen
        BallBehavior.ball_x = self.screen.get_width() / 2
        BallBehavior.ball_y = self.screen.get_height() / 2
        self.radius = 10
        self.velocity = 17
        self.screen_top = self.screen.get_height() / 10 + 10
        self.screen_bottom = self.screen.get_height() - 12
        self.new_round = True
        self.player_rect = None
        self.opponent_rect = None

    def draw_ball(self, player_rect, opponent_rect):
        score_tracker = ScoreTracker(self.screen)
        score_tracker.draw_to_screen()
        self.player_rect = player_rect
        self.opponent_rect = opponent_rect

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

        # changes opponent speed
        if ball_rect.colliderect(player_rect) or ball_rect.x >= self.screen.get_width() -1 or ball_rect.x <= 1:
            change_opponent_speed()

        # call movement function
        if BallBehavior.go_to == "go_top_left":
            move_ball("go_top_left")
        if BallBehavior.go_to == "go_top_right":
            move_ball("go_top_right")
        if BallBehavior.go_to == "go_bottom_left":
            move_ball("go_bottom_left")
        if BallBehavior.go_to == "go_bottom_right":
            move_ball("go_bottom_right")

        # play sounds
        if ball_rect.colliderect(player_rect) or ball_rect.colliderect(opponent_rect):
            BallBehavior.pong_paddle.play()
        if BallBehavior.ball_y < self.screen_top or BallBehavior.ball_y > self.screen_bottom:
            BallBehavior.pong_wall_bounce.play()

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
            if BallBehavior.score.ScoreTracker.player_score < 15:
                BallBehavior.score_sound.play()
            self.new_round = True

        # player scored
        if BallBehavior.ball_x > self.screen.get_width():
            BallBehavior.score.update_player_score()
            if BallBehavior.score.ScoreTracker.opponent_score < 15:
                BallBehavior.score_sound.play()
            self.new_round = True

        if self.new_round:
            BallBehavior.__init__(self, self.screen)
