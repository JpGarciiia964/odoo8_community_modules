# -*- encoding: utf-8 -*-
###########################################################################
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
    "name" : "account_invoice_seq_number",
    "version" : "1.0",
    "author" : 'Open Business Solutions, SRL.',
    "depends" : ["account", "account_sequence"],
    'complexity': 'easy',
    "description": """
    """,
    "website" : "http://obsdr.com",
    "category" : "Generic Modules/Accounting",
    "init_xml" : [
	],
    "demo_xml" : [
    ],
    "update_xml" : [
		'account_invoice_view.xml',
    ],
    "test" : [],
    "auto_install": False,
    "application": False,
    "installable": True,
    'license': 'AGPL-3',
}


