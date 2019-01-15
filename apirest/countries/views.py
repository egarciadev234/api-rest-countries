from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Country
from .serializers import CountrySerializer
from django.http import *

class ListCountries(APIView):
	def get(self, request):
		#Esta funcion retorna toda la informacion existente del modelo
		countries = Country.objects.all()
		countries_json = CountrySerializer(countries, many=True)
		return Response(countries_json.data)

	def post(self, request):
		#Esta funcion permite registrar un nuevo registro a nuestro modelo
		country_json = CountrySerializer(data = request.data)
		if country_json.is_valid():
			country_json.save()
			return Response(country_json.data, status=201)
		return Response(status=400)

class DetailCountry(APIView):
	def get_object(self, pk):
		#Esta funcion permite crear una funcion para extender la consulta al modelo una sola vez dentro de la clase
		try:
			return Country.objects.get(pk=pk)
		except Country.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		#Esta funcion permite devolver toda la informacion de un registro existente
		country = self.get_object(pk)
		country_json = CountrySerializer(country)
		return Response(country_json.data)
		

	def put(self, request, pk):
		#Esta funcion permite editar la informacion referente a un registro existente
		country = self.get_object(pk)
		country_json = CountrySerializer(country, data=request.data)
		if country_json.is_valid():
			country_json.save()
			return Response(country_json.data)
		return Response(status=400)
		
	def delete(self, request, pk):
		#Esta funcion permite elimnar la informacion de un registro existente
		country = self.get_object(pk)
		country.delete()
		return Response(status=204)