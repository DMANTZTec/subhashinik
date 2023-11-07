def pizza(size,*toppings,**details):
    print("pizzaa toppings")
    for topping in toppings:
            print(topping)
    print("orderdetails")
    for key,value in details.items():
          print(f'{key}:{value}')
pizza("large","pepperion","extra chesse","onions","mushrooms",gachibowli='pizzavibes',tip=20)