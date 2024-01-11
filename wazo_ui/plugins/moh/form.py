# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from flask_babel import lazy_gettext as l_
from wtforms.fields import FieldList, FormField, SelectField, StringField, SubmitField
from wtforms.validators import InputRequired

from wazo_ui.helpers.form import BaseForm

mode_map = {'custom': l_('Custom'), 'files': l_('Files'), 'mp3': l_('MP3')}

sort_map = {
    '': l_('None'),
    'alphabetical': l_('Alphabetical'),
    'random': l_('Random'),
    'random_start': l_('Random start'),
}


class MohFilesForm(BaseForm):
    name = StringField(l_('Name'), [InputRequired()])


class MohForm(BaseForm):
    name = StringField(
        l_('Name'),
        [InputRequired()],
        description=l_(
            'The name used by Asterisk (can only by set on create and must be unique)'
        ),
    )
    label = StringField(l_('Label'), description=l_('The label of the MOH class'))
    mode = SelectField(
        l_('Mode'),
        choices=[(k, v) for k, v in mode_map.items()],
        description=l_("The play mode of the MOH class"),
    )
    application = StringField(
        l_('Application'),
        description=l_('The command to run (only used when mode is "custom")'),
    )
    sort = SelectField(
        l_('Sort'),
        choices=[(k, v) for k, v in sort_map.items()],
        description=l_(
            "The order in which files are played (only used when mode is 'files')"
        ),
    )
    files = FieldList(FormField(MohFilesForm))
    submit = SubmitField(l_('Submit'))
