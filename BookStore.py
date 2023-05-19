import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}"


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Order:
    def __init__(self, customer, book):
        self.customer = customer
        self.book = book

    def get_order_summary(self):
        return f"Order Summary:\nBook: {self.book}\nCustomer: {self.customer.name}\nEmail: {self.customer.email}"


class Shop:
    def __init__(self, book_list):
        self.book_list = book_list

        self.root = tk.Tk()
        self.root.title("Online Bookstore")
        self.root.geometry("400x300")

        self.book_var = tk.StringVar()
        self.book_var.set("Select a book")
        self.book_combobox = tk.OptionMenu(self.root, self.book_var, *self.book_list)
        self.book_combobox.pack(pady=20)

        self.order_button = tk.Button(self.root, text="Order", command=self.confirm_order)
        self.order_button.pack(pady=10)

        self.root.mainloop()

    def confirm_order(self):
        selected_book = self.book_var.get()
        if selected_book != "Select a book":
            choice = messagebox.askyesno("Order Confirmation", f"Confirm order for {selected_book}?", icon='question')
            if choice:
                name = simpledialog.askstring("Customer Details", "Enter your name:")
                email = simpledialog.askstring("Customer Details", "Enter your email:")
                if name and email:
                    customer = Customer(name, email)
                    book = next(book for book in self.book_list if str(book) == selected_book)
                    order = Order(customer, book)
                    self.show_order_summary(order)
                    self.show_payment_receipt(order)
                else:
                    messagebox.showwarning("Invalid Input", "Invalid input. Order canceled.")
        else:
            messagebox.showwarning("No Book Selected", "Please select a book.")

    def show_order_summary(self, order):
        summary = order.get_order_summary()
        messagebox.showinfo("Order Summary", summary)

    def show_payment_receipt(self, order):
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Payment Receipt")
        receipt_window.geometry("700x700")

        receipt_label = tk.Label(receipt_window, text="Payment Receipt", font=("Arial", 14, "bold"))
        receipt_label.pack(pady=10)

        # Generate random transaction ID
        transaction_id = random.randint(100000, 999999)
        transaction_id_label = tk.Label(receipt_window, text=f"Transaction ID: {transaction_id}", font=("Arial", 12))
        transaction_id_label.pack()

        book_label = tk.Label(receipt_window, text=f"Book: {order.book}", font=("Arial", 12))
        book_label.pack()

        customer_label = tk.Label(receipt_window, text=f"Customer: {order.customer.name}", font=("Arial", 12))
        customer_label.pack()

        email_label = tk.Label(receipt_window, text=f"Email: {order.customer.email}", font=("Arial", 12))
        email_label.pack()

        receipt_window.mainloop()


def read_book_list_from_file(file_path):
    book_list = []
    with open(file_path, 'r') as file:
        for line in file:
            title, author, genre, price = line.strip().split(",")
            price = float(price)
            book = Book(title, author, genre, price)
            book_list.append(book)
    return book_list


def main():
    file_path = "F:/Programming/JAVA/Lab Project/BookStore/books.txt"
    book_list = read_book_list_from_file(file_path)
    shop = Shop(book_list)


if __name__ == '__main__':
    main()
