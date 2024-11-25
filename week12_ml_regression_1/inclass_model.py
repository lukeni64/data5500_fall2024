def my_ml_model(x,y):
    #logic
    if x < 50 and y < 500:
        color = "r"
    if x < 50 and y > 500:
        color = 'g'
    if x > 50 and y < 500:
        color = 'b'
    if x > 50 and y > 500:
        color = 'p'
    return color

print(my_ml_model(51,501))