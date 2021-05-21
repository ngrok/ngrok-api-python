# ngrok API client library for Python

This library wraps the [ngrok HTTP API](https://ngrok.com/docs/api) to make it
easier to consume in Python.

## Installation

This library is published on [PyPi](https://pypi.org/project/ngrok-api/)

    pip install ngrok-api

## Documentation

A quickstart guide and a full API reference are included in the [ngrok python API documentation](https://python-api.docs.ngrok.com)

## Quickstart

Please consult the [documentation](https://python-api.docs.ngrok.com) for additional examples.

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
