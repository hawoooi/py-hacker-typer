from HackerTyper import Typer

typerSource = open('source.txt', 'r').read()
typerTextStyle = Typer.Style.RED
typerCharsPerStroke = 3

def typerStart():
    print('this is made by hawoi ;v; and is a clone of hackertyper.net')

def typerEnd():
    print('end of typer.')

myTyper = Typer(
    source = typerSource,
    textStyle = typerTextStyle,
    charsPerStroke = typerCharsPerStroke,
)

myTyper.Connect(typerStart, 'start')
myTyper.Connect(typerEnd, 'end')

myTyper.Run()