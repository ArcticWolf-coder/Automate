import subprocess
import os
from multiprocessing import Pool


def run(task):
    # Do something with task here
    print("Handling {}".format(task))
    subprocess.call(["rsync", "-arq", src+task, dest])


home_path = os.path.expanduser('~')
src = home_path+"/data/prod/"
dest = home_path+"/data/prod_backup/"

if __name__ == "__main__":
    dirs = []

    for d in os.listdir(src):
        dirs.append(d)
    l = len(dirs)
    p = Pool(l)
    p.map(run, dirs)
