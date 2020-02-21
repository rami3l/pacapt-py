import argparse


def run():
    parser = argparse.ArgumentParser()

    operations = parser.add_mutually_exclusive_group()
    # operations include Q(uery), R(emove), and S(ync).
    operations.add_argument("-Q", "--query", dest="Q", action="store_true")
    operations.add_argument("-R", "--remove", dest="R", action="store_true")
    operations.add_argument("-S", "--sync", dest="S", action="store_true")

    options = parser.add_argument_group()
    options.add_argument("-c", dest="c", action="count", default=0)
    options.add_argument("-i", dest="i", action="store_true")
    options.add_argument("-l", dest="l", action="store_true")
    options.add_argument("-o", dest="o", action="store_true")
    options.add_argument("-s", dest="s", action="store_true")
    options.add_argument("-u", dest="u", action="store_true")
    options.add_argument("-y", dest="y", action="store_true")

    parser.add_argument('targets', metavar='TARGETS', type=str,
                        nargs='*', help='the target packages to deal with')

    args = parser.parse_args()
    print(
        f"""
        ### Debug ###
        {args}
        """)
    return args
