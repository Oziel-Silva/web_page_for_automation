from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse 
import socket

def index(request):
	return render(request, 'index.html',{})

def quarto(request):
	return render(request, 'quarto.html',{})

def sala(request):
	return render(request, 'sala.html',{})

def area_externa(request):
	return render(request, 'area_externa.html',{})

def open_socket(request):
	TCP_IP = "10.42.0.113"
	TCP_PORT = 9000
	MESSAGE = "1"
	BUFFER_SIZE = len(MESSAGE)

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((TCP_IP, TCP_PORT))
	sock.send(MESSAGE)
	data = sock.recv(BUFFER_SIZE)
	sock.close()