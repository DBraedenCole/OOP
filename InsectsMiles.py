import InsectClass as ic

def main():

    house_fly = ic.Insect()
    house_fly.flight_time()
    
    mosquito = ic.Insect()
    mosquito.flight_time()

    print(f"\nA housefly will fly {house_fly.get_flight_time()} miles.")
    print(f"A mosquito will fly {mosquito.get_flight_time()} miles.\n")


main()