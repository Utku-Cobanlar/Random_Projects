print("Hello, welcome to Tile World")
while True:
    try:
        wid = float(input("Enter width(in meters): "))
        heig = float(input("Enter height(in meters): "))
        cost = float(input("Enter the cost of a square meter of tiles: "))
        def cost_square(wid,heig,cost):
            x = wid*heig*cost
            return round(x,2)
    except:
        print("Enter a digit.")
    else:
        break

print("Total cost is " + str(cost_square(wid,heig,cost)) + "$")