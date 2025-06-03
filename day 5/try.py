
class Dog:
    try:
        dog= Dog()
        dog.sleep()
        print("sucessfully instantiate the claa dog")
    except TypeError as e:
        print(f"Error:{e}")
