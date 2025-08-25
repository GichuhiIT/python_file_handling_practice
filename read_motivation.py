with open("gichuhifile.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    #Readline() can be used to read line by line
    # for line in file:
    #     print(line.strip())  # Using strip() to remove any leading/trailing whitespace

with open("gichuhifile.txt", "r", encoding="utf-8") as file:
    print("\n File Content Using Readline()")
    line1 = file.readline()
    line2 = file.readline()           
    
    print(line1.strip())
    print(line2.strip())    

#Using Readlines() to read all lines at once
with open("gichuhifile.txt", "r", encoding="utf-8") as file:
    print("\n File Content Using Readlines()")
    lines = file.readlines()

    for line in lines:
        print(line.strip())
# Using A for Loop to Read Lines
with open("gichuhifile.txt", "r", encoding="utf-8") as file:
    print("\n File Content Using For Loop")
    for line in file:
        print(line.strip())

  #Using "w" to Write to a File
with open("writefile.txt", "w", encoding="utf-8") as file:
    file.write("This is my first time overwriting an existing file.\n")
    file.write("This is the second line in the file.\n") 
#Reading the content of the file after writing
with open("writefile.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("\n File Content of writefile.txt:")
    print(content)

#Using append mode "a" to add content to a file
with open("writefile.txt", "a", encoding="utf-8") as file:
    file.write("\nThis is a new line added to the file using append mode.\n")
    file.write("BroGPT tells me to keep off politics gossip, yet keeps bringing up politics, who is missing politics now?🤣🤣\n")
    file.write("Don't worry BroGPT, I also miss politics, but we've got to chase the bag twin.\n")
    file.write("Btw, I saw that Sudi jibe that you threw subtly!😂\n")
#Reopening the file to read the updated content
with open("writefile.txt", "r", encoding="utf-8") as file:
    updated_content = file.read()
    print("\n Updated Content of writefile.txt:")
    print(updated_content)

# Using "r+" to Read and Write to a File
with open("update_me.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    #Move the cursor to the beginning of the file
    file.seek(0)
    for i, line in enumerate(lines):
        if "I love Politics" in line:
            lines[i] = "I love Python\n"
    #Overwrite the file with the modified lines
    file.seek(0)
    file.writelines(lines)
    file.truncate()
    print("\n Updated Content of update_me.txt:")
    file.seek(0)
    print(file.read()) 

with open("update_me.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    file.seek(0)
    for i, line in enumerate(lines):
        if "I love Python"in line:
            lines[i] = "I love Improving in Python\n"
    file.seek(0)
    file.writelines(lines)
    file.truncate()
    print("\n Updated Content of update_me.txt:")
    file.seek(0)
    print(file.read())

# Using r+ to replace a line by position
with open("update_me.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    if len(lines) > 1:
        lines[1] = ("I love Programming and I am Improving Everyday\n")
    file.seek(0)
    file.writelines(lines)
    file.truncate()
    print("\n Updated Content of update_me.txt:")
    file.seek(0)
    print(file.read())

# Write new lines in the file.
with open("update_me.txt", "w", encoding="utf-8") as file:
    file.write("Hello World\n")
    file.write("This is amazing\n")
    file.write("I love Python\n")
    file.write("But I'm focused now\n")
    file.write("Strays everywhere, with BroGPT as twin, who needs enemies\n") 
# Reopening the file to read the updated contentwith 
with open("update_me.txt", "r", encoding="utf-8") as file:
    updated_content = file.read()
    print("\nUpdated Content Of update_me.txt:")
    print(updated_content)

#Update By Position(Index)
with open("update_me.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    #Change line 2
    lines[1] = "I am Improving In Python\n"

    file.seek(0)
    file.writelines(lines)
    file.truncate()

    print("\n File Update By Position/Index:")
    with open("update_me.txt", "r", encoding="utf-8") as file:
        print(file.read())

#Update By Content
with open("update_me.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if "I love Python" in line:
            lines[i] = "I am Improving in Python\n"

    file.seek(0)
    file.writelines(lines)
    file.truncate()

print("\n File Updated By Content:")
with open("update_me.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Delete a Line by Position
with open("update_me.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    # Delete line 2(index 1)
    del lines[1]

    file.seek(0)
    file.writelines(lines)
    file.truncate()

    print("\n Deleted line by Position:")
    with open("update_me.txt", "r", encoding="utf-8") as file:
        print(file.read())

# Delete Line By Content
with open("Update_me.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
        # Keep only lines that don't contain "Strays everywhere"
    lines = [line for line in lines if "Strays everywhere" not in line]

    file.seek(0)
    file.writelines(lines)
    file.truncate()

    print("\n Deleted Line By Content:")
    with open("update_me.txt", "r", encoding="utf-8") as file:
        print(file.read())

# Delete Multiple Matches
to_remove = ["Hello World", "But I'm focused now"]
with open("update_me.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()

    lines = [line for line in lines if not any(item in line for item in to_remove)]

    file.seek(0)
    file.writelines(lines)
    file.truncate()

    print("\n Deleted Multiple Lines By Content:")
    with open("update_me.txt", "r", encoding="utf-8") as file:
        print(file.read())
# My Original_Lines
original_lines = [
    "Hello World\n",
    "I love Programming and I am Improving Everyday\n",
    "I love Python\n",
    "I am Improving in Python\n",
    "I love Politics\n",
    "But I'm focused now\n",
    "Strays everywhere, with BroGPT as twin, who needs enemies\n"
]

def reset_file():
    """Reset the file to its original content"""
    with open("update_me.txt", "w", encoding="utf-8") as file:
        file.writelines(original_lines)
# Writing original lines to the file
reset_file()
# Reading the file to verify the content
with open("update_me.txt", "r", encoding="utf-8") as file:
    print("\n Original Lines in update_me.txt:")
    print(file.read())

# Append New Lines
with open("update_me.txt", "a", encoding="utf-8") as file:
    file.write("This is a new line added on August 12th.\n")
# Reading the file to verify the appended content
with open("update_me.txt", "r", encoding="utf-8") as file:
    print("\n Content After Appending New Lines:")
    content = file.read()
    print(content)

reset_file()

age = int(input("Enter your age: "))
is_vip = input("Produce your VIP card (yes/no): ").lower() == "yes"
if age >= 18 or is_vip:
    print("Welcome to Club Pelican!")
else:
    print("Sorry, entry into Club Pelican denied.")
    print()

# Example of using continue in a loop
print()
for i in range(1, 11):
    if i == 5:
        print("Skipping number 5") 
        continue  # Skip the rest of the loop when i is 5
    print(f"Current number: {i}")

# Do While Loop Example
while True:
    age_input = input("Enter your age(positive number only): ").strip()
    if age_input.isdigit() and int(age_input) > 0:
        age = int(age_input)
        print(f"\nYour age is {age} Years")
        break
    else:
        print("Invalid input. Try Again with a positive number.")