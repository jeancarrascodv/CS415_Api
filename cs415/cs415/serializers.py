from rest_framework import serializers
from cs415.models import Webuser, Addresstype, Useraddress, Userinfo, Phonetype, Userphone, Pagedata

class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webuser
        fields = ['web_user_id', 'first_name', 'last_name', 'email', 'created_date', 'is_active', 'last_login']

class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresstype
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = ['user_address_id', 'web_user_id', 'street_1', 'street_2', 'city', 'st', 'zip', 'country', 'created_date', 'address_type_id']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = ['user_info_id', 'web_user_id', 'profile_bio', 'profile_picture', 'modified_date', 'created_date']

class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetype
        fields = ['phone_type_id', 'phone_type']

class UserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userphone
        fields = ['user_phone_id', 'phone_type_id', 'phone_number', 'created_date', 'is_active', 'web_user_id']

class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagedata
        fields = ['page_data_id', 'page_name', 'page_title', 'page_description', 'page_picture', 'page_menu']
