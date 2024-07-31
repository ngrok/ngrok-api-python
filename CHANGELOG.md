<!-- Code generated for API Clients. DO NOT EDIT. -->

## 0.12.0
* Renamed the Policy Module to the Traffic Policy Module on HTTP Edge Routes, TCP Edges, and TLS Edges, which allows you to configure rules that can be used to influence and control traffic to and from your upstream service. The Traffic Policy itself is now specified as either a JSON or YAML string.

## 0.11.0

* Added support for the Bot User API. The Bot User API allows you to manage the bots that are registered to your ngrok account. You can automate the creation, management, and deletion of bot users in your account.

* Added support for the Policy Module on HTTP Edge Routes, TCP Edges, and TLS Edges, which allows you to configure rules that can be used to influence and control traffic to and from your upstream service.

## 0.10.0

ENHANCEMENTS:

* Added `owner_id` field to the `api_key`, `credential`, and `ssh_credential` resources. If supplied at credential creation, ownership will be assigned to the specified User or Bot. Only admins may specify an owner other than themselves. Defaults to the authenticated User or Bot.
* Added `failover_backend`, `http_response_backend`, and `tunnel_group_backend` resources. A Failover backend defines failover behavior within a list of referenced backends. Traffic is sent to the first backend in the list. If that backend is offline or no connection can be established, ngrok attempts to connect to the next backend in the list until one is successful.
