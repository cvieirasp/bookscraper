# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Strip all whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()
        
        # Switch Category and Product Type to lowercase
        lowercase_fields = ['category', 'product_type']
        for field_name in lowercase_fields:
            value = adapter.get(field_name)
            adapter[field_name] = value.lower()

        # Convert price to float
        price_fields = ['price_excl_tax', 'price_incl_tax', 'tax', 'price']
        for field_name in price_fields:
            value = adapter.get(field_name)
            adapter[field_name] = float(value.replace('£', ''))

        # Extract number of books from availability
        availability = adapter.get('availability')
        match = re.search(r'\d+', availability)
        if match:
            adapter['availability'] =  int(match.group(0))
        else:
            adapter['availability'] =  0

        # Extract number of reviews
        number_of_reviews = adapter.get('number_of_reviews')
        adapter['number_of_reviews'] = int(number_of_reviews)

        # Extract stars
        stars = adapter.get('stars')
        split_stars = stars.split(' ')
        stars_text = split_stars[1].lower()
        if stars_text == 'zero':
            adapter['stars'] = 0
        elif stars_text == 'one':
            adapter['stars'] = 1
        elif stars_text == 'two':
            adapter['stars'] = 2
        elif stars_text == 'three':
            adapter['stars'] = 3
        elif stars_text == 'four':
            adapter['stars'] = 4
        elif stars_text == 'five':
            adapter['stars'] = 5

        return item
