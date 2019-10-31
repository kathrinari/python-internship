
# JUNGLE : KHRYSTYNA OLIYNYK
import pickle 

f=open("hero.dat", "rb+")
hero=pickle.load(f) 

#Description of the setting
print("""\n\nAfter getting to the island the hero was wandering around, became hungry and decided to go in the direction 
		of the high and wonderful looking trees where she hoped to find some fruits.""")
input("[Enter]")
print("""After walking a few minutes she realized that the landscape
    that looked like woods was actually a jungle. Since the hero had  
    lost the spot where she entered and couldn't go back to the beach,  
    she had no other choice than to keep going.""")
input("[Enter]")
print("""She walked for a very long time
    struggling to get through bushes and other plants and trying not
    to be bitten by different animals and insects.""")
input("[Enter]")
print("""Suddenly the hero
    heard a wonderful sound and was trying to figure out where it was coming from.
    She realized that it was a red bird that was sitting
    on a twig of a tree next to the hero.""")
input("[Enter]")
print("""While she was watching the bird
    singing she didn't pay attention for a few seconds and was bitten by a snake.
    The hero fell down and felt a pain stronger than she'd ever experienced before.""")
input("[Enter]")
print("""She was sure that her death was coming but suddenly a monkey appeared beside
    her and said:
    'I have a ROSEMARY potion that will cure you but you have to help me to answer some
    questions for my homework for the jungle school.""")
input("[Enter]")
print("""I will ask you 5 questions and give you 3 possible answers for each question
    if you get 3 of these questions right I will give you your medicine 
	but if not, I will leave you and the consequences will be tremendous.'""", "\n")
input("[Enter]")

#drawing the bottle

    
start=("""
    ___
    | |""")

almost=("""
    ___
    | |
   /   \\
     
  """)
done=("""Please take this medicine. It will cure you immediately. And remember the letters pictured on the bottle. You will need them later!    
    ___
    | |
   /   \\
  |     |
  | dav |
  |_____|
  """)


#introduce choice
choice = None

#keeping track of right answers
right = 0
answer=0
while answer<5 or right<3:
#Questions (q) and possible answers(a)
    q1=print("\n1. What is a morpheme?") #q1+a1
    a1=print("""
            a - The smallest morphosyntactic unit
            b - A kind of mushroom that can only be found in Morrocco
            c - The smallest identifiable unit of speech""")
    choice= input("Choice: ")
    answer+=1
    if choice!= "a":
        print("Unfortunately its wrong. 'a' was the correct answer.")
    else:
        right+=1
        print("It is the right answer.")
        print(start)   
    q2=print("\n2. What is fundamental frequency of a speech signal?") #q2+a2
    a2=print("""
            a - How often one is able to say a letter
            b - The frequency of vibration of the vocal folds
            c - A frequency which occurs after a silent sound""")
    choice= input("Choice: ")
    answer+=1
    if choice!= "b":
        print("Unfortunately its wrong. 'b' was the answer we needed. Try your best next time. Remember we need 3 right answers and up to now you have answered", right, "questions right")
    else:
        right+=1
        print("Thank you. That's the right answer!")
        if right==1:
            print(start)
        elif right ==2:
            print(almost)
    q3= print("\n3. Which of the articulators is passive?") #q3+a3
    a3=print("""
            a - tongue
            b - lower jaw
            c - teeth""")
    choice= input("Choice: ")
    answer+=1
    if choice!="c":
        print("No, that is a wrong answer")
        if right<1:
            print ("I don't want to disappoint you. But there is no hope anymore. We only have", right, " right answers.")
    else:
        right+=1
        print("It is a right answer.")
        if right==1:
            print(start)
        elif right==2:
            print(almost)
        elif right==3:
            print("Well done. We have", right," right answers.")
            print(done)
            print("""
            __,__ 
   .--.  .-"     "-.  .--. 
  / .. \/  .-. .-.  \/ .. \ 
 | |  '|  /   Y   \  |'  | | 
 | \   \  \ 0 | 0 /  /   / | 
  \ '- ,\.-"`` ``"-./, -' / 
   `'-' /_   ^ ^   _\ '-'` 
       |  \._   _./  | 
       \   \ `~` /   / 
        '._ '-=-' _.'   
           '~---~' """)
            break
            
    q4=print("\n4. What does a rhyme consist of?") #q4=a4
    a4=print("""
             a - nucleus and coda
             b - onset and nucleus
             c - melody""")
    choice= input("Choice: ")
    answer+=1
    if choice!= "a":
        print("It's wrong.")
        if right<=1:
            print ("I don't want to disappoint you. But there is no hope anymore. We only have", right, " right answers.")		
			
    else:
        right+=1
        print("Wow! It is a right answer.") 
        if right==1:
            print(start)
        elif right==2:
            print(almost)
        elif right==3:
            print("Well done. We have", right," right answers.")
            print(done)
            print("""
            __,__ 
   .--.  .-"     "-.  .--. 
  / .. \/  .-. .-.  \/ .. \ 
 | |  '|  /   Y   \  |'  | | 
 | \   \  \ 0 | 0 /  /   / | 
  \ '- ,\.-"`` ``"-./, -' / 
   `'-' /_   ^ ^   _\ '-'` 
       |  \._   _./  | 
       \   \ `~` /   / 
        '._ '-=-' _.'  
           '~---~' """)
            break
        
    q5=print("\n5. What is a free morpheme?") #q5+a5
    a5=print("""
            a A morpheme that can be a word by itself
            b A monk who meditates a lot
            c A morpheme that can be connected to any affix""")
    choice= input("Choice: ")
    answer+=1
    if choice!="a":
        print("Unfortunately its wrong.")
    else:
        right+=1
        print("It is a right answer.")
        if right==1:
            print(start)
        elif right==2:
            print(almost)
        elif right==3:
            print("Well done. We have", right," right answers.")
            print(done)
            print("""
           __,__ 
  .--.  .-"     "-.  .--. 
 / .. \/  .-. .-.  \/ .. \ 
| |  '|  /   Y   \  |'  | | 
| \   \  \ 0 | 0 /  /   / | 
  \ '- ,\.-"`` ``"-./, -' / 
   `'-' /_   ^ ^   _\ '-'` 
       |  \._   _./  | 
       \   \ `~` /   / 
        '._ '-=-' _.'  
           '~---~' """)
            
            break
			
    if answer==5:
        print("\nI am sorry but you couldn't help me! You answered ", right, "instead of 3 right. Try again!") 
        print("Your hero is slowly getting weaker. You must hurry!") 
        hero.health-=5
        hero.status() 
        hero.check()
 
        print("""
         .-"-. 
       _/.-.-.\_ 
      ( ( o o ) ) 
       |/  "  \|     
        \\'/^\\' / 
        /`\ /`\ 
       /  /|\  \ 
      ( (/ T \) ) 
       \__/^\__/) """)
        
        right=0
        answer=0
    

        
input("\nPress the enter key to exit.")

f.close()