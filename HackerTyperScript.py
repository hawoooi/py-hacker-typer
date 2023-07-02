from readchar import readchar

class Style:
    BLACK          = '\033[30m'
    RED            = '\033[31m'
    GREEN          = '\033[32m'
    YELLOW         = '\033[33m'
    BLUE           = '\033[34m'
    MAGENTA        = '\033[35m'
    CYAN           = '\033[36m'
    WHITE          = '\033[37m'
    RESET          = '\033[0m'

source = open('source.txt', 'r').read()
sourceLen = len(source)

currentChar = 0
nextChar = 0

textStyle = Style.GREEN
charsPerStroke = 3

def addStr(string=''):
    global textStyle
    print(textStyle + string, end='', flush=True)

print('Recreated from hackertyper.net, made by hawoi ;v;\n')

while True:
    char = readchar()

    nextChar = currentChar + charsPerStroke
    
    if nextChar >= sourceLen:
        nextChar = sourceLen
        addStr(source[currentChar:nextChar])
        print(Style.RESET)
        break
    else:
        addStr(source[currentChar:nextChar])

    currentChar = nextChar