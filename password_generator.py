#importing the required modoules
import tkinter as tk
from tkinter import ttk 
import random as r
import pyperclip

#genarate passwort function for tab 2
def generate_password():
    # declaring the required input variables
    sentence = sentence_entry.get("1.0", "end-1c") 
    upnumber = int(uppercase_entry.get()) 
    specialcharsadd = special_checkbox_var.get()
    specialcharsnr = int(special_entry.get()) if specialcharsadd == "yes" else 0
    #declaring the other variables
    mod_sentence = ""
    password_raw = ""
    password_up = ""
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #if sentence have punctuation at the end ->remove
    for char in sentence:
        if not char[-1].isalpha():
            mod_sentence = sentence[:-1]
        else:
            mod_sentence = sentence
    #lower all uppercase from sentence and split words 
    list_sentence = mod_sentence.lower().split()
    #checking if the words have special chars in it and remove them
    for index, value in enumerate(list_sentence):
        for letter in value:
            if letter in special_chars:
                list_sentence[index] = list_sentence[index].replace(letter, '')
    #for loop adds first letter of every word and digits into a string
    for word in list_sentence:
        if word.isdigit():
            password_raw += word
        elif word.isalpha():
            password_raw += word[0]
    #generate a list with random  index values 
    randomuplist = r.sample(range(len(password_raw)), upnumber)
    #if user wants uppercase --> uppercase letters from the random index values list
    if upnumber > 0:
        for i in range(len(password_raw)):
            if i in randomuplist:
                password_up += password_raw[i].upper()
            else:
                password_up += password_raw[i]
    if upnumber == 0:
        password_up = password_raw
    #adds specialchars if user checked yes
    if specialcharsadd == "yes":
        for i in range(specialcharsnr):
            password_up += r.choice(special_chars)
            password_up += r.choice(numbers)
    
    password_text.config(state=tk.NORMAL)  # Enable text widget for editing
    password_text.delete(1.0, tk.END)  # Clear any previous content
    password_text.insert(tk.END, password_up)  # Insert the new password
    password_text.config(state=tk.DISABLED)  # Disable text widget after editing

#copy generated password from tab2
def copy_password_to_clipboard():
    password = password_text.get(1.0, tk.END).strip()  # Get the text from password_text
    if password:
        pyperclip.copy(password)  # Copy the password to the clipboard

#copy generated password from tab3
def copy_password_to_clipboard_tab3():
    password = generated_quick_password_label.get(1.0, tk.END).strip()  # Get the text from generated_quick_password_label
    if password:
        pyperclip.copy(password)  # Copy the password to the clipboard


#generate quick pw for tab 3 function
def quick_password():
    # password variables / settings
    pwlen = int(quick_password_length_entry.get())
    pwnum = int(pwlen * 0.2)
    pwchars = int(pwlen * 0.2)
    pwletters = int(pwlen * 0.6)
    sumpwvar = pwchars + pwnum + pwletters
    uppercase = int(pwlen * 0.3)

    #special chars list
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']
    # List of numbers
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    pw = []
    pw_final = ""
    #rounds up if pwlen not qual to sumpwvar
    if pwlen != sumpwvar:
        pwletters += (pwlen - sumpwvar)
    #generate random l,c,n
    for l in range(pwletters):
        pw.append(r.choice(letters))

    for c in range(pwchars):
        pw.append(r.choice(special_chars))

    for n in range(pwnum):
        pw.append(r.choice(numbers))
    
    r.shuffle(pw)  # Shuffle the characters to make the order random
    #creating the raw pw
    password_raw = ''.join(pw)
    #same as function 1, create randomized index values
    randomuppercaselist = r.sample(range(len(password_raw)), uppercase)
    #same as functino 1, uppercase from randomized index values and create final pw
    for i in range(len(password_raw)):
            if i in randomuppercaselist:
                pw_final += password_raw[i].upper()
            else:
                pw_final += password_raw[i]

    generated_quick_password_label.config(state=tk.NORMAL)  # Enable text widget for editing
    generated_quick_password_label.delete(1.0, tk.END)  # Clear any previous content
    generated_quick_password_label.insert(tk.END, pw_final)  # Insert the new password
    generated_quick_password_label.config(state=tk.DISABLED)  # Disable text widget after editing



