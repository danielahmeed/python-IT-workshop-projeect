import matplotlib.pyplot as plt
import numpy as np

semester_marks = {
    "Nilim": {
        "1st": [7.6, 8.7, 9],
        "2nd": [3.4, 6.7, 4.5],
        "3rd": [8.0, 8.5, 8.9],
        "4th": [9.0, 8.4, 7.0],
        "5th": [7.5, 8.5, 8.0]
    },
    "Nayan": {
        "1st": [6, 10, 5],
        "2nd": [9.0, 6.5, 4.2],
        "3rd": [4.6, 7.56, 8.0],
        "4th": [9.2, 6.4, 7.1],
        "5th": [7.95, 8.5, 8.4]
    },
    "Kunal": {
        "1st": [9.2, 4.5, 6.7],
        "2nd": [9.6, 7.4, 5.3],
        "3rd": [4.3, 8.8, 7.8],
        "4th": [9.1, 6.2, 7.4],
        "5th": [8.5, 4.0, 5.6]
    },
    "Vandita": {
        "1st": [8.5, 4.7, 7.9],
        "2nd": [8.2, 7, 5.2],
        "3rd": [7.1, 6.6, 6.3],
        "4th": [8.9, 4.2, 8.4],
        "5th": [8.8, 4.7, 9.6]
    },
    "Sovit": {
        "1st": [9.3, 4.6, 7.7],
        "2nd": [5.6, 7.7, 5.8],
        "3rd": [4.3, 8.8, 8.7],
        "4th": [9, 6.3, 8.4],
        "5th": [8.5, 4.9, 7.6]
    },
    "Siddhartha": {
        "1st": [9.7, 7.5, 7.7],
        "2nd": [9.1, 9.4, 8.3],
        "3rd": [5.6, 8.8, 7.8],
        "4th": [7.5, 6.2, 8.4],
        "5th": [8.5, 4.7, 9.6]
    },
    "Daniel": {
        "1st": [9.7, 4.9, 7.9],
        "2nd": [9.6, 7.2, 9.9],
        "3rd": [4.4, 8.98, 8.8],
        "4th": [9.3, 7.2, 7.9],
        "5th": [8.1, 6.0, 9.6]
    },
    "Subham": {
        "1st": [9.2, 8.5, 8.7],
        "2nd": [9.5, 7.4, 5.3],
        "3rd": [6.4, 8.8, 7.5],
        "4th": [9.2, 6.7, 6.9],
        "5th": [8.5, 4.7, 5.9]
    },
    "Rahul": {
        "1st": [9.2, 4.7, 6.8],
        "2nd": [9.9, 7.4, 8.3],
        "3rd": [4.9, 8.8, 7.8],
        "4th": [9.1, 6.4, 7.4],
        "5th": [8.5, 8.9, 5.6]
    },
}

def plot_student_marks(student_name):
    if student_name not in semester_marks:
        print("Student not found!")
        return
    student_data = semester_marks[student_name]

    semesters = list(student_data.keys())
    marks = list(student_data.values())
    marks_np = np.array(marks)
    num_subjects = marks_np.shape[1]
    bar_width = 0.15
    r = np.arange(len(semesters))

    # Define color palette
    colors = plt.cm.tab10(np.linspace(0, 1, num_subjects))

    # Define subject names
    subject_names = ['Maths', 'Physics', 'Chemistry']  # Add more subjects as needed

    # Plotting bars for each subject with custom colors and labels
    for i in range(num_subjects):
        plt.bar(r + i * bar_width, marks_np[:, i], width=bar_width, color=colors[i], edgecolor='black', linewidth=1.5, label=subject_names[i])

    plt.xlabel('Semesters', fontweight='bold', fontsize=12)
    plt.ylabel('SGPA', fontweight='bold', fontsize=12)
    plt.xticks([r + bar_width * ((num_subjects - 1) / 2) for r in range(len(semesters))], semesters, fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylim(0, 10)
    plt.title(f'Marks vs Semesters for {student_name}', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.gca().spines['top'].set_visible(False)  # Remove top spine
    plt.gca().spines['right'].set_visible(False)  # Remove right spine

    # Add data labels above each bar
    for i in range(len(semesters)):
        for j in range(num_subjects):
            plt.text(r[i] + j * bar_width, marks_np[i, j] + 0.2, f'{marks_np[i, j]:.1f}', ha='center', va='bottom', fontsize=9)

    # Add legend with custom colors
    plt.legend(loc='upper left', fontsize=10)

    plt.tight_layout()  # Adjust layout to prevent clipping

    plt.show()

# Rest of your code remains unchanged

choice = input("Enter the Name: ")

if choice.lower() == 'nilim':
    plot_student_marks("Nilim")
elif choice.lower() == 'nayan':
    plot_student_marks("Nayan")
elif choice.lower() == 'kunal':
    plot_student_marks("Kunal")
elif choice.lower() == 'sovit':
    plot_student_marks("Sovit")
elif choice.lower() == 'siddhartha':
    plot_student_marks("Siddhartha")
elif choice.lower() == 'daniel':
    plot_student_marks("Daniel")
elif choice.lower() == 'subham':
    plot_student_marks("Subham")
elif choice.lower() == 'rahul':
    plot_student_marks("Rahul")
else:
    print("Student not found!")