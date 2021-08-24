foods = ["apples", "bread", "cheese"]

for food in foods:
    if food == "apples":
        print(f"tu tienes que comprar esto {food}")
        break # detiene el bucle for
    print(food)
    

for index in range(1,11):
    print(f"{index} * 5 = {index * 5}")



# while
count = 4
while count <= 10:
    print(count)
    count += 1
