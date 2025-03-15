import pandas as pd


def students_and_examinations(students, subjects, examinations):
    exam_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    student_subjects = pd.merge(students, subjects, how='cross')
    data = student_subjects.merge(exam_count, how='left', on=['student_id', 'subject_name'])
    data = data.fillna(0)
    return data.sort_values(by=['student_id', 'subject_name'])


if __name__ == '__main__':

    data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
    students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype(
        {'student_id': 'Int64', 'student_name': 'object'})
    data = [['Math'], ['Physics'], ['Programming']]
    subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name': 'object'})
    data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'],
            [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
    examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype(
        {'student_id': 'Int64', 'subject_name': 'object'})
    print(students_and_examinations(students, subjects, examinations))