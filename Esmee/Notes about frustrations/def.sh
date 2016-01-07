#!/bin/bash
echo Definitie van $1 op het Web:
echo ""
curl -s -A 'Mozilla/4.0'  'http://www.google.be/search?q=define%3A+'$1  | html2text -ascii -nobs -style compact -width 80 | grep "*" -A 2