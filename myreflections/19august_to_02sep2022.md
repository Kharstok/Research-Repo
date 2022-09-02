<!-- keywords -->

# Testings Cool <span style="font-size:15px">\*5 times fast* </span>
Its nearly submission time! in the educational way!
Its been roughly a week since Ive typed a reflection in this format and so I want to cover what ive been doing over the last week or so.


1. Working through Python Koans
2. Exploring the python language
3. Properly formatting markdown files for viewing in Github rather than in VScode
4. Focussing on completing the technical support assignment to a high level as I had a couple areas of difficulty
5. Answering Romans reflection questions

Below ill elaborate on and reflect on these tasks before writing a summary of this assignment.
<br>
<br>
<br>
# Koans <span style="font-size:18px"> "in times of peace"</span>
Roman showed us [Python Koans](https://github.com/gregmalcolm/python_koans) on Github. It reminds me of textbooks in school, lots of questions/equations/code to solve. 

It was a good way to see a range of different operators, methods and built-in functions in python that I may not already be aware of as well as learn additional features of those that I was aware of. 

It was also a good boost to my confidence in writing code and my comprehension of it, particularly the traingle.py parts 1 and 2. Im wondering if, when I complete these koans, I could find somewhere that releases weekly challenges or something for python, it would be a good way to keep my brain 'flexible' and better remember what im learning.

As ive gone through the koans ive kept a file 'myCodeStudies\classPracticals\MyKoanWorkings.py' that has questions,workings and interesting moments ive encountered on the way, Some of these ill explore further below..
<br>
<br>
## Koans Koans <span style="font-size:15px"> "in times of war"</span>
Im particularly proud of the solution I wrote for 'triangle.py' parts one and two, I think its pretty tidy, easy to understand, I dont think i need all three lists.. probably I could just evaluate the number of duplicates directly in 'sides' without having to make additional lists but im happy that I could write this just based off of what I can recall from Robs class in level 4 and the previous activities we have done in Koans and in Romans challenges.

    def triangle(a, b, c):
        sides = [a, b, c]
        uniqueSides = []
        sideLengths = []

        if min(sides) <= 0:
            raise TriangleError #Exception present in actual .py file
        if (a + b + c) <= max(sides) * 2:
            raise TriangleError 
        
        for x in sides:
            if x not in uniqueSides:
                uniqueSides.append(x)
                sideLengths = len(uniqueSides)
        if sideLengths == 1:
            return 'equilateral'
        elif sideLengths == 2:
            return 'isosceles'
        else:
            return 'scalene'

The code below from 'control_statements.py' took me a while \*hah* to grasp. The issue was that I had overlooked 'while' so missed the fact that it was looping.

        def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1
        self.assertEqual(3628800, result)

Besides my 'favourite' and 'longest solve time' koans, the other notable koans have been discussed in the MyKoanWorkin.py mentioned previously.

I also want to note here that '\_\_doc__' is a pretty cool built in attribute that takes a string. Im not sure of a context I might use it in but I will keep it in mind and use it first chance I get. If I write paricularly long code it could be good to call on \_\_doc__ to remind me of what a function method does.
<br>
<br>

## Nobody expects the Python Inquisition!
Ive recorded any questions I have and have written them along with their answers so I can remind myself if ever I forget, Ive also created tests for areas I was unsure of which are found at 'myCodeStudies\classPracticals\MyKoanTests.py'

1. What is the difference between method and function, and attribute?
    - Functions can be called by name without being associate to an object (**independant**) and do not neccesarily have arguments associated to them. This includes in-built functions like max, min, eval ,list, among many others. Built-in function generally do require an argument to be passed.
    - A Method is different to a function in that it is called by its name but is **dependant** on an object of the class the method is associated with. As i understnad it, methods are class specific functions
    - An Attribute is a class specific variable. There are other things to consider like instance attributes and properties but I dont want to dive too deeply at this level of my learning

<br>

2. What bracket is used for what list, set, tuple etc and is there one word to describe all of them?
    - These can all be described as 'Arrays'
    - List [0, 0, 1, 'two'] Ordered, Changeable, Allows Duplicates
    - Set {0, 1, 'two'} Unordered, Unchangeable, No Duplicates
    - Tuple (0, 0, 1, 'two') Ordered, Unchangeable, Allows Duplicates
    - Dictionary {1: "one", 2: "two"} Ordered, Changeable, No Duplicates

<br>
<br>

# Notes
Links and notes going forward for the software project or outside of study.

cool video with spheres planets noise etc
https://www.youtube.com/watch?v=lctXaT9pxA0

and his terraforming one
https://www.youtube.com/watch?v=vTMEdHcKgM4

###### 15/08/22
using pyppi tools i managed to generate an image but when i changed the prompt updated the setting and everything all the images were very similar, im obviously doing something wrong but it was cool to try out. ill try again at somepoint but im too sick and lacking in energy to do a deep dive now

    a lush landscape covered in plant life, a pond is in focus, theres a large container ship floating on the lake

    a lush landscape of rolling hills covered in plant life theres a large metal ship floating on the lake

    a large metal ship floating on the lake

    a large metal ship | floating on a forest | raining cats