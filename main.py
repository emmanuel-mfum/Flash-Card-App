from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
canto_dict = {}

# --- Reading from CSV -----#

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/cantonese_words.csv")  # get the whole data from the csv file
    canto_dict = original_data.to_dict(orient="records")  # converts the data frame into a list of dictionaries
else:
    canto_dict = data.to_dict(orient="records")  # converts the data frame into a list of dictionaries



# ---- GENERATING WORDS -----#


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)  # deactivates the flip timer
    current_card = random.choice(canto_dict)
    new_word = current_card['Cantonese']
    canvas.itemconfig(card_title, text="Cantonese", fill="black")
    canvas.itemconfig(card_word, text=new_word, fill="black")
    canvas.itemconfig(canvas_image, image=front_card)  # set the background of the canvas
    flip_timer = window.after(3000, func=flip_card)  # flip the card after 3 seconds

# ----------- FLIP CARD -------------------------#


def flip_card():
    global canvas_image
    translation = current_card['English']
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=translation, fill="white")


# -------------- REMOVE CARD -------------------#

def is_known():
    global current_card, canto_dict
    canto_dict.remove(current_card) # removes word from the list of dictionaries
    next_card()
    words_to_learn = pandas.DataFrame(data=canto_dict)  # updates data without the removed word
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)  # save it into csv file




# --------------- UI SETUP ---------------------------#
window = Tk()  # create window
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, font="Arial 40 italic", text="")
card_word = canvas.create_text(400, 263, font="Arial 30 bold", text="")
canvas.grid(column=0, row=0, columnspan=2, sticky="EW")

# Buttons
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)


next_card()  # call the method after setting up of UI but before reaching the loop so no display placeholders

window.mainloop()
