# Code generated for API Clients. DO NOT EDIT.

import json
import os
import unittest
from typing import Optional, Mapping, Union, Dict, Any

import ngrok
import ngrok.http_client

def setup_api_client():
    c = ngrok.Client(os.getenv("NGROK_API_KEY"))
    mock = MockHTTPClient()
    if not os.getenv('TEST_NO_MOCK', False):
        c.http_client = mock
    elif os.getenv('TEST_DEBUG', False):
        c.http_client = RecordingHTTPClient(c.http_client.api_key, c.http_client.base_url)
    return c, mock

class TestQuickstartExamples(unittest.TestCase):
    def test_quickstart_examples(self):
        c, mock = setup_api_client()

        # list all online tunnels
        mock.returns(mock_tunnels_list)
        tunnels = c.tunnels.list()
        for t in tunnels:
            pass
        assert len(tunnels.tunnels) == 1

        # create an ip policy the allows traffic from some subnets
        mock.returns(mock_ip_policy)
        policy = c.ip_policies.create()
        for cidr in ["24.0.0.0/8", "12.0.0.0/8"]:
            mock.returns(mock_ip_policy_rule)
            rule = c.ip_policy_rules.create(cidr=cidr, ip_policy_id=policy.id, action="allow")
            assert rule.action == "allow"

        # list all ip policies, transparently fetching additional
        # pages for you if necessary
        mock.returns(mock_ip_policy_rules_list)
        for p in c.ip_policies.list():
            pass

        # create a credential
        mock.returns(mock_cred)
        cred = c.credentials.create()
        assert cred.metadata == ""

        # get a credential
        mock.returns(mock_cred)
        cred = c.credentials.get("cr_27nRxf2wJGXDKuTjMkUpaWMoN1B")
        assert cred.metadata == ""

        # update the metadata of a credential
        mock.returns(mock_updated_cred)
        cred.update(metadata=json.dumps({
            "foo": "bar",
        }))
        mock.returns(mock_updated_cred)
        cred = c.credentials.get("cr_27nRxf2wJGXDKuTjMkUpaWMoN1B")
        assert cred.metadata == "{foo:bar}"

        # or do it in single call
        mock.returns(mock_updated_cred)
        cred = c.credentials.update("cr_27nRxf2wJGXDKuTjMkUpaWMoN1B", metadata=json.dumps({
            "foo": "bar",
        }))
        assert cred.metadata == "{foo:bar}"

        with self.assertRaises(ngrok.Error):
            mock.returns(mock_ip_policy)
            policy = c.ip_policies.create()
            mock.returns(ngrok.Error(error_code=404, message="error", http_status_code=404, details=None))
            c.ip_policy_rules.create(cidr="24.0.0.0/8", ip_policy_id=policy.id, action="not a valid action")

def test_domains():
    c, mock = setup_api_client()

    mock.returns(mock_domains_list)
    c.reserved_domains.list()

    mock.returns(mock_reserved_domain)
    domain = c.reserved_domains.create(domain="foo.ngrok.io.lan")
    mock.returns(mock_reserved_domain)
    domain = c.reserved_domains.get(domain.id)
    assert domain.domain == "foo.ngrok.io.lan"

    mock.returns(None)
    domain.delete()

def test_addrs():
    c, mock = setup_api_client()

    mock.returns(mock_addrs_list)
    c.reserved_domains.list()

    mock.returns(mock_reserved_addr)
    addr = c.reserved_addrs.create()
    mock.returns(mock_reserved_addr)
    addr = c.reserved_addrs.get(addr.id)
    assert addr.addr == "1.tcp.ngrok.io.lan:20020"

    mock.returns(None)
    addr.delete()

def test_certificate_authorities():
    c, mock = setup_api_client()

    mock.returns(mock_empty_ca_list)
    c.certificate_authorities.list()

    mock.returns(mock_ca)
    ca_desc = "python api client tests"
    ca_created = c.certificate_authorities.create(ca_pem=ca_pem, description=ca_desc)
    assert ca_created.description == ca_desc

    # get the instance and assert it's the same
    mock.returns(mock_ca)
    ca_instance = c.certificate_authorities.get(ca_created.id)
    assert ca_created == ca_instance

    # update
    mock.returns(mock_ca_updated)
    ca_meta = '{"hello": "metadata"}'
    ca_updated = c.certificate_authorities.update(ca_created.id, metadata=ca_meta)
    assert ca_updated.metadata == ca_meta
    assert ca_created.id == ca_updated.id

    # get the instance again and assert it's the same
    mock.returns(mock_ca_updated)
    ca_instance_after_update = c.certificate_authorities.get(ca_updated.id)
    assert ca_updated == ca_instance_after_update

    # value is present in list
    mock.returns(mock_ca_list)
    ca_list = c.certificate_authorities.list()
    assert ca_created.id in [ca.id for ca in ca_list]

    # delete
    mock.returns(None)
    c.certificate_authorities.delete(ca_created.id)

    # 404 after delete
    try:
        mock.returns(ngrok.NotFoundError(error_code=0, message='Not Found', http_status_code=404, details={}))
        c.certificate_authorities.get(ca_created.id)
    except ngrok.NotFoundError as e:
        assert e.http_status_code == 404
    else:
        assert False

