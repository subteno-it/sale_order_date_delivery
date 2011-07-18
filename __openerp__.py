# -*- coding: utf-8 -*-
##############################################################################
#
#    sale_order_date_delivery module for OpenERP, This module allows to set a date instead of a delay for sale orders
#    Copyright (C) 2011 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#
#    This file is a part of sale_order_date_delivery
#
#    sale_order_date_delivery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    sale_order_date_delivery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Sale Order Date Delivery',
    'version': '1.0',
    'category': 'Generic Modules/Sales & Purchases',
    'description': """This module allows to set a date instead of a delay for sale orders""",
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'depends': [
        'base',
        'sale_order_dates',
    ],
    'init_xml': [],
    'images': [],
    'update_xml': [
        #'security/ir.model.access.csv',
        #'wizard/wizard.xml',
        'sale_order_view.xml',
    ],
    'demo_xml': [],
    'test': [
        'test/sale_order_date_delivery_test01.yml',
    ],
    #'external_dependancies': {'python': ['kombu'], 'bin': ['which']},
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
