import tkinter as tk
from tkinter import messagebox, Toplevel, Frame, Entry, Checkbutton, IntVar, Button
import calendar
import sqlite3
from datetime import datetime  # Ensure this is properly imported

class DiaryCalendar:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Diary Calendar")
        
        # Automatically set the current year and month based on the system date
        today = datetime.now()
        self.current_year = today.year
        self.current_month = today.month
        
        # Connect to the SQLite database (or create it if it doesn't exist)
        self.conn = sqlite3.connect("diary.db")
        self.cursor = self.conn.cursor()
        
        # Create the database table for storing diary entries
        self.create_table()
        
        # Create the main widgets for the application
        self.create_widgets()
        
        # Display the calendar for the current month
        self.show_calendar()
    
    def create_table(self):
        # Create the "diary" table if it doesn't already exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS diary (
                date TEXT,               -- The date of the diary entry
                task_number INTEGER,     -- The task number (used for ordering)
                task TEXT,               -- The task description
                completed INTEGER,       -- Whether the task is completed (0 or 1)
                PRIMARY KEY (date, task_number) -- Composite primary key
            )
        """)
        self.conn.commit()  # Save changes to the database
    
    def create_widgets(self):
        # Create and display the header showing the current month and year
        self.header = tk.Label(self.root, text=f"{self.current_month} - {self.current_year}", font=("Arial", 16))
        self.header.pack()
        
        # Create a frame to hold the calendar grid
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack()
    
    def show_calendar(self):
        """
        Displays the calendar for the current month with weekday headers. 
        Each day is represented as a button, allowing the user to open the diary entry for that date.
        Empty days (before the first and after the last day of the month) are left blank.
        """
        # Set the first day of the week to Sunday
        calendar.setfirstweekday(calendar.SUNDAY)

        # Clear any existing widgets in the calendar frame
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        
        # Add weekday headers
        days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for col, day in enumerate(days_of_week):
            tk.Label(self.calendar_frame, text=day, width=5, font=("Arial", 10, "bold")).grid(row=0, column=col)
        
        # Get the days of the month as a matrix (weeks as rows, days as columns)
        month_days = calendar.monthcalendar(self.current_year, self.current_month)

        # Loop through each week and day to create buttons for the calendar
        for row_index, week in enumerate(month_days, start=1):  # Start from row 1 to keep headers on row 0
            for col_index, day in enumerate(week):
                if day == 0:  # Empty cells for days outside the current month
                    lbl = tk.Label(self.calendar_frame, text="", width=5, height=2)
                    lbl.grid(row=row_index, column=col_index)
                else:
                    # Create a button for each day with a command to open the diary entry
                    btn = tk.Button(self.calendar_frame, text=str(day), width=5, height=2, 
                                    command=lambda d=day: self.open_diary_entry(d))
                    btn.grid(row=row_index, column=col_index)

    def open_diary_entry(self, day):
        # Open a new window for the selected day's diary entry
        date = f"{self.current_year}-{self.current_month:02d}-{day:02d}"  # Format the date as YYYY-MM-DD
        
        # Fetch existing tasks for the selected date from the database
        self.cursor.execute("SELECT task_number, task, completed FROM diary WHERE date = ? ORDER BY task_number", (date,))
        existing_tasks = self.cursor.fetchall()
        
        # Create a new window for the diary entry
        entry_window = Toplevel(self.root)
        entry_window.title(f"Diary Entry - {date}")
        entry_window.geometry("500x400")
        
        # Create a frame to hold the task table
        table_frame = Frame(entry_window)
        table_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Add headers for the task table
        tk.Label(table_frame, text="No.", width=5).grid(row=0, column=0)
        tk.Label(table_frame, text="Task", width=40).grid(row=0, column=1)
        tk.Label(table_frame, text="Completed", width=10).grid(row=0, column=2)
        
        # Lists to store task entry widgets and completion status variables
        task_entries = []
        completed_vars = []
        
        # Function to add a new task row to the table
        def add_task(task_number=None, task_text="", completed=0):
            row = len(task_entries) + 1  # Determine the row number
            tk.Label(table_frame, text=str(row), width=5).grid(row=row, column=0)  # Task number label
            task_entry = Entry(table_frame, width=40)  # Task description entry
            task_entry.grid(row=row, column=1)
            task_entry.insert(0, task_text)  # Pre-fill with existing task text if provided
            
            completed_var = IntVar(value=completed)  # Checkbox for task completion
            check = Checkbutton(table_frame, variable=completed_var)
            check.grid(row=row, column=2)
            
            # Store the task entry and completion status
            task_entries.append((row, task_entry))
            completed_vars.append(completed_var)
        
        # Add existing tasks to the table
        for task_num, task, completed in existing_tasks:
            add_task(task_num, task, completed)
        
        # Function to save all tasks to the database
        def save_entries():
            # Delete existing tasks for the selected date
            self.cursor.execute("DELETE FROM diary WHERE date = ?", (date,))
            
            # Insert updated tasks into the database
            for num, (row, task_entry) in enumerate(task_entries, start=1):
                task_text = task_entry.get().strip()  # Get the task text
                completed_status = completed_vars[num - 1].get()  # Get the completion status
                if task_text:  # Only save non-empty tasks
                    self.cursor.execute("INSERT INTO diary (date, task_number, task, completed) VALUES (?, ?, ?, ?)", 
                                        (date, num, task_text, completed_status))
            self.conn.commit()  # Save changes to the database
            messagebox.showinfo("Success", "Tasks saved successfully!")  # Show success message
            entry_window.destroy()  # Close the diary entry window
        
        # Add a button to add new tasks
        add_button = Button(entry_window, text="Add Task", command=lambda: add_task())
        add_button.pack(pady=5)
        
        # Add a button to save tasks
        save_button = Button(entry_window, text="Save", command=save_entries)
        save_button.pack(pady=5)
    
    def __del__(self):
        # Close the database connection when the object is deleted
        self.conn.close()

# Main entry point of the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = DiaryCalendar(root)  # Create an instance of the DiaryCalendar class
    root.mainloop()  # Start the Tkinter event loop