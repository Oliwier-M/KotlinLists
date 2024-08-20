from getSymptoms import all_symptoms
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
from tkinter import ttk

symptomWindow = tk.Tk()

symptomWindow.title('Symptoms')

# window size
window_w = 600
window_h = 750

# get screen dimensions
screen_w = symptomWindow.winfo_screenwidth()
screen_h = symptomWindow.winfo_screenheight()

# get center
center_w = int(screen_w / 2 - window_w / 2)
center_h = int(screen_h / 2 - window_h / 2)

# set window size and position, make the window not resizable
symptomWindow.geometry(f'{window_w}x{window_h}+{center_w}+{center_h}')
symptomWindow.resizable(False, False)

# instruction label
message = ttk.Label(symptomWindow, text="Please select the symptoms you're experiencing.", wraplength=window_w)
message.grid(row=0, column=0, columnspan=2)

symptoms = []

# # it can be changed later to be imported instead, I'm just stupid and wrote this whole thing
# text_list = ["coughing", "runny nose", "sneezing", "malaise", "difficulty swallowing", "fever", "sore throat",
#              "wheezing", "enlarged neck lymph nodes", "chills", "body aches", "vomiting", "rashes", "red eyes",
#              "watery eyes", "fatigue", "shortness of breath", "mucus in the throat", "headache", "joint pain",
#              "muscle ache", "loss of appetite", "pain during swallowing", "swollen parotid glands", "red bumps",
#              "fluid filled blisters", "swollen eyelids", "sensitivity to light", "stuffy nose",
#              "diarrhea", "dehydration"]

var_dict = {}

r = 1
c = 0

for text in all_symptoms:
    value = tk.StringVar()
    var_dict[text] = value

    checkbox = ttk.Checkbutton(symptomWindow,
                               text=text,
                               command=lambda txt=text: checked(txt),
                               variable=value,
                               onvalue=1,
                               offvalue=0)
    checkbox.grid(row=r, column=c, padx=40, sticky="w")

    for i in range(len(all_symptoms)):
        symptomWindow.grid_rowconfigure(i, weight=1)
        symptomWindow.grid_columnconfigure(0, weight=1)

    c += 1
    if c > 1:
        c = 0
        r += 1


def checked(symptom):
    check = var_dict[symptom].get()

    if check == '1':
        print(check)
        if symptom in symptoms:
            print("This symptom was already chosen")
        else:
            symptoms.append(symptom)
            print(symptoms)
    elif check == '0':
        print(check)
        if symptom in symptoms:
            symptoms.remove(symptom)
            print(symptoms)
        else:
            print("This symptom is not in the symptoms list")


def open_disease_window():
    symptomWindow.destroy()
    disease_window = tk.Tk()
    disease_window.title("Diagnostics")

    # set window size and position, make the window not resizable
    disease_window.geometry(f'{window_w}x{window_h}+{center_w}+{center_h}')
    disease_window.resizable(False, False)

    # instruction label
    message2 = ttk.Label(disease_window, text="Based on your symptoms, those are the diseases you might be "
                                              "experiencing:", wraplength=window_w, anchor='center', justify='center')
    message2.grid(row=0, column=0, padx=50)

    def disease_one():
        print("disease1")

    def disease_two():
        print("disease2")

    def disease_three():
        print("disease3")

    # first frame will contain 3 probable diseases, which will be buttons
    frame_diseases = ttk.Frame(disease_window, height=100, width=550, relief='groove', borderwidth='2')
    frame_diseases.grid(row=2, column=0, pady=20, padx=20)

    scrollbar = ttk.Scrollbar(frame_diseases, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas = tk.Canvas(frame_diseases, yscrollcommand=scrollbar.set, height=100, width=518)
    canvas.pack(expand=False)
    scrollbar.config(command=canvas.yview)

    button_frame = ttk.Frame(canvas, padding=(10, 0, 10, 0))
    canvas.create_window((0, 0), window=button_frame, anchor=tk.NW)

    # generate buttons based on the returned

    disease_button1 = tk.Button(button_frame, text="disease1", width=48, height=2, anchor='center', command=disease_one)
    disease_button1.pack()

    disease_button2 = tk.Button(button_frame, text="disease2", width=48, height=2, anchor='center', command=disease_two)
    disease_button2.pack()

    disease_button3 = tk.Button(button_frame, text="disease3", width=48, height=2, anchor='center',
                                command=disease_three)
    disease_button3.pack()

    button_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # when a disease button is pressed info sheet will be shown in the 2nd frame
    frame_info = ttk.Frame(disease_window, height=500, width=550, relief='groove', borderwidth='2')
    frame_info.grid(row=4, column=0, pady=20)


ttk.Button(symptomWindow, text="Evaluate", command=open_disease_window).grid(row=r + 4, column=0, columnspan=2)

symptomWindow.mainloop()
