import pygame
import sys

pygame.init()

WIDTH,HEIGHT = 800,600
BALL_RADIUS = 15
PADDLE_WIDTH,PADDLE_HEIGHT = 100,10
BALL_COLOR = (0,255,192)
PADDLE_COLOR = (0,96,255)
BACKGROUND_COLOR = (255,255,255)
FONT_COLOR = (0,0,0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping pong game")

ball_pos = [WIDTH // 2 , HEIGHT // 2 ] 
ball_vel = [3,3]

paddle_pos = [WIDTH // 2 - PADDLE_WIDTH // 2,HEIGHT - PADDLE_HEIGHT - 10]

score = 0

font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and  paddle_pos[0]  > 0:
        paddle_pos[0] -= 5
    if keys[pygame.K_RIGHT] and  paddle_pos[0]  < WIDTH - PADDLE_WIDTH:
        paddle_pos[0] += 5
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        score += 1
    if (paddle_pos[0] < ball_pos[0] < paddle_pos[0] + PADDLE_WIDTH and
            paddle_pos[1] < ball_pos[1] + BALL_RADIUS < paddle_pos[1] + PADDLE_HEIGHT):
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] > HEIGHT:
        print("Game over your score was:", score)
        pygame.quit()
        sys.exit()
    
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    score_text = font.render(f'Score: {score}',True,FONT_COLOR)
    screen.blit(score_text,(10,10))
    pygame.display.flip()
    pygame.time.delay(30)
