#
#  This file is to show my working on difficult tasks within Pytohn Koans

# TEST AREAS
# about_control_statements.py LINE 47
#       test global variables like i, where i equals etc
# about_lists.py LINE 37
#       test that new variables made from sliced lists still are a copy and not removing the items into the new list 
# indivudial
#       test 'type' for bracketed lists
# about_sets.py
#       cheat sheet for arithmatic operators
# about_iterations.py LINE 93
#       test how the result function works with multiple arguments

# LONGER PROBLEM AREAS (SOLVED = ##)
## about_control_statements.py LINE 36
## how does it get 3628800??
# about_exception.py

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
# SOLVED I miunderstood the input, it wanted literally what the string was

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
# SOLVED went back to this, managed to retireve error message the way i did in the tuples.py

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

# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_tuples.py
# ------------------

# Line 11
# Just a test to retrieve error message
count_of_three = (1, 2, 5)
try:
    count_of_three[2] = "three"
except TypeError as ex:
    msg = ex.args[0]
print(msg)
msg = "'tuple' object does not support item assignment"

# Line 24
# Not sure about '.asserRaises' and what it wants as an 'exception' 
def test_tuples_are_immutable_so_appending_is_not_possible(self):
    count_of_three =  (1, 2, 5)
    with self.assertRaises(__): count_of_three.append("boom")
# I didnt expect that an 'exception' is a representation of an error as an object. It makes sense I already knew you could capture an error message in a variable but hadnt clicked. We can also check if something == 'error message' or if it returns true.

# Line 39
# Took a second to get this. Tuples of one really do look weird
def test_tuples_of_one_look_peculiar(self):
    self.assertEqual(int, (1).__class__)
    self.assertEqual(tuple, (1,).__class__)
    self.assertEqual(tuple, ("I'm a tuple",).__class__)
    self.assertEqual(str, ("Not a tuple").__class__)

# Line 48
# Took a second to input (), just a matter of remembering what each bracket represents.
def test_creating_empty_tuples(self):
    self.assertEqual((), ())
    self.assertEqual((), tuple())

# Line 52
# Im gonna put this down as a warm-up for the morning, I should have known the correct layout
def test_tuples_can_be_embedded(self):
    lat = (37, 14, 6, 'N')
    lon = (115, 48, 40, 'W')
    place = ('Area 51', lat, lon)
    #self.assertEqual(('Area 51', 37, 14, 6, 'N', 115, 48, 40, 'W'), place)
    self.assertEqual(('Area 51',(37, 14, 6, 'N'),(115, 48, 40, 'W')), place)

# Line 56
# I got this one but just thought it was particularly cool how the list has several nested tuples and how certain values were retreived
def test_tuples_are_good_for_representing_records(self):
    locations = [
        ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
        ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
    ]

    locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )

    self.assertEqual("Cthulu", locations[2][0])
    self.assertEqual(15.56, locations[0][1][2])

# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_methods.py
# ------------------

#---------

# Line 10
# Rather long code with some area I dont understand. original code comments noted with ##
def my_global_function(a,b):
    return a + b

# class AboutMethods(Koan):
#     def test_calling_a_global_function(self):
#         # Is 5 as indicated in 'my_global_function' above
#         self.assertEqual(__, my_global_function(2,3))

#     ## NOTE: Wrong number of arguments is not a SYNTAX error, but a
#     ## runtime error.
#     def test_calling_functions_with_wrong_number_of_arguments(self):
#         try:
#             my_global_function()
#         except TypeError as exception:
#             msg = exception.args[0]

#         ## Note, the text comparison works for Python 3.2
#         ## It has changed in the past and may change in the future
#         self.assertRegex(msg,
#             r'my_global_function\(\) missing 2 required positional arguments')

#         try:
#             my_global_function(1, 2, 3)
#         except Exception as e:
#             msg = e.args[0]

#         ## Note, watch out for parenthesis. They need slashes in front!
#         self.assertRegex(msg, __)
#         print(msg)

# try:
#     my_global_function(1, 2, 3)
# except Exception as e:
#     msg = e.args[0]

## Note, watch out for parenthesis. They need slashes in front!
# self.assertRegex(msg, __)
# print(msg)
# msg = "'tuple' object does not support item assignment, my_global_function() takes 2 positional arguments but 3 were given" # over two lines seperated by ','
#         # Note, watch out for parenthesis. They need slashes in front!
# msg = 'my_global_function\(\) takes 2 positional arguments but 3 were given'

#--------