def test_abuse_reports():
    c, mock = setup_api_client()

    mock.returns(mock_abuse_report)
    report = c.abuse_reports.create(urls=["https://foo.ngrok.io:443"])
    assert report.hostnames[0].status == "BANNED"

    mock.returns(mock_abuse_report)
    report = c.abuse_reports.get(report.id)
    assert report.hostnames[0].status == "BANNED"

def test_agent_ingress():
    c, mock = setup_api_client()

    mock.returns(mock_agent_ingress)
    ingress = c.agent_ingresses.create(domain="foo")
    mock.returns(mock_agent_ingress)
    ingress = c.agent_ingresses.get(ingress.id)
    assert ingress.domain == "foo"

    mock.returns(None)
    ingress.delete()

def test_api_keys():
    c, mock = setup_api_client()

    mock.returns(mock_api_key)
    key = c.api_keys.create()
    mock.returns(mock_api_key)
    key = c.api_keys.get(key.id)
    assert key.id == "ak_27njujFZdCVl6tXApS7OkSm9Eab"

    mock.returns(None)
    key.delete()

def test_event_subscriptions():
    c, mock = setup_api_client()

    # create an event subscription with a source
    source = ngrok.datatypes.EventSourceReplace(c, {"type": "ip_policy_updated.v0"})
    mock.returns(mock_event_susbcription)
    ev_sub = c.event_subscriptions.create(description=description, sources=[source], destination_ids=[])
    assert ev_sub.description == description

    # delete the event subscription
    mock.returns(None)
    ev_sub.delete()

def test_backends():
    c, mock = setup_api_client()

    # create a 404 http response backend
    mock.returns(mock_backend_404)
    backend_404 = c.backends.http_response.create(description=description, body=body, status_code=status_code)
    assert backend_404.body == body
    assert backend_404.status_code == status_code

    # create a tunnel group backend
    mock.returns(mock_backend_tg)
    backend_tg = c.backends.tunnel_group.create(description=description)
    assert backend_tg.description == description

    # create a failover backend
    mock.returns(mock_backend_fo)
    backend_fo = c.backends.failover.create(description=description, backends=[backend_tg.id, backend_404.id])
    assert backend_fo.description == description

    # delete all the backends
    mock.returns(None)
    backend_fo.delete()
    backend_tg.delete()
    backend_404.delete()

def test_tcp_edges():
    c, mock = setup_api_client()

    backend_mutate = ngrok.datatypes.EndpointBackendMutate(c, {"enabled": True,
                                                               "backend_id": "bkdtg_26ttrtQgoYT4wF0LbAPyCliCTHu"})

    # create TCP edge
    mock.returns(mock_edge_tcp)
    tcp_edg = c.edges.tcp.create(hostports=["1.tcp.ngrok.io:20021"], backend=backend_mutate, description=description)
    assert tcp_edg.hostports == ["1.tcp.ngrok.io:20021"]
    assert tcp_edg.description == description

    # list TCP edges
    mock.returns(f"""{{"tcp_edges": [{mock_edge_tcp}]}}""")
    c.edges.tcp.list()

    # delete TCP edge
    mock.returns(None)
    tcp_edg.delete()

def test_tls_edges():
    c, mock = setup_api_client()

    backend_mutate = ngrok.datatypes.EndpointBackendMutate(c, {"enabled": True,
                                                               "backend_id": "bkdtg_26ttsZg57ucy3iShmgFeW5qnzR9"})

    # create TLS edge
    mock.returns(mock_edge_tls)
    tls_edg = c.edges.tls.create(hostports=["utthvga8.ngrok.io:443"], backend=backend_mutate, description=description)
    assert tls_edg.hostports == ["utthvga8.ngrok.io:443"]
    assert tls_edg.description == description

    # list TLS edges
    mock.returns(f"""{{"tls_edges": [{mock_edge_tls}]}}""")
    c.edges.tls.list()

    # delete TLS edge
    mock.returns(None)
    tls_edg.delete()

