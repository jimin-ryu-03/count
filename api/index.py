{\rtf1\ansi\ansicpg949\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, jsonify\
import google.generativeai as genai\
\
app = Flask(__name__)\
\
# \uc0\u49324 \u50857 \u51088 \u45784 \u51032  API \u53412 \
genai.configure(api_key="AQ.Ab8RN6LoHmmwQ9PAgenfdG0WPgFEudNQ_iudDPK5FS6rz5CFwQ")\
\
@app.route("/api/sigh", methods=["GET"])\
def get_sigh_analysis():\
    try:\
        model = genai.GenerativeModel('models/gemini-3-flash-preview')\
        # \uc0\u54620 \u49704  \u52852 \u50868 \u53552 \u50857  \u46021 \u49444  \u49373 \u49457 \
        response = model.generate_content("\uc0\u54620 \u49704 \u51012  \u54393  \u45236 \u49772 \u45716  \u49324 \u46988 \u50640 \u44172  \u45912 \u51648 \u45716  \u50500 \u51452  \u51687 \u44256  \u44592 \u48516  \u45208 \u49244  \u52384 \u54617 \u51201  \u46021 \u49444  \u54620 \u47560 \u46356 \u47564  \u54644 \u51452 \u49464 \u50836 . \u54620 \u44397 \u50612 \u47196 .")\
        return jsonify(\{"message": response.text\})\
    except Exception as e:\
        return jsonify(\{"error": str(e)\}), 500\
\
# Vercel \uc0\u49892 \u54665 \u51012  \u50948 \u54644  \u54596 \u50836 \
def handler(event, context):\
    return app(event, context)}
