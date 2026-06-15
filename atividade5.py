import numpy as np

classes = int(input('Quantidade de turmas: '))

total = []
for i in range(classes):
    students = int(input(f'Estudantes da {i+1} turma: '))

    while students > 40:
        students = int(input(f'Só 40 por turmas: '))

    total.append(students)

media = np.mean(total)
print(f'Media de estudantes: {media:.0f}')