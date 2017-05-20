from .message import MessageQueue
def includeme(config):
    config.scan('pyramid_flash_message')

