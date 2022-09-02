import requests

from configs.config import Config

from .auth import Auth
from .utils import is_successful, urljoin


def service_info(service_id):
    response = requests.get(
        urljoin(
            Config.instance().bms_url,
            '/api/viewer-services',
        ),
        headers=Auth.instance().jwt_header(),
    )

    if not is_successful(response):
        raise SystemExit('Not able to receive service details.')

    for service in response.json():
        if service['id'] == service_id:
            return service

def pattern_list(company_code, customer_id, service_id):
    response = requests.get(
        urljoin(
            Config.instance().bms_url,
            'api',
            f'companies/{company_code}',
            f'customers/{customer_id}',
            f'services/{service_id}',
            'patterns',
        ),
        headers=Auth.instance().jwt_header(),
    )

    if not is_successful(response):
        raise SystemExit('Not able to receive pattern list.')

    patterns = response.json()['services'][str(service_id)]['patterns']
    return [pattern for upid, pattern in patterns.items()]
