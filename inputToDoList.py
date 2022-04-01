toDoFile =open("TODOLIST.txt" ,"w")

toDoList = ""

toDoItem = input("Enter a to-do list item: ")
while toDoItem != "exit":
    toDoList = toDoList + toDoItem +"\n"
    toDoFile.write(toDoList)
    toDoItem = input("Enter a to-do list item: ")

toDoFile.close()