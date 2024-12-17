# Pilar OOP


# 1. Encapsulation (Enkapsulasi)

# Encapsulation adalah proses membungkus data dan metode (fungsi) dalam satu kesatuan yang disebut class. Data di dalam class hanya dapat diakses melalui fungsi-fungsi tertentu, bukan secara langsung dari luar class.

    # Tujuan: Melindungi data agar tidak dapat diakses atau diubah secara langsung.
    # Implementasi di Python:
        # Menggunakan modifier akses seperti _protected atau __private:
            # Public: Dapat diakses dari mana saja.
            # Protected: Diindikasikan dengan satu underscore _. Hanya boleh diakses oleh subclass atau dalam lingkup tertentu.
            # Private: Diindikasikan dengan dua underscore __. Hanya dapat diakses dari dalam class.
            
        
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self._bank_code = "1234"    # Protected attribute
        self.__balance = balance    # Private attribute

    def get_balance(self):
        return self.__balance  # Accessing private data through a method

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")

# Mengakses atribut dan metode
account = BankAccount("Malik", 1000)
print(account.owner)         # Public (Bisa diakses langsung)

print(account.get_balance()) # Private (Diakses lewat method)
print(account.deposit(10))
print(account.get_balance())

print(account._bank_code) # Protected atribut bisa di akses tanpa method
# print(account.__balance) # Private tidak bisa diakses dengan memanggil atributnya saja




print('\n',13*' </line> ','\n')



# 2. Abstraction (Abstraksi)

# Abstraction adalah proses menyembunyikan detail implementasi yang kompleks dan hanya menampilkan fungsionalitas utama kepada pengguna. Dalam Python, abstraksi dilakukan menggunakan class abstrak dengan bantuan modul abc (abstract base class).

    # Tujuan: Mengurangi kompleksitas kode dan memberikan kerangka kerja yang jelas.
    # Implementasi di Python:
        # Menggunakan decorator @abstractmethod.
        # Membuat class abstrak yang tidak bisa diinstansiasi langsung.
    
    
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # Error! Tidak bisa membuat instance dari class abstrak
rect = Rectangle(4, 5)
print(rect.area())        # Output: 20
print(rect.perimeter())   # Output: 18





print('\n',13*' </line> ','\n')





# 3. Inheritance (Pewarisan)

# Inheritance adalah mekanisme di mana sebuah class (child class) mewarisi atribut dan metode dari class lain (parent class). Python mendukung single inheritance dan multiple inheritance.

    # Tujuan: Mengurangi duplikasi kode dan memungkinkan pemakaian ulang (reuse).
    # Implementasi di Python:
        # Mendeklarasikan class child dengan menempatkan parent sebagai parameter.
    


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print(f"Car brand: {self.brand}, model: {self.model}")

car = Car("Toyota", "Corolla")
car.start()      # Output: Toyota is starting...
car.display()    # Output: Car brand: Toyota, model: Corolla






print('\n',13*' </line> ','\n')





# 4. Polymorphism (Polimorfisme)

# Polymorphism adalah kemampuan untuk menggunakan metode yang sama pada objek yang berbeda. Dalam Python, polimorfisme dapat dilakukan melalui:

    # Method Overriding: Subclass mendefinisikan ulang metode dari superclass.

    # Method Overloading (Simulasi): Fungsi yang fleksibel menerima parameter berbeda.

    # Tujuan: Mempermudah penyesuaian perilaku metode tanpa mengubah struktur dasar class.

    # Implementasi di Python:

        # Membuat metode dengan nama sama di class child (Overriding).
        
        
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow!
