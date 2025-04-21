from pygame import *


back = (200, 255, 255)
win_w = 600
win_h = 500
window = display.set_mode((win_w, win_h))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True
finish = True

sprite1 = transform.scale(image.load('wew.png'), (10, 110))
sprite2 = transform.scale(image.load('wew.png'), (10, 110))
ball_img = transform.scale(image.load('s.png'), (20, 20))  

x1 = 10
y1 = 200
x2 = 580
y2 = 200
speed = 10


ball_rect = Rect(win_w // 2, win_h // 2, 20, 20)
speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish != True:
        window.fill(back)
        

        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_UP] and y1 > 5:
            y1 -= speed
        if keys_pressed[K_DOWN] and y1 < win_h - 105:
            y1 += speed
            
        if keys_pressed[K_w] and y2 > 5:
            y2 -= speed
        if keys_pressed[K_s] and y2 < win_h - 105:
            y2 += speed
            

        ball_rect.x += speed_x
        ball_rect.y += speed_y
        
   
        if ball_rect.y > win_h - 20 or ball_rect.y < 0:
            speed_y *= -1
            

        racket1 = Rect(x1, y1, 10, 110)
        racket2 = Rect(x2, y2, 10, 110)
        
        if ball_rect.colliderect(racket1) or ball_rect.colliderect(racket2):
            speed_x *= -1


        if ball_rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball_rect.x > win_w:
            finish = True
            window.blit(lose2, (200, 200))


        window.blit(ball_img, (ball_rect.x, ball_rect.y))
        window.blit(sprite1, (x1, y1))
        window.blit(sprite2, (x2, y2))
    
    display.update()
    clock.tick(FPS)