def test_https_edges():
    c, mock = setup_api_client()

    # create a https edge
    mock.returns(mock_edge_https)
    edg = c.edges.https.create(description=description)
    assert edg.description == description

    # create a route with a failover backend attached to it
    # compression is also enabled
    backend_mutate = ngrok.datatypes.EndpointBackendMutate(c, {"enabled": True,
                                                               "backend_id": "bkdfo_26tiVQge4Ae9qXVmjORlUUbY6FJ"})
    compression = ngrok.datatypes.EndpointCompression(c, {"enabled": True})
    mock.returns(mock_edge_route_https)
    rte = c.edges.https_routes.create(edge_id=edg.id, match_type="path_prefix", match="/", backend=backend_mutate,
                                      compression=compression)
    assert rte.match_type == "path_prefix"
    assert rte.match == "/"
    assert rte.compression is not None

    # update the backend module
    mock.returns(mock_edge_route_https)
    c.edge_modules.https_edge_route_backend.replace(edge_id=edg.id, id=rte.id, module=backend_mutate)

    # list https edges
    mock.returns(f"""{{"https_edges": [{mock_edge_https}]}}""")
    c.edges.https.list()

    # delete https edge
    mock.returns(None)
    edg.delete()

description = "Test description"

body = "Test body"

status_code = 404

ca_pem = """
-----BEGIN CERTIFICATE-----
MIIDdTCCAl2gAwIBAgILBAAAAAABFUtaw5QwDQYJKoZIhvcNAQEFBQAwVzELMAkG
A1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv
b3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw05ODA5MDExMjAw
MDBaFw0yODAxMjgxMjAwMDBaMFcxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9i
YWxTaWduIG52LXNhMRAwDgYDVQQLEwdSb290IENBMRswGQYDVQQDExJHbG9iYWxT
aWduIFJvb3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaDuaZ
jc6j40+Kfvvxi4Mla+pIH/EqsLmVEQS98GPR4mdmzxzdzxtIK+6NiY6arymAZavp
xy0Sy6scTHAHoT0KMM0VjU/43dSMUBUc71DuxC73/OlS8pF94G3VNTCOXkNz8kHp
1Wrjsok6Vjk4bwY8iGlbKk3Fp1S4bInMm/k8yuX9ifUSPJJ4ltbcdG6TRGHRjcdG
snUOhugZitVtbNV4FpWi6cgKOOvyJBNPc1STE4U6G7weNLWLBYy5d4ux2x8gkasJ
U26Qzns3dLlwR5EiUWMWea6xrkEmCMgZK9FGqkjWZCrXgzT/LCrBbBlDSgeF59N8
9iFo7+ryUp9/k5DPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8E
BTADAQH/MB0GA1UdDgQWBBRge2YaRQ2XyolQL30EzTSo//z9SzANBgkqhkiG9w0B
AQUFAAOCAQEA1nPnfE920I2/7LqivjTFKDK1fPxsnCwrvQmeU79rXqoRSLblCKOz
yj1hTdNGCbM+w6DjY1Ub8rrvrTnhQ7k4o+YviiY776BQVvnGCv04zcQLcFGUl5gE
38NflNUVyRRBnMRddWQVDf9VMOyGj/8N7yy5Y0b2qvzfvGn9LhJIZJrglfCm7ymP
AbEVtQwdpf5pLGkkeB6zpxxxYu7KyJesF12KwvhHhm4qxFYxldBniYUr+WymXUad
DKqC5JlR3XC321Y9YeRq4VzW9v493kHMB65jUr9TU/Qr6cf9tveCX4XSQRjbgbME
HMUfpIBvFSDJ3gyICh3WZlXi/EjJKSZp4A==
-----END CERTIFICATE-----
""".strip()

