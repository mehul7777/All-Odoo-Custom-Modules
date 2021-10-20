from odoo import api, fields, models
import requests
import json


class WeatherInfo(models.Model):
    _name = 'weather.info'
    _rec_name = 'city'

    city = fields.Char("City")
    state_code = fields.Integer()
    wind_direction = fields.Integer()
    clouds = fields.Integer()
    description = fields.Char()

    # @api.onchange('city')
    # def onchange_partner_id(self):
    #         key = 'eb3f17ab30244966a3c266f7afc21a57'
    #         # city = input("Enter city name: ")
    #         url = f'https://api.weatherbit.io/v2.0/current?&city={self.city}&key=' + key
    #         response = requests.get(url)
    #         # print(response)
    #         dict_res = json.loads(response.text)
    #         attendances = self.env['weather.info'].search([
    #             ('id', '=', self.id),
    #         ])
    #         weather_data = attendances.update({
    #             'city': self.city,
    #             'state_code': dict_res["data"][0]["state_code"],
    #             'wind_direction': dict_res["data"][0]["wind_dir"],
    #             'clouds': dict_res["data"][0]["clouds"],
    #             'description': dict_res["data"][0]["weather"]["description"],
    #         })

