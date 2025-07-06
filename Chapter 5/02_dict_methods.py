marks = {
    "Sushmitha": 100,
    "Nithin": 56,
    "Rithesh": 23,
    0: "Sushmitha"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

print(marks.get("Sushmitha")) # Prints Sushmitha's marks
print(marks.get("DIDI", "Key not found")) # Returns "Key not found
print(marks["DIDI"]) # Returns an error