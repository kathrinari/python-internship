
#DESERT : SHANELLE GLANVILLE

import pickle 

f=open("hero.dat", "rb+")
hero=pickle.load(f) 


TERM_1 = "daki"
TERM_2 = "davveya"

print("""
                      __..-----') 
        ,.--._ .-'_..--...-' 
       '-"'. _/_ /  ..--''""'-. 
       _.--""...:._:(_ ..:"::. \ 
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ / 
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-' 
   "  / |  :' :/""\///)  /:.'    --(       )-- 
     / :( :( :(   (#//)  "       .-'\.___./'-. 
    / :/|\ :\_:\   \#//\            /  |  \ 
    |:/ | ""--':\   (#//)              ' 
    \/  \ :|  \ :\  (#//) 
         \:\   '.':. \#//\ 
          ':|    "--'(#///) 
                     (#///) 
                     (#///)              
                      \#///\           
                      (##///)          
                      (##///)          
                      (##///)          
                      (##///)         
                       \##///\        
                       (###///)       
                       (##////)__...--:: :...__ 
                       (#/::'''                 ""--.._ 
                  __..-'''                             "-._ 
          __..--""                                         '._ 
 ___..--""                                                    "-..___ 
   (_ ""---....___                                     __...--"" _) 
     ''''--...  ___''''''-----......._______......----''''''     --
                   '''''''       ---.....   ___....---- 
      """)

print("\nThe hero is blown away and makes a hard landing in the desert far away. She blacks out.") 
input("[Press Enter to continue.]")
print("\nSome time passes before she comes to. Upon awakening, she is woozy and in need of water.")
input("[Enter]")
print("\nShe sees what looks like a pool of water in the distance, but it disappears when she draws near.")
input("[Enter]")
print("\nShe must be hallucinating.")
input("[Enter]")
print("\nStill, perhaps she can find a cactus and extract water from the inside. She decides to wander around.")
input("[Enter]")
print("\nAt some point, she sees a band of orcs sailing through the sand on a banana boat.")
input("[Enter]")
print("\nThis is obviously another hallucination.")
input("[Enter]")
print("\nShe notices that they are all chanting, 'VE! VE! VE!' What could that mean? It sounds significant.")
input("[Enter]")
print("\nHours pass, yet still no water in sight. The hero collapses into the sand, despondent.")
input("[Enter]")
print("\nBut wait... what is that in the distance? It looks like a man riding a camel in her direction.")
input("[Enter]")
print("\nThe hero sits back up and desperately waves the traveler down, hoping that he is not a hallucination too.")
input("[Enter]")
print("\nHe's real! The traveler approaches the hero and gives her some water. The hero thanks him profusely.")
input("[Enter]")
print("\nThe traveler is curious to know what she's doing here, so she tells him that she's on a journey and explains what happened with the volcano.")
input("[Enter]")
print("\nThe traveler is intrigued. 'How well do you know the language of this land?' he asks.")
input("[Enter]")
print("\n'If you can help me remember the names of two items,' he continues, 'I will take you with me out of this desert.'")
input("[Enter]")
print("\n'You see, the king's favorite letter is 'D', and both the gifts I am giving him start with that letter.'")
input("[Enter]")
print("\n'Unfortunately, my memory has become a bit jumbled in my old age.' He holds up a pomegranate and a sprig of rosemary.")
input("[Enter]")
print("\n'Can you help me remember what they're called?'")
input("[Enter]")
print("\nEither the hero will figure this out, or it will be the last thing she does.")

guess_1 = input("[ENTER] TO START MINI-GAME: MIND UNSCRAMBLER")
counter = 0

print("\nThe hero has a feeling that she knows these words. Maybe they have something to do with the syllables she's encountered on her journey?")
while guess_1 != TERM_1:
    print("""
          K  I  E  P  Y  A 
          A  C  N  D  E  L 
          S  U  O  A  V  M 
          I  R  Q  K  E  W 
          E  J  A  I  X  P    
          E  D  A  V  R  O
          """)
    guess_1 = input("What could the word for pomegranate be?: ").lower()
    if guess_1 != TERM_1 and counter == 0:
        counter += 1
        print("\n\nNo, that's not right.")        
        print("Maybe the first syllable is 'DA?'")
    elif guess_1 != TERM_1 and counter == 1:
        counter += 1
        print("\n\nNo, that's not right either.")
        print("But it's coming back to me a little. I think the second syllable starts with the letter 'K.'")
    elif guess_1 != TERM_1 and counter == 2:
        counter += 1
        print("\n\nNo, that's not right either.")
        print("But the word is on the tip of my tongue! The vowel of second syllable must be either 'E' or 'I'.")
    elif guess_1 != TERM_1 and counter == 3:
        print("\n\nNo, that's still not it. Let's start over. Remember, the word starts with the letter 'D'...")
        print("Out of nowhere, random syllables flash in the hero's mind:")
        print("KI DAV YA DA VE")
        print("Surely these are a hint!")
        counter = 0

print("\n'Right, the word is daki,' the traveler smiles. 'Now I remember. Can you remind me of the other one as well?'")


guess_2 = input("[ENTER] TO START MINI-GAME: MIND UNSCRAMBLER II")
counter = 0

print("\nThe hero can nearly taste her freedom. All she must do is figure out the remaining word.")
while guess_2 != TERM_2:
    print("""
      K  I  E  P  A  A  N  Y 
      A  D  N  D  Y  L  I  C 
      S  U  A  A  V  M  X  W 
      I  R  Q  V  E  W  D  E 
      D  A  V  I  V  Y  A  S  
      E  D  A  V  R  E  O  T 
      V  W  K  O  X  M  Y  P 
      A  U  H  J  A  T  F  A 
      """)
    guess_2 = input("How might one say rosemary in the local language?: ").lower()
    if guess_2 != TERM_2 and counter == 0:
        counter += 1
        print("\n\nNo, that doesn't ring a bell.")
        print("I'm quite certain that this word has three syllables.")
    elif guess_2 != TERM_2 and counter == 1:
        counter += 1
        print("\n\nNo, that's not it either.")
        print("However, I do remember that one vowel is repeated twice in this word.")
    elif guess_2 != TERM_2 and counter == 2: 
        counter += 1
        print("\n\nGood try, but still not quite right.")
        print("I remember another interesting feature: one consonant is repeated twice as well.")
    elif guess_2 != TERM_2 and counter == 3:
        counter = 0
        print("\n\nLet's try this from the beginning. Remember, the word starts with the letter 'D'...")
        print("The hero thinks back to those syllables:")
        print("KI DAV YA DA VE")
        print("Hm...")
    
print("\n\n'Yes, you've got it!' the traveler exclaims. 'I am indebted to you. Come along with me, and we shall leave this desert.'") 
print("\nHe gives you two scrolls to remember the words.\n") 

hero.scripts_append("daki = pomegranate")
hero.scripts_append("davveya = rosemary") 
hero.show_scripts() 

print("\n\nAnd the hero's journey continues...")
input("THE END")

f.close()