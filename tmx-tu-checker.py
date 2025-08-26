tu_stack = []
file = input("Please enter the name of your file: ")
with open(file, "r", encoding="utf-8") as f:
    for lineno, line in enumerate(f, 1):
        if "<tu" in line:
            tu_stack.append(lineno)
        if "</tu" in line:
            if tu_stack:
                tu_stack.pop()
            else:
                print(f"Extra </tu> at line {lineno}")

if tu_stack:
    print("Unclosed <tu> tag(s) starting at line(s):", tu_stack)
else:
    print("All <tu> tags properly closed.")
