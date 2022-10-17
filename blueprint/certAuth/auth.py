import OpenSSL
from flask import request
from functools import wraps
import logging as logger
from cryptography import x509
from cryptography.x509.oid import NameOID

validUsers = [
    {'user': 'Suryansh', 'Email': 's@gmail.com'},
    {'user': 'Siemens', 'Email': 'dil2.0.energy@siemens-energy.com'}]


def certAuth(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            logger.info("Fetching the certificate from the request")
            cert_header = request.headers.get('Authorization')
            # no header then return false
            if cert_header is None:
                resp = {
                    "status": False,
                    "message": "invalid_header",
                    "description": "Invalid Header"
                }
                return resp, 511
            cert_header = cert_header.replace("\\n", "\n")
            cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_header)
            logger.info(cert_header, cert)
            # if certificate expired
            if cert.has_expired():
                logger.info("Certificate provided is expired")
                return {
                           "status": False,
                           "message": "invalid_certificate",
                           "description": "Certificate is Expired"
                       }, 511
            logger.info("Certificate provided is Invalid")
            # print(cert_header)
            c = bytes(cert_header, 'utf-8')
            cert = x509.load_pem_x509_certificate(c)
            common_name = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
            print(common_name)
            s = str(cert.subject)
            if validUsers[1]['user'] in s:
                return function(*args, **kwargs)
            else:
                resp = {
                    "status": False,
                    "message": "Invalid User",
                    "description": "Certificate passed is Invalid"
                }
                return resp, 511
        except Exception as e:
            logger.info("Certificate provided is Invalid")
            resp = {
                "status": False,
                "message": "invalid_certificate",
                "description": "Certificate passed is Invalid"
            }
            return resp, e

    return wrapper
