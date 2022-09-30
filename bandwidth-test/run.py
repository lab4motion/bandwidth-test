#!/usr/bin/env python3

import environments
from utils.auth import Auth
from utils.config import Config
from utils.url_modification import optimize_urls

from src import benchmark
from src import bms
from src.argparse import parser


def execute(service_id, optimize):
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

    if optimize:
        url_list = optimize_urls(
            urls=url_list,
            max_dimension=700,
            quality=50,
        )

    benchmark.start(urls=url_list)


if __name__ == '__main__':
    args = parser.parse_args()
    execute(service_id=args.service, optimize=args.optimize)
