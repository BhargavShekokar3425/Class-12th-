import os
location = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
import pickle
emp1={"rollno":101,"name":"student1","Marks":90}
emp2={"rollno":102,"name":"student2","Marks":56}
emp3={"rollno":103,"name":"student3","Marks":97}
emp4={"rollno":104,"name":"student4","Marks":19}
emp5={"rollno":105,"name":"student5","Marks":95}
emp6={"rollno":106,"name":"student6","Marks":92}
emp7={"rollno":107,"name":"student7","Marks":57}
emp8={"rollno":108,"name":"student8","Marks":99}
myfile=open(os.path.join(location,"sample5.dat"),"wb+")
pickle.dump(emp1,myfile)
pickle.dump(emp2,myfile)
pickle.dump(emp3,myfile)
pickle.dump(emp4,myfile)
pickle.dump(emp5,myfile)
pickle.dump(emp6,myfile)
pickle.dump(emp7,myfile)
pickle.dump(emp8,myfile)
print("succesful")
myfile.close()