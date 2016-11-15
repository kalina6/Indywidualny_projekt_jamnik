import random

games.init(screen_width = 1000, screen_height = 900, fps = 50)

class Jamnik(games.Sprite):
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.sprawdz_kolizje()

    def sprawdz_kolizje(self):
        for kur in self.overlapping_sprites:
            kur.handle_collide()



class Kur(games.Sprite):
    def handle_collide(self):
        self.x = random.randrange(games.screen.width)
        self.y=random.randrange(games.screen.height)


            

    
def main():
    wall_image = games.load_image("domi.png", transparent = False)
    games.screen.background = wall_image

    jamnik_image = games.load_image("jam.png")
    ten_jamnik = Jamnik(image = jamnik_image,
                        x=games.mouse.x,
                        y=games.mouse.y)
    games.screen.add(ten_jamnik)
     
    kurczak_image = games.load_image("ki4.png")
    kurczak_x = random.randrange(games.screen.width)
    kurczak_y = random.randrange(games.screen.height)
    ten_kurczak = Kur(image = kurczak_image,
                           x=games.mouse.x,
                           y=games.mouse.y)
    games.screen.add(ten_kurczak)

    games.mouse.is_visible = False
    games.screen.event_grab = True
        
    games.screen.mainloop()
#score=games.Text( value = 400, size = 80, color=color.yellow, x= 900, y=30)
#games.screen.add(score)

#wygrales=games.Message ( value="WYGRAŁEŚ!",
#                         size = 200,
#                         color = color.red,
#                        x=games.screen.width/2,
#                         y=games.screen.height/2,
#                         lifetime=300,
#                         after_death = games.screen.quit)
#games.screen.add(wygrales)


main()
