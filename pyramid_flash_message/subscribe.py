import os
from pyramid.threadlocal import get_current_request
from pyramid_layout.panel import panel_config
from pyramid.events import NewRequest
from pyramid.events import subscriber
from .message import MessageQueue


@panel_config(name='flash_message', renderer='pyramid_flash_message:flash_message.jinja2')
def flash_message(context, request):
    return {}

@subscriber(NewRequest)
def add_message(event):
    request = event.request
    message_queue = MessageQueue(request=request)
    request.message_queue = message_queue
