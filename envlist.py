#!/data/miniconda3/envs/env1/bin/python

from filelock import FileLock
import hickle
import sys

# set constants
file_path = "/data/picasso/envlist.hkl"
lock_path = "/data/picasso/envlist.khl.lock"
time_out_secs = 60

# program modes
READ_MODE = 0
WRITE_MODE = 1
RESET_MODE = 2

# get number of arguments
nargs = len(sys.argv)
if nargs > 3:
    print('Usage: envlist; envlist env; envlist envprefix nenvs')
    exit
elif nargs > 2:
    pmode = RESET_MODE
    envprefix = sys.argv[1]
    nenvs = sys.argv[2]
elif nargs > 1:
    pmode = WRITE_MODE
    env = sys.argv[1]
else:
    pmode = READ_MODE

lock = FileLock(lock_path, timeout=time_out_secs)

with lock:
    if pmode == RESET_MODE:
        # create a list (named clist) of nevns environments with the 
        # prefix envprefix
        # add code here
        clist = [f"{envprefix}{i}" for i in range(int(nenvs))]
    else:
        # load hickle file
        clist = hickle.load(file_path)

        if pmode == WRITE_MODE:
            clist.append(env)
            # append item to end of list
            # add code her
            clist.append(env)
        else:
            env = clist.pop(0)
            # get and remove env from clist
            # add code here
            # return env name
            print(env)

    # save hickle file
    hickle.dump(clist, file_path, mode="w")
