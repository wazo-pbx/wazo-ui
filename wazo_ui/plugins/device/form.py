# Copyright 2018-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from flask_babel import lazy_gettext as l_
from wtforms.fields import (
    BooleanField,
    FormField,
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import InputRequired, IPAddress, MacAddress

from wazo_ui.helpers.form import BaseForm


class DeviceOptionsForm(BaseForm):
    switchboard = BooleanField(l_('Switchboard'), default=False)


class DeviceForm(BaseForm):
    template_id = SelectField(l_('Template'), validators=[InputRequired()], choices=[])
    ip = StringField(l_('IP'), validators=[IPAddress()])
    mac = StringField(l_('MAC'), validators=[MacAddress()])
    model = StringField(l_('Model'))
    plugin = SelectField(l_('Plugin'), validators=[InputRequired()], choices=[])
    vendor = StringField(l_('Vendor'))
    version = StringField(l_('Version'))
    status = SelectField(
        l_('Status'),
        choices=[
            ('autoprov', l_('Autoprov')),
            ('configured', l_('Configured')),
            ('not_configured', l_('Not configured')),
        ],
    )
    options = FormField(DeviceOptionsForm)
    description = StringField(l_('Description'))
    submit = SubmitField()
