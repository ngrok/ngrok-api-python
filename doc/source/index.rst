..
  Code generated for API Clients. DO NOT EDIT.


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
    client = ngrok.Client("<API KEY>")

    # list all online tunnels
    for t in client.tunnels.list():
        print(t)

    # create an ip policy the allows traffic from some subnets
    policy = client.ip_policies.create()
    for cidr in ["24.0.0.0/8", "12.0.0.0/8"]:
        client.ip_policy_rules.create(cidr=cidr, ip_policy_id=policy.id, action="allow")


Automatic Paging
----------------

The ngrok API pages all list resources but this library abstracts that away
from you. All response objects from any ``list()`` methods return an object that
implements an ``__iter__()`` method which will automatically fetch additional
pages for you.

::

    import ngrok

    client = ngrok.Client("<API KEY>")

    # list all ip policies, transparently fetching additional
    # pages for you if necessary
    for p in client.ip_policies.list():
        print(p)


Instance Methods
----------------

Instance methods like ``update`` and ``delete`` can be invoked on an instance of an
API object itself as well as directly without needing to first fetch the object.

::
    import ngrok

    client = ngrok.Client("<API KEY>")

    # update the metadata of a credential
    cred = client.credentials.get("cr_1kYyunEyn6XHHlqyMBLrj5nxkoz")
    cred.update(metadata=json.dumps({
        "server_name": "giraffe-1",
    }))

    # or do it in single call
    cred = client.credentials.update("cr_1kYyunEyn6XHHlqyMBLrj5nxkoz", metadata=json.dumps({
        "server_name": "giraffe-1",
    }))


Error Handling
--------------

The ngrok API returns detailed information when an API call fails. Consult the
section on :ref:`errors <errors>` for additional details.

::

    import ngrok

    client = ngrok.Client("<API KEY>")

    try:
        policy = client.ip_policies.create()
        client.ip_policy_rules.create(cidr="24.0.0.0/8", ip_policy_id=policy.id, action="not a valid action")
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
  agent_ingresses
  api_keys
  application_sessions
  application_users
  tunnel_sessions
  failover_backends
  http_response_backends
  static_backends
  tunnel_group_backends
  weighted_backends
  bot_users
  certificate_authorities
  credentials
  edges_https_routes
  edges_https
  https_edge_mutual_tls_module
  https_edge_tls_termination_module
  edge_route_backend_module
  edge_route_ip_restriction_module
  edge_route_request_headers_module
  edge_route_response_headers_module
  edge_route_compression_module
  edge_route_circuit_breaker_module
  edge_route_webhook_verification_module
  edge_route_o_auth_module
  edge_route_saml_module
  edge_route_oidc_module
  edge_route_websocket_tcp_converter_module
  edge_route_user_agent_filter_module
  edge_route_traffic_policy_module
  edges_tcp
  tcp_edge_backend_module
  tcp_edge_ip_restriction_module
  tcp_edge_traffic_policy_module
  edges_tls
  tls_edge_backend_module
  tls_edge_ip_restriction_module
  tls_edge_mutual_tls_module
  tls_edge_tls_termination_module
  tls_edge_traffic_policy_module
  endpoints
  event_destinations
  event_subscriptions
  event_sources
  ip_policies
  ip_policy_rules
  ip_restrictions
  reserved_addrs
  reserved_domains
  ssh_certificate_authorities
  ssh_credentials
  ssh_host_certificates
  ssh_user_certificates
  tls_certificates
  tunnels
