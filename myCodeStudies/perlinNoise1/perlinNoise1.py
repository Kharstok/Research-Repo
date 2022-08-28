#FAAAAR, ive spent an hour or two trying to get this to run on VScode using (https://discourse.processing.org/t/tutorial-running-python-mode-in-vscode/7716?page=2) among other options and several different extensions so I give up.
# SOLVED: To run this code program download 'Processing' and the python extension for processing and open this file from there.





#https://www.youtube.com/watch?v=0emj42Bn-_Y&list=WL&index=3
# This was made by following the above video and seperated into sections to show how the code was at various steps
# Ordered from final iteration to initial iteration


#-----------------------------------------------------------------------------------
#Fifth iteration
#To test uncomment the section below this line only.. 

noise_scale = .02

def setup():
    size(1000, 750)
    
    background(100, 132, 158)
    
    # Generate a value between 0.0 and 1.0
    for x in range(1000):
        for y in range(750):
            n = noise(x * noise_scale, y * noise_scale)
            
            if (n > .5):
                stroke(204, 192, 155)
            if (n > .54):
                stroke(96, 117, 94)
            if (n > .70):
                stroke(150, 150, 150)
                
            if (n > .5):
                point(x, y)
                
#-----------------------------------------------------------------------------------
#Fourth iteration
#noise_scale may change value in each iteration
#If statments added, if n is greater than a certain number than 'stroke' adds a different colour
#To test uncomment the section below this line only.. 

# noise_scale = .02

# def setup():
#     size(1000, 750)
    
#     background(143, 196, 204)
    
#     # Generate a value between 0.0 and 1.0
#     for x in range(1000):
#         for y in range(750):
#             n = noise(x * noise_scale, y * noise_scale)
            
#             if (n > .5):
#                 stroke(204, 192, 155)
#             if (n > .7):
#                 stroke(96, 117, 94)
#             if (n > .85):
#                 stroke(150, 150, 150)
                
#             if (n > .5):
#                 point(x, y)
                
 #-----------------------------------------------------------------------------------
#Third iteration
#Background colour is changed
#Video says " the reason we dont see a fade is because by the time we start colouring we are already above .5 
#To test uncomment the section below this line only.. 

#noise_scale = .002

# def setup():
#     size(1000, 750)
    
#     background(143, 196, 204)
    
#     # Generate a value between 0.0 and 1.0
#     for x in range(1000):
#         for y in range(750):
#             n = noise(x * noise_scale, y * noise_scale)
#             if (n > .5):
#                 stroke(0, 0, 0, 255.0 * noise(x * noise_scale, y * noise_scale))
#                 point(x, y)

#-----------------------------------------------------------------------------------
#Second iteration
#Video describes this as 'zooming in' by adding the variable 'noise_scale' and multiplying the point x and y by that variable
#To test uncomment the section below this line only..    
        
#noise_scale = .02

#def setup():
#     size(1000, 750)

#     background(255, 255, 255)

#     # Generate a value between 0.0 and 1.0
#     for x in range(1000):
#     for y in range(750):
#         stroke(0, 0, 0, 255.0 * noise(x * noise_scale, y * noise_scale))
#         point(x, y)

#-----------------------------------------------------------------------------------
#First iteration
#Generates a 'TV static background'
#To test uncomment the section below this line only..

#def setup():
#     size(1000, 750)

#     background(225, 225, 225)

#     # Generate a value between 0.0 and 1.0
#     for x in range(1000):
#     for y in range(750):
#         stroke(0, 0, 0, 255.0 * noise(x, y))
#         point(x, y)

#-----------------------------------------------------------------------------------