mock_ca = """
{"id": "ca_1rxxVrrfOFJZ6sidyeheV7e2ONT", "uri": "https://api.ngrok.com/certificate_authorities/ca_1rxxVrrfOFJZ6sidyeheV7e2ONT", "created_at": "2021-05-02T04:59:28Z", "description": "python api client tests", "metadata": "", "ca_pem": "-----BEGIN CERTIFICATE-----\\nMIIDdTCCAl2gAwIBAgILBAAAAAABFUtaw5QwDQYJKoZIhvcNAQEFBQAwVzELMAkG\\nA1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv\\nb3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw05ODA5MDExMjAw\\nMDBaFw0yODAxMjgxMjAwMDBaMFcxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9i\\nYWxTaWduIG52LXNhMRAwDgYDVQQLEwdSb290IENBMRswGQYDVQQDExJHbG9iYWxT\\naWduIFJvb3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaDuaZ\\njc6j40+Kfvvxi4Mla+pIH/EqsLmVEQS98GPR4mdmzxzdzxtIK+6NiY6arymAZavp\\nxy0Sy6scTHAHoT0KMM0VjU/43dSMUBUc71DuxC73/OlS8pF94G3VNTCOXkNz8kHp\\n1Wrjsok6Vjk4bwY8iGlbKk3Fp1S4bInMm/k8yuX9ifUSPJJ4ltbcdG6TRGHRjcdG\\nsnUOhugZitVtbNV4FpWi6cgKOOvyJBNPc1STE4U6G7weNLWLBYy5d4ux2x8gkasJ\\nU26Qzns3dLlwR5EiUWMWea6xrkEmCMgZK9FGqkjWZCrXgzT/LCrBbBlDSgeF59N8\\n9iFo7+ryUp9/k5DPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8E\\nBTADAQH/MB0GA1UdDgQWBBRge2YaRQ2XyolQL30EzTSo//z9SzANBgkqhkiG9w0B\\nAQUFAAOCAQEA1nPnfE920I2/7LqivjTFKDK1fPxsnCwrvQmeU79rXqoRSLblCKOz\\nyj1hTdNGCbM+w6DjY1Ub8rrvrTnhQ7k4o+YviiY776BQVvnGCv04zcQLcFGUl5gE\\n38NflNUVyRRBnMRddWQVDf9VMOyGj/8N7yy5Y0b2qvzfvGn9LhJIZJrglfCm7ymP\\nAbEVtQwdpf5pLGkkeB6zpxxxYu7KyJesF12KwvhHhm4qxFYxldBniYUr+WymXUad\\nDKqC5JlR3XC321Y9YeRq4VzW9v493kHMB65jUr9TU/Qr6cf9tveCX4XSQRjbgbME\\nHMUfpIBvFSDJ3gyICh3WZlXi/EjJKSZp4A==\\n-----END CERTIFICATE-----\\n", "subject_common_name": "GlobalSign Root CA", "not_before": "1998-09-01T12:00:00Z", "not_after": "2028-01-28T12:00:00Z", "key_usages": ["cert_sign", "crl_sign"], "extended_key_usages": []}
"""

mock_ca_updated = """
{"id": "ca_1rxxVrrfOFJZ6sidyeheV7e2ONT", "uri": "https://api.ngrok.com/certificate_authorities/ca_1rxxVrrfOFJZ6sidyeheV7e2ONT", "created_at": "2021-05-02T04:59:28Z", "description": "python api client tests", "metadata": "{\\"hello\\": \\"metadata\\"}", "ca_pem": "-----BEGIN CERTIFICATE-----\\nMIIDdTCCAl2gAwIBAgILBAAAAAABFUtaw5QwDQYJKoZIhvcNAQEFBQAwVzELMAkG\\nA1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv\\nb3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw05ODA5MDExMjAw\\nMDBaFw0yODAxMjgxMjAwMDBaMFcxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9i\\nYWxTaWduIG52LXNhMRAwDgYDVQQLEwdSb290IENBMRswGQYDVQQDExJHbG9iYWxT\\naWduIFJvb3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaDuaZ\\njc6j40+Kfvvxi4Mla+pIH/EqsLmVEQS98GPR4mdmzxzdzxtIK+6NiY6arymAZavp\\nxy0Sy6scTHAHoT0KMM0VjU/43dSMUBUc71DuxC73/OlS8pF94G3VNTCOXkNz8kHp\\n1Wrjsok6Vjk4bwY8iGlbKk3Fp1S4bInMm/k8yuX9ifUSPJJ4ltbcdG6TRGHRjcdG\\nsnUOhugZitVtbNV4FpWi6cgKOOvyJBNPc1STE4U6G7weNLWLBYy5d4ux2x8gkasJ\\nU26Qzns3dLlwR5EiUWMWea6xrkEmCMgZK9FGqkjWZCrXgzT/LCrBbBlDSgeF59N8\\n9iFo7+ryUp9/k5DPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8E\\nBTADAQH/MB0GA1UdDgQWBBRge2YaRQ2XyolQL30EzTSo//z9SzANBgkqhkiG9w0B\\nAQUFAAOCAQEA1nPnfE920I2/7LqivjTFKDK1fPxsnCwrvQmeU79rXqoRSLblCKOz\\nyj1hTdNGCbM+w6DjY1Ub8rrvrTnhQ7k4o+YviiY776BQVvnGCv04zcQLcFGUl5gE\\n38NflNUVyRRBnMRddWQVDf9VMOyGj/8N7yy5Y0b2qvzfvGn9LhJIZJrglfCm7ymP\\nAbEVtQwdpf5pLGkkeB6zpxxxYu7KyJesF12KwvhHhm4qxFYxldBniYUr+WymXUad\\nDKqC5JlR3XC321Y9YeRq4VzW9v493kHMB65jUr9TU/Qr6cf9tveCX4XSQRjbgbME\\nHMUfpIBvFSDJ3gyICh3WZlXi/EjJKSZp4A==\\n-----END CERTIFICATE-----\\n", "subject_common_name": "GlobalSign Root CA", "not_before": "1998-09-01T12:00:00Z", "not_after": "2028-01-28T12:00:00Z", "key_usages": ["cert_sign", "crl_sign"], "extended_key_usages": []}
"""

