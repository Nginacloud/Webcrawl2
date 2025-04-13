class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f"{self.brand} {self.model} is powered on.")

class Smartphone(Device):
    def __init__(self, brand, model, storage, cameramegapixels):
        super().__init__(brand, model)
        self.storage = storage
        self.cameramegapixels = cameramegapixels

    def take_photo(self):
        print(f"taking a photo with{self.cameramegapixels}MP camera.")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.brand} {self.model}.")

phone1 = Smartphone("Samsung", "S24", "256GB", 12)
phone2 = Smartphone("Apple", "iPhone 14", "128GB", 12)

phone1.power_on()
phone1.take_photo()
phone2.install_app("Instagram")