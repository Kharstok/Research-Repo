<!-- Neri Oxman, Generators, Minecraft, Rempton, Caleb Compton, Perlin Noise, Pseudo-random -->
# Drink everytime you read 'Layer'
After looking into some works by Neri Oxman I became curious on visual simulations or 3d generators because the way her works have been displayed remind me of such things (and still may be exactly that). To explore that curiosity I thought on more simple 'generators' ive seen before, the first to come to mind were the generators I toyed with in Minecraft, im sure theyve come a long way since I was in school but the early pseudo-random map generator is the one ild like to look further into for now.

"(The maps generated are) random in the sense that you can’t predict what you are going to get from them, but they are 'smooth' – the value you get depends on the values around it, rather than each one being independent."

The quoted text is from Caleb Comptons at ['rempton games'](https://remptongames.com/2021/02/28/how-minecraft-generates-massive-virtual-worlds-from-scratch/) and assured me that i was on the right train of thought when I assumed that the generator considers each block (and the context of that block) when generating the map, the height for example is not completely random otherwise the odds of getting a mountain rather than a hilled terrain are very unlikely, several 'layers' are then passed over it, caves or any other negative space is also created when a certain 'layer' is passed as well as other layers generating biomes, ores and animals depending on the context (postion, height, tilemap) of blocks in the area.

I have an idea of what a 'layer' means to me and Caleb uses the same wording in his blog although he doesnt elaborate on it past calling it a layer of noise, nor does he discuss what these layers are being passed on.
Are they being passed on an initial layer of 'noise' that was truly generated randomly since there was no context for it to be pseudo-random?

I initially thought minecrafts generators would be basic and easy to understand, fooled by it being composed of blocks,
I think at this point to create a similar generator is beyond me, especially how (assumedly) complex the code for minecrafts generator is. It may not be out of reach however to create a 2D generator where 'layers' are passed on an initial layer of noise

In the next entry ill look further into 'layers of noise' and hopefully be able to start on moving this knowledge into Oxmans real of engineering, itn would be good practice to start making something of all the information rather than stock piling it. 
	
