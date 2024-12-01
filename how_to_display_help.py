import sys


def main():
    try:
        arguments = sys.argv
        how_to_display_help = arguments[0]
        r'--help' == arguments[1]
        r'--h' == arguments[2]
    except IndexError:
        print("Not enough arguments!")
        return 

    print("Script Name:", how_to_display_help)
    print('Help', (r'--h', r'--help'))
    print("That's how i can display help", r'--h')

def is_help(arguments):
    try:
      is_short_help = arguments.index('-h')
    except ValueError:
        is_short_help = False
    try:
        is_long_help = arguments.index('-help')
    except Value Error:
        is_long_help = False
    #is_long_help = arguments.index('--help')
    print("Czy jest short help", is_short_help)
    print("Czy jest long help", is_long_help)
        

if __name__ == "__main__":
    is_help(sys.argv)
    # main()




    
#Example input: python3 how_to_display_help smth smthsmth
