import sys
import platform,os
clear = ""
if "Windows" in platform.system():
    clear = "cls"
if "Linux" in platform.system():
    clear = "clear"
os.system(clear)
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    print("""%s
              #Made by Odelly %s%s
               
    """ % (R, W, Y))


def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()
banner()
a = print("""# This is an encryption tool :)
[1] - AES
[2] - Blowfish
[0] - To Exit
""")
x = int(input(">>> "))
if x == 1:
    os.system(clear)
    from encryption import AES
elif x == 2:
    os.system(clear)

    os.system(clear)
    from encryption import Blowfish
elif x == 3:
    os.system(clear)

else:
    exit()