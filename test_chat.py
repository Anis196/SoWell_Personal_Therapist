import google.generativeai as genai

# Authenticate with your API key
genai.configure(api_key=" )

# List all available models
models = genai.list_models()

for model in models:
    print("Model name:", model.name)
    print("Supported generation methods:", model.supported_generation_methods)
    print()
