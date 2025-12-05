# import pickle

# data = {"name": "Whoo", "age": 21, "marks": [90, 85, 88]}

# with open("data.pkl", "wb") as f:
#     pickle.dump(data, f)

# print("Data saved successfully!")


# import pickle

# with open("data.pkl", "rb") as f:
#     data = pickle.load(f)

# print(data)


import pickle

class Student:
    def __init__(self, name, reg):
        self.name = name
        self.reg = reg

s1 = Student("Whoo", 123)

# save
with open("student.pkl", "wb") as f:
    pickle.dump(s1, f)

# load
with open("student.pkl", "rb") as f:
    obj = pickle.load(f)

print(obj.name, obj.reg)
