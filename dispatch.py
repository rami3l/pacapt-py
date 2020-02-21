import subprocess as sp
import sys
import re


def dispatch(args):
    sys.tracebacklimit = 0

    # Query
    if args.Q:
        if args.c:
            sp.check_call(["brew", "log"]+args.targets)
        elif args.i:
            sp.check_call(["brew", "info"]+args.targets)
        elif args.l:
            sp.check_call(["brew", "list"]+args.targets)
        elif args.o:
            raise NotImplementedError
        elif args.s:
            out = sp.check_output(["brew", "list"]).decode("utf-8")
            result = [ln for ln in out.splitlines()
                      if re.search(args.targets[0], ln)]
            for i in result:
                print(i)
        elif args.u:
            out = sp.check_output(["brew", "outdated"]).decode("utf-8")
            result = [ln for ln in out.splitlines()
                      if re.search(args.targets[0], ln)]
            for i in result:
                print(i)
        else:
            # pacman -Q
            raise NotImplementedError

    # Remove
    elif args.R:
        if args.s:
            raise NotImplementedError
        else:
            # pacman -R
            sp.check_call(["brew", "remove"]+args.targets)

    # Sync
    elif args.S:
        if args.c == 1:
            sp.check_call(["brew", "cleanup"]+args.targets)
        elif args.c == 2:
            sp.check_call(["brew", "cleanup", "-s"]+args.targets)
        elif args.c == 3:
            raise NotImplementedError
        elif args.i:
            sp.check_call(["brew", "info"]+args.targets)
        elif args.s:
            sp.check_call(["brew", "search"]+[" ".join(args.targets)])
        elif args.u or args.y:
            if args.y:
                # pacman -Sy
                sp.check_call(["brew", "update"]+args.targets)
            if args.u:
                # pacman -Su
                sp.check_call(["brew", "upgrade"]+args.targets)
        else:
            # pacman -Q
            raise NotImplementedError

    else:
        raise NotImplementedError
