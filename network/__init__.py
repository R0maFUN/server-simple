import asyncio


connections = []


async def run_connection(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
) -> None:
    connections.append(writer)
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info("peername")
        if not data:
            print(f"Close connection from {addr}")
            break
        message = data.decode()
        text = message.replace("\n", "")
        print(f"received {text} from {addr}")
        for wr in connections:
            if wr != writer and not wr.is_closing():
                wr.write(message.encode())

    writer.close()
    try:
        connections.remove(writer)
    except ValueError:
        print("Why connection is absent?")
