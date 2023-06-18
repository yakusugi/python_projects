a = int(input("What is the vakue of a? "))
b = int(input("What is the vakue of b? "))
x = int(input("What is the vakue of x? "))

def eval_exp(a,b,x):
    exp_eval = a + b * x
    return exp_eval

exp_value = eval_exp(a,b,x)

print(f"The value of expression is {exp_value}")