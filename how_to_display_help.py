import sys


def main():
    try:
        arguments = sys.argv
        how_to_display_help = arguments[0]
        help = arguments[1]
        copy = arguments[2]
    except IndexError:
        print("Not enough arguments!")
        return 

    print("Script Name:", how_to_display_help)
    print("file name:", help)
    print("That's how i can display help", copy)

if __name__ == "__main__":
    main()

    
#Example input: python3 how_to_display_help smth smthsmth 
