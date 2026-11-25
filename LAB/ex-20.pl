% Student, teacher, subject, and subject-code database.
% student_teacher_subject_code(Student, Teacher, Subject, Code).
student_teacher_subject_code("Anu", "Rao", "Artificial Intelligence", "CS401").
student_teacher_subject_code("Bala", "Meena", "Database Systems", "CS402").
student_teacher_subject_code("Chitra", "Rao", "Logic Programming", "CS403").
student_teacher_subject_code("Dinesh", "Meena", "Computer Networks", "CS404").

% Query the full record:
% ?- student_teacher_subject_code("Anu", Teacher, Subject, Code).
% Teacher = "Rao",
% Subject = "Artificial Intelligence",
% Code = "CS401".

% Find students taught by a given teacher:
students_of_teacher(Teacher, Student) :-
    student_teacher_subject_code(Student, Teacher, _, _).
