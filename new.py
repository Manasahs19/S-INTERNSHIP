class User:
    def __new__(cls, name):
        print("Object is being created")
    def __init__(self, name):
        self.name=name
        print("Object is initialized")
user = User("Manasa")
