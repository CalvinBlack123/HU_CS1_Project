import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick
from powerup import Powerup
 
pygame.init()
 
BLACK = (0,0,0)
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
PINK1 = (239,62,91)
PINK2 = (242,98,121)
PINK3 = (246,143,160)
 


def main():

    background = pygame.image.load('neon-background--wallpaper.jpg')

    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Brick Breaker")
 
    all_sprites_list = pygame.sprite.Group()
    
    paddle = Paddle(RED, 100, 10)
    paddle.rect.x = 350
    paddle.rect.y = 560
    
    ball = Ball(WHITE,10,10)
    ball.rect.x = 345
    ball.rect.y = 195


    all_bricks = pygame.sprite.Group()
    for i in range(8):
        brick = Brick(PINK1,70,30)
        brick.rect.x = 30 + i* 100
        brick.rect.y = 60
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(7):
        brick = Brick(PINK2,70,30)
        brick.rect.x = 60 + i* 100
        brick.rect.y = 100
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    for i in range(6):
        brick = Brick(PINK3,70,30)
        brick.rect.x = 90 + i* 100
        brick.rect.y = 140
        all_sprites_list.add(brick)
        all_bricks.add(brick)

    powerup = Powerup(WHITE, 50, 50)
    powerup.rect.x = 100
    powerup.rect.y = 100

    powerup_group=pygame.sprite.Group()
    powerup_group.add(powerup)
    
    all_sprites_list.add(paddle)
    all_sprites_list.add(ball)

    bulletSound = pygame.mixer.Sound('Game_bullet.wav')

    music = pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1)

    score = 0
    lives = 3
    game_started = True
    ball_start = False
    
    clock = pygame.time.Clock()

    powerup_count = 0

    while game_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                game_started = False 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            paddle.moveLeft(10)
        if keys[pygame.K_d]:
            paddle.moveRight(10)
    
        all_sprites_list.update()

        if ball.rect.x>=790:
            ball.velocity[0] = -ball.velocity[0]
            bulletSound.play()
        if ball.rect.x<=0:
            ball.velocity[0] = -ball.velocity[0]
            bulletSound.play()
        if ball.rect.y>590:
            lives -= 1
            ball.rect.x = 345
            ball.rect.y = 195
            ball.velocity = [0,0]
            
        keys_pressed = pygame.key.get_pressed()
        if lives == 0:
                
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                screen.blit(text, (250,300))
                pygame.display.flip()
                pygame.time.wait(3000)
                game_started = False

        elif keys_pressed[pygame.K_SPACE] and ball.velocity == [0,0]:
            ball.velocity = [5,5]
                
        if ball.rect.y<40:
            ball.velocity[1] = -ball.velocity[1]
            

        if pygame.sprite.collide_mask(ball, paddle):
            ball.velocity[0] = ball.velocity[0]
            ball.velocity[1] = -ball.velocity[1]
            bulletSound.play()

        brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
        for brick in brick_collision_list:
            ball.velocity[0] = ball.velocity[0]
            ball.velocity[1] = -ball.velocity[1]

            score += 1
            powerup_count +=1
            brick.kill()
            bulletSound.play()
            if len(all_bricks)==0:

                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, WHITE)
                screen.blit(text, (200,300))
                pygame.display.flip()
                pygame.time.wait(3000)

                game_started=False

        screen.blit(background, (0,0))
        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(score), 1, WHITE)
        screen.blit(text, (20,10))
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (650,10))
        all_sprites_list.draw(screen)
        #if powerup_count == 5:

                #powerup_group.draw(screen)

        pygame.display.flip()

        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()