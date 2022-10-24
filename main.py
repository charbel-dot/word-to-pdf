import os
from termcolor import colored # add colors to text the easy way
from database import GUI

try:
    from docx2pdf import convert # @credits to whoever made this package

# handling any error while importing
except ImportError:
    print("docx2pdf package not found in your machine! Do you want to install it using pip (y/n) ? : ")
    userInput = str(input(""))

    if userInput == 'y' or userInput == 'Y':
        os.system("pip install docx2pdf")

    elif userInput == 'n' or userInput == 'N':
        print("\n\aExiting..")
        os.system("exit")

    else:
        print("\nPlease Enter yes or no! (y/n)")

# display a message if any file is found
def message() -> None:
    count = 0
    given_path = os.getcwd()
    ext = ["docx"]

    for path, dirs, files in os.walk(given_path):
        for file in files:
            if file == None or file == "":
                return print('\nCould not find any files ending with .docx extension\tTry again\a')
            for e in ext:
                if file.endswith(e):
                    count += 1

    if count >= 1:
        text = colored(f"Number of files found in this directory: {count}", 'blue', attrs=[])
        print(text)

    else:
        text = colored('* No files were found in this directory\a!', 'red', attrs=[])
        print(text)

message()

# finding files on the machine ending with .docx extension

def find(ext: list) -> str:
    global _path

    for path, dirs, files in os.walk(_path):
        for file in files:
            if file == None or file == "":
                return print('\nCould not find any files ending with .docx extension\tTry again\a')
            for e in ext:
                if file.endswith(e):
                    yield file

# converting files
def convert_to_pdf() -> None:
    for files in find(["docx"]):
        convert(files)

# work done
def done() -> None:
  print("\a\nConverted Successfully, Opening your folder! ")
  os.system('explorer .') # opening the folder

def open_folder() -> None:
    print("Opening your folder...\a")
    os.system("explorer .")

# exiting the program
def exit_program() -> None:
    print('\nExiting..')
    os.system('cls')
    os.system('exit')

# GUI part
print(GUI)

# taking inputs
try:
    response = str(input("Choose: "))
    username = os.getlogin()

except KeyboardInterrupt:
    print("\nExiting...\a")

if response == '1':
    _path = os.getcwd()
    os.chdir(_path)
    convert_to_pdf()
    done()

elif response == '2':
    _path = f"C:\\users\\{username}\\Documents\\"
    os.chdir(_path)
    open_folder()

elif response == '3':
    try:
        _path = str(input("\nEnter your path: "))
        if _path != "":
            os.chdir(_path)
            convert_to_pdf()
            done()

    except KeyboardInterrupt:
        print("\nExiting..\a")

elif response == '4':
    exit_program()

else:
  print("\aPlease enter a valid choice!")
