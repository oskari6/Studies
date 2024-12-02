def create_tuple(x: int, y: int, z: int):
    sum = x + y + z
    tuple = (min(x, y ,z), max(x, y , z), sum)
    return tuple

    

if __name__ == "__main__":
    tuple = create_tuple(5, 3, -1)
    print(tuple)