#!/usr/bin/python

import sys

search_string = sys.argv[1]
filename = sys.argv[2]

lines = [] # Lines from existing file
new_lines = [] # Lines to be written back to file
num_deleted_certs = 0

deleting = False # Logic control: determines if current line will be ignored

# Open file and read it into lines
with open(filename, 'r') as certs:
	lines = certs.readlines()

# Iterate through lines and delete lines belonging to a matching cert
for line in lines:
	
	if search_string in line:
		deleting = True
		num_deleted_certs += 1

	if not deleting:
		new_lines.append(line)

	if "-----END CERTIFICATE-----" in line:
		deleting = False

# Write results back to file
with open(filename, 'w') as certs:
	for line in new_lines:
		certs.write(line)

print "Done. Deleted {} certs.".format(num_deleted_certs)
