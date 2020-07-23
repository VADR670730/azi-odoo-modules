.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
Stock Forecast Detail
=====================

For a specified product, generate a schedule of future stock moves, with
running balance.

Unless the Confirmed flag is set, we also include the following:
- RFQs (unconfirmed purchase orders)
- Planned orders from mrp_multi_level
- Quotations (unconfirmed sale orders)
- Submitted stock requests

Usage
=====

- Click the *Moves* button on the product form.
- Run the wizard located at *Stock > Planning > Material Analysis*.

Known issues / Roadmap
======================

* No known issues

Possible `related issues
<https://github.com/asphaltzipper/azi-odoo-modules/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20
stock_forecast_detail%20>`_.

Changelog
=========

12.0.1.0.0 (2020-07-09)
~~~~~~~~~~~~~~~~~~~~~~~

* New module

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/asphaltzipper/azi-odoo-modules/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed `feedback
<https://github.com/asphaltzipper/azi-odoo-modules/issues/new?body=module:%20
stock_forecast_detail
%0Aversion:%209.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20
behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Contributors
------------

* Matt Taylor <mtaylor@asphaltzipper.com>

Funders
-------

The development of this module has been financially supported by:

* Asphalt Zipper, Inc.

Maintainer
----------

.. image:: http://asphaltzipper.com/img/elements/logo.png
   :alt: Asphalt Zipper, Inc.
   :target: http://asphaltzipper.com

This module is maintained by Asphalt Zipper, Inc.

To contribute to this module, please visit https://github.com/asphaltzipper/azi-odoo-modules.
