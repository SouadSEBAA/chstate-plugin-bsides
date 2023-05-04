#!/usr/bin/python3

import sys, os
from .config import *

def check_args(action, chall_dir):    
    if action not in (ACTION_HIDE, ACTION_UNHIDE):
        raise ValueError(f'{action}: Invalid action given\nValid actions are : {ACTION_HIDE} , {ACTION_UNHIDE}')
    else:
        path = os.path.join(chall_dir, 'challenge.yml')
        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} : no such file or directory")

# update challenge in the platform
def update(chall_dir):
    e = os.system('ctfcli challenge sync ' + chall_dir)
    if e != 0:
        raise Exception(f"Challenge couldn't be updated ... ")

def chstate(self, action, chall_directory):
    try:
        check_args(action, chall_directory)

        new_state = STATE_HIDDEN if action == ACTION_HIDE else STATE_VISIBLE

        # define challenge.yml pathname
        challenge_yml_pathname = os.path.join(chall_directory, 'challenge.yml')

        # read content of file
        f = open(challenge_yml_pathname, 'r+')
        lines = f.readlines()

        # write changes
        f.seek(0)
        for line in lines :
            if line.startswith("state:") :
                line = f"state: {new_state}"
            f.write(line)
        
        # update challenge visibility in the platform
        update(chall_directory)

    except Exception as e:
        print(f"{str(e)}")
        exit(1)


if __name__ == '__main__' :
    try:
        if len(sys.argv) == 3 :
            chstate(sys.argv[1], sys.argv[2])
        else:
            raise Exception(f"Usage : chstate.py NEW_STATE CHALL_DIRECTORY ")

    except Exception as e:
        print(f"{str(e)}")
        exit(1)
