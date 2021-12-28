#!/usr/bin/python3

import sys
import subprocess
from tabulate import tabulate
import re

arguments = ["domains", "subdomains", "chars", "wordpress"]


def help():
    funciones = [["domains", "http//web.com --> http//web.something.com   "],
                 ["subdomains", "http//web.com --> http//subdomain.web.com"],
                 ["chars", "Characters like: @ % &...                   "],
                 ["wordpress", "Plugins 'and' themes 'for' wordpress"]]

    head = ["Argument", "Definition"]
    print(tabulate(funciones, headers=head, tablefmt="pretty"))
    print("[USE] ------> python3 " + sys.argv[0] + " argument")
    print("  ---> Example: python3 " + sys.argv[0] + " domains")
    print("[list of arguments] -> {}" .format(arguments))



def param(arguments):
    param = sys.argv[1]
    if (param in arguments):
        return param
    else:
        help()
        exit(1)


def finder(parameter):
    try:
        proc = subprocess.Popen(["/usr/bin/find ~/ -name *{}*" .format(parameter), ""], stdout=subprocess.PIPE, shell=True)
        (out,err) = proc.communicate()
        out = out.split()
        return out
    except FileNotFoundError:
        installed()


def rayas():
    raya = "-"
    print(raya * 100)


if len(sys.argv) == 1:
    help()

def installed():
    print("You don have the SecList diccionary... let's intall it")
    try:
        proc = subprocess.check_call(["/usr/bin/which git", ""], shell=True)
        subprocess.run("git clone https://github.com/danielmiessler/SecLists.git", shell=True)
    except subprocess.CalledProcessError as Error:
        subprocess.run("wget -c https://github.com/danielmiessler/SecLists/archive/master.zip -O SecList.zip", shell=True)
        subprocess.run("unzip SecList.zip", shell=True)
        subprocess.run("rm -f SecList.zip", shell=True)
    finally:
        print("SecList installed in /usr/share/ directory")

if len(sys.argv) == 2:
    parameter = param(arguments)
    rutas = finder(parameter)
    rayas()
    print(" Parameter -->  {} " .format(parameter))
    rayas()
    for i in rutas:
        i = i.decode('utf-8')
        if not re.match(r".*vscode.*", i):
            print("   {}" .format(i))
    rayas()