mock_empty_ca_list = """
{"certificate_authorities": [], "uri": "https://api.ngrok.com/certificate_authorities", "next_page_uri": null}"""

mock_ca_list = f"""
{{"certificate_authorities": [{mock_ca_updated}], "uri": "https://api.ngrok.com/certificate_authorities", "next_page_uri": null}}
"""

mock_event_susbcription = """
    {
      "created_at": "2022-03-23T23:14:36Z",
      "description": "Test description",
      "destinations": [],
      "id": "esb_26o5oxfrHCu58Cl2pmrLEfEFDHk",
      "metadata": "",
      "sources": [],
      "uri": "https://api.ngrok.com/event_subscriptions/esb_26o5oxfrHCu58Cl2pmrLEfEFDHk"
    }
"""

mock_backend_404 = f"""
{{"id": "bkdhr_26tiVXibXEyRMIpFP8iH7YaViYV", "status_code": {status_code}, "body": "{body}", "description": "{description}"}}
"""

mock_backend_tg = f"""
{{"id": "bkdtg_26tiVRnYLbJr4VlLSj9uFB8J8N8", "description": "{description}"}}
"""

mock_backend_fo = f"""
{{"id": "bkdfo_26tiVQge4Ae9qXVmjORlUUbY6FJ", "description": "{description}"}}
"""

mock_edge_tcp = """
    {
      "backend": {
        "backend": {
          "id": "bkdtg_26ttrtQgoYT4wF0LbAPyCliCTHu",
          "uri": "https://api.ngrok.com/backends/tunnel_group/bkdtg_26ttrtQgoYT4wF0LbAPyCliCTHu"
        },
        "enabled": true
      },
      "created_at": "2022-03-26T00:35:11Z",
      "description": "Test description",
      "hostports": [
        "1.tcp.ngrok.io:20021"
      ],
      "id": "edgtcp_26ttrrQ7BvufaOHNk9vBNOcN11e",
      "ip_restriction": null,
      "metadata": "",
      "uri": "https://api.ngrok.com/edges/tcp/edgtcp_26ttrrQ7BvufaOHNk9vBNOcN11e"
    }
"""

mock_edge_tls = """
    {
      "backend": {
        "backend": {
          "id": "bkdtg_26ttsZg57ucy3iShmgFeW5qnzR9",
          "uri": "https://api.ngrok.com/backends/tunnel_group/bkdtg_26ttsZg57ucy3iShmgFeW5qnzR9"
        },
        "enabled": true
      },
      "created_at": "2022-03-26T00:35:17Z",
      "description": "Test description",
      "hostports": [
        "utthvga8.ngrok.io:443"
      ],
      "id": "edgtls_26ttsYpqOc6w0WFwi1PIZlN34X8",
      "ip_restriction": null,
      "metadata": "",
      "mutual_tls": null,
      "tls_termination": null,
      "uri": "https://api.ngrok.com/edges/tls/edgtls_26ttsYpqOc6w0WFwi1PIZlN34X8"
    }
"""

