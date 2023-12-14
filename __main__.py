from traceback import print_exc
from time import sleep

def main():
    pass

if __name__ == "__main__":
    try:
        main()
    except:
        print_exc()
        sleep(60*60*24)


