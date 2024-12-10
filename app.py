from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configurar la clave de la API de OpenAI
openai.api_key = "TU_CLAVE_API_AQUÍ"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    user_prompt = request.json.get("prompt", "Escribe un artículo sobre tecnología.")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-o",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en redacción de contenido detallado y educativo."},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        generated_text = response['choices'][0]['message']['content']
        return jsonify({"generated_content": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
