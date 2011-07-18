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
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    sale_order_date_delivery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv
from osv import fields
from datetime import date, timedelta

class sale_order_line(osv.osv):
    _inherit = 'sale.order.line'

    def _get_delay(self, cr, uid, ids, field_name, arg, context=None):
        """
        Returns the delay from the planned date
        """
        # Retrieve date_planned value as a date object
        date_planned = self.read(cr, uid, ids[0], ['date_planned'], context=context)['date_planned'].split('-')
        date_planned = date(int(date_planned[0]), int(date_planned[1]), int(date_planned[2]))
        # Retrieve the company security lead
        security_lead = self.pool.get('res.users').browse(cr, uid, uid).company_id.security_lead

        # Computes the delay from date planned and company security lead
        delay = date_planned - date.today() + timedelta(days=security_lead)

        return {ids[0]: delay.days}

    _columns = {
        'date_planned': fields.date('Date', required=True, help='Date planned for this line', readonly=True, states={'draft': [('readonly', False)]}),
        'delay': fields.function(_get_delay, method=True, string='Delivery Lead Time', type='float', store=False, help='Number of days between the order confirmation the shipping of the products to the customer', ),
    }

    def _get_default_date(self, cr, uid, context=None):
        """
        Returns the default date
        """
        return str(date.today())

    _defaults = {
        'date_planned': lambda self, cr, uid, c: self._get_default_date(cr, uid, context=c),
    }

sale_order_line()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
