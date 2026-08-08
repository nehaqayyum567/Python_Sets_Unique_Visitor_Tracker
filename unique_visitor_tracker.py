# This project simulates a visitor tracking system for websites or applications. It uses Python sets to efficiently manage visitor data, ensuring only unique entries are counted.
# 🎯 Objectives & Steps
# Create Visitor Sets
# Make two sets: one for Day 1 visitors, another for Day 2 visitors.
# Each visitor can be represented by a name, ID, or email.
# Track Unique Visitors
# Use len(set) to count total unique visitors.
# Print the set to show actual visitor names.
# *Find Returning Visitors
# Use intersection() to find visitors who came on both days.*
# *Find New Visitors
# Use difference() to find visitors who came only on Day 2.*
# Find All Visitors Across Days
# Use union() to combine both sets and show all visitors.*
#* Check Membership
# Ask the user for a visitor name.
# Use in to check if that visitor exists in either set.*
# *Find Non‑Visitors (Optional Advanced Feature)
# Define a universal set of all registered users.
# Use difference() to find who didn’t visit on either day.*


# Create Visitor Sets

# Make two sets: one for Day 1 visitors, another for Day 2 visitors.

# Each visitor can be represented by a name, ID, or email.


#for this we have to amke a  list of tuples
Day1_visitor = {("Ali",34,"ali@gmail.com"), ("Alia",29,"alia@gmail.com"), ("Alian",90,"alian@gmail.com")}
Day2_visitor = {("Ahmed", 45, "ahmed5437@gmail.com"), ("Ahin",98,"ahin@gmail.com"), ("Zendaya", 89, "zendaya@gmail.com"),("Alia",29,"alia@gmail.com")}
                                                       
#Track Unique Visitors
# Use len(set) to count total unique visitors.
# Print the set to show actual visitor names.


print(len(Day1_visitor))

print(len(Day2_visitor))

unique_visitors = len(Day1_visitor.union(Day2_visitor))
print(unique_visitors)


# Find Returning Visitors
# Use intersection() to find visitors who came on both days.


both_days = Day1_visitor.intersection(Day2_visitor)
print("Visitors who came on both days:", both_days)

#Find New Visitors
# Use difference() to find visitors who came only on Day 2.

new_visitors = Day2_visitor.difference(Day1_visitor)
print("Visitors who came only on day2:", new_visitors)

# Find All Visitors Across Days
# Use union() to combine both sets and show all visitors.

All_Visitors = Day1_visitor.union(Day2_visitor)
print("All visitors across both days:", All_Visitors)

# Check Membership
# Ask the user for a visitor name.
# Use in to check if that visitor exists in either set.

name = input("Enter visitor name:")
age = int(input("Enter age:"))
email = input("Enter email:")
visitors = (name,age,email)

if visitors in Day2_visitor | Day1_visitor:
    print("Yes this name exists")
else:
    print("Not exist")
    

# *Find Non‑Visitors (Optional Advanced Feature)
# Define a universal set of all registered users.
# Use difference() to find who didn’t visit on either day.*


universal_set = {
     ("Ali",34,"ali@gmail.com"),
    ("Alia",29,"alia@gmail.com"),
    ("Alian",90,"alian@gmail.com"),
    ("Ahmed",45,"ahmed5437@gmail.com"),
    ("Ahin",98,"ahin@gmail.com"),
    ("Zendaya",89,"zendaya@gmail.com"),
    ("NewUser",50,"newuser@gmail.com") 
}

print(universal_set.difference(Day1_visitor.union(Day2_visitor)))