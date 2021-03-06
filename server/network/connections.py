import asyncio


async def handle_connection(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter, sender
) -> None:
    sender.add_connection(writer)
    while True:
        data = await reader.read(1024)
        address = writer.get_extra_info("peername")
        if not data:
            print(f"Close connection from {address}")
            break
        message = data.decode()
        text = message.replace("\n", "")
        print(f"received {text} from {address}")
        sender.send_msg(writer, message)
    sender.remove_connection(writer)
