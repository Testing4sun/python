class Smartphone:

    brand = 'Samsung'
    model = 'Galaxy'
    number = '+79...'

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number
        print("Телефон: ", self.brand, "-", self.model, ".", self.number)
