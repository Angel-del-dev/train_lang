import sys
import lib.lexer as l

file_ext = 'tr'



if __name__ == '__main__':
    file_name = sys.argv[1]
    extension = file_name.split('.')[1]
    
    if(extension == file_ext):
        with open(file_name) as f:
            file_content = f.read()
            l.load(file_content)
    else:
        print('File extension is not valid')