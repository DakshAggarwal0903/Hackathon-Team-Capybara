import time as tm
import random as r

def jokes(num):
    jokes= ["Why couldn't the pony sing a lullaby?","What did one toilet say to the other?","Why can’t Elsa from Frozen have a balloon?","Why did the kid bring a ladder to school?","How are false teeth like stars?","What building in your town has the most stories?"," What is a computer's favorite snack?", "How do we know that the ocean is friendly?","What is a tornado’s favorite game to play?","  What animal is always at a baseball game?"," What did the little corn say to the mama corn?","What kind of tree fits in your hand?","Why did the student eat his homework?","What goes up but never comes down?","Why is the obtuse triangle always so frustrated?"]
    ans= ["She was a little horse","You look a bit flushed","Because she will 'let it go, let it go'","Because she wanted to go to high school","They come out at night","The public library","Computer chips","It waves","Twister","A bat","Where is pop corn?","A palm tree","Because the teacher told him it was a piece of cake", " Your age","Because it’s never right."]
    a,b= jokes[num],ans[num]
    return a,b

