import json as JSON
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

    def fromJSON(self, json): # json is a json formatted string
        parsedObject = JSON.loads(json) # JSON is a library
        # print(parsedObject)
        attributeDict = parsedObject["pizza"]
        self.name = attributeDict["name"]
        self.size = attributeDict["size"]
        self.toppings = attributeDict["toppings"]
        self.crust = attributeDict["crust"]




def test():
    pizza = Pizza()
    pizza.size = 100
    pizza.name = "Success"
    pizza.toppings = [True, False, True]
    pizza.crust = 50
    pizzaJSON = pizza.toJSON()
    #print(pizzaJSON)
    pizzaB = Pizza()
    pizzaB.fromJSON(pizzaJSON)
    pizzaBJSON = pizzaB.toJSON()
    #print(pizzaBJSON)
    #if (pizzaJSON == pizzaBJSON):
    #    #print("Success")
    #else:
     #   print("Pizza toJSON fromJSON test failed!")

    assert (pizzaJSON == pizzaBJSON) , ("Pizza toJSON fromJSON test failed!")



test()
