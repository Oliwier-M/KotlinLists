from ctypes import windll

import main
import matchDieaseses as match

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

diseases = main.save_diseases()
all_symptoms = main.get_symptoms(diseases)
symptoms = []
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
    probable_diseases = match.matching_diseases(symptoms, diseases)

    symptomWindow.withdraw()
    disease_window = tk.Tk()
    disease_window.title("Diagnostics")

    # set window size and position, make the window not resizable
    disease_window.geometry(f'{window_w}x{window_h}+{center_w}+{center_h}')
    disease_window.resizable(False, False)

    # button to go back to the previous screen
    def go_back():
        disease_window.withdraw()
        symptomWindow.deiconify()

    ttk.Button(disease_window, text="←", width=5, command=go_back).grid(row=0, column=0, sticky='w')

    # instruction label
    message2 = ttk.Label(disease_window, text="Based on your symptoms, those are the diseases you might be "
                                              "experiencing:", wraplength=window_w, anchor='center', justify='center')
    message2.grid(row=1, column=0)

    # first frame will contain 3 probable diseases, which will be buttons
    frame_diseases = ttk.Frame(disease_window, height=100, width=550, relief='groove', borderwidth='2')
    frame_diseases.grid(row=3, column=0, pady=20, padx=20)

    scrollbar = ttk.Scrollbar(frame_diseases, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas = tk.Canvas(frame_diseases, yscrollcommand=scrollbar.set, height=100, width=518)
    canvas.pack(expand=False)
    scrollbar.config(command=canvas.yview)

    button_frame = ttk.Frame(canvas, padding=(10, 0, 10, 0))
    canvas.create_window((0, 0), window=button_frame, anchor=tk.NW)

    # generate buttons based on the returned probable diseases
    for disease in diseases:
        for pd in probable_diseases:
            if disease.name == pd[0]:
                matching_symptoms = pd[1]
                disease_button = tk.Button(button_frame, text=disease.name, width=48, height=2, anchor='center',
                                           command=lambda d=disease, s=matching_symptoms: show_disease_info(d, s))
                disease_button.pack()

    button_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # when a disease button is pressed info sheet will be shown in the 2nd frame
    frame_info = ttk.Frame(disease_window, height=480, width=550, relief='groove', borderwidth='2')
    frame_info.grid_rowconfigure(0, weight=0, minsize=480)
    frame_info.grid_columnconfigure(0, weight=0, minsize=550)
    frame_info.grid(row=5, column=0, pady=20)

    disease_info = ttk.Label(frame_info, text="You must choose at least one symptom to see what disease you might have.", wraplength=550, anchor='w')
    if len(probable_diseases) == 0:
        disease_info.pack()
    care_label = ttk.Label(frame_info, text="", anchor='center', justify='center', foreground="red")
    symptoms_label = ttk.Label(frame_info, text="", wraplength=550, anchor='w')

    def show_disease_info(d, s):
        """Upon pressing a button with the name of the matching disease it will display the description of the disease,
         along with user's symptoms, matching symptoms and an information whether urgent medical care is required.

        Args:
             d: object Disease
             s: list of string representing matching symptoms (symptoms that occur both in the user and the disease)
             formatted_s: string from formatting the "s" list
             u_sym:   a list of unique symptoms that the user experiences
             formatted_u_sym: string from formatting the "u_sym" list
             c_sym:   a list of common symptoms that the user experiences
             symptoms: list of strings representing user symptoms
             user_symptoms: string from formatting the "symptoms" list
        """
        disease_info.config(text="")
        care_label.config(text="")
        symptoms_label.config(text="")
        print(s)

        # format matching symptoms list for the label display
        formatted_s = ', '.join(s)
        u_sym = []

        for symptom in s:
            for unique_symptom in match.unique_symptoms(diseases):
                if symptom == unique_symptom:
                    u_sym.append(symptom)

        formatted_u_sym = ', '.join(u_sym)

        if d.urgent_care_needed == "True":
            care_label.config(text="!!!Urgent consultation with a medic professional is advised!!!")
        care_label.pack()

        user_symptoms = ', '.join(symptoms)

        if len(u_sym) > 0:
            symptoms_label.config(text=f"Your symptoms: {user_symptoms}. \n\nThese symptoms: {formatted_s} indicate you might be suffering from {d} disease. It's unique symptoms are {formatted_u_sym}.\n")
        else:
            symptoms_label.config(text=f"Your symptoms: {user_symptoms}. \n\nThese symptoms: {formatted_s} indicate you might be suffering from {d} disease.\n")

        info = d.description
        disease_info.config(text=info)
        symptoms_label.pack()
        disease_info.pack()


ttk.Button(symptomWindow, text="Evaluate", command=open_disease_window).grid(row=r + 4, column=0, columnspan=2)

symptomWindow.mainloop()
