import requests

from utils.auth import Auth
from utils.config import Config
from utils.utils import is_successful, urljoin


def companies_list():
    response = requests.get(
        urljoin(
            Config.instance().bms_url,
            '/api/companies',
        ),
        headers=Auth.instance().jwt_header(),
    )

    if not is_successful(response):
        raise SystemExit('Not able to receive companies list.')

    return list(response.json()['companies'].keys())


def customers_list(company_code):
    response = requests.get(
        urljoin(
            Config.instance().bms_url,
            '/api',
            f'/companies/{company_code}',
            '/customers',
        ),
        headers=Auth.instance().jwt_header(),
    )

    if not is_successful(response):
        raise SystemExit('Not able to receive customers list.')

    return [
        int(customer_id) for customer_id in response.json()['customers'].keys()
    ]


def products_list(company_code, customer_id):
    response = requests.get(
        urljoin(
            Config.instance().bms_url,
            '/api',
            f'/companies/{company_code}',
            f'/customers/{customer_id}',
            '/products',
        ),
        headers=Auth.instance().jwt_header(),
    )

    if not is_successful(response):
        raise SystemExit('Not able to receive products list.')

    return [product for barcode, product in response.json()['products'].items()]


def product_update(body, company_code, customer_id, product_id):
    response = requests.patch(
        urljoin(
            Config.instance().bms_url,
            '/api',
            f'/companies/{company_code}',
            f'/customers/{customer_id}',
            f'/products/{product_id}',
        ),
        json=body,
        headers=Auth.instance().jwt_header(),
    )

    if not is_successful(response):
        raise SystemExit('Not able to update a product.')

    return response


def patterns_list(company_code, customer_id, product_id):
    response = requests.get(
        urljoin(
            Config.instance().bms_url,
            '/api',
            f'/companies/{company_code}',
            f'/customers/{customer_id}',
            f'/products/{product_id}',
            '/patterns'
        ),
        headers=Auth.instance().jwt_header(),
    )

    if not is_successful(response):
        raise SystemExit('Not able to receive patterns list.')

    return [pattern for upid, pattern in response.json()['patterns'].items()]


def pattern_update(body, company_code, customer_id, product_id, pattern_upid):
    response = requests.patch(
        urljoin(
            Config.instance().bms_url,
            '/api',
            f'/companies/{company_code}',
            f'/customers/{customer_id}',
            f'/products/{product_id}',
            f'/patterns/{pattern_upid}',
        ),
        json=body,
        headers=Auth.instance().jwt_header(),
    )

    if not is_successful(response):
        raise SystemExit('Not able to update a pattern.')

    return response
