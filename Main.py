import pygame
from Opponent import OpponentBehavior
from Player import PlayerBehavior
from Ball import BallBehavior
from Score import ScoreTracker
from pygame import mixer

pygame.init()
mixer.init()

# constants
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VELOCITY = 17

# class instances
player = PlayerBehavior(SCREEN)
opponent = OpponentBehavior(SCREEN)
ball = BallBehavior(SCREEN)
score_tracker = ScoreTracker(SCREEN)

winner = False
running = True

mixer.music.load('PongBackground.wav')
mixer.music.play(-1)
game_over_sound = mixer.Sound('PongGameOver.wav')


# main loop
def main():
    global running
    global winner
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        draw_window()
        if winner:
            pygame.time.delay(5000)
            running = False


def draw_background(mid_screen, line_width):
    line_starts = []
    line_ends = []

    line_init = SCREEN.get_height() / 30
    line_length = line_init
    for starts in range(30):
        line_starts.append(line_length)
        line_length = line_length + line_init

    tracker = 0
    for ends in range(30):
        current_start = line_starts[tracker]
        line_ends.append(current_start + line_init * .5)
        tracker += 1

    for lines in range(30):
        pygame.draw.line(SCREEN, WHITE, (mid_screen, line_starts[lines]), (mid_screen, line_ends[lines]), line_width)


def draw_window():
    # refreshes screen
    SCREEN.fill(BLACK)

    # positions
    mid_screen = SCREEN.get_width() / 2
    line_width = int(SCREEN.get_width() / 100)

    # player handler
    player.move_player()
    player.draw_to_screen()

    # opponent handler
    opponent.move_opponent()
    opponent.draw_to_screen()

    # ball handler
    ball.draw_ball(PlayerBehavior.player_rect, OpponentBehavior.opponent_rect)

    draw_background(mid_screen, line_width)

    check_winner()

    pygame.display.update()


def check_winner():
    global winner

    font = pygame.font.SysFont("5Computers In Love", int(SCREEN.get_height() / 20))
    player_1_wins_surface = font.render("Player 1 Wins!", True, WHITE)
    player_2_wins_surface = font.render("Player 2 Wins!", True, WHITE)

    if ScoreTracker.player_score == 15:
        SCREEN.blit(player_1_wins_surface, (SCREEN.get_width() / 10, SCREEN.get_height() / 3))
        game_over_sound.play()
        winner = True

    if ScoreTracker.opponent_score == 15:
        SCREEN.blit(player_2_wins_surface, (SCREEN.get_width() / 1.9, SCREEN.get_height() / 3))
        game_over_sound.play()
        winner = True


if __name__ == "__main__":
    main()
