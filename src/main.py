def main():
    print("Welcome to the Band Name Generator!")
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    band_name = city + " " + pet
    print(f"Your band name could be: {band_name}")

if __name__ == "__main__":
    main()