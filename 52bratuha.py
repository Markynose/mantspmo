result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a is less than b")
        if b > 100:
            raise IndexError("b is greater than 100")
        return a/b
    except Exception as e:
        print(f"Error in divider function: {type(e).__name__} - {e}")
        raise

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    try:
        
        res = divider(key, data[key])
        result.append(res)
    except ValueError as e:
        print(f"ValueError caught: {e}")
    except IndexError as e:
        print(f"IndexError caught: {e}")
    except TypeError as e:
        print(f"TypeError caught: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__} - {e}")

print("Final result:", result)