#Создай собственный Шутер!
from pygame import *
from random import randint
from time import time as timer


'''создаём окно'''
win_width = 700
win_height = 500
display.set_caption('Космическая битва')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))


score = 0 #сбито кораблей
lost = 0 #пропущено кораблей
max_lost = 3 #макс. допустимое число пропущенных кораблей
goal = 10 #количество кораблей, которое нужно сбить для победы
life = 3 #очки жизни


'''классы'''
class GameSprite(sprite.Sprite):
    '''класс-родитель для других классов'''
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        '''конструктор класса'''
        sprite.Sprite.__init__(self)

        '''каждый спрайт хранит свойство изображения - image'''
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        '''каждый спрайт хранит свойство rect - прямоугольник, в который он вписан'''
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        '''метод для отрисовки героя'''
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    '''класс главного игрока'''
    def update(self):
        '''метод для управления игроком'''
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        '''стрельба'''
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    '''класс спрайта-врага'''
    def update(self):
        self.rect.y += self.speed
        global lost
        ''''исчезает, если дойдёт до края экрана'''
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1


class AsteroidEnemy(GameSprite):
    '''класс астероидов'''
    def update(self):
        self.rect.y += self.speed
        ''''исчезает, если дойдёт до края экрана'''
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0


class Bullet(GameSprite):
    '''класс спрайта-пули'''
    def update(self):
        '''движение пули'''
        self.rect.y += self.speed
        '''пуля исчезает, если дойдёт до края экрана'''
        if self.rect.y < 0:
            self.kill()


'''игровые спрайты'''
ship = Player('rocket.png', 5, win_height - 100, 80, 100, 10)


monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()

'''астероиды'''
asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = AsteroidEnemy('asteroid.png', randint(30, win_width - 30), -40, 80, 50, randint(1, 7))
    asteroids.add(asteroid)


'''фоновая музыка'''
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

'''шрифты и надписи'''
font.init()
font1 = font.SysFont('Arial', 80)
font2 = font.SysFont('Arial', 36)
win = font1.render('ПОБЕДА', True, (255, 255, 255))
lose = font1.render('ПОРАЖЕНИЕ', True, (194, 0, 0))

'''игровой цикл'''
finish = False #переменная, отвечающая за работу спрайтов в игре
run = True #флаг цикла


rel_time = False #проверяет, идёт ли перезарядка
num_fire = 0 #переменная для подсчёта выстрелов

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if not rel_time and num_fire < 5:
                    num_fire += 1
                    fire_sound.play()
                    ship.fire()
                if num_fire >= 5 and not rel_time:
                    '''если игрок сделал 5 выстрелов'''
                    last_time = timer()
                    rel_time = True

    if not finish:
        '''обновляем фон'''
        window.blit(background, (0, 0))

        '''пишем текст на экране'''
        text = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text, (10, 50))


        '''подключаем движение спрайтов'''
        ship.update()
        monsters.update()
        bullets.update()
        asteroids.update()

        '''отображаем спрайты'''
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)

        '''перезарядка'''
        if rel_time:
            now_time = timer()

            if now_time - last_time < 3:
                '''пока не прошло 3 секунды - выводим информацию о перезарядке'''
                reload = font2.render('Идёт перезарядка...', 1, (170, 0, 0))
                window.blit(reload, (260, 460))
            else:
                '''если прошло 3 сек - обнуляем счётчик пуль и сбрасываем флаг перезарядки'''
                num_fire = 0
                rel_time = False


        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            '''этот цикл повторится столько раз, сколько монстров подбито'''
            score += 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)


        '''если спрайт коснулся врага - уменьшается жизнь'''
        if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteroids, False):
            sprite.spritecollide(ship, monsters, True)
            sprite.spritecollide(ship, asteroids, True)
            life -= 1


        '''проигрыш'''
        if life == 0 or lost >= max_lost:
            finish = True #мы проиграли - стафим фон и больше не управляем спрайтами
            window.blit(lose, (200, 200))


        '''выигрыш - проверка, сколько очков набрали?'''
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))


        '''задаём разный цвет в зависимости от количества жизней'''
        if life == 3:
            life_color = (0, 150, 0)
        if life == 2:
            life_color = (208, 184, 0)
        if life == 1:
            life_color = (170, 0, 0)

        text_life = font1.render(str(life), 1, life_color)
        window.blit(text_life, (650, 10))

        display.update()

    time.delay(50)


