#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This tool generates the excel sheet titles according to the schema defined in Transparenzinformationen.txt

import string

result = ''
for j in range(1, 11):
	for i in range(1, 4):
		result = result + '\t' + str(j) + string.ascii_uppercase[i-1]

# print(result)



result = ''
for r in range(1, 21):
	for j in range(1, 11):
		for i in range(1, 4):
			result = result + '\t' + "='" + str(j) + string.ascii_uppercase[i-1] + "'!A{}".format(str(r))

print(result)

