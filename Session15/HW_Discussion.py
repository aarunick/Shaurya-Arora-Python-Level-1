# Homework Question 14 discussion
subjects=set() #Empty set

subjects.add("Python")
subjects.add("Java")
subjects.add("JavaScript")
subjects.add("C++")

print(subjects)

subjects.remove("Java")

print(subjects)


print("---------------")

# Homework Question 15 discussion

A = {2, 4, 6, 8, 10}
B = {6, 8, 10, 12, 14}

union=A.union(B)
print("UNION",union)

intersection=A.intersection(B)
print("INTERSECTION",intersection)
