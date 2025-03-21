# 📆 Diary Calendar

## ✨ Overview
**Diary Calendar** is your all-in-one personal task manager and daily journal, seamlessly integrated into an interactive calendar. Stay organized, track your progress, and never miss a task again! ✅

Whether you're managing your daily to-dos or keeping a journal, Diary Calendar makes it simple and efficient.

---

## 🚀 Features
- 🗓 **Interactive Calendar**  
  Easily navigate and click on any date to log or view tasks.
  
- 📝 **Task Management**  
  Organize tasks in a structured, numbered table with an intuitive interface.
  
- ✅ **Progress Tracking**  
  Mark tasks as completed and stay on top of your productivity goals.
  
- 💾 **Data Persistence**  
  All tasks and entries are securely saved in an SQLite database, ensuring no data is lost.

- 🔄 **Auto-Save & Retrieval**  
  Entries are automatically saved and can be retrieved even after restarting the app.

---

## 🛠 Requirements
Ensure you have the following installed on your system:
- 🐍 **Python 3.7+**  
  The app is built using Python, so make sure you have it installed.
  
- 📦 **Tkinter**  
  Comes pre-installed with Python and is used for the graphical interface.
  
- 🗃 **SQLite3**  
  Built into Python for managing the database.

---

## 🏃‍♂️ Getting Started
Follow these steps to get started with Diary Calendar:

1. **Clone or Download** this repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the script using the following command:
   ```sh
   python diary_calendar.py
   ```
4. **Click on a date** in the calendar to open the task manager for that day.
5. **Add, edit, or manage tasks** in the user-friendly task table.
6. **Mark tasks as completed** by checking them off.
7. Reopen the date to view or modify saved tasks.

---

## 🗄 Database Structure
All entries are stored in an SQLite database file named `diary.db`. The database follows this structure:

| Column Name   | Data Type | Description                          |
|---------------|-----------|--------------------------------------|
| 📅 `date`     | TEXT      | The date of the task entry (YYYY-MM-DD). |
| 🔢 `task_number` | INTEGER   | Sequential task ID for the day.       |
| 📝 `task`     | TEXT      | The description of the task.         |
| ✅ `completed` | INTEGER   | `0` for pending tasks, `1` for completed tasks. |

---

## 🔮 Future Enhancements
Here are some planned features to make Diary Calendar even better:
- ⏪ **Month Navigation**  
  Easily switch between months to view or manage tasks from previous or upcoming dates.
  
- 📤 **Export to CSV/TXT**  
  Export your tasks and entries for external use or backup.
  
- ☁ **Cloud Sync**  
  Sync your diary across devices and access it from anywhere.

---

## 👨‍💻 Author
Crafted with ❤️ by **Kevin Kinyanjui**.  
Contributions, feedback, and ideas are always welcome! Feel free to reach out or submit a pull request.

---

## 📜 License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.