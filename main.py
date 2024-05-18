from bicycle import Bicycle
from customer import Customer
from rental_shop import RentalShop

def main():
    # Create a rental shop
    shop = RentalShop("Happy Wheels Bike Shop")
    
    # Create some bicycles
    bike1 = Bicycle("Trek", "Marlin 5")
    bike2 = Bicycle("Giant", "Talon 3")

    # Add bicycles to the shop's inventory
    shop.add_bicycle(bike1)
    shop.add_bicycle(bike2)

    # Create a customer
    alice = Customer("Alice")

    # Customer rents a bike
    print(shop.rent_bicycle(alice, bike1))

    # Customer returns a bike
    print(shop.return_bicycle(alice, bike1))

if __name__ == "__main__":
    main()
