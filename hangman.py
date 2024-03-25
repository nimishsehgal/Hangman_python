import random
words=["elephant", "guitar", "rainbow", "balloon", "necklace",
    "butterfly", "telescope", "pancake", "keyboard", "umbrella",
    "fireworks", "sunflower", "backpack", "lighthouse", "caterpillar",
    "waterfall", "seashell", "snowflake", "dragonfly", "pinecone"]
str=random.choice(words)
ans=""
i=0
ans=["_"]*len(str)
chances=7
win=False
while(chances>0 and win==False):
    print("Current word:", "".join(ans))
    print("You have {} chances left.".format(chances))
    x=input("Enter the choice: ")
    if len(x)>1:
        if x==str:
            win=True
        else:
            chances-= 1
    else:
        flag=0
        for i in range(len(str)):
            if str[i]==x:
                flag=1
                ans[i]=x
        if flag==0:
            chances-= 1
            
        else:
            curr="".join(ans)
            if curr==str:
                win=True
if win==True:
    print("Correct Guess: ", "".join(ans))
    print("Congratulations on winning the game.")
else:
    print("The correct answer is {}.".format(str))
    print("Better luck next time.")
