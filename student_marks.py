def manage_student_marks():
    # Predefined dictionary of student marks
    student_data = {
        "Alice": 85,
        "Bob": 72,
        "Charlie": 90,
        "Diana": 68,
        "Ethan": 78
    }
    
    print("STUDENT MARK LOOKUP")
    print("-------------------")
    
    while True:
        name = input("\nEnter student name (or 'quit' to exit): ").strip()
        
        if name.lower() == 'quit':
            break
            
        if name in student_data:
            print(f"{name}'s marks: {student_data[name]}")
        else:
            print(f"Student '{name}' not found in records.")
            
        print("\nCurrent students in records:")
        print(", ".join(student_data.keys()))

if __name__ == "__main__":
    manage_student_marks()