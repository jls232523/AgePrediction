import os
import shutil
# Organizes the images files of UTK dataset into 116 folders that correspond to each age class

def main():
    #tries until valid path is found
    while True:
        try:
            path = input('Enter path to files: ')
        except OSError:
            print('Error finding directory')
        else:
            make_dirs(path)
            break

#creates a 116 folders for the corresponding age classes and move the images accordingly
def make_dirs(path):
    files = os.listdir()
    os.chdir(path)
    for i in range(1,117):
        # make directory for age
        os.mkdir(str(i))
        # find all files of that age and move them to the new directory
        for file in files:
            age = file[:file.index('_')]
            if age == str(i):
                shutil.move(os.getcwd()+'/'+file, os.getcwd()+'/'+str(i))

if __name__ == '__main__':
    main()



