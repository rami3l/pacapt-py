import subprocess as sp
import sys


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
            sp.check_call(["brew", "list", "|", "grep"]+args.targets)
        elif args.u:
            sp.check_call(["brew", "outdated", "|", "grep"]+args.targets)
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
            sp.check_call(["brew", "search"]+args.targets)
        elif args.u and args.y:
            # pacman -Syu
            sp.check_call(["brew", "update"])
            sp.check_call(["brew", "upgrade"]+args.targets)
        elif args.u:
            # pacman -Su
            sp.check_call(["brew", "upgrade"]+args.targets)
        elif args.y:
            # pacman -Sy
            sp.check_call(["brew", "update"]+args.targets)

        else:
            # pacman -Q
            raise NotImplementedError

    else:
        raise NotImplementedError
