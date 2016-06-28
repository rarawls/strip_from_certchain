# strip_from_certchain
Python script to remove all certificates matching a keyword in the subject from a certificate chain.

### Assumptions

The certificate chain file is expected to be a concatenation of certificates in the following format:

    subject=/C=US/O=U.S. Government/OU=DoD/OU=PKI/CN=DOD CA-27
    issuer=/C=US/O=U.S. Government/OU=DoD/OU=PKI/CN=DoD Root CA 2
    -----BEGIN CERTIFICATE-----
    MIIFTDCCBDSgAwIBAgICAbIwDQYJKoZIhvcNAQEFBQAwWzELMAkGA1UEBhMCVVMx
    ...
    14Km5+I3fjt7Bngmb2xFcw==
    -----END CERTIFICATE-----

### Usage

    python strip_from_certchain.py <<search_string>> <<file_name>>
    
or

    ./strip_from_certchain.py <<search_string>> <<file_name>>
    
For example, the following will remove all of the email certificate authorities from, say, a DoD certificate chain:

    python strip_from_certchain EMAIL DoD_CAs.pem

### Disclamer

There is plenty of work to be done - like a safer usage and a help message.  Also, the ability to match against the issuer as well... Basically, this script is useful in a very small use case: removing the email CAs from a DoD CA chain file.  YMMV.
