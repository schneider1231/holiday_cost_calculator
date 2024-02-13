def plane_cost(city_flight):
    """
    Calculates the cost of the flight depending on the location
    """
    # holiday locations and daily cost
    destinations = { 
       "london":1000, 
       "tokyo":800,
       "new york":600,
       "paris":250,
    }

    if city_flight in destinations:
        cost = destinations[city_flight]         
    return cost   


def hotel_cost(num_nights):
    """
    Calculates the total cost of the hotel with the rate of 70 per night
    """
    cost = 70 * num_nights
    return cost      


def car_rental(rental_days):
    """
    Calculates the total cost of the rental car with the rate of 50 per day
    """
    car_cost = 50 * rental_days
    return car_cost


def holiday_cost(hotel_cost,plane_cost,car_rental):
    """
    Calculates the total cost of the holiday by adding up all the costs
    """
    total = hotel_cost + plane_cost + car_rental
    return total


def main():
    """
    Gets an input from the user for the different locations, nights to be stayed 
    and car rental days then calls the functions to calculate the total costs 
    and returns the prices
    """
    locations = ["london", "tokyo", "new york", "paris"]
    print(f"destinations: {locations}")
    city = input("Choose your destination: ").lower()

    while city not in locations:
        print("incorrect entry")
        city = input("Choose your destination: ").lower()

    while True:    
        try:
            nights = int(input("How many nights you will be staying: "))
            break
        except:
            print("Enter a number pls")   

    while True:    
        try:
            rent_days = int(input("How many days you will rent a car: "))
            break
        except:
            print("Enter a number pls")   
    

    hotel_total = hotel_cost(nights)
    flight_total = plane_cost(city)
    car_total = car_rental(rent_days)
    holiday_total = holiday_cost(hotel_total, flight_total, car_total)

    print(f"\nThe total cost of staying in the hotel for {nights} nights is: £{hotel_total}")
    print(f"The flight to {city} is: £{flight_total}")
    print(f"The total cost  of the car rental for {rent_days} days is: £{car_total}")
    print(f"the total cost for the holiday is £{holiday_total}")


main()