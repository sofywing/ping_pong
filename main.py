from pygame import*
init()

W = 800
H = 500

window = display.set_mode((W, H))
bg = transform.scale(image.load('bg.jpg'), (W, H)) #трансформуємо розміри картинки під вікно

clock = time.Clock() #лічильник кадрів


class GameSprite(sprite.Sprite): #базовий клас для всіх спрайтів
    def __init__(self, img, x, y, width, height, speed_x, speed_y): #конструктор класу
        super().__init__() 
        self.image = transform.scale(image.load(img), (width, height)) 
        self.rect = self.image.get_rect() #автоматичне створення хітбокса
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.width = width
        self.height = height
    
    def draw(self): #метод малювання картинки
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite): #клас для гравців
    keys_pressed = key.get_pressed() #змінна списку натиснутих кнопок

    def update_l(self): #управління лівого гравця
        keys_pressed = key.get_pressed() #змінна списку натиснутих кнопок
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < H - self.height:
            self.rect.y += self.speed_y

    def update_r(self): #управління правого гравця
        keys_pressed = key.get_pressed() #змінна списку натиснутих кнопок
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < H - self.height:
            self.rect.y += self.speed_y


class Ball(GameSprite):
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y
    


player1 = Player('rk1.png', 5, 5, 150, 150, 10, 10)
player2 = Player('rk1.png', 650, 250, 150, 150, 10, 10)
ball = Ball('mg.png', W/2, H/2, 70, 70, 5, 5)
game = True
while game:
    window.blit(bg, (0, 0))
    player1.draw()
    player2.draw()

    player1.update_l()
    player2.update_r()

    ball.draw()
    ball.move()

    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        ball.speed_x *= -1

    if ball.rect.y < 0 or ball.rect.y > H - ball.height:
        ball.speed_y *= -1


    clock.tick(100)
    display.update()
