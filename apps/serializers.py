from rest_framework import serializers

from apps.contacts.models import Contacts

# class ContactsModel:
#     def __int__(self, name, phone):
#         self.title = name
#         self.phone = phone


class ContactsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    phone = serializers.CharField()
    date_of_birth = serializers.DateField()
    is_auto_generated = serializers.BooleanField(default=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    group_id = serializers.IntegerField()

    def create(self, validated_data):
        return Contacts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.name)
        instance.is_auto_generated = validated_data.get('is_auto_generated', instance.name)
        instance.created_at = validated_data.get('created_at', instance.name)
        instance.updated_at = validated_data.get('updated_at', instance.name)
        instance.group_id = validated_data.get('group_id', instance.name)
        instance.save()
        return instance






# def encode():
#     model = ContactsModel(name, )
#     # class Meta:
#     #     model = Contacts
#     #     fields = ("name", "phone")
#
