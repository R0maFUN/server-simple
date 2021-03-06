"""
    @TODO write docs
"""
import asyncio
from functools import partial
from server.network.connections import handle_connection
from server.network.sendbacker import SendBacker


def main():
    """
    @TODO write docs
    """
    loop = asyncio.get_event_loop()
    sender = SendBacker()
    handler = partial(handle_connection, sender=sender)
    run_accepts = asyncio.start_server(
        client_connected_cb=handler,
        host="127.0.0.1",
        port=8018,
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
