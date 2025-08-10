print("This project is about storing,updating,deleting and retrieving data from a database.")

# Can be customized to fit specific database requirements
students = { 0 : { "ALICE" : { "age": 20, "major": "Computer Science" } } ,
            1 : { "BOB" : { "age": 22, "major": "Mathematics" } },
            2 : { "CHARLIE" : { "age": 23, "major": "Physics" } },
            3 : { "DAVID" : { "age": 24, "major": "Chemistry" } },
            4 : { "EVE" : { "age": 25, "major": "Biology" } } }

# Function to add a new student
name = input("Enter the student name: ").upper()
age = int(input("Enter age: "))
major = input("Enter major: ")
new_id = max(students.keys()) + 1  # Auto-incrementing key
students[new_id] = {name: {"age": age, "major": major}}

# To update a student's information
update_id = int(input("Enter the student ID to update (or -1 to skip): "))
if update_id in students:
    name = input("Enter the new student name: ").upper()
    age = int(input("Enter the new age: "))
    major = input("Enter the new major: ")
    students[update_id] = {name: {"age": age, "major": major}}
    # Voice Over
    import pyttsx3
    engine = pyttsx3.init()
    # getting details of current voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female, 0 for male
    engine.say("The student ID u updated was: " + str(update_id) + " and their name is: " +
               name + " and their age is: " + str(age) + " and their major is: " + major)
    engine.runAndWait()

# To retrieve a student's information
students_id = input("Enter the student ID to retrieve: ")
students.get(students_id)  # PRO TIP! = Enter none to see updated database 
print(students.get(students_id))

# To delete a student's ID
deleted = students.pop(int(input("Enter the student ID to delete: ")), None)
print("Deleted:", deleted)

# Display the updated student database
print("Updated student database is :\n", students)