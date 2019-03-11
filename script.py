import sys
import os
from dotenv import load_dotenv
from pathlib import Path


def createPathFile(file):
    return Path('.') / file


load_dotenv(dotenv_path=createPathFile(sys.argv[2]))


def replaceSymbolInFile(file, configFile):
    print("File before replace:" + "\n")
    print(file.read() + "\n")
    file.seek(0)

    for char in file.read():
        configFile.seek(0)
        if os.getenv(char) is not None and char in configFile.read():
            txt = file.read().replace(char, os.getenv(char))
            file.seek(0)
            file.write(txt)
    file.seek(0)
    print("File after replace:" + "\n")
    print(file.read())


if __name__ == "__main__":
    try:
        file = open(createPathFile(sys.argv[1]), 'r+')
        configFile = open(createPathFile(sys.argv[2]), 'r')
    except Exception as e:
        print("You have a problem with your files \n " + str(e))
        sys.exit()
    replaceSymbolInFile(file, configFile)
