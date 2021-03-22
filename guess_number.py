#%%python
import tkinter
import math
import tkinter.messagebox
import random

answer = ""
guessed_num = []


# Function to convert   
def listToString(s):  
    str1 = ""   
    for elements in s:  
        str1 += str(elements)
        str1 += " "     
    return str1 

def bigger():
    global bottom, upper, guess
    bottom = guess + 1
    guess_num()
    label.configure(text = answer)
    print(answer)

def smaller():
    global bottom, upper, guess
    upper = guess - 1
    guess_num()
    label.configure(text = answer)

def bingo():
    result = tkinter.messagebox.askyesno("Got it!!", "BINGOOO Play Again?")
    if result == True:
        root.destroy()
        init_game()
    else:
        root.quit()
    
 
def guess_num():
    global answer, bottom, upper, guess
    guess = int((bottom+upper)/2)
    guessed_num.append(guess)
    if bottom == guess or upper == guess:
        answer = "The answer must be " + str(bottom)
        result = tkinter.messagebox.askyesno("Got it!!", answer)
        if result == True:
            asking = tkinter.messagebox.askyesno("BINGO!!!", "BINGOO :) .... Play Again?")
            if asking == True:
                root.destroy()
                init_game()
            else:
                root.quit()
        else:
            asking = tkinter.messagebox.askyesno("Hey", "You tricked me :( Play Again?")
            if asking == True:
                root.destroy()
                init_game()
            else:
                root.quit()
    answer = "Is it " + str(guess) + "?"
    print(guessed_num)

    guess_hist = "Guess History..." + str(listToString(guessed_num))
    guess_history.configure(text = guess_hist)


def start_game():
    global answer, bottom, upper, guess, guess_history
    bottom = int(bottom_hint.get())
    upper = int(upper_hint.get())
    if bottom == upper:
        answer = "The answer must be " + str(bottom)
        result = tkinter.messagebox.askyesno("Got it!!", answer)
        if result == True:
            asking = tkinter.messagebox.askyesno("BINGO!!!", "BINGOO :) .... Play Again?")
            if asking == True:
                root.destroy()
                init_game()
            else:
                root.quit()
        else:
            asking = tkinter.messagebox.askyesno("Hey", "You tricked me :( Play Again?")
            if asking == True:
                root.destroy()
                init_game()
            else:
                root.quit()
    guess = int((bottom+upper)/2)
    guessed_num.append(guess)
    answer = "Is it " + str(guess) + "?"
    label.configure(text = answer)
    tkinter.Button(root, text='Smaller', command=smaller).place(x=50,y=300)
    tkinter.Button(root, text='Bigger', command=bigger).place(x=150,y=300)
    tkinter.Button(root, text='BINGO!', command=bingo).place(x=250,y=300)
    guess_hist = "Guess History..." + str(listToString(guessed_num))
    guess_history = tkinter.Label(root, text=guess_hist)
    guess_history.place(x=10,y=370)
 
def btn_confirm():
    global bottom_hint, upper_hint
    #input 

    say_hello = "Hello... " + str(text_name.get())
    label.configure(text = say_hello)

    label_guess=tkinter.Label(root,text='Give the bottom Range')
    label_guess.place(x=10,y=150)

    bottom_hint=tkinter.Entry(root,width=10)
    bottom_hint.place(x=150,y=150)

    label_guess=tkinter.Label(root,text='Give the Upper Range')
    label_guess.place(x=10,y=200)

    upper_hint=tkinter.Entry(root,width=10)
    upper_hint.place(x=150,y=200)

    btnCheck=tkinter.Button(root,text='GO',command=start_game)
    btnCheck.place(x=250,y=150,width=50,height=28)

def quit():
    global root
    root.quit()

def init_game(): 
    global label, root, text_name, guessed_num
    #name
    root = tkinter.Tk()
    root.minsize(350,400)
    root.title('My GAME')
    label = tkinter.Label(root,text="Let Me Guess Your Number :D")
    label.pack()
    label_name=tkinter.Label(root,text="Your Name ? ")
    label_name.place(x=10,y=60)
    text_name=tkinter.Entry(root,width=20)
    text_name.place(x=10,y=90)
    btnOK = tkinter.Button(root,text="OK",command=btn_confirm)
    btnOK.place(x=200,y=90,width= 30, height=28)
    tkinter.Button(root, text="Quit", command=quit).pack()
    guessed_num = []
    root.mainloop()

init_game()