mock_edge_https = """
    {
      "created_at": "2022-03-22T16:32:38Z",
      "description": "Test description",
      "hostports": null,
      "id": "edghts_26kToO8qAA2ylYbFIkywHDSzOUs",
      "metadata": "",
      "mutual_tls": null,
      "routes": [
        {
          "backend": null,
          "circuit_breaker": null,
          "compression": {"enabled": true},
          "created_at": "2022-03-22T16:35:00Z",
          "description": "",
          "edge_id": "edghts_26kToO8qAA2ylYbFIkywHDSzOUs",
          "id": "edghtsrt_26kU6Fg06LuS6Kk5HpSR0UORGk1",
          "ip_restriction": null,
          "match": "/",
          "match_type": "path_prefix",
          "metadata": "",
          "oauth": null,
          "oidc": null,
          "request_headers": null,
          "response_headers": null,
          "saml": null,
          "uri": "",
          "webhook_verification": null,
          "websocket_tcp_converter": null
        }
      ],
      "tls_termination": null,
      "uri": "https://api.ngrok.com/edges/https/edghts_26kToO8qAA2ylYbFIkywHDSzOUs"
    }
"""

mock_edge_route_https = """
        {
          "backend": null,
          "circuit_breaker": null,
          "compression": {"enabled": true},
          "created_at": "2022-03-22T16:35:00Z",
          "description": "",
          "edge_id": "edghts_26kToO8qAA2ylYbFIkywHDSzOUs",
          "id": "edghtsrt_26kU6Fg06LuS6Kk5HpSR0UORGk1",
          "ip_restriction": null,
          "match": "/",
          "match_type": "path_prefix",
          "metadata": "",
          "oauth": null,
          "oidc": null,
          "request_headers": null,
          "response_headers": null,
          "saml": null,
          "uri": "",
          "webhook_verification": null,
          "websocket_tcp_converter": null
        }
"""

mock_domains_list = """
{
  "next_page_uri": null,
  "reserved_domains": [
    {
      "certificate": {
        "id": "cert_1x0gxFw5yk5hP9l5CCCeZFJGQYe",
        "uri": "https://api.ngrok.com/tls_certificates/cert_1x0gxFw5yk5hP9l5CCCeZFJGQYe"
      },
      "certificate_management_policy": null,
      "certificate_management_status": {
        "provisioning_job": null,
        "renews_at": "2021-09-27T00:00:00Z"
      },
      "cname_target": null,
      "created_at": "2021-07-29T23:26:04Z",
      "description": "",
      "domain": "foo.bar.eu.ngrok.io",
      "http_endpoint_configuration": null,
      "https_endpoint_configuration": null,
      "id": "rd_1y0gxIswrmoFkUNRtcFI7Jp3kxc",
      "metadata": "",
      "region": "eu",
      "uri": "https://api.ngrok.com/reserved_domains/rd_1y0gxIswrmoFkUNRtcFI7Jp3kxc"
    },
    {
      "certificate": null,
      "certificate_management_policy": null,
      "certificate_management_status": null,
      "cname_target": null,
      "created_at": "2021-08-06T17:52:19Z",
      "description": "",
      "domain": "example.sa.ngrok.io",
      "http_endpoint_configuration": null,
      "https_endpoint_configuration": {
        "id": "ec_1gUC0ny5iRymskdQR19d3toQfqm",
        "uri": "https://api.ngrok.com/endpoint_configurations/ec_1fHC0ny5iRymskdQR19d3toQfqm"
      },
      "id": "rd_1P3s6a44QOx89K42NUPV94Jrtqv",
      "metadata": "",
      "region": "sa",
      "uri": "https://api.ngrok.com/reserved_domains/rd_1P3s6a44QOx89K42NUPV94Jrtqv"
    },
    {
      "certificate": {
        "id": "cert_1wEAwMH75dWjyiceoDA0xw5WY09",
        "uri": "https://api.ngrok.com/tls_certificates/cert_1wEAwMH75dWjyiceoDA0xw5WY09"
      },
      "certificate_management_policy": {
        "authority": "letsencrypt",
        "private_key_type": "rsa"
      },
      "certificate_management_status": {
        "provisioning_job": null,
        "renews_at": "2021-10-02T00:00:00Z"
      },
      "cname_target": "gqgmkjdu.cname.ngrok.io",
      "created_at": "1970-01-01T00:00:00Z",
      "description": "",
      "domain": "name.example.com",
      "http_endpoint_configuration": null,
      "https_endpoint_configuration": null,
      "id": "rd_8iLLoZgFuC6mYrgRf5NM",
      "metadata": "",
      "region": "us",
      "uri": "https://api.ngrok.com/reserved_domains/rd_8iLLoZgFuC6mYrgRf5NM"
    }
  ],
  "uri": "https://api.ngrok.com/reserved_domains"
}
"""

