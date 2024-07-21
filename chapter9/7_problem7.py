with open('log.txt')as f:
    lines=f.readlines()
    lineNo=1
    for line in lines:
        if('python' in line):
            print(f"python is present in line {lineNo} ")
        lineNo +=lineNo
        break
    else:
        print("python is not present")