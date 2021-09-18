import ngrok
import ngrok.http_client
import json
import os
from typing import Optional, Mapping, Union, Dict, Any

def setup_api_client():
    c = ngrok.Client(os.getenv("NGROK_API_KEY"))
    mock = MockHTTPClient()
    if not os.getenv('TEST_NO_MOCK', False):
        c.http_client = mock
    elif os.getenv('TEST_DEBUG', False):
        c.http_client = RecordingHTTPClient(c.http_client.api_key, c.http_client.base_url)
    return c, mock

def test_domains():
    c, mock = setup_api_client()
    mock.returns(mock_domains_list)
    c.reserved_domains.list()

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
    ca_meta='{"hello": "metadata"}'
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

mock_ca_list = """
{"certificate_authorities": ["""+mock_ca_updated+"""], "uri": "https://api.ngrok.com/certificate_authorities", "next_page_uri": null}
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
