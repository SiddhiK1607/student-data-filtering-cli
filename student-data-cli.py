student_data = [ 
    {"name": "Alice", "major": "CS", "cgpa": 7.8}, 
    {"name": "Sima", "major": "IT", "cgpa": 8.1}, 
    {"name": "Manu", "major": "CS", "cgpa": 9.5}, 
    {"name": "Diana", "major": "DS", "cgpa": 7.9}, 
    {"name": "Riya", "major": "DS", "cgpa": 8.0}, 
] 
def display_results(results, title): 
    print(f"{title} ({len(results)} Found) ") 
    if not results: 
        print("No matches.") 
    else: 
        for student in results: 
            print(f"Name: {student['name']}, Major: {student['major']}, CGPA:{student['cgpa']:.1f}") 
def run_filter_program(data): 
    while True: 
        print("==Filter Menu ===") 
        print("1. Filter by Major | 2. Filter by Min CGPA | 3. Exit") 
        choice = input("Enter choice (1-3): ") 
        if choice == '1': 
            target = input("Enter Major: ").upper() 
            results = [s for s in data if s['major'] == target] 
            display_results(results, f"Major = {target}") 
        elif choice == '2': 
            try: 
                min_cgpa = float(input("Enter Min CGPA: ")) 
                results = [s for s in data if s['cgpa'] >= min_cgpa] 
                display_results(results, f"Min CGPA >= {min_cgpa:.1f}") 
            except ValueError: 
                print("Error: Invalid number.") 
        elif choice == '3': 
            print("Exiting. Goodbye!") 
            break 
        else: 
            print("Invalid choice.") 
if __name__ == "__main__": 
    run_filter_program(student_data) 