import os
import django
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from authors_app.models import Author, Quote, Tag
from m10.settings import env


class Command(BaseCommand):
    help = 'Migrate data from MongoDB to PostgreSQL'

    def handle(self, *args, **kwargs):

        client = MongoClient(env("MONGO_STRING"))
        db = client.get_database("module9")


        authors_collection = db.get_collection('authors')
        authors=authors_collection.find({})
        for author in authors:
            Author.objects.get_or_create(
                fullname=author["fullname"],
                born_date=author["born_date"],
                born_location=author["born_location"],
                description=author["description"]
            )

        
        quotes_collection = db.get_collection('quotes')
        quotes=quotes_collection.find({})
        for quote in quotes:
            tags_list = []
            for tag in quote['tags']:
                # print(tag)
                t, _ = Tag.objects.get_or_create(name=tag)
                tags_list.append(t)
                # print(tags_list)
            author = authors_collection.find_one({'_id': quote['author']})
            a = Author.objects.get(fullname=author['fullname'])
            # print(a)
            q = Quote.objects.get_or_create(
                quote=quote['quote'],
                author=a,
            )
            for tag in tags_list:
                q[0].tags.add(tag)


        self.stdout.write(self.style.SUCCESS('Successfully migrated data from MongoDB to PostgreSQL'))