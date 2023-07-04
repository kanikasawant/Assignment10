import tkinter as tk
import webbrowser as wb

root = tk.Tk()

# Entry 
entry = tk.Entry(root, font=("Times New Roman", 30), width=30)
entry.grid(row=0, column=0)


l1 = tk.Label(root, font=("Times New Roman", 20))
l1.grid(row=1, column=0)

#display
def display():
    search = entry.get()
    print(search)
    if search:
        l1.config(text="Navigating to Vedantu..")
        
        wb.open(f"https://vedantu.com/?q={search}")
    else:
        print("Please enter something")

#search button
search_button = tk.Button(root, text="Search", font=("Times New Roman", 20),bg="pink", activebackground="yellow", command=display)
search_button.grid(row=3, column=0)

#close button
close_button = tk.Button(root, text="Close", font=("Times New Roman", 20),bg="brown", activebackground="orange", command=root.destroy)
close_button.grid(row=4, column=0)

root.mainloop()