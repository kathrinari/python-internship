# Python Final Project Pygame 
# by Team Carlotte, Shauni, Laila, Jule

# Starting sequence for game "Addakhat, azhat"

# Code for Mainloop by Charlotte
# Code for Player and animation by Laila
# Starting sequence with tkinter by Jule
# Both parts assembled to be functioning by Shauni

import pickle 
from tkinter import *

class Application(Frame):
    #create class for buttons
    def __init__(self, master):
        #initialize the frame
        score = 0 #initialize variable
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create label for main instruction
        self.inst_lbl = Label(self, text = "Welcome to the Jump and Run game, where you can find out something about the words 'addakhat' and 'azhat'"
											"\nFor controls use the arrow keys to move and space to jump. \n You need to collect 3 coins and make it to the flag in order to recieve the hint.")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        # create launching button
        self.launch_bttn = Button(self, text = "Start the game" , command = self.launch)
        self.launch_bttn.grid(row = 1, column = 0, sticky = W)

        # create label for score
        self.score_lbl = Label(self, text = "Click the button to reveal the information")
        self.score_lbl.grid(row = 2, column = 0, sticky = W)

        # create button to reveal the answer
        self.answer_bttn = Button(self, text = "Reveal the answer", command = self.answer)
        self.answer_bttn.grid(row = 3, column = 0, sticky = W)

        # create text widget to display information
        self.info_txt = Text(self, width = 60, height = 10, wrap = NONE)
        self.info_txt.grid(row = 4, column = 0, columnspan = 2, sticky = W)

        # create button to exit
        self.quit_bttn = Button(self, text = "Quit", command = quit)
        self.quit_bttn.grid(row = 1, column = 1, sticky = W)
        

    #create method to start game 
    def launch(self):
        import mainloop #include mainloop file
        self.score = mainloop.Mainloop() #extract score from mainloop file
        
        

    #create method to reveal information
    def answer(self):
        information = self.info_txt.get(0.0, END)
        if self.score >= 3: #if 3 coins collected, reveal secret information
            information = """'Addakhat' means 'to feed' and 'azhat' means 'to give'.
 Both words can be changed easily through
 derivational morphology. For example, by adding
 the morph 'es' at the beginning,
 you can reverse the meaning of 'azhat' (to give)
 to 'esazhat' (to take back). As seen in
 the inscription, you form an imperative
 by adding an 's' at the end."""  
        else:  #No information, if not enough coins
            information = """Sorry, you haven't collected enough coins.
Play again :-)""" 
            
        self.info_txt.delete(0.0, END)
        self.info_txt.insert(0.0, information)  

  
#main
root = Tk()
root.title("'Addakhat' and 'azhat'")
root.geometry("800x600")
app = Application(root)
root.mainloop()


f=open("hero.dat", "rb+")
hero=pickle.load(f)         

hero.scripts_append("addakhat = to feed")
hero.scripts_append("azhat = to give")
hero.show_scripts()
           
f.close() 