# PyFile
*technologies used*: Python, os.py

### Project overview

[//]: # (![Decision Tree 1]&#40;imgs/decision_tree.png&#41;)

"PyFile" automates file management.
Upon receiving a user-specified folder path containing a diverse array of files, the program
autonomously creates a designated folder. Subsequently, it systematically organizes the assorted files within this
folder based on their types.

### Goals

- automatically organize files within a specified folder based on their file extensions
- user has to input a folder path

### Approach

To kickstart the functionality of this program, my initial step was to establish a way to interact with the operating system.
I quickly identified the **os module** as a suitable solution and leveraged its *listdir()* method to retrieve a list of files requiring organization.
Following that, I implemented a *for* loop to iterate through each file, creating a new directory for each file extension using the *makedirs()* method.
To ensure the program doesn't create duplicate folders when there are multiple files with the same extension, I utilized the *exist_ok=True* parameter, which verifies if the target directory already exists. If it does, the creation of a new directory is omitted.


### Challenges Faced
### Lessons Learned
### Future Enhancements