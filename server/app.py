"""
    @TODO write docs
"""
import asyncio
from functools import partial
import argparse
from server.network.connections import handle_connection
from server.network.sendbacker import SendBacker


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
    """
    @TODO write docs
    """
    args = parse_args()

    loop = asyncio.get_event_loop()
    sender = SendBacker()
    handler = partial(handle_connection, sender=sender)
    run_accepts = asyncio.start_server(
        client_connected_cb=handler,
        host=args["address"],
        port=args["port"],
        loop=loop,
    )
    print("start server")
    try:
        server = loop.run_until_complete(run_accepts)
        loop.run_forever()
    except KeyboardInterrupt:
        print("Stopped...")
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()
        print("Close server")


if __name__ == "__main__":
    main()
