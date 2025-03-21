import pandas as pd
import random

def assign_clients_and_developers(num_students=35, students=None):
    # Create a list of student IDs
    if not students:
        students = [f"Student {i+1}" for i in range(num_students)]

    # Initialize the assignments
    assignments = []

    # Shuffle students for lead developer assignment
    lead_developers = students.copy()
    random.shuffle(lead_developers)

    # Initialize a dictionary to track how many times a student has been hired
    hired_count = {student: 0 for student in students}

    # Assign lead developers and additional developers
    for i, client in enumerate(students):
        # Lead developer is predetermined
        lead_dev = lead_developers[i]
        hired_count[lead_dev] += 1

        # Select 2 more developers ensuring unique and valid hires
        possible_devs = [s for s in students if s != client and s != lead_dev and hired_count[s] < 3]
        
        if len(possible_devs) < 2:
            raise ValueError("Not enough students to satisfy the constraints. Consider increasing the number of students.")

        additional_devs = random.sample(possible_devs, 2)

        # Update hired count
        for dev in additional_devs:
            hired_count[dev] += 1

        # Record the assignment
        assignments.append([client, lead_dev] + additional_devs)

    # Create DataFrame
    #pd.DataFrame(assignments, columns=["Client", "Lead Developer", "Developer 2", "Developer 3"]).to_csv('output_client_dev_wdd130.csv', index=False)
    df = pd.DataFrame(assignments, columns=["Client", "Lead Developer", "Developer 2", "Developer 3"])
    df.index = range(1, len(df) + 1)
    return df

# Example usage:
example_students_list = ["Albert Allen", 
                         "Bob Barker", 
                         "Carl Calzone", 
                         "David Dodson", 
                         "Erwin Engles", 
                         "Faith Findle", 
                         "Gerty Garland", 
                         "Howard Hughes", 
                         "Ichi Ipson", 
                         "Jacob Johnson", 
                         "Karl Knight", 
                         "Luey Lewis", 
                         "Manford Mann", 
                         "Nelson Norton", 
                         "Oscar Oswald", 
                         "Patsy Peterson", 
                         "Quinn Quizlton", 
                         "Rob Rymer", 
                         "Sandra Silverton",
                         "Terry Thompson",
                         "Ulysses Underwood",
                         "Victor Valdez",
                         "Wally Winchester",
                         "Xavier Xanadu",
                         "Yolanda Yurt",
                         "Zander Zacharias"]
df = assign_clients_and_developers(students=example_students_list)
print(df)
