# What part of this code creates a random output?

    noise_scale = 0.2
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
    
    # noise() noise is a function that returns the perlin noise value at specific co-ordinates. In the case of the above code those co-ordinates are (x * noise_scale) and (y * noise_scale). noise_scale is set to 0.2, this is to ensure that the numbers returned are not integers as this always return the same value for example 1, 43, 98, 2, 6000 and every other could all return .6789 which would ruin the output