import asyncio
from functools import partial


class SendBacker:
    def __init__(self):
        self.connections = []

    def add_connection(self, connection: asyncio.StreamWriter) -> None:
        """
        @TODO check connections
        """
        self.connections.append(connection)

    def remove_connection(self, writer: asyncio.StreamWriter) -> None:
        writer.close()
        try:
            self.connections.remove(writer)
        except ValueError:
            print("Why connection is absent?")

    @staticmethod
    def sender(
        writer_dst: asyncio.StreamWriter,
        writer_src: asyncio.StreamWriter,
        message: str,
    ) -> None:
        if writer_dst != writer_src and not writer_dst.is_closing():
            writer_dst.write(message.encode())

    def send_msg(self, writer, message: str) -> None:
        sender_with_msg = partial(
            SendBacker.sender, writer_src=writer, message=message
        )
        list(map(sender_with_msg, self.connections))
