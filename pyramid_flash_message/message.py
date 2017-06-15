from pyramid.threadlocal import get_current_request


class MessageQueue():
    danger = 'danger'
    warning = 'warning'
    info = 'info'
    success = 'success'

    def __init__(self, message_type=info, source='', mapping={}, domain=None, **kwargs):
        self.type = message_type
        self.source = source
        self.mapping = mapping

        if not (source):
            self.body = 'no notice found'
            self.type = MessageQueue.info

    def add(self, body, message_type=None, source=None, mapping=None, domain=None, **kwargs):
        if message_type:
            self.type = message_type
        if source:
            self.source = source
        if mapping:
            self.mapping = mapping

        self.domain = domain
        self.body = body

        # TODO: check if message queue is full

        request = get_current_request()

        request.session.flash({"type": self.type,
                               'source': self.source,
                               'body': self.body,
                               'mapping': self.mapping,
                               'domain': self.domain})

        # TODO: refactor it
        while True:
            try:
                request.session._set_cookie(request.response)
                break
            except:
                request.session['_f_'].pop(0)

    def __len__(self):
        request = get_current_request()
        return len(request.session.peek_flash())

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
