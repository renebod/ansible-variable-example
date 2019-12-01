import os
import shutil
from jinja2 import Template


students = ['Alice Appleworth', 'Bob Bananarama', 'Carlos Carrot']

filename = "workshop_python_edition_01.yml"
f = open(filename,"w+")
f.write("version: '3.2'\n\nservices:\n\n")

with open('docker-compose_template.j2') as file_:
    template = Template(file_.read())


# Here we create student services
studentnumber = 0
for student in students:
     studentnumber = studentnumber + 1
     tm = template.render(student=student, number=str(format(studentnumber, '03d')))
     f.write(tm + "\n" * 3)


# This is for networks
f.write("networks:\n")
studentnumber = 0
for student in students:
    studentnumber = studentnumber + 1
    f.write("  student" + format(studentnumber, '03d') + ":\n")


# Copy the notebooks per student
if os.path.exists('./students'):
    shutil.rmtree('students')
studentnumber = 0
for student in students:
    studentnumber = studentnumber + 1
    shutil.copytree('notebooks/workshop_part_01', 'students/student' + format(studentnumber, '03d'))


studentnumber = 0
for student in students:
     studentnumber = studentnumber + 1
     print(student + " kan gebruik maken van host:8" + format(studentnumber, '03d'))
