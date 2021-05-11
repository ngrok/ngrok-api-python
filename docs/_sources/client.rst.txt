Client
=====================================

:class:`~ngrok.Client` is the root object of the `ngrok-api` library. Construct
a Client with an API Key. Then you can access API Services as properties of the
Client object:

::

    import ngrok

    # construct the api client
    ng = ngrok.Client("<API KEY>")

    # list all ip policies
    for policy in ng.ip_policies.list():
        print(policy)
 
    # create an ngrok agent authtoken
    cred = api.tunnel_credentials.create()
    print(cred)

.. automodule:: ngrok
    :members: Client
    :undoc-members: Client
