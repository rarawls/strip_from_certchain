#!/usr/bin/python

import sys

class Cert:
	""" Class representing a .pem formatted x.509 certificate """

	subject = '' # subject=/C=US/O=U.S. Government/OU=DoD/OU=PKI/CN=DOD CA-27
	issuer = '' # issuer=/C=US/O=U.S. Government/OU=DoD/OU=PKI/CN=DoD Root CA 2
	certificate = '' #base64 encoded certificate data, less the begin/end lines
	
	HEADER = '-----BEGIN CERTIFICATE-----'
	FOOTER = '-----END CERTIFICATE-----'
	
# 	def __init__(self, subject, issuer, certificate):
# 		self.subject = subject
# 		self.issuer = issuer
# 		self.certificate = certificate
		
	def __init__(self, pem):
		self.subject = pem[0].strip()
		self.issuer = pem[1].strip()
		pem.pop() #remove footer
		
		for line in pem[3:]:
			self.certificate += line
		
		self.certificate = self.certificate.strip() # remove trailing CR

	def subjectContains(self, s):
		return s in self.subject
	
	def issuerContains(self, s):
		return s in self.issuer
	
	def getSubject(self):
		return self.subject
	
	def getIssuer(self):
		return self.issuer

	def getCertificate(self):
		return self.certificate

	def getPEM(self):
		return '{}\n{}\n{}\n{}\n'.format(self.subject,
										self.issuer,
										self.HEADER,
										self.certificate,
										self.FOOTER)

class CertChain:
	""" Class representing a certificate chain of .pem x.509 certs """
	
	certs = [Cert]
	
	def __init__(self, lines):
	
		certLines = []
		processing = False
		
		for line in lines:
			
			if Cert.HEADER in line:
				processing = True
				continue
			elif processing and Cert.FOOTER in line:
				cert = Cert(certLines)
				self.addCert(cert)
				print cert.getPEM()
				print certLines
				certLines = []
				processing = False
			
			if processing and (not line is ''):
				certLines.append(line)

	def addCert(self, cert):
		self.certs.append(cert)
	
	def removeCert(self, cert):
		self.certs.remove(cert)
		
	def getCerts(self):
		return self.certs
	
	def removeCertsWithSubjectsContaining(self, s):
		self.certs = [c for c in self.certs if not c.subjectContains(s)]

search_string = sys.argv[1]
filename = sys.argv[2]

lines = [] # Lines from existing file
num_deleted_certs = 0

# Open file and read it into lines
with open(filename, 'r') as certs:
	lines = certs.readlines()

certChain = CertChain(lines)

print Cert(lines).getPEM()





# Iterate through lines and delete lines belonging to a matching cert
# for line in lines:
# 	
# 	if search_string in line:
# 		deleting = True
# 		num_deleted_certs += 1
# 
# 	if not deleting:
# 		new_lines.append(line)
# 
# 	if "-----END CERTIFICATE-----" in line:
# 		deleting = False

# Write results back to file
# with open(filename, 'w') as certs:
# 	for line in new_lines:
# 		certs.write(line)
# 
# print "Done. Deleted {} certs.".format(num_deleted_certs)
