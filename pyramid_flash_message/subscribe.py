import math
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.request import Request
from pyramid.view import view_config
from pyramid_layout.panel import panel_config
from .message import MessageQueue


@panel_config(name='flash_message', renderer='pyramid_flash_message:flash_message_panel.jinja2')
def flash_message_panel(context, request: Request, per_page=None, read=True):

    if not per_page:
        default_per_page = request.registry.settings.get('flash_message.default_per_page', 20)
        per_page = int(request.params.get('per_page', default_per_page))

    print(per_page)
    if read:
        messages = request.session.pop_flash()[:per_page * -1: -1]
    else:
        messages = request.session.peek_flash()[:per_page * -1: -1]

    return {'flash_message_queue': messages}


@view_config(route_name='flash_message', permission='user', xhr=True, renderer='json')
@view_config(route_name='flash_message', permission='user', renderer='pyramid_flash_message:flash_message_view.jinja2')
def message_view(context, request: Request):
    page = int(request.params.get('message_page', 1))
    default_per_page = request.registry.settings.get('flash_message.default_per_page', 100)
    per_page = int(request.params.get('per_page', default_per_page))
    read = True if request.params.get('read') else False

    current_page = page

    if read:
        messages = request.session.pop_flash()[page * per_page:(page - 1) * per_page: -1]
    else:
        messages = request.session.peek_flash()[ page * per_page: (page - 1) * per_page: -1]

    total_page = math.ceil(len(messages) / per_page)

    return {'messages': messages, "current_page": current_page, 'total_page': total_page}


@subscriber(NewRequest)
def add_message(event):
    request = event.request
    message_queue = MessageQueue(request=request)
    request.message_queue = message_queue