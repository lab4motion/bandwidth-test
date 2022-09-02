#!/usr/bin/env python3

from configs import environments
from configs.config import Config
from src import benchmark
from src import bms
from src.argparse import parser
from src.auth import Auth


def execute(service_id):
    Config(config_provider=environments.DIG_2021_1())
    Auth(
        sso_url=Config.instance().sso_url,
        username=Config.instance().username,
        password=Config.instance().password
    )

    service = bms.service_info(service_id=service_id)
    patterns = bms.pattern_list(
        company_code=service['company'],
        customer_id=service['customer'],
        service_id=service['id'],
    )
    url_list = [pattern['image'] for pattern in patterns]

    benchmark.start(urls=url_list)


if __name__ == '__main__':
    args = parser.parse_args()
    execute(service_id=args.service)
