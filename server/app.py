"""
    @TODO write docs
"""
import argparse
from server.network.HandlerConnects import HandlerConnects


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-ip",
        "--address",
        default="0.0.0.0",
        action="store",
        help="ip address",
    )
    parser.add_argument(
        "-p", "--port", default=8018, type=int, action="store", help="port"
    )
    return vars(parser.parse_args())


def main():
    args = parse_args()
    server = HandlerConnects(args)
    server.run()


if __name__ == "__main__":
    main()
