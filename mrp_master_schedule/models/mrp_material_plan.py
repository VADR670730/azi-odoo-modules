# -*- coding: utf-8 -*-
# © 2016 Matt Taylor
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)


class MrpMaterialPlan(models.Model):
    _inherit = "mrp.material_plan"

    build_id = fields.Many2one(
        comodel_name='mrp.schedule.line',
        string='MSBuild',
        index=True,
        help='Master Schedule Line item that created this planned order.'
    )

    @api.model
    def purge_old_plan(self):
        # purge old plan
        super(MrpMaterialPlan, self).purge_old_plan()

        warehouse = self.env['stock.warehouse'].search([], limit=1)
        location = warehouse.lot_stock_id

        domain = [('schedule_id.state', '=', 'released'), ('product_id', '!=', False)]
        scheduled_builds = self.env['mrp.schedule.line'].search(domain)
        _logger.info("Creating dependent demand from %s scheduled builds", len(scheduled_builds))
        for build in scheduled_builds:
            # create independent demand
            new_order = self.create(
                self._prepare_planned_order(
                    build.product_id,
                    1,
                    self._get_bucket_from_date(build.date_finish),
                    location,
                    origin=build.name
                )
            )
            # create dependent demand
            new_order._create_dependent_demand()

    def _get_planning_horizon(self):
        last_bucket_date = super(MrpMaterialPlan, self)._get_planning_horizon()

        # check for a later schedule date
        schedule_domain = [('schedule_id.state', '=', 'released'), ('product_id', '!=', False)]
        last_build = self.env['mrp.schedule.line'].search(schedule_domain, order="date_finish DESC", limit=1)
        last_build_date = last_build and datetime.strptime(last_build.date_finish, DEFAULT_SERVER_DATE_FORMAT).date()
        if last_build and last_build_date > last_bucket_date:
            last_bucket_date = self._get_bucket_from_date(last_build.date_finish)

        return last_bucket_date
