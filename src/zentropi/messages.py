# coding=utf-8

from .frames import Message
from .handlers import Registry


class Messages(Registry):
    def message(self, name, data=None, space=None, internal=False, source=None, reply_to=None):
        frame_ = Message(name=name, data=data, space=space, source=source, reply_to=reply_to)
        frame, handlers = self._handlers.match(frame=frame_)
        for handler in handlers:
            ret_val = self._trigger_frame_handler(
                frame=frame, handler=handler, internal=internal)
            if ret_val is not None:
                raise NotImplementedError('Send message as reply.')
        return frame
