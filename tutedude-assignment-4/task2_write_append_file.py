# Write user input to a file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data written to output.txt")

# Append more data
more_text = input("Enter text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(more_text + "\n")

print("Data appended to output.txt")

# Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())