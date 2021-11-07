print(" *** Wind classification ***")
wind =  input("Enter wind speed (km/h) : ")
wind = float(wind)
if wind > 0 and wind <= 50.99:
    print("Wind classification is Breeze.")
if wind > 52 and wind <= 55.99:
    print("Wind classification is Depression.")
if wind > 56 and wind <= 101.99:
    print("Wind classification is Tropical Storm.")
if wind >= 102 and wind <= 208.99:
    print("Wind classification is Typhoon.")
if wind >= 209:
    print("Wind classification is Super Typhoon.")
