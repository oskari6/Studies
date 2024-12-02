class Recording:
    def __init__(self, length):
        if length < 0:
            raise ValueError()
        self.__length = length
    
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length < 0:
            raise ValueError()
        else:
            self.__length = length
    
if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)