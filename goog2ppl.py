#!/usr/bin/env python
# Python's regular expression library
import re
import sys
import os

# Gets first command line argument
source = open(sys.argv[1])

contact = ''
outCard = []

cardNum = 0
for line in source:
    if not re.search(r'END:VCARD', line):
        # Is it a N: line?
        if re.search(r'(N:)(.+)(;;;)', line):
            # listOfFields = lof
            lof = line[2:].split(";")
            # swap first 2 fields. I want first name first
            lof[0], lof[1] = lof[1], lof[0]
            allLowercase   = [x.rstrip().lower() for x in lof]
            filteredFields = filter(None, allLowercase)
            # replace ' ' with '_' to handle names like "van Zandt" gracefully
            contact = "_".join( filteredFields ).replace(' ', '_')


            # contact = (re.sub(r'(N:)(.+)(;;;)', r'\2', line)).replace(';','')
            if re.search(r'(N:)(;;;)', line):
                contact = 'MISSING CONTACT FIELD ' + str(cardNum)
            # Get rid of extra newlines.
            contact = contact.rstrip()
    outCard.append(line)
    if re.search(r'END:VCARD', line):
        filename = contact + '.vcf'
        counter = 1
        # increment a counter in filename if the original name allready exists
        while os.path.exists( filename ):
            filename = contact + ("_(%s).vcf" % counter )
            counter += 1
        outfile = open(filename, 'w')
        for line in outCard:
            outfile.write("%s" % line)
        outCard = []
        cardNum = cardNum + 1
