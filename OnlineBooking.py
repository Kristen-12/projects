import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import messagebox, simpledialog





# Function to create a database connection
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("booking_system.db")
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to create the bookings table
def create_table(connection):
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS booking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        phone TEXT NOT NULL,
        booking_date TEXT NOT NULL,
        booking_time TEXT NOT NULL,
        destination TEXT NOT NULL,
        departure TEXT NOT NULL,
        
        status TEXT NOT NULL CHECK(status IN ('booked', 'cancelled'))
    );
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

# Function to add a booking
def add_booking(connection, name, email,address, phone, booking_date, booking_time,destination,departure):
    insert_sql = '''
    INSERT INTO booking (name, email,address, phone, booking_date, booking_time, destination,departure,status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    status = 'booked'  # By default, the booking is confirmed as 'booked'
    try:
        cursor = connection.cursor()
        cursor.execute(insert_sql, (name, email,address, phone, booking_date, booking_time, destination,departure,status))
        connection.commit()
        messagebox.showinfo("Success", "Booking added successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to view all bookings
def view_bookings(connection):
    select_sql = "SELECT * FROM booking"
    try:
        cursor = connection.cursor()
        cursor.execute(select_sql)
        bookings = cursor.fetchall()
        return bookings
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        messagebox.showerror("Error", f"An error occurred: {e}")
        return []

# Function to cancel booking
def cancel_booking(connection, booking_id):
    update_sql = '''
    UPDATE booking
    SET status = 'cancelled'
    WHERE id = ?
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(update_sql, (booking_id,))
        connection.commit()
        messagebox.showinfo("Success", "Booking status updated to cancelled")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to delete a booking
def delete_booking(connection, booking_id):
    delete_sql = "DELETE FROM booking WHERE id = ?"
    try:
        cursor = connection.cursor()
        cursor.execute(delete_sql, (booking_id,))
        connection.commit()
        messagebox.showinfo("Success", "Booking deleted successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Functionality
class BookingSystemApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Online Booking System")
        self.root.geometry("600x400")

        # Create connection and table
        self.connection = create_connection()
        create_table(self.connection)

        # Create UI components
        self.create_widgets()

    def create_widgets(self):

        #background image
        self.bg_image = tk.PhotoImage(file="D:\Advanced Programming\wrld.png")
        self.background_label = tk.Label(self.root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)  

        # Labels
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        
        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.grid(row=1, column=0, padx=10, pady=5)

        self.label_address = tk.Label(self.root, text="Address:")
        self.label_address.grid(row=2, column=0, padx=10, pady=5)

        self.label_phone = tk.Label(self.root, text="Phone:")
        self.label_phone.grid(row=3, column=0, padx=10, pady=5)
        
        self.label_date = tk.Label(self.root, text="Booking Date (YYYY-MM-DD):")
        self.label_date.grid(row=4, column=0, padx=10, pady=5)
        
        self.label_time = tk.Label(self.root, text="Booking Time (HH:MM):")
        self.label_time.grid(row=5, column=0, padx=10, pady=5)

        self.label_destination  =tk.Label(self.root, text="Destination:")
        self.label_destination.grid(row=6, column=0,padx=10, pady=5)

        self.label_departure = tk.Label(self.root, text="Departure:")
        self.label_departure.grid(row=7, column=0, padx=10, pady=5)

        # Entry Fields
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)
        
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=1, column=1)

        self.entry_address = tk.Entry(self.root)
        self.entry_address.grid(row=2, column=1)
        
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=3, column=1)
        
        self.entry_date = tk.Entry(self.root)
        self.entry_date.grid(row=4, column=1)
        
        self.entry_time = tk.Entry(self.root)
        self.entry_time.grid(row=5, column=1)

        self.entry_destination = tk.Entry(self.root)
        self.entry_destination.grid(row=6, column=1)

        self.entry_departure = tk.Entry(self.root)
        self.entry_departure.grid(row=7, column=1)

        # Buttons
        self.button_add = tk.Button(self.root, text="Add Booking", command=self.add_booking)
        self.button_add.grid(row=8, column=0, padx=10, pady=20)

        self.button_view = tk.Button(self.root, text="View Bookings", command=self.view_bookings)
        self.button_view.grid(row=8, column=1, padx=10, pady=20)

        self.button_cancel = tk.Button(self.root, text="Cancel Booking", command=self.cancel_booking)
        self.button_cancel.grid(row=9, column=0, padx=10, pady=20)

        self.button_delete = tk.Button(self.root, text="Delete Booking", command=self.delete_booking)
        self.button_delete.grid(row=9, column=1, padx=10, pady=20)

    def add_booking(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        phone = self.entry_phone.get()
        booking_date = self.entry_date.get()
        booking_time = self.entry_time.get()
        destination = self.entry_destination.get()
        departure = self.entry_departure.get()

        if name and email and phone and booking_date and booking_time:
            add_booking(self.connection, name, email, address, phone, booking_date, booking_time,destination,departure)
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def view_bookings(self):
        bookings = view_bookings(self.connection)
        view_window = tk.Toplevel(self.root)
        view_window.title("View Bookings")
        
        tk.Label(view_window, text="Bookings").grid(row=0, column=0, padx=10, pady=10)

        row = 1
        for booking in bookings:
            tk.Label(view_window, text=f"ID: \t \t{booking[0]},\n Name:\t \t {booking[1]},\n Email: \t {booking[2]},\n Address: \t{booking[3]},\n Phone: \t \t {booking[4]}, \nDate: \t \t{booking[5]},\n Time: \t \t{booking[6]},\n Destination: \t{booking[7]}, \n Departure: \t{booking[8]},\n Status: \t \t{booking[9]}\n").grid(row=row, column=0, padx=10, pady=5)
            row += 1

    def cancel_booking(self):
        booking_id = self.get_booking_id()
        if booking_id:
            cancel_booking(self.connection, booking_id)
        else:
            messagebox.showerror("Error", "Please enter a valid booking ID")

    def delete_booking(self):
        booking_id = self.get_booking_id()
        if booking_id:
            delete_booking(self.connection, booking_id)
        else:
            messagebox.showerror("Error", "Please enter a valid booking ID")

    def get_booking_id(self):
        booking_id = simpledialog.askinteger("Input", "Enter Booking ID:")
        return booking_id

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingSystemApp(root)
    root.mainloop()
