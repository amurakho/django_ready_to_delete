import string
from slugify import slugify
import random
# import os


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(content):
    slug = slugify(content)
    new_slug = "{slug}-{randstr}".format(
        slug=slug, randstr=random_string_generator(size=4))
    return new_slug


def get_product_image_dir_path(instance, filename):
    # name = f'image_{instance.product.title}_{instance.product.code}/{filename}'
    # return os.path.join('products', name)
    return f'image_{instance.product.title}_{instance.product.code}/{filename}'