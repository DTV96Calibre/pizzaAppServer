NUM_TOPPINGS = 3

class Pizza:
    name = "New Pizza"
    size = 1
    toppings = [True for i in range(NUM_TOPPINGS)]
    crust = 1

    def toJSON(self):
        json = "{\n  \"pizza\": {\n    \"size\": " + str(self.size) +\
                ",\n    \"crust\": " + str(self.crust) +\
                ",\n    \"name\": \"" + self.name +"\""\
                ",\n    \"toppings\": ["
        for i in range(len(self.toppings)):
            json += "\n      " + str(self.toppings[i]).lower()
            if (i < len(self.toppings)-1):
                json += ","
        json += "\n    ]\n  }\n}"
        return json

def test():
    pizza = Pizza()
    print(pizza.toJSON())

test()
