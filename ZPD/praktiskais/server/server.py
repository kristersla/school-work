from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import json
from urllib.parse import urlparse, parse_qs
import subprocess

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, data):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        if self.path.startswith('/getData'):
            query = parse_qs(urlparse(self.path).query)
            video_id = query.get('video_id', [''])[0]  # Get the video_id parameter from the query string
            with open('praktiskais\server\youtube_id.json', 'w') as json_file:
                json.dump({"youtube_id": video_id}, json_file)
            response_data = self.run_try_script(video_id)
            self._send_response(response_data)


    def run_try_script(self, video_id):
        try:
            # Run try.py and capture its output
            output = subprocess.check_output(['python', 'praktiskais\\comments\\hybrid_RoB&VAD.py'], text=True)

            # Construct the response message
            response_message = f'{output.strip()}'

            return {'message': response_message}

        except Exception as e:
            print(f"Error running try.py: {e}")
            return {'message': f'Error running try.py: {e}'}

if __name__ == '__main__':
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Python server is running at http://localhost:8080')
    httpd.serve_forever()
