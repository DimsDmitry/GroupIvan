from pygame import *

class GameSprite(sprite.Sprite):
    '''класс-родитель для других классов'''
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        '''конструктор класса'''
        super().__init__()

        '''каждый спрайт хранит свойство изображения - image'''
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        '''каждый спрайт хранит свойство rect - прямоугольник, в который он вписан'''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        '''метод для отрисовки платформы'''
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    '''класс-наследник для платформы'''
    def move_right(self):
        '''движение платформы справа'''
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 5:
            self.rect.y += self.speed

    def move_left(self):
        '''движение платформы слева'''
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 5:
            self.rect.y += self.speed


#игровая сцена
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

back = (200, 255, 255)
window.fill(back)

#создание спрайтов игры
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('ИГРОК 1 ПРОИГРАЛ', True, (149, 0, 0))
lose2 = font.render('ИГРОК 2 ПРОИГРАЛ', True, (149, 0, 0))

#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)
        racket1.move_left()
        racket2.move_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1

        #если мяч достигает границ экрана, меняем направление его движения
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)