from flask import Flask, jsonify
import google.generativeai as genai

app = Flask(__name__)

# API 키 설정
genai.configure(api_key="AQ.Ab8RN6LoHmmwQ9PAgenfdG0WPgFEudNQ_iudDPK5FS6rz5CFwQ")

@app.route("/api/sigh", methods=["GET"])
def get_sigh_analysis():
    try:
        model = genai.GenerativeModel('models/gemini-3-flash-preview')
        # 한숨 카운터용 독설 생성
        response = model.generate_content("한숨을 푹 내쉬는 사람에게 던지는 아주 짧고 기분 나쁜 철학적 독설 한마디만 해주세요. 한국어로.")
        return jsonify({"message": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel 실행을 위해 필요
def handler(event, context):
    return app(event, context)
