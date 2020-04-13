def print_menu():
    print ('-' * 20)
    print(' PyHouse - Welcome')
    print ('-' * 20)

    print('[1] Register New Item')
    print('[2] Display Catalog')
    print('[3] Display Items with No Stock')
    print('[4] Update Stock Manually')
    print('[5] Print Stock Value')
    print('[6] Remove Item From Stock')
    print('[7] List Categories')

    print('[x] Exit')

def print_header(title):
    print('\n') # \n\n 2 blank lines
    print('-' * 60)
    print(title)
    print('-' * 60)