mock_addrs_list = """
{
  "next_page_uri": null,
  "reserved_addrs": [
    {
      "addr": "1.tcp.ngrok.io.lan:20020",
      "created_at": "2022-04-14T19:03:19Z",
      "description": "",
      "endpoint_configuration": null,
      "id": "ra_27kiEWP6f5f987k0yUlcPE46GZf",
      "metadata": "",
      "region": "us",
      "uri": "https://api.ngrok.com/reserved_addrs/ra_27kiEWP6f5f987k0yUlcPE46GZf"
    }
  ],
  "uri": "https://api.ngrok.com/reserved_addrs"
}
"""

mock_tunnels_list = """
{
  "next_page_uri": null,
  "tunnels": [
    {
      "endpoint": {
        "id": "ep_27nRDPONKvdRWvyUOjJhzllpbhn",
        "uri": "https://api.ngrok.com/endpoints/ep_27nRDPONKvdRWvyUOjJhzllpbhn"
      },
      "forwards_to": "http://localhost:8080",
      "id": "tn_27nRDPONKvdRWvyUOjJhzllpbhn",
      "metadata": "",
      "proto": "https",
      "public_url": "https://853095c920d0.ngrok.io",
      "region": "us",
      "started_at": "2022-04-14T16:29:02Z",
      "tunnel_session": {
        "id": "ts_27nRDLESs1giNY2HHMNPyMNuPh5",
        "uri": "https://api.ngrok.com/tunnel_sessions/ts_27nRDLESs1giNY2HHMNPyMNuPh5"
      }
    }
  ],
  "uri": "https://api.ngrok.com.lan/tunnels"
}
"""

mock_ip_policy = """
{
  "created_at": "2022-04-14T16:30:32Z",
  "description": "",
  "id": "ipp_27nROi2mDmPHZ92203L5aJgCefH",
  "metadata": "",
  "uri": "https://api.ngrok.com/ip_policies/ipp_27nROi2mDmPHZ92203L5aJgCefH"
}
"""

mock_ip_policy_rule = """
{
  "action": "allow",
  "cidr": "24.0.0.0/8",
  "created_at": "2022-04-14T16:32:47Z",
  "description": "",
  "id": "ipr_27nRfcc4p85cMaHmApkVxpQDOJo",
  "ip_policy": {
    "id": "ipp_27nROi2mDmPHZ92203L5aJgCefH",
    "uri": "https://api.ngrok.com/ip_policies/ipp_27nROi2mDmPHZ92203L5aJgCefH"
  },
  "metadata": "",
  "uri": "https://api.ngrok.com/ip_policy_rules/ipr_27nRfcc4p85cMaHmApkVxpQDOJo"
}
"""

mock_ip_policy_rules_list = """
{
  "ip_policy_rules": [
    {
      "action": "allow",
      "cidr": "12.0.0.0/8",
      "created_at": "2022-04-14T16:33:58Z",
      "description": "",
      "id": "ipr_27nRoYzr2pPCWdwzZIP6husmX6C",
      "ip_policy": {
        "id": "ipp_27nROi2mDmPHZ92203L5aJgCefH",
        "uri": "https://api.ngrok.com/ip_policies/ipp_27nROi2mDmPHZ92203L5aJgCefH"
      },
      "metadata": "",
      "uri": "https://api.ngrok.com/ip_policy_rules/ipr_27nRoYzr2pPCWdwzZIP6husmX6C"
    },
    {
      "action": "allow",
      "cidr": "24.0.0.0/8",
      "created_at": "2022-04-14T16:32:47Z",
      "description": "",
      "id": "ipr_27nRfcc4p85cMaHmApkVxpQDOJo",
      "ip_policy": {
        "id": "ipp_27nROi2mDmPHZ92203L5aJgCefH",
        "uri": "https://api.ngrok.com/ip_policies/ipp_27nROi2mDmPHZ92203L5aJgCefH"
      },
      "metadata": "",
      "uri": "https://api.ngrok.com/ip_policy_rules/ipr_27nRfcc4p85cMaHmApkVxpQDOJo"
    }
  ],
  "next_page_uri": null,
  "uri": "https://api.ngrok.com/ip_policy_rules"
}
"""

mock_cred = """
{
  "acl": [],
  "created_at": "2022-04-14T16:35:11Z",
  "description": "",
  "id": "cr_27nRxf2wJGXDKuTjMkUpaWMoN1B",
  "metadata": "",
  "token": "27nRxf2wJGXDKuTjMkUpaWMoN1B_7pUKA1z533U7sGpshjCkU",
  "uri": "https://api.ngrok.com/credentials/cr_27nRxf2wJGXDKuTjMkUpaWMoN1B"
}
"""

