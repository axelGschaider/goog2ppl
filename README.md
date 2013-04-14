goog2ppl
========

A Python script to convert Google Contacts to a format readable by [ppl](http://ppladdressbook.org/).

Takes a vcf file and splits it into separate cards named after the
camelcase contents of their `N:` (name) lines. 

##Caveats
* Hardly tested, but works for me. So backup first!
* Outputs bunches of vcf files to the directory from which it's run.

##Usage
From an initialized ppl directory:

1. `mv <contacts file> <contacts file>.bak` because I don't like it when people
get mad at me.

2. `./goog2ppl.py <contacts file>` to make cards for your contacts.

3. `git add *.vcf && git commit -a` to make the imported contacts visible
to ppl.
