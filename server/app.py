import asyncio
from server.network import run_connection


def main():
    loop = asyncio.get_event_loop()
    run_accepts = asyncio.start_server(
        client_connected_cb=run_connection,
        host="127.0.0.1",
        port=8018,
        loop=loop,
    )

    try:
        server = loop.run_until_complete(run_accepts)
        loop.run_forever()
    except KeyboardInterrupt:
        print("Stopped...")
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()


if __name__ == "__main__":
    main()