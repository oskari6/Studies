from collections import Counter

class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        counter = Counter(my_list)
        most_common = counter.most_common(1)
        return most_common[0][0] if most_common else None
    
    @classmethod
    def doubles(cls, my_list: list):
        seen = set()
        duplicates = set()
        for item in my_list:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        return len(duplicates)
    
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))