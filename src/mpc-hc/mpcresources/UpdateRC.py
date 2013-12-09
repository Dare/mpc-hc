# (C) 2013 see Authors.txt
#
# This file is part of MPC-HC.
#
# MPC-HC is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# MPC-HC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

from TranslationData import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        RuntimeError('Invalid number of parameters. Usage: UpdateRC.py <filename>')

    filename = sys.argv[1]

    translationData = TranslationData()
    translationData.loadFromPO('PO\\' + filename, 'po')
    translationData.translateRC(r'..\mpc-hc.rc', filename)
    # Write back the PO file to ensure it's properly normalized
    translationData.writePO('PO\\' + filename, 'po')
