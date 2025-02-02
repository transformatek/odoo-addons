from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class ResUsersApiKeys(models.Model):
    _inherit = 'res.users.apikeys'

    @api.model
    def create_and_return_key(self, values):
        # Create the API key
        api_key = self.create(values)
        # Return the newly created API key (which is only available once)
        return {'key': api_key.token}