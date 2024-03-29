from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from dotenv import load_dotenv
load_dotenv()
import os
import requests
TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')

# Create your views here.
class Endpoints(APIView):
    def get(self, request):
        print("TWITTER_API_KEY:", TWITTER_API_KEY)
        data = ['/advocates', '/advocates/: username']
        return Response(data)
#@permission_classes([IsAuthenticated])
class AdvocateList(APIView):
    def get(self, request):
        query = request.query_params.get('query', '')
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvocateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AdvocateDetail(APIView):
    def get_object(self, username):

        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse("Advocate does not exist!")

    def get(self, request, username):
        head = {'Authorization': f'API_KEY {TWITTER_API_KEY}'}

        url = "https://api.twitter.com/2/users/by/username/" + str(username)
        response = requests.get(url, headers=head).json()

        # Print the entire response to inspect its structure
        print('RESPONSE FROM TWITTER:', response)

        # Check if 'data' exists in the response
        if 'data' in response:
            data = response['data']
            print('DATA FROM TWITTER:', data)
        else:
            print('Error: No data found in the response')

        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)

        return Response(serializer.data)

    def put(self, request, username):

        advocate = self.get_object(username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        serializer = AdvocateSerializer(advocate, many=False)

        return Response(serializer.data)
    def delete(self, request, username):

        advocate = self.get_object(username)
        advocate.delete()

        return Response('user was deleted')
class CompaniesList(APIView):
    def get(self,request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)