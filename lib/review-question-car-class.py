# Finish the implementation of the Car class so it has the functionality described below


class Car:
    pass


volvo_lightning = Car("Volvo", "Lightning")
yugo = Car("Zastava", "Yugo")
lada = Car("AvtoVAZ", "Lada")

volvo_lightning.make
# => "Volvo"
volvo_lightning.model
# => "Lightning"

yugo.drive
# => "VROOOOOOOOOOOOM!"

Car.all
# => [#<Car:0x00007fae28930f20>, #<Car:0x00007fae28923370>, #<Car:0x00007fae2891ae78>]

# BONUS:

Car.brake
# => "SCREEEECH!"

volvo_lightning = Car(make="Volvo", model="Lightning")

volvo_lightning.make
# => "Volvo"
volvo_lightning.model
# => "Lightning"
