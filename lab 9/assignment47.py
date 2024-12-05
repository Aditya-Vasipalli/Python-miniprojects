#Program to merge two Python dictionaries
# Creating two dictionaries
dict1 = {
    "name": "Alice",
    "age": 25
}

dict2 = {
    "city": "New York",
    "country": "USA"
}

# Merging dictionaries using update() method
dict1.update(dict2)
print("Merged dictionary using update():", dict1)

# Merging using {**dict1, **dict2} syntax: 
merged_dict = {**dict1, **dict2}
print("Merged dictionary using {**dict1, **dict2}:", merged_dict)