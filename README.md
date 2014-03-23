goog2ppl
========

A Python script to convert Google Contacts to a format readable by [ppl](http://ppladdressbook.org/).

Takes a vcf file and splits it into separate cards named after the
camelcase contents of their `N:` (name) lines. 
Takes a vcf file and splits it into separate cards. These cards are named after the lowercase elements of their `N:` (name) lines. These elements are connected by a `_`. This is ought to mimic the naming of `ppl scrape`. Overwriting existing vCards is prevented by adding a counter to the name if the card already exists. 
Contrary to the original script by `shushcat` this version leaves the `N:` line untouched.

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
