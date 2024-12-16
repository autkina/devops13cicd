import http.server
import socketserver
PORT = 8000
class TestMe(): #test me for tests
	def take_five(self): #return a number
		return 5
	def port(self): # return port for smthg
		return PORT
if __name__ == '__main__': #exe
	Handler = http.server.SimpleHTTPRequestHandler
	with socketserver.TCPServer(("", PORT), Handler) as http: #a little magic
		print("serving at port", PORT)
		http.serve_forever()
