import argparse

def show_all(args): 
    for c in range(len(contents)):
        if "finish working" in contents[c].lower() and args.username.lower() in contents[c].lower():
            print("----------------------------------------------------------")
            while True:                
                print(contents[c], end="")
                if contents[c+1][0].isnumeric():
                    c += 1
                else:
                    break

def show_one(args):
    lines = []
    for i in range(len(contents)):
        if args.weekday.lower() in contents[i].lower() and args.month.lower() in contents[i].lower() and args.day.lower() in contents[i].lower():
            lines = contents[i:]
            print(contents[i], end="")

    for c in range(1, len(lines)):
        if "finish working" in lines[c].lower() and args.username.lower() in lines[c].lower():
            while True:
                print(lines[c], end="")
                if lines[c+1][0].isnumeric():
                    c += 1
                else: 
                    break
        elif "---" in lines[c]:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finish Working scan tool")
    parser.add_argument("username", type=str, help="Your Kakaotalk username")
    parser.add_argument("filepath", type=str, help="Exported Log path")
    parser.add_argument("-w", "--weekday", type=str, help="A specific weekday")
    parser.add_argument("-d", "--day", type=str, help="A specific day")
    parser.add_argument("-m", "--month", type=str, help="A specific month")
    args = parser.parse_args()

    _file = open(args.filepath, "r", encoding="utf8")
    contents = list(_file.readlines())
    
    if args.weekday and args.day and args.month:
        show_one(args)
    else:
        if not args.weekday and not args.day and not args.month:
            show_all(args)
        else:
            print("Missed information")