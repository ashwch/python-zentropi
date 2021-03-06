# coding=utf-8
"""
Copyright 2017 Harshad Sharma

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os

from . import fields
from . import utils
from .agent import Agent
from .agent import on_timer
from .connections import Connection
from .connections.in_memory import InMemoryConnection
from .events import Events
from .fields import Field
from .frames import Command
from .frames import Event
from .frames import Frame
from .frames import State
from .spaces import Spaces
from .symbols import KINDS
from .zentropian import Zentropian
from .zentropian import on_event
from .zentropian import on_message
from .zentropian import on_state

__version__ = "0.1.1"

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

__all__ = [
    '__version__',
    'Agent',
    'BASE_PATH',
    'Command',
    'Connection',
    'Event',
    'Events',
    'Frame',
    'Field',
    'fields',
    'InMemoryConnection',
    'KINDS',
    'on_event',
    'on_message',
    'on_state',
    'on_timer',
    'Spaces',
    'State',
    'utils',
    'Zentropian',
]
