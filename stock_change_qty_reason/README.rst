============================
Stock Change Quantity Reason
============================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:e42963c1ceb4ff0656f2056a4ea9454c5c027c2c7e1aece1aff34de97ed33287
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fstock--logistics--warehouse-lightgray.png?logo=github
    :target: https://github.com/OCA/stock-logistics-warehouse/tree/14.0/stock_change_qty_reason
    :alt: OCA/stock-logistics-warehouse
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/stock-logistics-warehouse-14-0/stock-logistics-warehouse-14-0-stock_change_qty_reason
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/stock-logistics-warehouse&target_branch=14.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module extends the product stock management and allows to set a reason
in inventory adjustments globally or per line.

It also can manage preset reasons optionally.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To enable preset reason feature, you must:

- Go to: Inventory > Settings > Inventory Adjustment
- Enable: Preset Change Qty Reason
- Enable: Technical Settings > Manage Stock Change Qty Preset Reasons

Once is activate you will require te add a Preset reason to validate stock
products change quantity.


To allow an Stock Manager configure preset reasons easily, you should:

- Select Stock Manager user on: Settings > Users
- Enable: Technical Settings > Manage Stock Change Qty Preset Reasons
- Go to Inventory > Configuration > Inventory Adjustment > Change Qty Reasons

Known issues / Roadmap
======================

* Add a reason from Update Quantity button in Product Form View has been removed. This button no longer opens an Inventory Adjustment, it opens directly the stock quant view. Therefore, it must be decided how to implement the logic to add a reason when quantity is updated.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/stock-logistics-warehouse/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/stock-logistics-warehouse/issues/new?body=module:%20stock_change_qty_reason%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* ACSONE SA/NV

Contributors
~~~~~~~~~~~~

* Denis Roussel <denis.roussel@acsone.eu>
* Meyomesse Gilles <meyomesse.gilles@gmail.com>
* Andreas Dian S.P <andreasdian777@gmail.com>
* Héctor Villarreal <hector.villarreal@forgeflow.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/stock-logistics-warehouse <https://github.com/OCA/stock-logistics-warehouse/tree/14.0/stock_change_qty_reason>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
