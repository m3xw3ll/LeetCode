from sortedcontainers import SortedList
import collections


class FoodRating:
    def __init__(self, foods, cuisines, ratings):
        self.ratings={}
        self.cuisine={}
        self.by_cuisine=collections.defaultdict(lambda:SortedList())
        for food,cuisine,rating in zip(foods,cuisines,ratings):
            self.cuisine[food]=cuisine
            self.ratings[food]=rating
            self.by_cuisine[self.cuisine[food]].add((-rating,food))

    def change_rating(self, food, new_rating):
        prevRating = -self.ratings[food]
        self.ratings[food] = new_rating
        self.by_cuisine[self.cuisine[food]].remove((prevRating, food))
        self.by_cuisine[self.cuisine[food]].add((-new_rating, food))

    def highest_rating(self, cuisine):
        return self.by_cuisine[cuisine][0][1]


if __name__ == '__main__':
    fr = FoodRating(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                    ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                    [9, 12, 8, 15, 14, 7])
    print(fr.highest_rating('korean'))
    print(fr.highest_rating('japanese'))
    print(fr.change_rating('sushi', 16))
    print(fr.highest_rating('japanese'))
    print(fr.change_rating('ramen', 16))
    print(fr.highest_rating('japanese'))