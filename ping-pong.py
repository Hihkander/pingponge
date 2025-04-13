from pygame import*
class GameSprite(sprite.Sprite): #Основной класс спрайта
    def __init__(self, player_image, player_x, player_y, player_speed, size_x=65, size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
 
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_width - 80:
            self.rect.x += self.speed
 
class Player(GameSprite): # Класс для врага
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

window = display.set_mode((700, 700))
window.set_caption(55)
FPS = 60
game = True
finish = False
while game:
 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background, (0,0))
        
 
    display.update()
    clock.tick(FPS)
