personal_details_tuple = ("John", "Doe", 16, 175, 65, "Computer Science")

print("Original Tuple:", personal_details_tuple)
print("Type before conversion:", type(personal_details_tuple))

personal_details_list = list(personal_details_tuple)

print("\nConverted List:", personal_details_list)
print("Type after conversion:", type(personal_details_list))

personal_details_list[5] = "Physics"
print("\nUpdated List (Subject changed):", personal_details_list)