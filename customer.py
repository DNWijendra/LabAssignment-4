class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_bikes = []

    def rent_bike(self, bike):
        if not bike.is_rented:
            bike.rent()
            self.rented_bikes.append(bike)
            return f"{self.name} has rented {bike.brand} {bike.model}."
        else:
            return f"{bike.brand} {bike.model} is already rented."

    def return_bike(self, bike):
        if bike in self.rented_bikes:
            bike.return_bike()
            self.rented_bikes.remove(bike)
            return f"{self.name} has returned {bike.brand} {bike.model}."
        else:
            return f"{self.name} did not rent {bike.brand} {bike.model}."