from rest_framework import serializers
from .models import Tabinfo

class TabinfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tabinfo
        fields = ('tab_name', 'ingredients', 'unit_mg', 'company', 'uses', 'side_effect',)

        def create(self, validated_data):
            return Tabinfo.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.tab_name = validated_data.get('tab_name', instance.tab_name)
            instance.ingredients = validated_data.get('ingredients', instance.ingredients)
            instance.unit_mg = validated_data.get('unit_mg', instance.unit_mg)
            instance.company = validated_data.get('company', instance.company)
            instance.uses = validated_data.get('uses', instance.uses)
            instance.side_effects = validated_data.get('side_effects', instance.side_effects)
            instance.save()
            return instance
