from livewires import games, color
import random

games.init(screen_width = 800, screen_height = 800, fps = 50)
games.music.load("bonus.mp3")
game = True
    
class Buton(games.Sprite):
    image = games.load_image("button.png")
    def __init__(self):
        super(Buton, self).__init__(image = Buton.image,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2)
    def update(self):
        if games.mouse.is_pressed(0):
            granie()
            self.destroy()
                                    

class Jamnik(games.Sprite):
    image = games.load_image("jam200.png")


    def __init__(self):
        #używam funkcji super aby zapewnić sobie wywołanie metody init
        #nastepnie definiuję atrybut score- obiekt klasy Text
        super(Jamnik, self).__init__(image = Jamnik.image,
                                     x=games.mouse.x,
                                     bottom = games.screen.height)

        self.score = games.Text(value = 0, size=50, color=color.black,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        #sprawdza czy jamnik nie wyszedł za rozmiary ekranu i ustawia
        #zmiana pozycji na wyznaczoną przez pozycję x myszy
        
        self.x = games.mouse.x

        if self.left <0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.zlap()

    
    def zlap(self):
    #metoda ta sprawdza czy jamnik złapał już jakies kurczaki
        for kur in self.overlapping_sprites:
            self.score.value +=10
            self.score.right = games.screen.width -10
            kur.zderzenie()
   #dla każdego obiektu kótry zachodzi na jamnika, metoda zwieksza liczbe punktow
   # o 10. potem obiecuje ze prawy brzeg obiektu klasy Text teprezenujacego
   #wynik jest zawsze oddalona o 10 pikseli od prawej krawedzi ekranu, bez wzgledu na ilosc cyfr
   


class Kur(games.Sprite):

    image = games.load_image("chicken.png")
    speed=3

    def __init__(self, x, y = 90):
        super(Kur,self).__init__(image = Kur.image, x = x,y = y, dy = Kur.speed)

    #sprawdzam czy obiekt nie dotarł do granicy ekranu
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
        game = False
        
       
            
class Murzyn(games.Sprite):
    
    image = games.load_image("murzynka.png")

    def __init__(self, y = 180, speed = 5, zmiana_ruch = 2000):
        
        super(Murzyn, self).__init__(image = Murzyn.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = speed)
        
        self.zmiana_ruch = zmiana_ruch
        self.time_til_drop = 10 #po jakim czasie zrzuca kure

    
    def update(self):
        
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.zmiana_ruch) == 0:
           self.dx = -self.dx
                
        self.tworz()


    def tworz(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 0.5
        else:
            new_kur = Kur(x = self.x)
            games.screen.add(new_kur)

            # ustaw margines na mniej więcej 30% wysokości kury, niezależnie od prędkości kury   
            self.time_til_drop = int(new_kur.height * 1.3 / Kur.speed) + 1      
 
def granie():
    
    the_murzyn = Murzyn()
    games.screen.add(the_murzyn)

    the_jamnik = Jamnik()
    games.screen.add(the_jamnik)
    games.mouse.is_visible = False

    games.screen.event_grab = False


    
    
def main():

    # ładuję obraz do pamięci operacyjnej aby utworzyć obiekt obrazu następnie
    #funkcja load_image ładuje obraz przechowywany w pliku .png i przypisuje
    #powstały obiekt obrazu do zmiennej wall_image 
    wall_image = games.load_image("800tlo.png", transparent = False)
    games.screen.background = wall_image
    
    
    start = Buton()
    games.screen.add(start)

        


    games.music.play(-1)    
    games.screen.mainloop()
    
    


    
main()

