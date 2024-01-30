import os
import glob


def get_ordered_files(dir_name):
    # Get list of all files only in the given directory
    list_of_files = filter(os.path.isfile, glob.glob(dir_name + '/*'))

    # Sort list of files based on creation time in ascending order
    list_of_files = sorted(list_of_files, key=os.path.getmtime)

    return list_of_files

def site(path, out, reversed):

    f = get_ordered_files(path)
    if reversed:
        f = f[::-1]
    f = [f'"{s}"' for s in f]
    s = ' '.join(f)
    exec_string = f"img2pdf {s} -o {out}"
    return exec_string


front_out = "out/front.pdf"
back_out = "out/back.pdf"
merged_out = "out/merged.pdf"

os.system(site("./front", front_out, False))
os.system(site("./back", back_out, True))
os.system(f"pdftk A={front_out} B={back_out} shuffle A B output {merged_out}")
