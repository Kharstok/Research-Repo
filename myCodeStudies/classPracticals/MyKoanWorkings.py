#
#  This file is to show my working on difficult tasks within Pytohn Koans

# QUESTIONS FOR ROMAN
# What does the {0:.{1}f} portion of this code mean?
def test_any_python_expression_may_be_interpolated(self):
    import math

    decimal_places = 4
    string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
        decimal_places)
    self.assertEqual(__, string)



# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_strings.py
# ------------------

# line 31
# def test_use_single_quotes_to_create_string_with_double_quotes(self):
#     string = 'He said, "Go Away."'
#     self.assertEqual(True, string)
string = 'He said, "Go Away."'
print (type(string))
print (type(string) == str)
# it returns as expected <class 'str'> 
# so im unsure why it wont accept me saying True.. 
# It also wont accept false or any reasonable answer i put in
# ive left it commented out and will address later so that I can carry on

# line 45
string = "It was the best of times,\n\
It was the worst of times."
print(len(string))
# I had thought either 50 starting at 0 or 40 excluding spaces.
# Its 52 so i think it must be including the quotation marks
print(string)
# nope doesnt print the quotation marks so either it starts at 1 and a \n\ counts as 1 character or it starts at 0 and \n\ counts as 2 characters

# line 52
string = """
Howdy,
world!
"""
print(len(string))
print(string)
# Ive no idea why its 15 unless its starting at 0 and inlcuding the additional quotes as characters but not the border quotes
# OHHHH never mind ive got it, its asking that whats typed out is equal to the content of string 

# line 95
# Last question
# Got it, so /n is 1 character which means line 45 does = 52 because it starts at 1 and the /n/ equals 1
# I still dont under stand line 52, ill ask about this.


# -------------------------------------------------------------------------------------------------------------------------------------------------
# about_none.py
# ------------------

# line 29
try:
    None.some_method_none_does_not_know_about()
except Exception as ex:
        ex2 = ex
# This doesnt return anything for me to be able to answer the question, it doesnt return anything at all.

# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_lists.py
# ------------------

# line 37
# had an issue understanding this one. 
# as i understand it now its slicing lists.
# slicing returns a new list from another list
# Lst[ Initial : End : IndexJump ]
def test_slicing_lists(self):
    noms = ['peanut', 'butter', 'and', 'jelly']

    self.assertEqual(['peanut'], noms[0:1])
    self.assertEqual(['peanut', 'butter'], noms[0:2])
    self.assertEqual([], noms[2:2])
    self.assertEqual(['and', 'jelly'], noms[2:20])
# these ones are empty because the intial (4 or 5) does not a contain a value in the list (which has values in position 0-3 only)
    self.assertEqual([], noms[4:0])
    self.assertEqual([], noms[4:100])
    self.assertEqual([], noms[5:0])

# line 60
# initially thought that the final part as in the '2' in 'list(range(0, 8, 2))' was an index jump but it looks like its a multiplyer / in multiples of
def test_ranges_with_steps(self):
    self.assertEqual([5, 4], list(range(5, 3, -1)))
    #self.assertEqual([2, 3, 4, 5, 6, 7], list(range(0, 8, 2)))
    self.assertEqual([0, 2, 4, 6], list(range(0, 8, 2)))
    #self.assertEqual([3, 6], list(range(1, 8, 3)))
    # or perhaps a plus+
    # no i realise in typing that its a 'step'
    self.assertEqual([1, 4, 7], list(range(1, 8, 3)))
    self.assertEqual([5, 1, -3], list(range(5, -7, -4)))
    self.assertEqual(__, list(range(5, -8, -4)))

# Line 108
# the rest was pretty straight forward, it mentioned at the end of the page that popping from the left was inefficient, use collections.deque instead ill look that up.
# [deques](https://docs.python.org/3/library/collections.html#collections.deque) is an object from the 'collections' library in python. Optimized for queue based lists involving fixed lengths and edge appendement/popping

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Side Note: Pretty happy with myself, Ive gone through ListAssignments and Dictionaries unscathed
# about_string_manipulation.py
# ------------------

# Line 20
# the square root of 5 is 2.23606 which is now in position [0]
# so if its like lists 0:.{1}anything just means the first one is the only 'pulled' value, ild still like to know what it means though
def test_any_python_expression_may_be_interpolated(self):
    import math

    decimal_places = 4
    string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
        decimal_places)
    self.assertEqual("The square root of 5 is 2.2361", string)

# ord() returns the unicode number
def test_single_characters_can_be_represented_by_integers(self):
    self.assertEqual(97, ord('a'))
    self.assertEqual(__, ord('b') == (ord('a') + 1))