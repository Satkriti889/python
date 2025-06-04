class Battery:
    def __init__(self):
        model=input("Enter the model : ")
        self.model = model
        self.__battery_level = 80
        print(f"The model of your phone is {self.model}.")

    def charge(self):
        print(f"Your phone has {self.__battery_level}% charge.")

    def charging(self,charged):
        if charged>0:
            self.__battery_level+=charged
            print(self.__battery_level)
        else:
            print("The charge needs to be positive.")
        
    def use(self,usedcharge):
        if usedcharge>0:
            self.__battery_level-=usedcharge
            print(self.__battery_level)
        else:
            print("The number should be positive.")
        
        if self.__battery_level<20:
            print("Power saving mode turned on")

        else:
            return " "

def take_input():
    c1=Battery()

    charged=int(input("Enter the charged charge: "))
    c1.charging(charged)
    usedcharge=int(input("Enter the used charge: "))
    c1.use(usedcharge)

take_input()