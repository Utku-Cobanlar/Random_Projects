import random
n = int(input("Enter the amount of flips you want to simulate: "))
out_list = ["Heads", "Tails"]
result = []
heads = 0
tails = 0
for a in range(1,n+1):
    x = random.choice(out_list)
    result = result + [x]
    if str(x) == "Heads":
        heads += 1
    else:
        tails += 1
print("Number of heads is {}".format(heads))
print("Number of tails is {}".format(tails))
print(result)