#!/usr/bin/python
# 
#  Copyright (C) 2011 Raghu Udiyar <raghusiddarth@gmail.com>
#  
#  This copyrighted material is made available to anyone wishing to use,
#  modify, copy, or redistribute it subject to the terms and conditions
#  of the GNU General Public License, either version 2 of the License, or
#  (at your option) any later version
# 
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# 
# 
#  Description:
#  
# 
#  Author: Raghu Udiyar <raghusiddarth@gmail.com>
#
# Example of usage:
# 
# $
#

import sys
import os

def main(file_name):
    total = 0
    fname = open(file_name,'ro')
    for line in fname:
        if "BIOS-e820:" in line:
            l = line.split(' ')[2]
            h = line.split(' ')[4]
            result = int(h, 16) - int(l, 16)
            total = total + result
            line = line.strip('\n')
            print line + "  : " + '%s' % result
    print "Total : %s" % total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: %s <e820 file>" % sys.argv[0])
    
    if not os.path.exists(sys.argv[1]):
        sys.exit("Error: file not found")
    main(sys.argv[1])
    exit(0)

# vim: autoindent tabstop=4 expandtab smarttab shiftwidth=4 softtabstop=4 tw=0
