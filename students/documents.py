from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Students
# from elasticsearch_dsl import analyzer,

# html_strip = analyzer(
#         'html_strip',
#         tokenizer="standard",
#         filter=["lowercase", "stop", "snowball"],
#         char_filter=["html_strip"]
#     )

@registry.register_document
class CarDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'new_students'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
        
       

    class Django:
        model = Students # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'registration_number',
            'first_name',
            'last_name',
            'gender',
            'date_of_admission',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        queryset_pagination = 1000