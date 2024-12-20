from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from cs415.models import Webuser, Addresstype, Useraddress, Userinfo, Phonetype, Userphone, Pagedata
from cs415.serializers import ( WebUserSerializer, AddressTypeSerializer, UserAddressSerializer, UserInfoSerializer, PhoneTypeSerializer, UserPhoneSerializer, PageDataSerializer )
from drf_yasg.utils import swagger_auto_schema


class WebUserAPIView(APIView):
    @swagger_auto_schema(responses={200: WebUserSerializer(many=True)})
    def get(self, request):
        users = Webuser.objects.all()
        serializer = WebUserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=WebUserSerializer, responses={201: WebUserSerializer})
    def post(self, request, *args, **kwargs):
        request.data['created_date'] = str(datetime.now())
        request.data['is_active'] = 1
        serializer = WebUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SingleWebUserAPIView(APIView):
    @swagger_auto_schema(operation_description="Get Single WebUser", responses={200: WebUserSerializer})
    def get(self, request, web_user_id):
        user_data = {}
        user = Webuser.objects.get(web_user_id=web_user_id)
        user_serial = WebUserSerializer(user)
        user_data.update({"user": user_serial.data})
        addresses = UserAddressSerializer(Useraddress.objects.filter(web_user=user), many=True)
        user_data.update({"addresses": addresses.data})
        info = UserInfoSerializer(Userinfo.objects.filter(web_user=user), many=True)
        user_data.update({"info": info.data})
        phone = UserPhoneSerializer(Userphone.objects.filter(web_user=user).select_related(), many=True)
        user_data.update({"phones": phone.data})
        return Response(user_data)
        try:
            webuser_obj = Webuser.objects.get(web_user_id=web_user_id)
            serializer = WebUserSerializer(webuser_obj)
            return Response(serializer.data)
        except Webuser.DoesNotExist:
            return Response({'error': 'WebUser not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Update WebUser", request_body=WebUserSerializer)
    def patch(self, request, web_user_id):
        try:
            webuser_obj = Webuser.objects.get(web_user_id=web_user_id)
            serializer = WebUserSerializer(webuser_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Webuser.DoesNotExist:
            return Response({'error': 'WebUser not found'}, status=status.HTTP_404_NOT_FOUND)


class AddressTypeAPIView(APIView):
    @swagger_auto_schema(responses={200: AddressTypeSerializer(many=True)})
    def get(self, request):
        address_types = Addresstype.objects.all()
        serializer = AddressTypeSerializer(address_types, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AddressTypeSerializer, responses={201: AddressTypeSerializer})
    def post(self, request, *args, **kwargs):
        serializer = AddressTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SingleAddressTypeAPIView(APIView):
    @swagger_auto_schema(operation_description="Get Single AddressType", responses={200: AddressTypeSerializer})
    def get(self, request, address_type_id):
        try:
            address_type = Addresstype.objects.get(address_type_id=address_type_id)
            serializer = AddressTypeSerializer(address_type)
            return Response(serializer.data)
        except Addresstype.DoesNotExist:
            return Response({'error': 'AddressType not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Update AddressType", request_body=AddressTypeSerializer)
    def patch(self, request, address_type_id):
        try:
            address_type = Addresstype.objects.get(address_type_id=address_type_id)
            serializer = AddressTypeSerializer(address_type, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Addresstype.DoesNotExist:
            return Response({'error': 'AddressType not found'}, status=status.HTTP_404_NOT_FOUND)


class UserAddressAPIView(APIView):
    @swagger_auto_schema(responses={200: UserAddressSerializer(many=True)})
    def get(self, request):
        user_addresses = Useraddress.objects.all()
        serializer = UserAddressSerializer(user_addresses, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserAddressSerializer, responses={201: UserAddressSerializer})
    def post(self, request, *args, **kwargs):
        serializer = UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SingleUserAddressAPIView(APIView):
    @swagger_auto_schema(operation_description="Get Single UserAddress", responses={200: UserAddressSerializer})
    def get(self, request, user_address_id):
        try:
            user_address = Useraddress.objects.get(user_address_id=user_address_id)
            serializer = UserAddressSerializer(user_address)
            return Response(serializer.data)
        except Useraddress.DoesNotExist:
            return Response({'error': 'UserAddress not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Update UserAddress", request_body=UserAddressSerializer)
    def patch(self, request, user_address_id):
        try:
            user_address = Useraddress.objects.get(user_address_id=user_address_id)
            serializer = UserAddressSerializer(user_address, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Useraddress.DoesNotExist:
            return Response({'error': 'UserAddress not found'}, status=status.HTTP_404_NOT_FOUND)


class UserInfoAPIView(APIView):
    @swagger_auto_schema(responses={200: UserInfoSerializer(many=True)})
    def get(self, request):
        user_infos = Userinfo.objects.all()
        serializer = UserInfoSerializer(user_infos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserInfoSerializer, responses={201: UserInfoSerializer})
    def post(self, request, *args, **kwargs):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SingleUserInfoAPIView(APIView):
    @swagger_auto_schema(operation_description="Get Single UserInfo", responses={200: UserInfoSerializer})
    def get(self, request, user_info_id):
        try:
            user_info = Userinfo.objects.get(user_info_id=user_info_id)
            serializer = UserInfoSerializer(user_info)
            return Response(serializer.data)
        except Userinfo.DoesNotExist:
            return Response({'error': 'UserInfo not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Update UserInfo", request_body=UserInfoSerializer)
    def patch(self, request, user_info_id):
        try:
            user_info = Userinfo.objects.get(user_info_id=user_info_id)
            serializer = UserInfoSerializer(user_info, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Userinfo.DoesNotExist:
            return Response({'error': 'UserInfo not found'}, status=status.HTTP_404_NOT_FOUND)


class PhoneTypeAPIView(APIView):
    @swagger_auto_schema(responses={200: PhoneTypeSerializer(many=True)})
    def get(self, request):
        phone_types = Phonetype.objects.all()
        serializer = PhoneTypeSerializer(phone_types, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PhoneTypeSerializer, responses={201: PhoneTypeSerializer})
    def post(self, request, *args, **kwargs):
        serializer = PhoneTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SinglePhoneTypeAPIView(APIView):
    @swagger_auto_schema(operation_description="Get Single PhoneType", responses={200: PhoneTypeSerializer})
    def get(self, request, phone_type_id):
        try:
            phone_type = Phonetype.objects.get(phone_type_id=phone_type_id)
            serializer = PhoneTypeSerializer(phone_type)
            return Response(serializer.data)
        except Phonetype.DoesNotExist:
            return Response({'error': 'PhoneType not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Update PhoneType", request_body=PhoneTypeSerializer)
    def patch(self, request, phone_type_id):
        try:
            phone_type = Phonetype.objects.get(phone_type_id=phone_type_id)
            serializer = PhoneTypeSerializer(phone_type, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Phonetype.DoesNotExist:
            return Response({'error': 'PhoneType not found'}, status=status.HTTP_404_NOT_FOUND)


class UserPhoneAPIView(APIView):
    @swagger_auto_schema(responses={200: UserPhoneSerializer(many=True)})
    def get(self, request):
        user_phones = Userphone.objects.all()
        serializer = UserPhoneSerializer(user_phones, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserPhoneSerializer, responses={201: UserPhoneSerializer})
    def post(self, request, *args, **kwargs):
        serializer = UserPhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SingleUserPhoneAPIView(APIView):
    @swagger_auto_schema(operation_description="Get Single UserPhone", responses={200: UserPhoneSerializer})
    def get(self, request, user_phone_id):
        try:
            user_phone = Userphone.objects.get(user_phone_id=user_phone_id)
            serializer = UserPhoneSerializer(user_phone)
            return Response(serializer.data)
        except Userphone.DoesNotExist:
            return Response({'error': 'UserPhone not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Update UserPhone", request_body=UserPhoneSerializer)
    def patch(self, request, user_phone_id):
        try:
            user_phone = Userphone.objects.get(user_phone_id=user_phone_id)
            serializer = UserPhoneSerializer(user_phone, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Userphone.DoesNotExist:
            return Response({'error': 'UserPhone not found'}, status=status.HTTP_404_NOT_FOUND)


class PageDataAPIView(APIView):
    @swagger_auto_schema(responses={200: PageDataSerializer(many=True)})
    def get(self, request):
        page_data = Pagedata.objects.all()
        serializer = PageDataSerializer(page_data, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PageDataSerializer, responses={201: PageDataSerializer})
    def post(self, request, *args, **kwargs):
        serializer = PageDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SinglePageDataAPIView(APIView):
    @swagger_auto_schema(operation_description="Get Single PageData", responses={200: PageDataSerializer})
    def get(self, request, page_data_id):
        try:
            page_data = Pagedata.objects.get(page_data_id=page_data_id)
            serializer = PageDataSerializer(page_data)
            return Response(serializer.data)
        except Pagedata.DoesNotExist:
            return Response({'error': 'PageData not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_description="Update PageData", request_body=PageDataSerializer)
    def patch(self, request, page_data_id):
        try:
            page_data = Pagedata.objects.get(page_data_id=page_data_id)
            serializer = PageDataSerializer(page_data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Pagedata.DoesNotExist:
            return Response({'error': 'PageData not found'}, status=status.HTTP_404_NOT_FOUND)
