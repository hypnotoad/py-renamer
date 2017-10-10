import os
from tkinter import filedialog

'''
getPath()

*Opens a window (filedialog from tkinter) to get the path to the desired directory

*Arguments:
    - loop: boolean;
           True if you want the function to keep asking for a directory until a valid one is provided;
           False otherwise (not recommended);
'''


def getPath(loop):
    if loop:
        while True:
            path = filedialog.askdirectory()
            if path:
                return path
    else:
        return filedialog.askdirectory()


'''
rename()

*Renames the given file/directory, after checking if there isn't already a file/directory with the new name

*Arguments:
    - file_or_dir: string;
    - i: int (it'll be converted to string);
        It is the new file/directory name;
        It is increased in ascending order (unless reverse == True, then it's descending order)
    - directories: list of directories
    - files: list of files
'''


def rename(file_or_dir, i, directories, files):
    if os.path.isdir(file_or_dir) and str(i) not in directories:  # Directories
        os.rename(file_or_dir, str(i))
    else:                                                         # Files
        new_name = '{}.{}'.format(str(i), file_or_dir.split('.')[-1])  # Gets the file's extension
        if new_name not in files:
            os.rename(file_or_dir, new_name)


'''
order()

*This is the main function that wraps up all the others
 Renames files and/or directories in ascending or descending order, starting from *i*;
 It can avoid files that start with the string inside the variable *ignore*
 It can rename directories and files separately
 
*Arguments:
    - loop: boolean;
            If True, the getPath() function will keep asking for a directory until a valid one is provided;
    - ignore: string;
              Files/directories that start with this string will be ignored and won't be renamed;
              Default value: ' ', which doesn't make a difference, since files/directories can't start with whitespace;
    - rename_dir: boolean;
                  If True, directories are also renamed (you can set a separate counting for files and directories with
                  variable independent;
    - independent: boolean;
                   If True, files and directories will be renamed separately;
                   The rename_dir variable must be True in order to rename directories as well (not only files);
    - i: int;
         The counting starts from this integer;
    - reverse: boolean;
               If True, files/directories will be renamed in the opposite of alphabetical order;
'''


def order(loop=True, ignore=' ', rename_dir=False, independent=True, i=1, reverse=False):
    path = getPath(loop)

    if reverse:
        full_list = os.listdir(path)[::-1]
    else:
        full_list = os.listdir(path)

    os.chdir(path)

    directories = []
    files = []

    for item in full_list:  # Iterates through the list of files/directories and puts them into different lists
        if os.path.isdir(item):
            directories.append(item)
        else:
            files.append(item)

    x = i  # Stores the value of i, in case it needs to be reseted (i.e. if independent == True)

    if rename_dir:
        for dir in directories:
            if not dir.startswith(ignore):
                rename(dir, i, directories, files)
                i += 1

    if independent:
        i = x

    for file in files:
        if not file.startswith(ignore):
            rename(file, i, directories, files)
            i += 1
