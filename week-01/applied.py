from ISLP import load_data

college = load_data("College")
auto = load_data("Auto")

print(college.shape, auto.shape)
print(college.head())
print(auto.head())
