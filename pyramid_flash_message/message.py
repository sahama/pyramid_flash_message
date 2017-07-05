from pyramid.threadlocal import get_current_request
import logging

log = logging.getLogger(__name__)


class MessageQueue():
    danger = 'danger'
    warning = 'warning'
    info = 'info'
    success = 'success'

    def __init__(self, message_type=info, source='', mapping={}, domain=None, **kwargs):
        self.type = message_type
        self.source = source
        self.mapping = mapping
        self.domain = domain

        if not (source):
            self.body = 'no notice found'
            self.type = MessageQueue.info

    def add(self, body, message_type=None, source=None, mapping=None, domain=None, **kwargs):
        if not message_type:
            message_type = self.type
        if not source:
            source = self.source
        if not mapping:
            mapping = self.mapping
        if not domain:
            domain = self.domain

        request = get_current_request()

        # TODO: check if session is enabled
        # TODO: refactor it
        try:

            request.session.flash({"type"   : message_type,
                                   'source' : source,
                                   'body'   : body,
                                   'mapping': mapping,
                                   'domain' : domain})

            # TODO: check if message queue is full
            # TODO: refactor it
            while True:
                try:
                    request.session._set_cookie(request.response)
                    break
                except:
                    log.warning('session if full. we have to remove some message message_queue.')
                    request.session['_f_'].pop(0)
        except:
            log.error("can not access to session. message can't add to message_queue")
            log.info("message is: source:{source} type:{type} body:{body} mapping:{mapping} domain:{domain}".format(
                type=message_type,
                source=source,
                body=body,
                mapping=mapping,
                domain=domain
                )
            )

    def __len__(self):
        request = get_current_request()
        return len(request.session.peek_flash())

    def __repr__(self):
        # TODO: this get just last message. modify to get list of all messages
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
