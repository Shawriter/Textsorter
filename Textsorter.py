#!/usr/bin/env python
import os
import sys
from sys import stdout
global path
global s
BLUE, RED, WHITE, YELLOW, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;32m', '\033[0m'
stdout.write(GREEN+'''              ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |  Text Sorter    |  |  |     |         |      |
     |  |                               |  |  |/----|`---=    |      |
     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------' \n
Every line of text on the file is read, and those are sorted into alphabetical order. \n
Usage: Write path to the file you want to sort into alphabetical/numerical order, write "exit" to exit the program.\n''')


def main():

    while True:
        try:
            path = input("Path to file: ")
            if path == "exit":
                print("Exited.")
                sys.exit(0)
            else:
                pass
            s = str(path)
            file = open(s, 'r+')
            break
        except OSError:
            print("Invalid path, make sure the path is exact. \n")
            # return main()

    # s = str(path) #Muuttaa sanaksi

    #print (s)
    #file = open( s, 'r+')
    #read_data = file.read()
    sorttaaja(file, s)
    # file.close()


def sorttaaja(x, a):

    lista = []
    #sanat = str(lista)
    for line in x:
        lista.append(line)
        lista.sort()
    sanat = str(lista)
    x.close()
    file2 = open(a, 'w')
    for sana in lista:
        file2.write(sana)
    file2.close()
    print("Sorted \n")
    lopetus()


def lopetus():

    path2 = input("Sort more files y/n?: ")
    if path2 == "y":
        main()
    elif path2 == "n":
        print("Exited.")
        sys.exit(0)
    else:
        print("Invalid choice \n")
        lopetus()


if __name__ == "__main__":
    main()
