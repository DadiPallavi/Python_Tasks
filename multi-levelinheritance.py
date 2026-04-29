# Grand Parent Class
class Camera:
    camera_mp = "64 MP"

    def take_photo(self):
        print("Taking Photo...")


# Parent Class
class MusicPlayer(Camera):
    brand = "Sony"

    def play_music(self):
        print("Playing Music...")


# Child Class
class SmartPhone(MusicPlayer):
    model_name = "Samsung Galaxy"

    def show_details(self):
        print("Model Name:", self.model_name)
        print("Camera:", self.camera_mp)
        print("Music Brand:", self.brand)
        super().play_music()
        super().take_photo()


# Object 1
p1 = SmartPhone()


p1.show_details()
