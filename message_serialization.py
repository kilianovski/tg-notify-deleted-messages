from telethon.events import NewMessage
from telethon.tl.types import PeerChat
from telethon.tl.custom.message import Message
import pickle


class SerializableMessage():

    @staticmethod
    def serialize(message: NewMessage.Event):
        smsg = Message(
            id=message.id,
            to_id=message.to_id,
            date=message.date,
            message=message.message,
            out=message.out,
            from_id=message.from_id,
            fwd_from=message.fwd_from,)

        return pickle.dumps(smsg)

    @staticmethod
    def deseriaze(binary):
        return pickle.loads(binary)