import customtkinter as ctk

root = ctk.CTk()
root.geometry("500x500")

def button_func():
    final_result = []
    character = result_string.get()
    new_words = character.split()

    # character loop from chr to ord
    # if checkbox_var.get() - > True
    if checkbox_var.get() == "-A":
        print(checkbox_var.get())

        for current_chr in range(len(character)):
            index = character[current_chr]
            from_character_to_ord = ord(index)
            final_result.append(str(from_character_to_ord))
        
        print(" ".join(final_result))

    else: 
        for char in range(len(new_words)):
            current_string = int(new_words[char])
            final_result.append(chr(current_string))
        
        print(" ".join(final_result))
        label_var.set(f'The result: {" ".join(final_result)}')


def delete_button():
    entry_one.delete(0, "end")
    

    
result_string = ctk.StringVar()
#Entry widget run
entry_one = ctk.CTkEntry(master=root, corner_radius=5, textvariable=result_string, width=300)
entry_one.grid(row=5, columnspan=1, column=100)

#Label widget running....
show_me_result_result = ctk.StringVar(value=" ")
show_me_result = ctk.CTkLabel(master=root, textvariable=show_me_result_result)
show_me_result.grid(row=6, column=20)

#button widget created
submit_button = ctk.CTkButton(master=root, text="Submit", command=button_func)
submit_button.grid(row=7, column=100)

#radio-button widget
checkbox_var = ctk.StringVar()
checkbox_widget = ctk.CTkRadioButton(master=root, text="ASCII",text_color="cornsilk2", font=("Arial", 15) ,variable=checkbox_var, value="-A")
checkbox_widget.grid(row=0, column=0, sticky=ctk.NE)

second_checkbox = ctk.CTkRadioButton(master=root, text="ChR", text_color="cornsilk3", font=("Arial", 15), variable=checkbox_var, value="-B")
second_checkbox.grid(row=1, column=0)

#clear_button 
clear_button = ctk.CTkButton(master=root, text="Clear", fg_color="#b01c1c", command=delete_button, width=50, height=35)
clear_button.grid(row=7, column=105)

label_var = ctk.StringVar()
label_result = ctk.CTkLabel(master=root, textvariable=label_var)
label_result.grid(row=8, column=5)

root.mainloop()
