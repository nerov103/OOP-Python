class Car():
    name = ""
    color = ""

    def start():
        print("Starting the engine")

Car.name = "Promio"
Car.color = "White"

print("name of Car", Car.name)
print("Color", Car.color)

Car.start()

print(dir(Car))



