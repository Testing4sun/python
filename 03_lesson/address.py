class Address:
    index = '450000'
    city = 'Ufa'
    street = 'Mira'
    building = '1'
    apartment = '11'

    def __init__(self, index, city, street, building, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment

    def __str__(self):
        return (f'{self.index}, {self.city}, {self.street}, '
                f'{self.building} - {self.apartment}')
