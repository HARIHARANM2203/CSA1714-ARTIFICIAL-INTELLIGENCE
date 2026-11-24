
% Student Database Facts
student(arun, cse, 21).
student(bala, it, 22).
student(chitra, cse, 20).
student(divya, ece, 21).

% Rule to find students by department
department_student(Dept, Name) :-
    student(Name, Dept, _).

% Rule to find students above a given age
above_age(Age, Name) :-
    student(Name, _, StudentAge),
    StudentAge > Age.
