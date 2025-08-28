from flask import Flask, Response

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<title>Site Hacklendi</title>
<style>
    body, html {
        margin: 0;
        padding: 0;
        height: 100%;
        overflow: hidden;
        background-color: black;
        color: #00ff00;
        font-family: "Courier New", Courier, monospace;
    }
    .title {
        position: absolute;
        top: 20px;
        width: 100%;
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00;
    }
    .subtitle {
        position: absolute;
        top: 80px;
        width: 100%;
        text-align: center;
        font-size: 1.5em;
        text-shadow: 0 0 5px #00ff00;
    }
    canvas { display: block; }
</style>
</head>
<body>
<div class="title">SITE HACKLENDI</div>
<div class="subtitle">Sistem güvenliği ihlal edildi</div>
<canvas id="cmatrix"></canvas>
<script>
const canvas = document.getElementById('cmatrix');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const cols = Math.floor(canvas.width / 20);
const ypos = Array(cols).fill(0);
function matrix() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#00ff00';
    ctx.font = '20px monospace';
    for (let i = 0; i < ypos.length; i++) {
        const text = String.fromCharCode(33 + Math.random() * 94);
        ctx.fillText(text, i * 20, ypos[i] * 20);
        if (ypos[i] * 20 > canvas.height && Math.random() > 0.975) ypos[i] = 0;
        else ypos[i]++;
    }
}
setInterval(matrix, 50);
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
</script>
</body>
</html>
"""

@app.route("/")
def hack():
    return Response(html, mimetype='text/html')

# Gunicorn için __main__ kısmı boş bırakabiliriz
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
