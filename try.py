def arg_split(arg):
    try:
        param, value = arg.split("=")
    except ValueError:
        return
    if value[0] == "\"":
        value = value[1:len(value) - 1]
    elif "." in value:
        try:
            value = float(value)
        except ValueError:
            return
    else:
        value = int(value)
    print(param)
    print(value)

arg_split("a=\"aster\"")
arg_split("b=12.3")
arg_split("c=-04")
