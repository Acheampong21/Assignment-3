'COMPUTER APPLICATION ASSIGNMENT'
'INDEX NUMBER: 6949921 CIVIL 2'
'NAME: YEBOAH ACHEAMPONG DENNIS'
"""
@author: Dennis Da Vinci-DD
"""

# Define the dictionary of available cars and their prices
cars = {
    'Toyota Corolla': 30000,
    'Honda Civic': 25000,
    'Ford Mustang': 40000,
    'Chevrolet Camaro': 45000,
    'Nissan Altima': 28000,
    'BMW 3 Series': 50000,
    'Audi A4': 55000,
    'Mercedes-Benz C-Class': 60000,
    'Lexus ES': 45000,
    'Hyundai Sonata': 27000,
    'Kia Optima': 26000,
    'Mazda3': 28000,
    'Subaru Impreza': 29000,
    'Volkswagen Golf': 30000,
    'Volvo S60': 55000,
    'Tesla Model 3': 50000,
    'Porsche 911': 100000,
    'Ferrari 458 Italia': 300000,
    'Lamborghini Aventador': 500000,
    'Bugatti Chiron': 3000000,
    'Maserati GranTurismo': 150000,
    'Aston Martin Vantage': 200000,
    'McLaren 720S': 300000,
    'Lotus Evora': 80000,
    'Alfa Romeo Giulia': 40000,
    'Jaguar F-Type': 70000,
    'Land Rover Range Rover Sport': 90000,
    'Jeep Wrangler': 35000,
    'GMC Sierra': 45000,
    'Ram 1500': 40000
}


# Ask the user for their car brand
car_brand = input("Enter your car brand: ")

# Check if the car brand is in the dictionary
if car_brand in cars:
    print("Yes, the car is available.")
    print(f"The price of {car_brand} is ${cars[car_brand]:,}.")
else:
    print("Sorry, the car is not available.")
