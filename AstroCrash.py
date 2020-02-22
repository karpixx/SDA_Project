#Odczytaj klawisz
#Demonstruje odczytywanie klawiatury

from superwires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)
missile_sound = games.load_sound("poziom.wav")
games.music.load("temat.mid")

choice = None
while choice != "0":
    print(
    """
    Dźwięk i muzyka
    
    0 - zakończ
    1 - odtwórz dźwięk pocisku
    2 - odtwarzaj cyklicznie dźwięk pocisku
    3 - zatrzymaj odtwarzanie dźwięku pocisku
    4 - odtwórz temat muzyczny
    5 - odtwarzaj cyklicznie temat muzyczny
    6 - zatrzymaj odtwarzanie tematu muzycznego
    """
    )
    choice = input("Wybieram: ")
    print()

    if choice == "0":
        print("Żegnaj!")
    elif choice == "1":
        missile_sound.play()
        print("Odtworzenie dźwięku pocisku")
    elif choice == "2":
        loop = int(input("Ile razy powtórzyć odtwarzanie? (-1 = bez końca): "))
        missile_sound.play(loop)
        print("Cykliczne odtwarzanie dźwięku pocisku")
    elif choice == "3":
        missile_sound.stop()
        print("Zatrzymanie odtwarzania dźwięku pocisku")
    elif choice == "4":
        games.music.play()
        print("Odtworzenie tematu muzycznego.")
    elif choice == "5":
        games.music.play()
        loop = int(input("Ile razy powtórzyc odtwarzanie? (-1 = bez końca): "))
        print("Odtworzenie cykliczne tematu muzycznego")
    elif choice == "6":
        games.music.stop()
        print("Zatrzymanie odtwarzania tematu muzycznego")
    # nieprzewidziany wybór
    else:
        print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")


class Ship(games.Sprite):
    """Poruszający się statek kosmiczny"""
    def update(self):
        """Kierowanie ruchem statku na podstawie wciśniętych klawiszy"""
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1
        """Obracanie statku w pożądanym kierunku na podstawie wciśniętych klawiszy"""
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1
        """Obracanie statku natychmiast, o określoną ilość stopni"""
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

def main():
    nebula_image = games.load_image("mglawica.jpg", transparent = 0)
    games.screen.background = nebula_image

    ship_image = games.load_image("statek.bmp")
    the_ship = Ship(image = ship_image,
                    x = games.screen.width/2,
                    y = games.screen.height/2)
    games.screen.add(the_ship)

    explosion_files = ["eksplozja1.bmp",
                       "eksplozja2.bmp",
                       "eksplozja3.bmp",
                       "eksplozja4.bmp",
                       "eksplozja5.bmp",
                       "eksplozja6.bmp",
                       "eksplozja7.bmp",
                       "eksplozja8.bmp",
                       "eksplozja9.bmp"]
    explosion = games.Animation(images = explosion_files,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                n_repeats = 0,
                                repeat_interval = 5)
    games.screen.add(explosion)

    games.screen.mainloop()

main()