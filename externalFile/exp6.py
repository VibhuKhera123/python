def main():
    try:
        with open("file.txt") as f:
            data = f.read()
    except FileNotFoundError as e:
        print("File Not Found")

    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(e)    
    try:
        import my_module
    except ImportError as e:
        print(e)
    try:
        print(geek)
    except NameError as e:
        print(e)
    try:
        int("abc")
    except ValueError as e:
        print(e)
    try:
        list.append()
    except TypeError as e:
        print("TypeS Error")
    

if __name__ == "__main__":
    main()
