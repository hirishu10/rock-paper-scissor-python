# 
# Rock,, Paper Scissor 
# Programme with Python and Tkinter
# ----------------------------------------->
# 

from tkinter import *
import random

window = Tk()

# Icon
game_icon = PhotoImage(file="logo.png")

# Store the player points
up = 0
cp = 0

window.geometry("420x420") # size of the canvas
window.config(background="black")
window.iconphoto(True, game_icon)

icon = PhotoImage(file="logo.png")

# window is not resizable
window.resizable(0, 0)

window.title('Rock Scissor Paper (Game)') # Title of the canvas


def play_rps(getuser):
    user_points = int(point_string.get())
    comp_points = int(point2_string.get())

    user_input = getuser

    computer_guess = random.randint(1, 3)

    guessing_rock = 1
    guessing_paper = 2
    guessing_scissor = 3

    #   add the icon as per computer choose!
    if computer_guess == guessing_rock:
        comp_label.config(image=rock)
    elif computer_guess == guessing_paper:
        comp_label.config(image=paper)
    else:
        comp_label.config(image=scissor)

    # 1 for rock
    # 2 for paper
    # 3 for scissor

    # Algorithm
    if (user_input == guessing_rock and computer_guess == guessing_scissor) or \
            (user_input == guessing_paper and computer_guess == guessing_rock) or \
            (user_input == guessing_scissor and computer_guess == guessing_paper):
        win_lose.config(text=win_text, fg="#46eb34")
        user_points += 1

        point_string.set(str(user_points))

        # point_label.config(text=f"{point_string} | {comp_points}", font=("Arial", 18, "bold"))
        point_label.config(text="{} | {}".format(point_string.get(), point2_string.get()))
        window.update()

    elif (user_input == guessing_scissor and computer_guess == guessing_rock) or \
            (user_input == guessing_rock and computer_guess == guessing_paper) or \
            (user_input == guessing_paper and computer_guess == guessing_scissor):
        win_lose.config(text=lose_text, fg="red")
        comp_points += 1

        point2_string.set(str(comp_points))

        # point_label.config(text=f"{point_string} | {comp_points}", font=("Arial", 18, "bold"))
        point_label.config(text="{} | {}".format(point_string.get(), point2_string.get()))
        window.update()
    else:
        win_lose.config(text=draw_text, fg="light green")


# If the Rock Button Clicked
def rock_click():
    new_game.place(x=174, y=178)
    label2.config(text='                     👆             ')
    user_label.config(image=rock)
    rock_button.config(state=DISABLED)
    scissor_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    play_rps(1)

# If the Scissor Button Clicked
def scissor_click():
    new_game.place(x=174, y=178)
    label2.config(text='                     👆             ')
    user_label.config(image=scissor)
    rock_button.config(state=DISABLED)
    scissor_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    play_rps(3)

# If the Paper Button Clicked
def paper_click():
    new_game.place(x=174, y=178)
    label2.config(text='                     👆             ')
    user_label.config(image=paper)
    rock_button.config(state=DISABLED)
    scissor_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    play_rps(2)


# new game
def ng():
    label2.config(text="Click below icon to proceed")
    win_lose.config(text=nt_str, fg="light green")
    user_label.config(image="")
    comp_label.config(image="")
    new_game.place_forget()
    rock_button.config(state=NORMAL,
                       bg='white',
                       fg='dark green',
                       activeforeground="#0b78e6"
                       )
    scissor_button.config(state=NORMAL,
                          bg='white',
                          fg='dark green',
                          activeforeground="#0b78e6"
                          )
    paper_button.config(state=NORMAL,
                        bg='white',
                        fg='dark green',
                        activeforeground="#0b78e6"
                        )


point_string = StringVar()
point2_string = StringVar()
point_string.set(str(0))
point2_string.set(str(0))

#  Its display player's points above the top.
point_label = Label(window,text="{} | {}".format(point_string.get(),point2_string.get()),
                    font=("Arial", 18, "bold"),
                    width=38,
                    height=1)
point_label.place(x=0, y=1)

# Assigning the images of the rock,paper,scissor
rock = PhotoImage(file="rockg.png")
paper = PhotoImage(file="paperg.png")
scissor = PhotoImage(file="scissorg.png")

u = Label(window,
          text="Player1",
          font=("Arial", 20, "bold", "underline"),
          bg="black",
          fg='#059F4C')
u.place(x=50, y=30)

user_label = Label(window,
                   bg='black',
                   fg='light green',
                   width=100,
                   height=100,
                   image="")
user_label.place(x=20, y=75)

win_text = "You\nWin :)"
lose_text = "You\nLoose :("
draw_text = "Match\nDraw :O"
nt_str = "\nVs"
win_lose = Label(window,
                 text=nt_str,
                 font=("Poppins Medium", 25, "italic"),
                 bg='black',
                 fg='light green',
                 width=6)
win_lose.place(x=155, y=70)

c = Label(window,
          text="Player2",
          font=("Arial", 20, "bold", "underline"),
          bg="black",
          fg='#059F4C')
c.place(x=280, y=30)

comp_label = Label(window,
                   bg='black',
                   fg='light green',
                   width=100,
                   height=100,
                   image="")
comp_label.place(x=280, y=75)

new_game = Button(window, text="New Game", fg="red", command=ng)


label1 = Label(window,
               text="Rock Scissor Paper",
               font=("Times New Roman", 50, "bold"),
               bg="white",
               fg="red",
               image=icon,
               compound="top")
label1.place(x=0, y=200)

label2 = Label(label1, text="Click below icon to proceed", bg="white", fg="red")
label2.place(x=120, y=0)


# Rock
rock_button = Button(label1,
                     text="Rock",
                     command=rock_click,
                     font=('cosmic sans', 20, 'bold'),
                     bg='white',
                     fg='dark green',
                     activeforeground="#0b78e6"
                     )
rock_button.place(x=88, y=130)

# Scissior
scissor_button = Button(label1,
                        text="Scissor",
                        command=scissor_click,
                        font=('cosmic sans', 20, 'bold'),
                        bg='white',
                        fg='dark green',
                        activeforeground="#0b78e6")
scissor_button.place(x=165, y=130)


# Paper
paper_button = Button(label1,
                      text="Paper",
                      command=paper_click,
                      font=('cosmic sans', 20, 'bold'),
                      bg='white',
                      fg='dark green',
                      activeforeground="#0b78e6")
paper_button.place(x=266, y=130)

window.mainloop()
