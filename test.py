import tkinter
from tkinter import ttk

# Function to save data
def save_data(name_entry, email_entry, phone_entry):
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if name and email and phone:
        with open('data.txt', 'a') as f:
            f.write(f"{name}|{email}|{phone}\n")
            f.flush()

        name_entry.delete(0, tkinter.END)
        email_entry.delete(0, tkinter.END)
        phone_entry.delete(0, tkinter.END)
        list_records()

# Function to list records in the table
def list_records():
    for row in tree.get_children():
        tree.delete(row)

    try:
        with open('data.txt', 'r') as f:
            for idx, line in enumerate(f, start=1):
                line = line.strip()
                if line:
                    fields = line.split('|')
                    if len(fields) == 3:
                        name, email, phone = fields
                        tree.insert("", "end", values=(idx, name, email, phone))
    except FileNotFoundError:
        pass

# Function to search records in the table
def search_data(search_entry):
    search_term = search_entry.get().lower()
    for row in tree.get_children():
        tree.delete(row)

    try:
        with open('data.txt', 'r') as f:
            for idx, line in enumerate(f, start=1):
                line = line.strip()
                if line:
                    fields = line.split('|')
                    if len(fields) == 3:
                        name, email, phone = fields
                        if search_term in name.lower() or search_term in email.lower() or search_term in phone:
                            tree.insert("", "end", values=(idx, name, email, phone))
    except FileNotFoundError:
        pass

# Main tkinter window setup
root = tkinter.Tk()
root.title("Data Management System")
root.geometry("760x400")

# Form label
form_label = tkinter.Label(root, text="Form")
form_label.grid(row=0, column=2, columnspan=4)

#color trreview


# Name label and entry
name_label = tkinter.Label(root, text="Name:", fg="blue")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = tkinter.Entry(root, width=20)
name_entry.grid(row=1, column=1)

# Email label and entry
email_label = tkinter.Label(root, text="Email:")
email_label.grid(row=1, column=2, padx=10, pady=10)
email_entry = tkinter.Entry(root)
email_entry.grid(row=1, column=3)

# Phone label and entry
phone_label = tkinter.Label(root, text="Phone:")
phone_label.grid(row=1, column=4, padx=10, pady=10)
phone_entry = tkinter.Entry(root)
phone_entry.grid(row=1, column=5)

# Save button
save_button = tkinter.Button(root, text="Save", width=15, height=2, bg="grey", command=lambda: save_data(name_entry, email_entry, phone_entry))
save_button.grid(row=1, column=6, columnspan=6, padx=10, pady=10)

# Search entry and button
search_entry = tkinter.Entry(root, width=26)
search_entry.grid(row=3, column=0, columnspan=2, pady=10)     
search_button = tkinter.Button(root, text="Search", width=15, height=2, bg="gold", command=lambda: search_data(search_entry))
search_button.grid(row=3, column=2)

# Table (Treeview) for displaying data
columns = ("S.No.", "Name", "Email", "Phone")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Set column headings
tree.heading("S.No.", text="S.No.")
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.heading("Phone", text="Phone")

# Configure columns to adjust to table behavior
tree.column("S.No.", width=50, anchor="center")
tree.column("Name", width=150, anchor="w")
tree.column("Email", width=270, anchor="w")
tree.column("Phone", width=200, anchor="w")

# Add and configure scrollbars
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

# Layout table (Treeview) and vertical scrollbar
tree.place(x=2, y=150, width=725, height=300)
vsb.place(x=726, y=150, height=300)

# Adjust column and row configuration
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start listing records on startup
list_records()

root.mainloop()