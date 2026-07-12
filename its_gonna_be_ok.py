import customtkinter as ctk
import random

BG_COLOR = "#EEDA94"
TEXT_COLOR = "#B7704C"
HOVER_COLOR = "#FFE16F"
WHITE = "#FFFFFF"
BUTTONS = "#EED2B3"

ctk.set_appearance_mode("Light")

window = ctk.CTk()
window.title("Its Going To Be Okay!")
window.geometry("600x500")
window.configure(fg_color= BG_COLOR)
window.attributes('-fullscreen', True)

random_txts = ["You are loved!", "You are special!", "You are beautiful!", "You are worthy of love!", "You are perfect just the way you are!", "Your hair looks so good!",
               "Do it for your younger self!", "You can get through this!", "God wouldn't give you a challenge He didn't think you couldn't take", 
               "Everything happens for a reason", "Che sara sara!", "It will all work out in the end", "You have a gorgeous smile!", "Take a deep breathe",
               "You are going to be okay.", "Your nose is perfect","Your teeth are super white", "Your eyes are perfect", "Your body is tea",
               "You are skinny", "You will be heatlhy", "You are trying your best, and that's all anyone can ask for", "Find the brightness in the darkest tunnels",
               "You are never alone.", "There are so many people who love you."]

count = 0

def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()


def start_up():

    title = ctk.CTkLabel(
        window,
        text = "Its Going To Be Okay!",
        font = ("Comic Sans MS", 65, "bold"),
        text_color = TEXT_COLOR,
        fg_color = "transparent"
    )
    title.pack(pady=20)
    title.place(relx=0.5, rely=0.38, anchor="center")

    continue_button = ctk.CTkButton(
        window,
        text="PROVE IT",
        command= show_button_screen,
        fg_color= BUTTONS,
        hover_color=HOVER_COLOR,
        text_color=TEXT_COLOR,
        font=("Comic Sans MS", 55),
        corner_radius = 20
    )
    continue_button.pack(pady=20)
    continue_button.place(relx=0.5, rely=0.5, anchor="center")

def show_button_screen():

    clear_screen()

    random_txt_button = ctk.CTkButton(
        window,
        text = "MAKE IT BETTER",
        command = random_txt_screen,
        fg_color = BUTTONS,
        hover_color = HOVER_COLOR,
        text_color = TEXT_COLOR,
        font = ("Comic Sans MS", 45),
        corner_radius = 30
    )
    random_txt_button.pack(pady=20)
    random_txt_button.place(relx=0.5, rely=0.5, anchor="center")


def random_txt_screen():

    clear_screen()
    number = random.randint(0, len(random_txts)-1)
    rand_text = random_txts[number]

    texts_show = ctk.CTkLabel(
        window,
        text= rand_text,
        font=("Comic Sans MS", 65),
        text_color=TEXT_COLOR,
        fg_color="transparent",
        wraplength= 700
    )
    texts_show.pack(pady=10)
    texts_show.place(relx=0.5, rely=0.27, anchor="center")

    global count
    count += 1

    show_button_screen_button = ctk.CTkButton(
        window,
        text = "MAKE IT BETTER",
        command = random_txt_screen,
        fg_color = BUTTONS,
        hover_color = HOVER_COLOR,
        text_color = TEXT_COLOR,
        font = ("Comic Sans MS", 45),
        corner_radius = 30
    )
    show_button_screen_button.pack(pady=20)

    show_button_screen_button.place(relx=0.5, rely=0.5, anchor="center")

    if count >= 5:
        finish_button()

def finish_button():

    finish_button = ctk.CTkButton(
        window,
        text = "okay, this feels better",
        command = finish_screen,
        fg_color = BUTTONS,
        hover_color = HOVER_COLOR,
        text_color = TEXT_COLOR,
        font = ("Comic Sans MS", 45),
        corner_radius = 30
    )
    finish_button.pack(pady=20)
    finish_button.place(relx=0.5, rely=0.62, anchor="center")

def finish_screen():
    clear_screen()
    finish_label = ctk.CTkLabel(
        window,
        text = "I'm glad you feel better! I told you it was going to be okay!",
        font = ("Comic Sans MS", 45),
        text_color = TEXT_COLOR,
        fg_color = "transparent"
    )
    finish_label.pack(pady=20)
    finish_label.place(relx=0.5, rely=0.5, anchor="center")

    exit_button = ctk.CTkButton(
        window,
        text = "i'll be here the next time you need me :)",
        command = exit_program,
        fg_color = BUTTONS,
        hover_color = HOVER_COLOR,
        text_color = TEXT_COLOR,
        font = ("Comic Sans MS", 45),
        corner_radius = 30
    )
    exit_button.pack(pady=20)
    exit_button.place(relx=0.5, rely=0.7, anchor="center")

def exit_program():
    window.destroy()


start_up()
window.mainloop()

