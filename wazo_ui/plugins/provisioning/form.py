# Copyright 2018-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import pytz

from flask_babel import lazy_gettext as l_
from wtforms.fields import (
    SubmitField,
    StringField,
    HiddenField,
    SelectMultipleField,
    SelectField,
    FormField,
    BooleanField
)
from wtforms.fields.html5 import IntegerField
from wtforms.validators import InputRequired, Length, IPAddress, Regexp, URL

from wazo_ui.helpers.form import BaseForm


def list_timezones():
    result = [('', l_('None'))]
    # XXX: Should use REST API /timezones to avoid disparities with different systems
    result.extend(list(zip(pytz.all_timezones, pytz.all_timezones)))
    return result


class ConfigRegistrarForm(BaseForm):
    id = HiddenField()
    X_type = StringField(default='registrar')
    parent_ids = SelectMultipleField(l_('Parent'), choices=[], default=[])
    raw_config = StringField(default={'X_key': 'xivo'})
    displayname = StringField(l_('Name'), validators=[InputRequired(), Length(max=128)])
    registrar_main = StringField(l_('Registrar main'), validators=[InputRequired(), Length(max=128)])
    registrar_backup = StringField(l_('Registrar backup'), validators=[Length(max=128)])
    proxy_main = StringField(l_('Proxy main'), validators=[InputRequired(), Length(max=128)])
    proxy_backup = StringField(l_('Proxy Backup'), validators=[Length(max=128)])
    submit = SubmitField(l_('Submit'))


class RawConfigDeviceForm(BaseForm):
    X_key = StringField(default='xivo')
    locale = SelectField(l_('Language'), choices=[
        ('', l_('None')),
        ('de_DE', 'de_DE'),
        ('en_US', 'en_US'),
        ('es_ES', 'es_ES'),
        ('fr_FR', 'fr_FR'),
        ('fr_CA', 'fr_CA'),
        ('it_IT', 'it_IT'),
        ('nl_NL', 'nl_NL'),
        ('pl_PL', 'pl_PL'),
    ])
    timezone = SelectField(l_('Timezone'), choices=list_timezones())
    protocol = SelectField(l_('Protocol'), choices=[
        ('', l_('None')),
        ('SIP', 'SIP'),
        ('SCCP', 'SCCP')
    ])
    config_encryption_enabled = BooleanField(l_('Enabled encryption config file'), default=False)
    ntp_enabled = BooleanField(l_('Enabled NTP'), default=False)
    ntp_ip = StringField(l_('NTP server'), validators=[IPAddress])
    sip_dtmf_mode = SelectField(l_('SIP DTMF mode'), choices=[
        ('', l_('None')),
        ('RTP-in-band', 'RTP-in-band'),
        ('RTP-out-of-band', 'RTP-out-of-band'),
        ('SIP-INFO', 'SIP-INFO')
    ])
    user_username = StringField(l_('User username'), validators=[InputRequired(), Length(max=128)])
    user_password = StringField(l_('User password'), validators=[InputRequired(), Length(max=128)])
    admin_username = StringField(l_('Admin username'), validators=[InputRequired(), Length(max=128)])
    admin_password = StringField(l_('Admin password'), validators=[InputRequired(), Length(max=128)])
    sip_subscribe_mwi = BooleanField(l_('Explicit notification of messages'), default=False)
    vlan_enabled = BooleanField(l_('VLAN Enabled'))
    vlan_id = IntegerField(l_('VLAN ID'), validators=[Regexp('^[0-9]+$')])
    vlan_priority = IntegerField(l_('VLAN Priority'), validators=[Regexp('^[0-9]+$')])
    vlan_pc_port_id = IntegerField(l_('VLAN PC Port ID'), validators=[Regexp('^[0-9]+$')])


class ConfigDeviceForm(BaseForm):
    id = HiddenField()
    X_type = StringField(default='device')
    parent_ids = SelectMultipleField(l_('Parent'), choices=[], default=[])
    raw_config = FormField(RawConfigDeviceForm)
    label = StringField(l_('Label'), validators=[InputRequired(), Length(max=128)])
    submit = SubmitField(l_('Submit'))


class GeneralConfigurationForm(BaseForm):
    plugin_server = StringField(l_('Plugin server URL'), validators=[InputRequired(), Length(max=2048), URL()])
    http_proxy = StringField(l_('HTTP Proxy'), validators=[Length(max=2048), URL()])
    https_proxy = StringField(l_('HTTPS Proxy'), validators=[Length(max=2048), URL()])
    ftp_proxy = StringField(l_('FTP Proxy'), validators=[Length(max=2048), URL()])
    locale = StringField(l_('Locale'), validators=[Length(max=5), Regexp(r'^[a-z]{2}_[A-Z]{2}$')])
    NAT = BooleanField(l_('NAT'))


class NetworkConfigurationForm(BaseForm):
    provision_host = StringField(l_('Provisioning host'))
    provision_http_port = IntegerField(l_('Provisioning port'), validators=[Regexp('^[0-9]+$')])
    rest_host = StringField(l_('REST API host'))
    rest_https_port = IntegerField(l_('REST API HTTPS port'), validators=[Regexp('^[0-9]+$')])


class ConfigurationForm(BaseForm):
    general_config = FormField(GeneralConfigurationForm)
    network_config = FormField(NetworkConfigurationForm)
    submit = SubmitField(l_('Submit'))