# Line 129
# Didnt quite understand this, testing something out
def method_with_documentation(self):
    "A string placed at the beginning of a function is used for documentation"
    return "ok"

def test_the_documentation_can_be_viewed_with_the_doc_method(self):
    self.assertRegex(self.method_with_documentation.__doc__, "A string placed at the beginning of a function is used for documentation")\

print(method_with_documentation.__doc__)
# Pretty cool, didnt expect that.
#  __doc__ is a built in attribute containing the value/information of the string placed at the beginning of a function


# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_control_statements.py
# ------------------

# Line 30
# The terminal says this should end up with result = 362880..
# I have no idea why that would be the answer.
# Have messaged Roman
def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1

i = 1
result = 1
while i <= 10:
    result = result * i
    i += 1

print(result)
# SOLVED: before Roman messaged back too. Its while so it repeats until i is greater than 10

# Line 54
# wasnt sure what % was as an operator, it returns the remainder from a division.
# which means all items in the list are the numbers that had a decimal or a remainder
# if it didnt have a remainder (remainder == 0) then it would 'continue'
# continue is a keyword that similar to break, it skips the code that follows if conditions are met but continues with the loop
def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0: continue
            result.append(i)
        self.assertEqual([1], result)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_sets.py
# ------------------

# Line 28
# I dont really understand the questions here
def test_creating_sets_using_strings(self):
    self.assertEqual(__, {'12345'})
    self.assertEqual(__, set('12345'))

print({'12345'})
print(set('12345'))
print(set('12345'))
print(sorted(set('12345')))

# Line 36
# Had to google this one, pretty interesting, should add to 'cheat sheet'
def test_set_have_arithmetic_operators(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        self.assertEqual(__, scotsmen - warriors)
        self.assertEqual(__, scotsmen | warriors)
        self.assertEqual(__, scotsmen & warriors)
        self.assertEqual(__, scotsmen ^ warriors)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_triangles.py / triangle.py
# Own code written
# ------------------
# im not sure that im answering this as intended but ill give it a go.
# WOO im pretty happy with this, didnt have any issues writing this except initially i mixed up the numbering
# initially had sideLengths == 3.. then equilateral but no because there would only be 1 side that made it into uniqueSides
# I may actually still have some of the wording misleading but the idea is correct

def triangle(a, b, c):
    sides = [a, b, c]
    uniqueSides = []
    sideLengths = []


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

# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_exceptions.py
# ------------------

# Had trouble with the start of this section and had to use the hints in terminal, I understand what its trying to explain but I dont entirely understand how it work since so many new methods were added like MRO.
# I was surprised that I couldnt find anything on what MRO is doing that was relevant to this section.. perhaps ive entirely misunderstood.
# Definitely an area ill need to work on.
#---------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_triangles2.py / triangle.py
# Own code written
# ------------------
def triangle(a, b, c):
    sides = [a, b, c]
    uniqueSides = []
    sideLengths = []

    if min(sides) <= 0:
        raise TriangleError #Present in actual .py file
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

# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_iteration.py 
# ------------------

# Line 93
def test_reduce_will_blow_your_mind(self):
        import functools
        # As of Python 3 reduce() has been demoted from a builtin function
        # to the functools module.

        result = functools.reduce(self.add, [2, 3, 4])
        self.assertEqual(int, result.__class__)
        # Reduce() syntax is same as Python 2
        ## -- Reduce(self.add, ..) has added together the contents of the list giving us 9

        self.assertEqual(9, result)

        result2 = functools.reduce(self.multiply, [2, 3, 4], 1)
        self.assertEqual(24, result2)
        ## -- Reduce(self.multiply, .., ..) has multiplied the list values in order (2 x 3 x 4 = 24)
        ## -- The 1 at the end im not sure what its doing, im wondering if its declaring how many results we want? reducing it down to one integer. Ill add this to the test pile.

        # Extra Credit:
        # Describe in your own words what reduce does.
        ## -- Description above --

# --------------------------------------------------------------------------------------------------------------------------------------------------
# about_comprehension.py 
# ------------------

# Line 44
# all possible combinations are added to the comprehension list a little similar to a dictionary
# initially i had expected the answer would be 2 
def test_double_list_comprehension(self):
    list_of_eggs = ['poached egg', 'fried egg']
    list_of_meats = ['lite spam', 'ham spam', 'fried spam']


    comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]


    self.assertEqual("poached egg and lite spam", comprehension[0])
    self.assertEqual(6, len(comprehension))