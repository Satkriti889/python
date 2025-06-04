class Battery:
    def __init__(self,model,battery_level):
        self.__model = model
        self.__battery_level = battery_level
        print(f"The model of your phone is {self.__model}.")

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
            return
c1=Battery("Samsung",50)
c1.charge()
c1.charging(30)
c1.use(70)