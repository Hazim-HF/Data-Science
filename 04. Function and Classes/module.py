# %%
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

# %%
def make_pizza(size, *toppings): 
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:") 
    for topping in toppings: 
        print("- " + topping) 



# %%
