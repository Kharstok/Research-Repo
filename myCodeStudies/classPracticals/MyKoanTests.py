# TEST AREAS
# about_control_statements.py LINE 47
#       test global variables 
# about_lists.py LINE 37
#       test that new variables made from sliced lists still are a copy and not removing the items into the new list 
# indivudial
#       test 'type' for bracketed lists




#---------------------------------------------------------------
# Test One

print("\n \n---------------------------------------------")
print("Test 1 - Global vs Local Variables \nExpected Result: 4, 44, 4, 55, 55\n")
i = str(4)
print(i)

def test_function_variables_are_local(i):
    i += 4
    print(i)
    
test_function_variables_are_local(40)

print(i)

def test_global_statement():
    global i 
    i = 55
    print(i)

test_global_statement()
print(i)
print("\n---------------------------------------------")

#-------------------------------------------------------------------
#Test Two

print("Test 2 - Sliced lists remain the same \nExpected Result: \nnoms:  ['peanut', 'butter', 'and', 'jelly'] \nslice: ['butter', 'and']\n")

def test_slicing_lists_are_not_destructive():
    global noms
    noms = ['peanut', 'butter', 'and', 'jelly']

    global slicenoms
    slicenoms = noms[1:3]
 

test_slicing_lists_are_not_destructive()
print(f"Actual Result: \nnoms:  {noms} \nslice: {slicenoms}")
print("\n \n---------------------------------------------")

#-----------------------------------------------------
# Test Three

# - These can all be described as 'Arrays'
# - List [0, 0, 1, 'two'] Ordered, Changeable, Allows Duplicates
# - Set {0, 1, 'two'} Unordered, Unchangeable, No Duplicates
# - Tuple (0, 0, 1, 'two') Ordered, Unchangeable, Allows Duplicates
# - Dictionary {1: "one", 2: "two"} Ordered, Changeable, No Duplicates

print("Test 3 - Array types\n")
list_test = [0, 0, 1, 'two']
set_test = {0, 1, 'two'}
tuple_test = (0, 0, 1, 'two')
dictionary_test = {1: "one", 2: "two"}

print(f'{list_test} is type {type(list_test)}\n')
print(f'{set_test} is type {type(set_test)}\n')
print(f'{tuple_test} is type {type(tuple_test)}\n')
print(f'{dictionary_test} is type {type(dictionary_test)}')
print("\n \n---------------------------------------------")

#-----------------------------------------------------

