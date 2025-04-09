import os
import shutil
import time
import sys

print("Esse é um bot de organização de arquivos baseados no seu tipo (pdf, exe e etc).\nCuidado com o diretorio em que você colocar esse bot pois ele pode causar erros imprevistos")
# Path where the files are located and where folders will be created
path = input("Digite o caminho completo da pasta (exemplo: C:/Users/gusta/Separador): ")
if not os.path.isdir(path):
    print("Diretorio invalido, encerrando o programa")
    time.sleep(5)
    sys.exit()

# Get all file names in the specified directory
file_names = os.listdir(path)

# Initialize a set to hold unique file extensions
file_extensions = set()

# Populate the set with file extensions (in lowercase to avoid duplicates due to case differences)
for file_name in file_names:
    if os.path.isfile(os.path.join(path, file_name)):  # Ensure it's a file, not a directory
        extension = os.path.splitext(file_name)[1].lower()
        if extension:  # Ensure there is an extension
            file_extensions.add(extension)
# Move files to their respective folders
for file_name in file_names:
    # Skip directories
    if os.path.isdir(os.path.join(path, file_name)):
        continue

    # Get the file extension and corresponding folder name
    file_extension = os.path.splitext(file_name)[1].lower()
    if file_extension:
        folder_name = file_extension[1:] + " files"
        target_folder_path = os.path.join(path, folder_name)
        if not os.path.exists(target_folder_path):
            os.makedirs(target_folder_path)
        # Full path for the file's current location and the target location
        current_file_path = os.path.join(path, file_name)
        target_file_path = os.path.join(target_folder_path, file_name)

        # Move the file if it's not already in the target folder
        if not os.path.exists(target_file_path):
            shutil.move(current_file_path, target_file_path)
path = input("Prontinho, arquivos organizados")