.. _errors:

Errors
=====================================

When any method invoked against the ngrok API returns an error, a Exception of
:class:`ngrok.Error` will be raised.

The exception includes details that will allow you to robustly handle any error
returned by the API. The :attr:`ngrok.Error.error_code` field allows you to
handle any error in the ngrok system. Consult our `API Errors Documentation
<https://ngrok.com/docs/errors>`_ for the list of error codes the API may
return.

Handling Errors
---------------

If the API returns an unexpected 404, a :class:`ngrok.NotFoundError` will be
raised. Ensure that you check for it first because it is a subclass of :class:`ngrok.Error`.

.. code-block::

    try:
        client.ip_policies.get(id)
    except ngrok.NotFoundError as e:
        client.ip_policies.create()
    except ngrok.Error as e:
        # something else happened


Other validation errors are best distinguished by their error code. Consult our
documentation for the `list of all ngrok error codes <https://ngrok.com/docs/errors>`_.

::

    try:
        client.edges.https.create(hostports=["url-without-port.ngrok.io"])
    except ngrok.Error as e:
        if e.error_code == "ERR_NGROK_7104":
            # handle a specific condition
        else:
            raise


If the ngrok API fails with an undefined response or there is some kind of
network error, there are no guarantees about the type of exception thrown
at that point it is best to use a naked ``except`` block or to catch a ``RuntimeError``.

::

    try:
        client.ip_policies.create()
    except RuntimeError:
        # an unexpected network error that you could retry


Exception Classes
-----------------

.. automodule:: ngrok
    :members: Error, NotFoundError
