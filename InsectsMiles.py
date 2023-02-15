import InsectClass as ic

def main():

    housefly = ic.Insect('housefly',2,4)
    mosquito = ic.Insect('mosquito',2,4)

    housefly.flight_time()
    mosquito.flight_time()

    print(f"A {mosquito.get_name()} will fly {mosquito.get_miles()} miles.")
    print(f"A {housefly.get_name()} will fly {housefly.get_miles()} miles.")


main()