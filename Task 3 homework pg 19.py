
def convertkilometersintomiles(mil):
    pass


def price_of_trip(mil, costpermile):
  #  ppmile = 15
    return costpermile*mil


cost = 15
kil = float(input("entre the distance in kilometers "))
miles = round(1.61*kil, 2)
print("your distance in miles is", miles)
print("the cost of the trip is ", price_of_trip(miles, cost))

