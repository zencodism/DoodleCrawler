#!/bin/bash

URL="https://hrsa.cunyfirst.cuny.edu/psc/cnyhcprd/GUEST/HRMS/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL"
java -cp /home/www/Doodle/htmlunit-2.15-OSGi.jar:/home/www/Doodle/DCrawler/bin DCrawler $URL

