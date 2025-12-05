# Session 8 Problem 2 Car.py

# define the object
class Car:
    """ A class representing a car with make, model, sticker price, and discount price. """
    def __init__(self, make, model, sticker_price, discount_price):
        self.make = make      # e.g., Audi
        self.model = model    # e.g., A4
        self.sticker_price = sticker_price  # e.g., 40000.00
        self.discount_price = discount_price  # e.g., 36000.00

    def discounted_price(self):
        """Calculate and return the discounted price of the car."""
        return self.sticker_price * 0.9  # 10% discount
        
    def __str__(self):
         """Provide a string representation of the car details."""
         return (f"{self.make} {self.model}, " 
                 f"Sticker Price: ${self.sticker_price:.2f}, "
                 f"Discount Price: ${self.discounted_price():.2f}")
                 
        
class Sport(Car):
    """ A class respresenting a sports car that inherits from Car."""
    
    def __init__(self, make, model, sticker_price, discount_price): # Add discount_price parameter
        super().__init__(make, model, sticker_price, discount_price)  # Pass discount_price to the parent class

        # Initialize options for sports features
        self.sports_wheels = 'No'
        self.sports_engine = 'No'
        self.sport_interior = 'No'
    
    def set_sports_wheels(self, options):
        """Set sports wheels option."""
        self.sports_wheels = options.upper()

    def set_sports_engine(self, options):
        """Set sports engine option."""
        self.sports_engine = options.upper()

    def set_sport_interior(self, options):
        """Set sport interior option."""
        self.sport_interior = options.upper()

    def updated_price(self):
        """Calculate the total updated price based on selected options."""
        total_price = self.discounted_price()
        updated_price = total_price
        if self.sports_wheels == 'YES':
            updated_price += 1000.00
        if self.sports_engine == 'YES':
            updated_price += 3000.00
        if self.sport_interior == 'YES':
            updated_price += 2000.00
            
        return updated_price
    
    def price_with_options(self):
        """Display the updated price with options."""
        return (f"{self.make} {self.model}, "
                F"Sticker Price: ${self.sticker_price:.2f}, "
                f"Discont Price: ${self.sticker_price:.2f}, "
                f"Sports Wheels: {self.sports_wheels}, "
                f"Sports Engine: {self.sports_engine}, "
                f"Sport Interior: {self.sport_interior}, "
                f"{self.updated_price():.2f}")
    
# Main program to demonstrate the Car and Sport classes
def main():
    # Instantiate a Sport car object with a discount price
    my_sport_car = Sport("Audi", "A4", 40000.00, 36000.00)  # Add discount_price here

    # Display the initial car details
    print(my_sport_car)
    
    # Set options to 'Yes' 
    my_sport_car.set_sports_wheels('Yes')  # Include sports wheels
    my_sport_car.set_sports_engine('Yes')  # Include sports engine
    my_sport_car.set_sport_interior('Yes')  # Include sport interior    
    
    # Display the price with options
    print("\nAfter adding options:")
    print(my_sport_car) 
    
if __name__ == "__main__":
    main()
        

       