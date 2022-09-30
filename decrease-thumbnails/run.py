#!/usr/bin/env python3

import environments
from utils.auth import Auth
from utils.config import Config

from src import bms
from src.argparse import parser
from src.helper import decrease_thumbnails, find_company


def execute(customer_id):
    Config(config_provider=environments.DIG_2021_1())
    Auth(
        sso_url=Config.instance().sso_url,
        username=Config.instance().username,
        password=Config.instance().password
    )

    company_code = find_company(customer_id=customer_id)
    products = bms.products_list(
        company_code=company_code,
        customer_id=customer_id,
    )
    decrease_thumbnails(
        products=products,
        company_code=company_code,
        customer_id=customer_id,
        max_dimension=700,
        quality=50,
    )


if __name__ == '__main__':
    args = parser.parse_args()
    execute(customer_id=args.customer)
