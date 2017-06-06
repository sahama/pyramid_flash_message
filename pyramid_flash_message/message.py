from pyramid.threadlocal import get_current_request


class MessageQueue():
    danger = 'danger'
    warning = 'warning'
    info = 'info'
    success = 'success'

    def __init__(self, body='', message_type=info, source='', mapping={}, **kwargs):
        self.type = message_type
        self.body = body
        self.source = source
        self.mapping = mapping

        if not (source or body):
            self.body = 'no notice found'
            self.type = MessageQueue.info

    def add(self, body, message_type=None, source=None, mapping=None, **kwargs):
        if message_type:
            self.type = message_type
        if source:
            self.source = source
        if mapping:
            self.mapping = mapping
        self.body = body

        # TODO: check if message queue is full

        request = get_current_request()

        request.session.flash({"type": self.type, 'source': self.source, 'body': self.body, 'mapping': self.mapping})

    def __repr__(self):
        request = get_current_request()
        user = request.authenticated_userid
        return 'source:{0} ip:{4} type:{1} user:{2} message:{3}'.format(
            self.source,
            self.type,
            user,
            (self.body, self.mapping),
            (lambda x: x.remote_addr if x else '')(request)
        )

    def __str__(self):
        return self.__repr__()
