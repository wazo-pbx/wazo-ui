# Copyright 2020-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_menu.classy import register_flaskview
from wazo_ui.helpers.plugin import create_blueprint

from .service import PhonebookService, ManagePhonebookService
from .view import PhonebookView, ManagePhonebookView

phonebook = create_blueprint('phonebook', __name__)


class Plugin(object):

    def load(self, dependencies):
        core = dependencies['flask']
        clients = dependencies['clients']

        PhonebookView.service = PhonebookService(clients['wazo_dird'])
        PhonebookView.register(phonebook, route_base='/phonebooks')
        register_flaskview(phonebook, PhonebookView)

        ManagePhonebookView.service = ManagePhonebookService(clients['wazo_dird'])
        ManagePhonebookView.register(phonebook, route_base='/manage_phonebooks')
        register_flaskview(phonebook, ManagePhonebookView)

        core.register_blueprint(phonebook)
