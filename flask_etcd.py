# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

try:
    from urllib import parse as urlparse
except ImportError:
    import urlparse

import etcd


class Etcd(etcd.Client):
    DEFAULT_CONFIG = {
        'ETCD_CLIENT_URL': 'http://127.0.0.1:2379',
    }
    EtcdAlreadyExist = etcd.EtcdAlreadyExist
    EtcdKeyNotFound = etcd.EtcdKeyNotFound

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        for k,v in self.DEFAULT_CONFIG.items():
            app.config.setdefault(k, v)
        self.app = app

    @property
    def client(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'etcd'):
                uri = urlparse.urlparse(self.app.config['ETCD_CLIENT_URL'])
                ctx.etcd = etcd.Client(host=uri.hostname, port=uri.port or 2379)
            return ctx.etcd

    @property
    def election(self):
        return self.client.election

    @property
    def leader(self):
        return self.client.leader

    @property
    def machines(self):
        return self.client.machines

    def write(self, *args, **kwargs):
        """Proxy function for internal client object."""
        return self.client.write(*args, **kwargs)

    def set(self, *args, **kwargs):
        """Proxy function for internal client object."""
        return self.client.set(*args, **kwargs)

    def read(self, *args, **kwargs):
        """Proxy function for internal client object."""
        return self.client.read(*args, **kwargs)

    def get(self, *args, **kwargs):
        """Proxy function for internal client object."""
        return self.client.get(*args, **kwargs)

    def test_and_set(self, *args, **kwargs):
        """Proxy function for internal client object."""
        return self.client.test_and_set(*args, **kwargs)

    def update(self, *args, **kwargs):
        """Proxy function for internal client object."""
        return self.client.update(*args, **kwargs)

    def get_lock(self, *args, **kwargs):
        """Proxy function for internal client object."""
        return self.client.get_lock(*args, **kwargs)

    def watch(self, *args, **kwargs):
        """Proxy function for internal client object."""
        return self.client.watch(*args, **kwargs)
