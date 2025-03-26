# utils/file_handler.py

import os
import json

def load_data(filepath):
    if not os.path.exists(filepath):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        return {"expenses": [], "budget": {}}
    
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Warning: Could not decode JSON. Starting with empty data.")
        return {"expenses": [], "budget": {}}

def save_data(filepath, data):
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"❌ Error saving data: {e}")
