class _Style:
    """ANSI color codes"""
    BLACK          = '\033[30m'
    RED            = '\033[31m'
    GREEN          = '\033[32m'
    YELLOW         = '\033[33m'
    BLUE           = '\033[34m'
    MAGENTA        = '\033[35m'
    CYAN           = '\033[36m'
    WHITE          = '\033[37m'
    RESET          = '\033[0m'

class Typer:
    Style = _Style()

    def __init__(self, source='', textStyle='', charsPerStroke=3):
        """
        Creates the Hacker Typer. Note that this doesn't run immeadiately.

        :param source: the string that the hacker typer will gradually print out
        :param textStyle: the colors for the hacker typer, use Typer.Style for colors
        :param charsPerStroke: the amount characters printed out each time you hit a key
        :return: the hacker typer object
        """
        from readchar import readchar as _Getch
        from signal import signal, SIGINT, SIGHUP, SIGTERM
        from requests import get

        if source == '':
            source = get('https://raw.githubusercontent.com/duiker101/Hacker-Typer/master/kernel.txt').text
            
        if textStyle =='':
            textStyle = ''

        self.source = source
        self.sourceLen = len(self.source)
        self.charsPerStroke = charsPerStroke
        self.textStyle = textStyle
        self.currentChar = 0
        self.nextChar = 0
        self.getch = _Getch

        def exitHandler(signum, frame):
            """Exit handler"""
            print(self.Style.RESET, flush=True)

            if hasattr(self, 'functionEnd') == True:
                self.functionEnd()

            exit(0)

        signal(SIGINT , exitHandler)
        signal(SIGHUP , exitHandler)
        signal(SIGTERM, exitHandler)


    def Connect(self, function, position: str):
        """
        Connect the function to the start / end of the hacker typer.

        :param function: the function to be connected
        :param position: the position the function will be connected, has to be 'front' or 'end'
        """
        if position.lower() == 'start':
            self.functionStart = function
        elif position.lower() == 'end':
            self.functionEnd = function
        else:
            print('"position" argument must be "start" or "end"')

    def Run(self):
        """Runs the hacker typer."""

        def addString(string=''):
            """Adds text to the screen without adding a newline character"""
            print(self.textStyle + string, end='', flush=True)

        if hasattr(self, 'functionStart') == True:
            self.functionStart()

        while True:
            getch = self.getch()

            nextChar = self.currentChar + self.charsPerStroke

            if nextChar >= self.sourceLen:
                nextChar = self.sourceLen
                addString(self.source[self.currentChar:nextChar])
                print(self.Style.RESET)
                break
            else:
                addString(self.source[self.currentChar:nextChar])

            self.currentChar = nextChar

        if hasattr(self, 'functionEnd') == True:
            self.functionEnd()