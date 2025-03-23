from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "مرحبًا بك في البث الصوتي!"

@app.route("/stream")
def stream():
    def generate_audio():
        with open("Sound.mp3", "rb") as f:
            chunk = f.read(1024)
            while chunk:
                yield chunk
                chunk = f.read(1024)

    return Response(generate_audio(), mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
