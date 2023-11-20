from flask import Flask, request, jsonify
import json
import subprocess

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        input_data = data.get('data')

        # Print the received data to the terminal
        print(f"Received data from extension: {input_data}")

        # Write the YouTube ID to a JSON file
        with open('praktiskais\server\youtube_id.json', 'w') as json_file:
            json.dump({"youtube_id": input_data}, json_file)

        # Execute try.py
        filename_for_output = "praktiskais/comments/hybrid_RoB&VAD.py"
        try_process = subprocess.Popen(["python", filename_for_output], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try_output, try_error = try_process.communicate()

        if try_process.returncode == 0:
            print(f"output: {try_output.decode('utf-8')}")
            result = {"result": try_output.decode('utf-8')}
        else:
            print(f"Error running try.py: {try_error.decode('utf-8')}")
            result = {"error": try_error.decode('utf-8')}

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
