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

yugo.drive()
# => "VROOOOOOOOOOOOM!"

Car.all
# => [<__main__.Car object at 0x1049247c0>, <__main__.Car object at 0x1049247c8>, <__main__.Car object at 0x1049247d6>]

# BONUS:

Car.brake()
# => "SCREEEECH!"

volvo_lightning = Car(make="Volvo", model="Lightning")

volvo_lightning.make
# => "Volvo"
volvo_lightning.model
# => "Lightning"
