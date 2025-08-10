# Student Database Management System

This project is a simple **Python-based Student Database Management System** that allows storing, updating, deleting, and retrieving student records. It uses Python dictionaries to store data with each student assigned a unique ID.  

Users can add new students by entering their name, age, and major — the program automatically generates a new ID. The update feature allows modifying existing records, with **voice feedback** using the `pyttsx3` library to announce updated details. Records can also be retrieved by student ID or removed entirely.  

The program is easily customizable for different database needs, making it a useful example for beginners learning **data handling**, **dictionary manipulation**, **user input**, and **text-to-speech integration** in Python.

---

# Features
- **Add Students** — Add a new student record with auto-generated ID.
- **Update Students** — Modify an existing record with voice confirmation.
- **Retrieve Students** — View details of any student by ID.
- **Delete Students** — Remove a student record by ID.
- **Voice Feedback** — Announces updates using `pyttsx3`.

---

# Requirements
- Python 3.x
- Install `pyttsx3` library:
```bash
pip install pyttsx3
