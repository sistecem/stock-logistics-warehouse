# Copyright 2023 Raumschmiede (http://www.raumschmiede.de)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

SINGLEPACKAGE = "singlepackage"
MULTIPACKAGE = "multiplepackage"
NORESTRICTION = "norestriction"


class StockLocation(models.Model):
    _inherit = "stock.location"

    package_restriction = fields.Selection(
        selection=lambda self: self._selection_package_restriction(),
        help="""
            Control if the location can contain products not in a package.

            Options:
              * Mandatory and unique: The location cannot have products not
                part of a package and you cannot have more than 1 package on
                the location
              * Mandatory and not unique:  The location cannot have products
                not part of a package and you may have store multiple packages
                on the location
              * Not mandatory: The location can contain products not part of a
                package
        """,
        required=True,
        store=True,
        default="norestriction",
    )

    @api.model
    def _selection_package_restriction(self):
        return [
            (MULTIPACKAGE, "Mandatory"),
            (SINGLEPACKAGE, "Mandatory and unique"),
            (NORESTRICTION, "Not mandatory"),
        ]
