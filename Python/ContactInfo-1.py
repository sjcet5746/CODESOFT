#5.Contact Information: Store name, phone number, email, and address for each contact.
#Add Contact: Allow users to add new contacts with their details.
#View Contact List: Display a list of all saved contacts with names and phone numbers.
#Search Contact: Implement a search function to find contacts by name or phone number.
#Update Contact: Enable users to update contact details.
#Delete Contact: Provide an option to delete a contact.
#User Interface: Design a user-friendly interface for easy interaction.
import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x400")

        self.contacts = {}  # Dictionary to store contacts

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Contact Book", font=('Arial', 16))
        self.title_label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email address:")
        address = simpledialog.askstring("Input", "Enter address:")
        if name in self.contacts:
            messagebox.showinfo("Info", "Contact already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Info", "Contact added successfully.")

    def view_contacts(self):
        self.result_text.delete(1.0, tk.END)
        for name, info in self.contacts.items():
            contact_info = f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n\n"
            self.result_text.insert(tk.END, contact_info)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter contact name or phone number:")
        if not search_term:
            return
        found_contacts = []
        for name, info in self.contacts.items():
            if search_term in name or search_term in info['phone']:
                contact_info = f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n\n"
                found_contacts.append(contact_info)
        if found_contacts:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, ''.join(found_contacts))
        else:
            messagebox.showinfo("Info", "No contact found.")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
        if name not in self.contacts:
            messagebox.showinfo("Info", "Contact not found.")
            return
        phone = simpledialog.askstring("Input", f"Enter new phone number (current: {self.contacts[name]['phone']}):")
        email = simpledialog.askstring("Input", f"Enter new email address (current: {self.contacts[name]['email']}):")
        address = simpledialog.askstring("Input", f"Enter new address (current: {self.contacts[name]['address']}):")
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Info", "Contact updated successfully.")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Info", "Contact deleted successfully.")
        else:
            messagebox.showinfo("Info", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()