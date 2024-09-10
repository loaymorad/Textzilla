import os

def divider(file, batch_size):
    
    with open(file, 'r') as f:
        lines = f.readlines()  # Read all lines at once

    if len(lines) == 0:
        return
    
    file_number = 1
    
    folder_name = file.split(".")[0]
    os.mkdir(folder_name)
    for i in range(0, len(lines), batch_size): # range(start, stop, step) => 0,100,200,...
        batch = lines[i:i + batch_size]  # 0 - 100, 100 - 200, ...
        with open(f'{folder_name}/{file_number}.txt', 'w') as fl:
            fl.writelines(batch)
        file_number += 1
        
def compiner(*files):
    with open("big.txt", 'w') as big_file:
        
        for file in files:
            with open(file, 'r') as small_file:
                big_file.writelines(small_file.readlines())
    
def menu():
    print("Menu:")
    print("divider")
    print("compiner")
    print("exit")
    choice = input("python main.py <choiceFromMenu> file.txt <NumberOfDivisionIfThere> ")
    return choice            
        
if __name__ == "__main__":
    import sys
    
    while True:
        menu()
        
        if sys.argv[1] == "compiner":
            files = sys.argv[2:]
            compiner(*files)
        
        elif sys.argv[1] == "divider":
            file = sys.argv[2]
            batch_size = sys.argv[3]
            
            divider(file, int(batch_size))
        elif sys.argv[1] == "exit":
            sys.exit()
        else:
            continue