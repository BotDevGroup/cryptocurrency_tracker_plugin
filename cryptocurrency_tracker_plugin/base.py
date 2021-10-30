# -*- coding: utf-8 -*-
from marvinbot.handlers import CommandHandler
from marvinbot.plugins import Plugin
from datetime import datetime
import logging
import requests

log = logging.getLogger(__name__)


class CryptocurrencyTrackerPlugin(Plugin):
    def __init__(self):
        super(CryptocurrencyTrackerPlugin, self).__init__('cryptotracker_plugin')

    def get_default_config(self):
        return {
            'short_name': self.name,
            'enabled': True,
            'cryptonator.base_url': 'https://api.cryptonator.com/api/ticker/'
        }

    def configure(self, config):
        self.config = config

    def setup_handlers(self, adapter):
        self.add_handler(CommandHandler('ticker', self.on_ticker,
                                        command_description='Fetch volume-weighted price, total 24h volume, rate '
                                                            'change.')
                         .add_argument('base', help='Base currency code')
                         .add_argument('target', nargs='?', help='Target currency code', default='USD'))

    def setup_schedules(self, adapter):
        pass

    def provide_blueprint(self, config):
        pass

    def fetch_ticker(self, base, target):
        base_url = self.config.get('cryptonator.base_url')
        url = f'{base_url}{base}-{target}'
        log.info(f'fetching {url}')
        headers = {
            'Accept': 'application/json; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    def on_ticker(self, update, base, target='USD'):
        target = target.upper()
        base = base.upper()
        message = update.effective_message

        try:
            data = self.fetch_ticker(base, target)
            ticker = data['ticker']
            timestamp = data['timestamp']
            if data is None or not data['success']:
                error = data['error']
                message.reply_text(text=f'❌ Unable to fetch ticker information for {base}-{target}.'
                                        f'Reason: {error}')
            date = datetime.fromtimestamp(timestamp)
            change = ticker['change']
            change_emoji = '📈' if float(change) > 0 else '📉'
            change_word = 'rising' if float(change) > 0 else 'falling'
            price = ticker['price']
            volume = ticker['volume']
            message.reply_text(text=f'*{base}* -> *{target}* @ {date} UTC\n\n'
                                    f'💰 Price: {price} \n'
                                    f'{change_emoji} 1-Hour Change: {change} ({change_word})\n'
                                    f'📊 24-Hour Volume: {volume}',
                               parse_mode='markdown')
        except Exception as ex:
            message.reply_text(text=f'❌ Unable to fetch ticker information for {base}-{target}. Reason: {ex}')
            log.error(ex)


