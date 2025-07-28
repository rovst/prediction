from data import data

def average():
    if not data:
        return 0
    a = data[-1]  # last submitted list of ints
    avg = sum(a) / len(a)
    print("Average:", avg)
    return avg
