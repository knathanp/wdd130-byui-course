# This program is used to organize a class into clients and 3 person dev teams
# Give the assign_clients_and_developers() function a list of the names of your students
# and it will assign everyone as a client, a developer lead, and a two other dev teams.
# Or, give the function the number of students and it will organize the assignments with
# generic student names (student 1, student 2, etc.)

import pandas as pd
import random

def assign_clients_and_developers(num_students=35, students=None):
    if not students:
        students = [f"Student {i+1}" for i in range(num_students)]

    for attempt in range(100):  # Retry loop in case of failure
        lead_devs = students.copy()
        random.shuffle(lead_devs)

        # Make sure no student is their own lead dev
        if any(client == lead for client, lead in zip(students, lead_devs)):
            continue  # Try a different shuffle

        jr_dev_counts = {s: 0 for s in students}
        assignments = []

        try:
            for i, client in enumerate(students):
                lead_dev = lead_devs[i]

                # Exclude client and lead_dev from Jr. Dev candidates
                possible_jrs = [s for s in students if s != client and s != lead_dev and jr_dev_counts[s] < 2]

                if len(possible_jrs) < 2:
                    raise ValueError("Not enough Jr. Developers left to assign for this client.")

                jr_devs = random.sample(possible_jrs, 2)
                for dev in jr_devs:
                    jr_dev_counts[dev] += 1

                assignments.append([client, lead_dev] + jr_devs)

            # Confirm every student is a Jr. Dev exactly twice
            if all(count == 2 for count in jr_dev_counts.values()):
                df = pd.DataFrame(assignments, columns=["Client", "Lead Developer", "Jr. Developer", "Jr. Developer"])
                df.index = range(1, len(df) + 1)
                return df

        except ValueError:
            continue

    raise RuntimeError("Failed to generate a valid assignment after 100 attempts.")



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

# file_students_list = []
# with open("students_list_sp25_1.txt", "r") as student_file:
#     for student in student_file:
#         file_students_list.append(student.strip())
#     df = assign_clients_and_developers(students=file_students_list)
#     print(df)

# file_students_list = []
# with open("students_list_sp25_2.txt", "r") as student_file:
#     for student in student_file:
#         file_students_list.append(student.strip())
#     df = assign_clients_and_developers(students=file_students_list)
#     print(df)


df = assign_clients_and_developers(32)
print(df)
df = assign_clients_and_developers(34)
print(df)

