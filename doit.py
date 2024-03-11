import os
import tkinter as tk
from tkinter import messagebox

def create_folder_structure(root_directory, num_features):
    for i in range(1, num_features + 1):
        feature_name = f"feature_{i}"
        feature_path = os.path.join(root_directory, feature_name)
        os.makedirs(feature_path)
        
        subfolders = ['screens', 'widgets', 'models', 'services', 'view_models']
        for subfolder in subfolders:
            os.makedirs(os.path.join(feature_path, subfolder))

def create_folders():
    directory = entry_directory.get()
    num_features = int(entry_num_features.get())

    try:
        create_folder_structure(directory, num_features)
        messagebox.showinfo("Success", "Folder structure created successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Folder Structure Creator")

# Label and Entry for directory path
label_directory = tk.Label(root, text="Directory Path:")
label_directory.grid(row=0, column=0, padx=5, pady=5)
entry_directory = tk.Entry(root, width=50)
entry_directory.grid(row=0, column=1, padx=5, pady=5)

# Label and Entry for number of features
label_num_features = tk.Label(root, text="Number of Features:")
label_num_features.grid(row=1, column=0, padx=5, pady=5)
entry_num_features = tk.Entry(root)
entry_num_features.grid(row=1, column=1, padx=5, pady=5)

# Button to create folders
button_create = tk.Button(root, text="Create Folders", command=create_folders)
button_create.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Start GUI main loop
root.mainloop()
