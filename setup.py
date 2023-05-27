import os

# Get the path of the current directory
current_dir = os.getcwd()


# Create the .bat file content
bat_content = """
@echo off
python "{script_path}" %*
""".format(script_path=os.path.join(current_dir, "main.py"))

# create Scripts folder
if not os.path.exists(os.path.join(current_dir, "Scripts")):
    os.mkdir(os.path.join(current_dir, "Scripts"))

# Define the .bat file path
bat_file_path = os.path.join(os.environ["SystemRoot"], "System32", "qr.bat")

# Write the .bat file content to the file
with open(bat_file_path, "w") as file:
    file.write(bat_content)
