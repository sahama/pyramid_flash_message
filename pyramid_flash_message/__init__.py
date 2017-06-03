from .message import MessageQueue
def includeme(config):
    config.include('pyramid_jinja2')
    config.include('pyramid_layout')
    config.scan('pyramid_flash_message')
    config.add_route('flash_message', '/flash_message')

