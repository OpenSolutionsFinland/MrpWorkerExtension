# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Open Solutions Finland 2013.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Manufacturing Worker Extension",
    "version" : "1.0",
    "author" : "Open Solutions Finland",
    "description" : """
*** Manufacturing Worker Extension ***
Simplifies partial manufacturing process
***********************************
    """,
    "website" : "http://www.opensolutions.fi",
    "depends" : ["base","mrp","stock", "product_quality"],
    "category" : "Manufacturing",
    "init_xml" : [],
    "demo_xml" : [],
    "data" : [
              'mrp_extension_view.xml',
			  'mrp_extension_report.xml'
                    ],
    'test': [
             ],
    'installable': True,
    'active': False,
    'certificate': '',
}
