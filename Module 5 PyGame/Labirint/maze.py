#создай игру "Лабиринт"!
import time

from pygame import *

'''игровая сцена'''

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Догонялки')

background = transform.scale(image.load('background.jpg'), (win_width, win_height))


class GameSprite(sprite.Sprite):
    '''класс-родитель для спрайтов'''

    def __init__(self, player_image, player_x, player_y, player_speed):
        '''конструктор класса'''
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    '''класс-наследник для спрайта-игрока (управляется стрелками)'''
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 5:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 5:
            self.rect.y += self.speed


class Enemy(GameSprite):
    '''класс-наследник для спрайта-киборга (перемещается сам)'''
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 620:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        '''картинка стены - прямоугольник'''
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        '''каждый спрайт - прямоугольник rect'''
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



'''персонажи игры'''

player = Player('hero.png', 5, 420, 4)
monster = Enemy('cyborg.png', 620, 280, 2)
final = GameSprite('treasure.png', 580, 420, 0)

w1 = Wall(171, 225, 46, 100, 20, 450, 10)
w2 = Wall(171, 225, 46, 100, 480, 365, 10)
w3 = Wall(171, 225, 46, 100, 20, 10, 370)
# w4 = Wall(171, 225, 46, 50, 480, 365, 10)
# w5 = Wall(171, 225, 46, 50, 480, 365, 10)


'''музыка'''
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


'''игровой цикл'''
game = True
finish = False
clock = time.Clock()
FPS = 60

'''шрифт'''
font.init()
font = font.Font(None, 70)
win = font.render('ПОБЕДА', True, (255, 212, 1))
lose = font.render('ПОРАЖЕНИЕ', True, (187, 0, 1))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if not finish:
        window.blit(background, (0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        # w4.draw_wall()
        # w5.draw_wall()

        '''проигрыш'''
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()

        '''выигрыш'''
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()


    display.update()
    clock.tick(FPS)

