from livewires import games

games.init(screen_width = 1000, screen_height = 972, fps = 50)

wall_image = games.load_image("wyj.png", transparent = False)
games.screen.background = wall_image

kurczak_image = games.load_image("kurak2.jpg")
kurak = games.Sprite(image = kurczak_image, x=550, y=400)
games.screen.add(kurak)

games.screen.mainloop()
