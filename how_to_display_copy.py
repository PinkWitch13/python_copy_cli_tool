import shutil
def copy(source=input, clone=''): 
            if not source.endswith('.txt'):
                return print("It's not a txt file!")
            else:
                shutil.copy(source, clone)
copy("Kuba.txt", "copy_Kuba.txt")

        
        
 

