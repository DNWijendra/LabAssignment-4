class RentalShop:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_bicycle(self, bicycle):
        self.inventory.append(bicycle)
        return f"{bicycle.brand} {bicycle.model} added to the inventory."

    def rent_bicycle(self, customer, bicycle):
        if bicycle in self.inventory and not bicycle.is_rented:
            customer.rent_bike(bicycle)
            self.inventory.remove(bicycle)
            return f"{bicycle.brand} {bicycle.model} rented to {customer.name}."
        else:
            return f"{bicycle.brand} {bicycle.model} is not available for rent."

    def return_bicycle(self, customer, bicycle):
        if bicycle in customer.rented_bikes:
            customer.return_bike(bicycle)
            self.inventory.append(bicycle)
            return f"{bicycle.brand} {bicycle.model} returned by {customer.name}."
        else:
            return f"{customer.name} did not rent {bicycle.brand} {bicycle.model} from us."
