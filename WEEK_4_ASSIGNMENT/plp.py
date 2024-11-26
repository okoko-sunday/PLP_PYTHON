def file_reader():
    user = input('Write file name with extention name(e.g file.txt)\n Enter here: ')
    try:
        john = int(input('Select 1 or 2 for read or write \n 1 Read\n 2 Write\nEnter here:'))
        if john == 1:
            with open(user, 'r') as file:
                content = file.read()
                print(content)
        elif john == 2:
            write = input('Write or append here: ')
            with open(user, 'a') as file:
                file.write(write + '\n')
                
            with open(user, 'r') as file:
                content = file.read()
                print(content)
        else:
            print('invalid selection')
            
    except FileNotFoundError:
        print('File not found')
        
file_reader()
        