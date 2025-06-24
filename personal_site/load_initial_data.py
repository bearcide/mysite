# load_initial_data.py
import json
from points.models import Section, Point, BulletPoint

def load_data():
    with open('fixtures.json') as f:
        data = json.load(f)
        
        for item in data:
            if item['model'] == 'points.section':
                section = Section.objects.create(
                    title=item['fields']['title'],
                    description=item['fields']['description']
                )
                section.tags.add(*item['fields']['tags'])
                
            elif item['model'] == 'points.point':
                point = Point.objects.create(
                    section=Section.objects.get(pk=item['fields']['section']),
                    title=item['fields']['title'],
                    description=item['fields']['description'],
                    start_date=item['fields']['start_date'],
                    end_date=item['fields']['end_date']
                )
                point.tags.add(*item['fields']['tags'])
                
            elif item['model'] == 'points.bulletpoint':
                bullet = BulletPoint.objects.create(
                    point=Point.objects.get(pk=item['fields']['point']),
                    sentence=item['fields']['sentence']
                )
                bullet.tags.add(*item['fields']['tags'])

if __name__ == '__main__':
    load_data()