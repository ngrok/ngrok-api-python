
ngrok-api
#########

This is the official helper library for working with the `ngrok
HTTP API <https://ngrok.com/docs/api>`_ from Python.

Getting Started
===============

Installation
------------

::

    pip install ngrok-api


Quickstart Example
------------------

After you've installed the package, you'll need an API key. Create one on the
`API Keys page of your ngrok dashboard <https://dashboard.ngrok.com/api/keys>`_.

In your application's code, construct an :class:`~ngrok.Client` object
with the API key. API services can be accessed as properties of the client
object. That's it!

::

    import ngrok

    # construct the api client
    ng = ngrok.Client("<API KEY>")

    # list all online tunnels
    for t in ng.tunnels():
        print(t)

    # create an ip policy the allows traffic from some subnets
    policy = ng.ip_policies.create(action="allow")
    for cidr in ["24.0.0.0/8", "12.0.0.0/8"]:
        ng.ip_policy_rules.create(cidr=cidr, ip_policy_id=policy.id)
 

Transparent Paging
------------------

The ngrok API pages all list resources but this library abstracts that away
from you. All response objects from any ``list()`` methods return an object that
implements an ``__iter__()`` method which will automatically fetch additional
pages for you.

::

    import ngrok

    ng = ngrok.Client("<API KEY>")

    # list all ip policies, transparently fetching additional
    # pages for you if necessary
    for p in ng.ip_policies.list():
        print(p)


Instance Methods
----------------

Instance methods like ``update`` and ``delete`` can be invoked on an instance of an
API object itself as well as directly without needing to first fetch the object.

::

    # update the metadata of a credential
    cred = ng.credentials.get("cr_1kYyunEyn6XHHlqyMBLrj5nxkoz")
    cred.update(metadata=json.dumps({
        "server_name": "giraffe-1",
    }))

    # or do it in single call
    cred = ng.credentials.update("cr_1kYyunEyn6XHHlqyMBLrj5nxkoz", metadata=json.dumps({
        "server_name": "giraffe-1",
    }))


Error Handling
--------------

The ngrok API returns detailed information when an API call fails. Consult the
section on :ref:`errors <errors>` for additional details.

::

    import ngrok

    ng = ngrok.Client("<API KEY>")

    try:
        ng.ip_policies.create(action="not a valid action")
    except ngrok.Error as e:
        print("http status code", e.http_status_code)
        print("ngrok error code", e.error_code)
        print("ngrok error message", e.message)
        print("optional additional error-specific details", e.details)

API Reference
=============

.. toctree::
  :caption: API

  client
  datatypes
  errors

.. toctree::
  :caption: Services

  abuse_reports
  api_keys
  certificate_authorities
  credentials
  event_streams
  event_destinations
  ip_policies
  ip_policy_rules
  ip_restrictions
  ip_whitelist
  endpoint_configurations
  endpoint_logging_module
  endpoint_circuit_breaker_module
  endpoint_compression_module
  endpoint_tls_termination_module
  endpoint_ip_policy_module
  endpoint_mutual_tls_module
  endpoint_request_headers_module
  endpoint_response_headers_module
  endpoint_o_auth_module
  endpoint_webhook_validation_module
  endpoint_saml_module
  endpoint_oidc_module
  reserved_addrs
  reserved_domains
  ssh_certificate_authorities
  ssh_credentials
  ssh_host_certificates
  ssh_user_certificates
  tls_certificates
  tunnel_sessions
  tunnels
