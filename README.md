<!-- Code generated for API Clients. DO NOT EDIT. -->

# ngrok API client library for Python

This library wraps the [ngrok HTTP API](https://ngrok.com/docs/api) to make it
easier to consume in Python.

## Installation

This library is published on [PyPi](https://pypi.org/project/ngrok-api/):

    pip install ngrok-api

## Support

The best place to get support using this library is through the [ngrok Slack Community](https://ngrok.com/slack). If you find any bugs, please contribute by opening a new GitHub issue.

## Documentation

A quickstart guide and a full API reference are included in the [ngrok python API documentation](https://python-api.docs.ngrok.com).

## Quickstart

Please consult the [documentation](https://python-api.docs.ngrok.com) for additional examples.

    import ngrok

    # Construct the API client
    client = ngrok.Client("<API KEY>")

    # List all online tunnels
    for t in client.tunnels.list():
        print(t)

    # Create an IP policy that allows traffic from some subnets
    policy = client.ip_policies.create()
    for cidr in ["24.0.0.0/8", "12.0.0.0/8"]:
        client.ip_policy_rules.create(cidr=cidr, ip_policy_id=policy.id, action="allow")
