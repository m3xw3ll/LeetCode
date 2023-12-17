# [Design a Food Rating System](https://leetcode.com/problems/design-a-food-rating-system/description/?envType=daily-question&envId=2023-12-17)

Design a food rating system that can do the following:

- Modify the rating of a food item listed in the system.
- Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:

- FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
    - foods[i] is the name of the ith food,
    - cuisines[i] is the type of cuisine of the ith food, and
    - ratings[i] is the initial rating of the ith food.
- void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

Example 1:
```
Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".
```
Solution
```python
from sortedcontainers import SortedList
import collections

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings={}
        self.cuisine={}
        self.by_cuisine=collections.defaultdict(lambda:SortedList())
        for food,cuisine,rating in zip(foods,cuisines,ratings):
            self.cuisine[food]=cuisine
            self.ratings[food]=rating
            self.by_cuisine[self.cuisine[food]].add((-rating,food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        prevRating = -self.ratings[food]
        self.ratings[food] = newRating
        self.by_cuisine[self.cuisine[food]].remove((prevRating, food))
        self.by_cuisine[self.cuisine[food]].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.by_cuisine[cuisine][0][1]


if __name__ == '__main__':
    fr = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                    ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                    [9, 12, 8, 15, 14, 7])
    print(fr.highestRated('korean'))
    print(fr.highestRated('japanese'))
    print(fr.changeRating('sushi', 16))
    print(fr.highestRated('japanese'))
    print(fr.changeRating('ramen', 16))
    print(fr.highestRated('japanese'))
```