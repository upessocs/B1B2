import tkinter as tk #GUI

# from file_organizer import organize_files
# Create the main window

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x250")  # Set the window sizeFunction to be called when the button is clicked

def show_input():
    user_input = entry.get()  # Get text from the entry box
    print("User input:", user_input)#Label for entry

label = tk.Label(root, text="Laber text content")
label.pack(pady=10)  # Add padding around the labelEntry (input block) where user can type text

entry = tk.Entry(root, width=70)
entry.pack(pady=5)#Button to trigger the function show_input

button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=10)#Start the GUI event loop

root.mainloop()