import json
from django.core.management.base import BaseCommand
from dashboard.models import DataEntry
from django.utils import timezone
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Load data from JSON file into DataEntry model'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file to load data from')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as f:
            data = json.load(f)
            for i,entry in enumerate(data, start=1):
                print("Inserting Data................",i)
                self._create_data_entry(entry)
            print("Inserted All The Data: ",len(data))

    def _create_data_entry(self, entry):
        # Convert types and handle empty strings
        end_year = int(entry['end_year']) if entry['end_year'] else None
        intensity = int(entry['intensity']) if entry['intensity'] else None
        sector = entry['sector'] if entry['sector'] else None
        topic = entry['topic'] if entry['topic'] else None
        insight = entry['insight'] if entry['insight'] else None
        url = entry['url'] if entry['url'] else None
        region = entry['region'] if entry['region'] else None
        start_year = int(entry['start_year']) if entry['start_year'] else None
        impact = int(entry['impact']) if entry['impact'] else None
        added = self._parse_date(entry['added'])
        published = self._parse_date(entry['published'])
        country = entry['country'] if entry['country'] else None
        relevance = int(entry['relevance']) if entry['relevance'] else None
        pestle = entry['pestle'] if entry['pestle'] else None
        source = entry['source'] if entry['source'] else None
        title = entry['title'] if entry['title'] else None
        likelihood = int(entry['likelihood']) if entry['likelihood'] else None

        # Create DataEntry instance
        DataEntry.objects.create(
            end_year=end_year,
            intensity=intensity,
            sector=sector,
            topic=topic,
            insight=insight,
            url=url,
            region=region,
            start_year=start_year,
            impact=impact,
            added=added,
            published=published,
            country=country,
            relevance=relevance,
            pestle=pestle,
            source=source,
            title=title,
            likelihood=likelihood
        )

    def _parse_date(self, date_str):
        if date_str:
            try:
                dt = parse_datetime(date_str)
                if dt is not None:
                    return timezone.make_aware(dt, timezone.get_current_timezone())
            except ValueError:
                return None
        return None
