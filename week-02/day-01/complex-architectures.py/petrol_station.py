class Station:
  def __init__(self, gas_amount = 10000):
    self.gas_amount = gas_amount
  def refill(self, car, amount):
    self.gas_amount -= amount
    result = car.fill(amount)
    if result > 0:
      self.gas_amount += result
    
      

class Car:
  def __init__(self, gas_amount = 0, capacity = 100):
    self.gas_amount = gas_amount
    self.capacity = capacity

  def fill(self, amount):
    overflow = 0
    if self.gas_amount + amount <= self.capacity:
      self.gas_amount += amount
    else:
      overflow = self.gas_amount + amount - self.capacity
      self.gas_amount = self.capacity
    return overflow


station = Station()
car = Car()

station.refill(car, 10)
print(station.gas_amount)
station.refill(car, 100)
print(station.gas_amount)
station.refill(car, 200)
print(station.gas_amount)


"""
#### Petrol Station
- Create `Station` and `Car` classes
- `Station`
  - gas_amount
  - refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
- `Car`
  - gas_amount
  - capacity
  - create constructor for `Car` where:
    - initialize gas_amount -> 0
    - initialize capacity -> 100
"""