#!/usr/bin/python
from OpenSSL import crypto, SSL
from os.path import exists, join



CERT_FILE = 'cert.crt'
KEY_FILE = 'cert.key'

#print CERT_FILE
#print KEY_FILE


def create_self_signed_cert(cert_dir):
    """
    If cert.crt and cert.key don't exist in /etc/nginx, create a new
    self-signed cert and keypair and write them into that directory.
    """

    if not exists(join(cert_dir, CERT_FILE)) or not exists(join(cert_dir, CERT_FILE)):
        #create a Key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)
       
	print k
	#create a self-signed cert
	cert = crypto.X509()
	cert.get_subject().C = "IN"
        cert.get_subject().ST = "AP"
        cert.get_subject().L = "HYDERABAD"
        cert.get_subject().O = "Nexiilabs"
        cert.get_subject().OU = "DEVOPS"
      #  cert.get_subject().CN = CN
 	cert.set_issuer(cert.get_subject())
	cert.set_pubkey(k)
	cert.sign(k, 'sha1')
	open(join(cert_dir, CERT_FILE), "wt").write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
	open(join(cert_dir,KEY_FILE), "wt").write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))


create_self_signed_cert("/etc/nginx")
