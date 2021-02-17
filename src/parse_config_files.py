from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def main():
    #data = load(stream, Loader=Loader)
    #output = dump(data, Dumper=Dumper)

if __name__ == '__main__':
    main()


