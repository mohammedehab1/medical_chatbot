# Fine-Tuned Medical Model

This project uses a fine-tuned medical language model specialized for:

- Symptom understanding
- Medical question answering
- Doctor specialty recommendations
- Arabic medical conversations
- Voice-based medical assistance

The model was customized using prompt engineering and medical-focused conversational tuning to improve response quality and medical relevance.

---

# Fine-Tuning Goals

- Improve Arabic medical understanding
- Generate safer medical responses
- Reduce hallucinations
- Improve doctor specialty recommendations
- Better conversational medical support

---

#  Model Capabilities

- Arabic medical chat
- Voice medical assistant
- Symptom-based guidance
- Medical conversational AI
- AI voice response generation

---

# AI Stack

- Fine-Tuned Medical LLM
- LangChain
- Whisper ASR
- Edge-TTS
- FastAPI

---

# Project Structure

```text
medical_chatbot/
│
├── controller/
│   ├── __init__.py
│   ├── ASRController.py
│   ├── AudioPreprocessor.py
│   ├── ChatController.py
│   ├── LLMController.py
│   └── TTSController.py
│
├── data/
│   ├── .gitignore
│   └── .gitkeep
│
├── helpers/
│   ├── __init__.py
│   └── config.py
│
├── models/
│   ├── __init__.py
│   ├── asr_output.py
│   ├── llm_output.py
│   └── tts_output.py
│
├── notebooks/
│   └── finetuned_llm.ipynb
│
├── routes/
│   ├── __init__.py
│   ├── chat.py
│   └── check.py
│
├── stores/
│   ├── llm/
│   │   ├── chat_engine.py
│   │   ├── llm_service.py
│   │   ├── memory/
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   └── chat_memory.py
│   │   │
│   │   ├── templates/
│   │   │   ├── __pycache__/
│   │   │   ├── template_parser.py
│   │   │   └── prompts.py
│   │   │
│   │   └── locales/
│   │       ├── ar/
│   │       │   ├── __pycache__/
│   │       │   ├── __init__.py
│   │       │   └── prompts.py
│   │       │
│   │       └── en/
│   │           ├── __pycache__/
│   │           ├── __init__.py
│   │           └── prompts.py
│   │
│   ├── tts/
│   │   └── tts_service.py
│   │
│   └── whisper/
│       └── whisper_service.py
│
├── utils/
│   └── AudioRecorder.py
│
├── .env
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
├── LICENSE
├── README.md