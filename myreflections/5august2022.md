<!-- Perlin Noise, Minecraft, Grasshopper, Grasshopper3d, Processing, myCodeStudies, to-do-list, -->

# Navigating Noise
## Perlin Noise
Carrying on from the entry on minecrafts generators ive found that the noise Caleb referred to was Perlin Noise and that the layers being passed are composed of this noise, the way that thxy are composed I hope to explore in this post.

I found information on the noise layers on the [minecraft wiki](https://minecraft.fandom.com/wiki/Noise_generator), easy enough, though there is an overwhelming number of layers and it looks as though multiple layers within each, one to deternine a biome, another within to determine block/tile map types and more further for things like plants buildings and NPCs like animals or villagers.

Early in the hunt i found [this video](https://www.google.com/url?sa=t&source=web&rct=j&url=https://m.youtube.com/watch%3Fv%3DTZFv493D7jo&ved=2ahUKEwjL_taBhK35AhU4wzgGHXGqBjcQFnoECEQQBQ&usg=AOvVaw1ueQ5mAT95h2kY-JDv6jB6) by nova840 it shows part of his journey in 3D map generation (and his fear of cooking🤭), something to keep in mind going forward but not the first step im looking for.

Im surprised to find a huge variety of uses for perlin noise! Ill list them with description below before explaining to future me (and i suppose whoever else reads this?) what perlin noise actually is.. 
	
1. [Joyce[MinionsArt]](https://minionsart.github.io/tutorials/) Uses perlin noise to create shaders in Unity. Their [Twitter](https://twitter.com/minionsart) also has some great posts.
2. [Parametric House](https://parametrichouse.com/?s=perlin+noise&asl_active=1&p_asid=1&p_asl_data=cXRyYW5zbGF0ZV9sYW5nPTAmc2V0X2ludGl0bGU9Tm9uZSZzZXRfaW5jb250ZW50PU5vbmUmc2V0X2luZXhjZXJwdD1Ob25lJnNldF9pbnBvc3RzPU5vbmU=) Has a few videos on pottery made (or atleast designed) using perlin noise as well as 'objects'. They mention using a program called [Grasshopper3d](https://www.grasshopper3d.com/)
3. ['Understanding Simple Perlin Noise - Generating Islands'](https://www.youtube.com/watch?v=0emj42Bn-_Y&list=WL&index=3) A great video that introduced me to ['Processing'](https://processing.org/) I followed along with the video and created the program which is now 'perlinNoise1'in the 'myCodeStudies' folder

[Understanding Simple Perlin Noise - Generating Islands.](https://www.youtube.com/watch?v=0emj42Bn-_Y&list=WL&index=3) - Im glad I came across this, it was a good opportunity to actually code something im not sure what part of the code is actually creating the 'random-ness' though I know there is a random aspect to it since what is displayed changes each time. Rather than look into that right away and loose track of my thoughts, ive created a 'to-do-list' in the repository.

So future me and co.. 
### What is perlin noise? 
Perlin noise is a type of gradient noise alongside simplex, open simplex, and others. Its pseudo-random ouput lends well to being used in the context of graphics generation when more organic forms are required (such as terrain and heightmaps, textures like smoke, fire or water and less common situations like pottery and 3d printing in the case of parametric house). From the context of what ive been looking at it also seems to be a processing power efficient way to get results for the previously mentioned use cases
### How does it work
As I understand it at the moment, Perlin noise like regular noise can be understood as waves. when it is passed position like the x and y co-ordinates the 'noise value' is returned for example the high point of a wave could return a value of .99 and the lowest point a value of .000001 however two co-ordinates on the x and y axis that are close together would not return vastly different values. if two x,y co-ordinates are close together you may get values returned for each set of co-ordinates as 0.607 and 0.598. In a height map this would produce a smooth curve rather than erratic and unnatural highs and lows.

so far ive only seen perlin noise called upon as functions and applied to something, noise() in Processing and mathf.perlinnoise in Unity. I wonder if there is a way to define it as a function so that you can see the inner workings or perhaps perlin noise itself is generated someway? I expect this is also where 'seeds' come from in order to produce the same noise map each time.

## In other news...
While looking into generators using perlin noise I also came acorss [this video](https://www.youtube.com/watch?v=20KHNA9jTsE&list=WL&index=9) which is FANTASTIC, I learnt of alot of new terms through this video which ill list below
1. Voxels
2. Marching Cubes
3. Wave Function Collapse

The video linked to [this devlog](https://forums.tigsource.com/index.php?topic=54424.msg1237532#msg1237532) by the creators of Phantom Brigade, ive not heard of the game but I like the way that created their maps. They used the Marching Cubes method and create a system for their tilesets and each sets compatability with others. I plan to look further into this at somepoint but would rather stick to my explorations into perloin noise for now rather than overload myself. 

Ive become aware also that this research repository so far has become quite.. autotelic(last weeks 'word of the week:' won by Roman). Ive always enjoyed learning but perhaps at this point I should focus this research repository more.. or otherwise leave it as a general one and have a project specific 'branch'. My concern is mostly based on the fact that I intended to create a note taking applciation for the Software Project assignment but isntead my focus has been gripped by perlin nose, generators and simulations.. is it perhaps better to follow my focus and hope that in the end I can craft it into something suitable for the assignment?
