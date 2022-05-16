import typer
import os
from rich.console import Console
from rich.table import Table
import encoder

console = Console()
app = typer.Typer()

def show(plainText, data):    
    console.print(f"The plain text String: {plainText.decode('utf-8')}", style='bold blue')
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Type", style="dim", width=20)
    table.add_column("Output", min_width=20)

    for ops in data:
        table.add_row(ops, data[ops])
    
    console.print(table)

def stringCheck(string):
    if string == "":    
        plainText = bytes(input('Enter the string: '), 'utf-8')
    else: 
        plainText = bytes(string, 'utf-8')
    return plainText

def typeCheck(typ, output):
    if typ == "":     
        result = output
    else:
        result = {}
        if typ in output.keys():
            result[typ] = output[typ]
        else: 
            console.print("This type of Encoding or Hashing is not enabled in this tool.", style='bold red')
            result["Invalid operation"] = "I am sorry"
    return result

def verifyFile(file):
    return os.path.exists(file)

encode_help = 'Performs various types of encoding e.g. Base64, Base32, URL etc.'
@app.command(short_help=encode_help)
def encode(string: str=typer.Option("","--string", "-s", help="Enter the string value. However it is optional to use.", show_default=False), 
            type: str=typer.Option("","--type", "-t", help="Type of Encoding. If you don't know what type of hash to use. Simply don't use this option(--type)", show_default=False),
            list:bool=typer.Option(False,"--list", "-l", help="List the available encoding operations")):
    if list == True:
        console.print("Base64, Base32, URL, etc")
        exit(0)
    plainText = stringCheck(string=string)
    output = encoder.encoder(ptext=plainText)
    result = typeCheck(typ=type, output=output)
    show(plainText, result)

enhash_help = 'Perfoms various types of hashings such as SHA, MD5 etc'
@app.command(short_help=enhash_help)
def enhash(string: str=typer.Option("","--string", "-s", help="Enter the string value. However it is optional to use.", show_default=False), 
            file: str=typer.Option("","--file", "-f", help="Enter the file name", show_default=False),
            type: str=typer.Option("","--type", "-t", help="Type of hash. If you don't know what type of hash to use. Simply don't use this option(--type)", show_default=False),
            list: bool=typer.Option(False,"--list", "-l", help="List the available SHA operations", show_default=False)):
    if list == True:
        for h in encoder.hash_funcs:
            console.print(h) 
        exit(0)
    if file != "":
        if verifyFile(file):
            output = encoder.hash_func_itr(file)
            result = typeCheck(typ=type, output=output)
            show(bytes(file, 'utf-8'), result)
        else:
            console.print(f"{file} : File doesn't exist.", style="bold red")
    else:
        plainText = stringCheck(string=string)
        output = encoder.hasher(ptext=plainText)
        result = typeCheck(typ=type, output=output)
        show(plainText, result)

if __name__ == '__main__':
    app()








