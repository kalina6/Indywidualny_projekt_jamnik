from livewires import games, color
import random

games.init(screen_width = 800, screen_height = 800, fps = 50)

class Jamnik(games.Sprite):
    image = games.load_image("jam200.png")


    def __init__(self):
        super(Jamnik, self).__init__(image = Jamnik.image,
                                     x=games.mouse.x,
                                     bottom = games.screen.height)

        self.score = games.Text(value = 0, size=25, color=color.black,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x

        if self.left <0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.zlap()


    def zlap(self):
        for kur in self.overlapping_sprites:
            self.score.value +=10
            self.score.right = games.screen.width -10
            kur.zderzenie()
   



class Kur(games.Sprite):

    image = games.load_image("chicken.png")
    speed=2

    def __init__(self, x, y = 90):
        super(Kur,self).__init__(image = Kur.image, x = x,y = y, dy = Kur.speed)

    def update(self):
        if self.bottom>games.screen.height:
            self.zakoncz_gre()
            self.destroy()

    def zderzenie(self):
        self.destroy()

    def zakoncz_gre(self):
        end_message = games.Message(value = "Koniec gry!",
                                    size =90,
                                    color=color.black,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        
        games.screen.add(end_message)
        
            
class Murzyn(games.Sprite):
    
    image = games.load_image("murzynka.png")

    def __init__(self, y = 180, speed = 5, zmiana_ruch = 2000):
        
        super(Murzyn, self).__init__(image = Murzyn.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = speed)
        
        self.zmiana_ruch = zmiana_ruch
        self.time_til_drop = 2


    def update(self):
        
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.zmiana_ruch) == 0:
           self.dx = -self.dx
                
        self.tworz()


    def tworz(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_kur = Kur(x = self.x)
            games.screen.add(new_kur)

            # ustaw margines na mniej więcej 30% wysokości kury, niezależnie od prędkości kury   
            self.time_til_drop = int(new_kur.height * 1.3 / Kur.speed) + 1      
 
            

    
def main():

   
    wall_image = games.load_image("800tlo.png", transparent = False)
    games.screen.background = wall_image

    the_murzyn = Murzyn()
    games.screen.add(the_murzyn)

    the_jamnik = Jamnik()
    games.screen.add(the_jamnik)
    games.mouse.is_visible = False

    games.screen.event_grab = True


    games.screen.mainloop()
           
    
main()

