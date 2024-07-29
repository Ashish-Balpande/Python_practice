

story = """BLIND FAITH
Posted on July 1, 2024 (1050 words) 
“Do come through to the lounge. I’ve heard so much about you, Peter.” 
“Oh, yeah, right, thanks.” “My husband’s still at the church. He’ll be along presently. 
When he’s finished the service.” We proceeded along a deep-carpeted corridor. 
Photographs of smiling family members hung on the walls and a tall grandfather clock 
ticked ponderously, attempting to keep the silence at bay. Peter sat on a red-leather 
sofa with his back to a bay window, overlooking a neat garden which receded into the distance. 
He wore blue jeans; a black leather jacket and his long hair was washed and in a neat pony tail. 
“This room’s very nice Mrs. Johnson.” “Oh, thank you, yes, there are many family heirlooms, 
as you can see. She gestured around at glass cabinets. All under lock and key!” 
She blushed furiously. “Oh, er, I mean ….” “Of course, Mrs. Johnson.” Peter gave a charming smile. 
“You can’t be too careful around here.”"""


def lengthOfStory(story1):
    print("\nThe length of story is :", len(story1))
    numOfLines = 0
    
    #for i in story1:
        #if i

def numOfCapitalLetter(story1):
    lower = 0
    upper = 0
    upperList = []
    
    for i in story1:
        if (i.islower()):
            lower+=1
        elif (i.isupper()):
            upper+=1
            upperList.append(i)
            
    print("\nThe number of Small Letter is :", lower)
    print("\nThe number of Capital Letter is :", upper)
    print("Capital Letter is :", upperList)

def numOfWords(story1):
    words = story1.split()
    wordsNum = len(words)
        
    print("\nThe number of Words is :", wordsNum)
    print("Words is :", words)

def digitInStory(story1):
    num = 0
    numList = []
    
    for i in story1:
        if (i.isdigit()):
            num+=1
            numList.append(i)
            
    print("\nThe number of Digit is :", num)
    print("Digit is :", numList)

def spCharInStory(story1):
    spChar = 0
    spCharList = []
    
    for i in story1:
        if not (i.isalnum()) and not i.isspace():
            spChar+=1
            spCharList.append(i)
            
    print("\nThe number and alpa is :", spChar)
    print("Numbers is :", spCharList)



#story = input("Write the story : \n")
print(story)
print("\n=============================================================================")
#lengthOfStory(story)
numOfCapitalLetter(story)
numOfWords(story)
digitInStory(story)
spCharInStory(story)