import glob
import sys


def file_merge(path, extension):
    files = glob.glob(f"{path}\\*.{extension}")
    print(files)

    with open(f"{path}merged.{extension}", "wb") as f_new:
        for f in files:
            with open(f, "rb") as f_org:
                f_new.write(f_org.read())


if __name__ == "__main__":
    args = sys.argv
    if 3 <= len(args):
        file_merge(args[1], args[2])
    else:
        print("Arguments are too short")