#creating root window and title
root = tk.Tk()
root.title("Password Generator")

# Create a Notebook widget to hold the tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create tabs
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="Welcome")
notebook.add(tab2, text="Mnemonic PW")
notebook.add(tab3, text="Quick PW")

#with and height window 
window_width = 600
window_height = 500
#--------------------------------
#specify the minimum and maximum widht, height of window
root.minsize(window_width, window_height)
root.maxsize(700, 600)
#------------------------------
#place window in the middle
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#------------------------------


# Text for the first tab
first_tab_content = """
This tool offers two options for generating secure passwords.


Option 1 - mnemonic-pw:

Input: Apple is my favorite smartphone brand.
Output example: aiMfSb_2#0

-----------------------------------

Option 2 - quick-pw:

Input: Desired password length (e.g., 15)
Output example: i8[1]hjEqOJ/3tp

"""

tab1_label = tk.Label(tab1, text=first_tab_content, font=("None", 15), wraplength=400, justify="left")
tab1_label.pack(pady=10)


#tab 2 content for the mnemonic pw----
explanation_label = tk.Label(tab2, text="Write a memorable phrase into the text box below.", font=("None", 15))
explanation_label.pack()

# Sentence input
sentence_entry = tk.Text(tab2, height=5, width=40, font=("None", 15), wrap=tk.WORD)  # Increased height and word wrap
sentence_entry.pack(pady=5)

# Uppercase count input
uppercase_label = tk.Label(tab2, text="How many letters should be uppercase (0 for all lowercase):", font=("None", 15), wraplength=400)
uppercase_label.pack(padx=20)
uppercase_entry = tk.Entry(tab2, font=("None", 15), width=5)
uppercase_entry.pack(pady=5)

# Checkbox for special characters
special_checkbox_var = tk.StringVar(value="no")  # Default value
special_checkbox = tk.Checkbutton(tab2, text="Include special characters?", variable=special_checkbox_var, onvalue="yes", offvalue="no", font=("None", 15))
special_checkbox.pack(pady=5)

# Additional input if checkbox is checked
def update_special_entry_state(*args):
    if special_checkbox_var.get() == "yes":
        special_entry.config(state=tk.NORMAL)
    else:
        special_entry.config(state=tk.DISABLED)

special_checkbox_var.trace_add("write", update_special_entry_state)
special_label = tk.Label(tab2, text="How many numbers/special chars?:", font=("None", 15))
special_label.pack()
special_entry = tk.Entry(tab2, state=tk.DISABLED, font=("None", 15), width=5)
special_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(tab2, text="Generate Password", command=generate_password, font=("None", 15))
generate_button.pack(pady=10)

# Password output
password_text = tk.Text(tab2, wrap=tk.NONE, height=1, width=20, state=tk.DISABLED, font=("None", 15))
password_text.pack(pady=10)

#Copy to clipboard
copy_button = tk.Button(tab2, text="Copy to Clipboard", command=copy_password_to_clipboard, font=("None", 15))
copy_button.pack(pady=10)
#end of tab 2 content

# Elements for tab3
label_quick_tab3 = tk.Label(tab3, text="Create a quick password based on the length:", font=("None", 15))
label_quick_tab3.pack(pady=10)

label_quick_length = tk.Label(tab3, text="How long should the password be:", font=("None", 15))
label_quick_length.pack()

quick_password_length_entry = tk.Entry(tab3, font=("None", 15), width=5)
quick_password_length_entry.pack()

generate_quick_button = tk.Button(tab3, text="Generate Password", command=quick_password, font=("None", 15))
generate_quick_button.pack(pady=10)

# Use Text widget for displaying generated password
generated_quick_password_label = tk.Text(tab3, wrap=tk.WORD, height=1, width=25, state=tk.DISABLED, font=("None", 15))
generated_quick_password_label.pack()

copy_quick_button = tk.Button(tab3, text="Copy to Clipboard", command=copy_password_to_clipboard_tab3, font=("None", 15))
copy_quick_button.pack(pady=10)




# Start the GUI event loop
root.mainloop()

