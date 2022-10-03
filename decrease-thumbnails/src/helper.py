import base64
import imghdr
import hashlib
import requests

from utils.url_modification import optimize_url
from utils.utils import to_bytes

from . import bms


def find_company(customer_id):
    for company_code in bms.companies_list():
        if customer_id in bms.customers_list(company_code):
            return company_code
    raise SystemExit(f'No company found for customer {customer_id}')


def decrease_thumbnails(
    products, company_code, customer_id, max_dimension, quality,
):
    count = len(products)
    print(f'Start decreasing the thumbnails size for {count} products.')

    for idx, product in enumerate(products):
        print(f'{idx + 1}/{count} - {product["barcode"]} ... ',
              end=' ', flush=True)
        decrease_product(
            product=product,
            company_code=company_code,
            customer_id=customer_id,
            max_dimension=max_dimension,
            quality=quality,
        )

        patterns = bms.patterns_list(
            company_code=company_code,
            customer_id=customer_id,
            product_id=product['productID'],
        )
        for pattern in patterns:
            print(f'    {pattern["UPID"]} ... ', end=' ', flush=True)
            decrease_pattern(
                pattern=pattern,
                company_code=company_code,
                customer_id=customer_id,
                product_id=product['productID'],
                max_dimension=max_dimension,
                quality=quality,
            )
    print()
    print('Decreasing the size of thumbnails is completed successfully.')


def decrease_product(
    product, company_code, customer_id, max_dimension, quality,
):
    unit = 'KB'

    original_url = product['images']['front']
    original_thumbnail = requests.get(original_url).content

    decreased_url = optimize_url(
        url=original_url,
        max_dimension=max_dimension,
        quality=quality,
    )
    decreased_thumbnail = requests.get(decreased_url).content
    bms.product_update(
        body={'images': {'front': image2json(decreased_thumbnail)}},
        company_code=company_code,
        customer_id=customer_id,
        product_id=product['productID'],
    )

    original_size = to_bytes(content=original_thumbnail, ndigits=2, unit=unit)
    decreased_size = to_bytes(content=decreased_thumbnail, ndigits=2, unit=unit)
    print(f'{original_size} {unit} to {decreased_size} {unit}')


def decrease_pattern(
    pattern, company_code, customer_id, product_id, max_dimension, quality,
):
    unit = 'KB'

    original_url = pattern['image']
    original_thumbnail = requests.get(original_url).content

    decreased_url = optimize_url(
        url=original_url,
        max_dimension=max_dimension,
        quality=quality,
    )
    decreased_thumbnail = requests.get(decreased_url).content
    bms.pattern_update(
        body={'image': image2json(decreased_thumbnail)},
        company_code=company_code,
        customer_id=customer_id,
        product_id=product_id,
        pattern_upid=pattern['UPID'],
    )

    original_size = to_bytes(content=original_thumbnail, ndigits=2, unit=unit)
    decreased_size = to_bytes(content=decreased_thumbnail, ndigits=2, unit=unit)
    print(f'{original_size} {unit} to {decreased_size} {unit}')


def image2json(image: bytes):
    md5 = hashlib.md5(image).digest()
    extension = imghdr.what('', h=image)
    if extension not in ['jpeg', 'bmp', 'png']:
        raise SystemExit(f'Invalid image extension {extension}')
    return {
        'data': base64.b64encode(image).decode('utf-8'),
        'md5': base64.b64encode(md5).decode('utf-8'),
        'ext': 'jpg' if extension == 'jpeg' else extension,
    }
