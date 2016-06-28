# strip_from_certchain
Python script to remove all certificates matching a keyword in the subject from a certificate chain.

Usage: 

    python strip_from_certchain <<search_string>> <<file_name>>
    
or

    ./strip_from_certchain <<search_string>> <<file_name>>
    
For example, the following will remove all of the email certificate authorities from, say, a DoD certificate chain:

    python strip_from_certchain EMAIL DoD_CAs.pem

There is plenty of work to be done - like a safer usage and a help message.  Also, the ability to match against the issuer as well.