mock_updated_cred = """
{
  "acl": [],
  "created_at": "2022-04-14T16:35:11Z",
  "description": "",
  "id": "cr_27nRxf2wJGXDKuTjMkUpaWMoN1B",
  "metadata": "{foo:bar}",
  "token": "27nRxf2wJGXDKuTjMkUpaWMoN1B_7pUKA1z533U7sGpshjCkU",
  "uri": "https://api.ngrok.com/credentials/cr_27nRxf2wJGXDKuTjMkUpaWMoN1B"
}
"""

mock_abuse_report = """
{
  "created_at": "2022-04-14T17:40:52Z",
  "hostnames": [
    {
      "hostname": "foo.ngrok.io:443",
      "status": "BANNED"
    }
  ],
  "id": "abrp_27nZwwT46wPkmfFfysoE7LpVjbR",
  "metadata": "",
  "status": "PROCESSED",
  "uri": "https://api.ngrok.com/abuse_reports/abrp_27nZwwT46wPkmfFfysoE7LpVjbR",
  "urls": [
    "https://foo.ngrok.io:443"
  ]
}
"""

mock_agent_ingress = """
{
  "created_at": "2022-04-14T18:59:38Z",
  "description": "",
  "domain": "foo",
  "id": "agin_27njWu1U9FR823pTuRTh8mgrY3h",
  "metadata": "",
  "ns_targets": [
    "1.kube-dns.kube-system.svc.cluster.local.",
    "2.kube-dns.kube-system.svc.cluster.local.",
    "3.kube-dns.kube-system.svc.cluster.local.",
    "4.kube-dns.kube-system.svc.cluster.local."
  ],
  "region_domains": [
    "tunnel.us.foo"
  ],
  "uri": "https://api.ngrok.com.lan/agent_ingresses/agin_27njWu1U9FR823pTuRTh8mgrY3h"
}

"""

mock_api_key = """
{
  "created_at": "2022-04-14T19:02:48Z",
  "description": "",
  "id": "ak_27njujFZdCVl6tXApS7OkSm9Eab",
  "metadata": "",
  "token": "27njujFZdCVl6tXApS7OkSm9Eab_7MufErgFn7SeihmP7v9mn",
  "uri": "https://api.ngrok.com/api_keys/ak_27njujFZdCVl6tXApS7OkSm9Eab"
}
"""

mock_reserved_addr = """
{
  "addr": "1.tcp.ngrok.io.lan:20020",
  "created_at": "2022-04-14T19:03:19Z",
  "description": "",
  "endpoint_configuration": null,
  "id": "ra_27kiEWP6f5f987k0yUlcPE46GZf",
  "metadata": "",
  "region": "us",
  "uri": "https://api.ngrok.com/reserved_addrs/ra_27kiEWP6f5f987k0yUlcPE46GZf"
}
"""

mock_reserved_domain = """
{
  "acme_challenge_cname_target": null,
  "certificate": null,
  "certificate_management_policy": null,
  "certificate_management_status": null,
  "cname_target": null,
  "created_at": "2022-04-14T19:04:14Z",
  "description": "",
  "domain": "foo.ngrok.io.lan",
  "http_endpoint_configuration": null,
  "https_endpoint_configuration": null,
  "id": "rd_27nk5WLm85y0wqi13XNLobu3Xff",
  "metadata": "",
  "region": "us",
  "uri": "https://api.ngrok.com/reserved_domains/rd_27nk5WLm85y0wqi13XNLobu3Xff"
}
"""

class RecordingHTTPClient(ngrok.http_client.HTTPClient):
    """ prints all responses received to stdout, useful for creating mocked outputs """
    def do(self, method: str, path: str, query_params: Mapping[str, str] = None, payload: Mapping[str, Any] = None) -> Optional[Dict[str, Any]]:
        ret = super(RecordingHTTPClient, self).do(method, path, query_params, payload)
        print(json.dumps(ret))
        return ret

class MockHTTPClient(ngrok.http_client.HTTPClient):
    def __init__(self):
        pass

    def returns(self, val: Union[Optional[Dict[str, Any]], Exception]):
        if isinstance(val, str):
            self._val = json.loads(val)
        else:
            self._val = val

    def do(self, method: str, path: str, query_params: Mapping[str, str] = None, payload: Mapping[str, Any] = None) -> Optional[Dict[str, Any]]:
        if isinstance(self._val, Exception):
            raise self._val
        else:
            return self._val
