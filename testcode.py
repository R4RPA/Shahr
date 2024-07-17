pip install cryptography

from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Read the .crt file
with open("yourfile.crt", "rb") as crt_file:
    crt_data = crt_file.read()

# Load the certificate
cert = x509.load_pem_x509_certificate(crt_data, default_backend())

# Write the certificate to a .pem file
with open("yourfile.pem", "wb") as pem_file:
    pem_file.write(cert.public_bytes(encoding=x509.Encoding.PEM))
