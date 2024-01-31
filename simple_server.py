from http.server import BaseHTTPRequestHandler, HTTPServer


# Request handler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Sending HTTP headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Determining the Requested Path
        path = self.path

        # Parsing request parameters
        params = {}
        if '?' in path:
            path, params_str = path.split('?', 1)
            params = dict(pair.split('=') for pair in params_str.split('&'))

        # Processing GET requests
        if path == '/':
            # Sending the byte string "Hello, World!"
            self.wfile.write(b'Hello, World!')
        elif path == '/greet':
            # Getting the user parameter from a request
            user = params.get('user', 'Guest')

            # Send a personalized greeting
            greeting = f'Hello, {user}!'
            self.wfile.write(greeting.encode('utf-8'))
        elif path == '/about':
            # Sending a byte string "About Us"
            self.wfile.write(b'About Us')
        else:
            # If the path is not recognized, send 404
            self.send_error(404, 'Not Found')

    def do_POST(self):
        # Sending HTTP headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Receiving data from a POST request
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Converting data to a string and displaying it in console
        data_str = post_data.decode('utf-8')
        print(f'Received POST data: {data_str}')

        # Sending a "you are welcome" response
        self.wfile.write(b'You are welcome')


# Set the server address and port
host = 'localhost'
port = 8000

# Create an HTTP server instance with the specified handler
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

# Displaying information about the launch
print(f'Starting server on {host}:{port}')

# We start the server and wait for the event to complete
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    # Close the server when finished
    server.server_close()
    print('Server stopped.')
