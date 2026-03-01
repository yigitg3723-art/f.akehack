from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Hack Paneli</title>
<style>
body { background:black; color:lime; font-family:monospace; text-align:center; }
button { padding:10px; font-size:18px; }
</style>
</head>
<body>
<h1>ULTRA HACK SISTEMI</h1>
<p id="text">Hazir...</p>
<button onclick="baslat()">Baslat</button>

<script>
function baslat(){
    let text = document.getElementById("text");
    let yuzde = 0;
    let interval = setInterval(function(){
        yuzde += 10;
        text.innerHTML = "Sistem hackleniyor... %" + yuzde;
        if(yuzde >= 100){
            clearInterval(interval);
            text.innerHTML = "😄 SAKA YAPTIM! TELEFON GUVENDE 😎";
        }
    }, 500);
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

app.run(host="0.0.0.0", port=5000)
