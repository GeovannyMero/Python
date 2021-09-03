def temp_convet(var):
    try:
        return int(var)
    except ValueError:
        print("erro")

temp_convet("2")