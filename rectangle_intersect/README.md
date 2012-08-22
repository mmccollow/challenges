#Rectangle intersection

###Excerpt from: [http://www.reddit.com/r/dailyprogrammer/comments/y26pr/8102012_challenge_87_easy_rectangle_intersection/](http://www.reddit.com/r/dailyprogrammer/comments/y26pr/8102012_challenge_87_easy_rectangle_intersection/)

Write a function that calculates the intersection of two rectangles, returning either a new rectangle or some kind of null value.

You're free to represent these rectangles in any way you want: tuples of numbers, class objects, new datatypes, anything goes. For this challenge, you'll probably want to represent your rectangles as the x and y values of the top-left and bottom-right points. (Rect(3, 3, 10, 10) would be a rectangle from (3, 3) (top-left) to (10, 10) (bottom-right).)

As an example, rectIntersection(Rect(3, 3, 10 10), Rect(6, 6, 12, 12)) would return Rect(6, 6, 10, 10), while rectIntersection(Rect(4, 4, 5, 5), Rect(6, 6, 10 10)) would return null.