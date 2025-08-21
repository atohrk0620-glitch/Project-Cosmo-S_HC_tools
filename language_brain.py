import os
import re
import random
import datetime
import nltk
from nltk.tokenize import word_tokenize
from joblib import Parallel, delayed, Memory
from tqdm import tqdm
from rich.console import Console

nltk.download('punkt')

console = Console()
BASE_DIR = "language_data"
OUT_DIR = os.path.join(BASE_DIR, "learned")
CACHE_DIR = os.path.join(BASE_DIR, "cache")
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)
memory = Memory(CACHE_DIR, verbose=0)

MAX_SIZE = 1024 * 1024
ENCODING = "utf-8"

@memory.cache
def tokenize(text):
    return word_tokenize(text)

def determine_difficulty(level):
    rules = {
        1: {"min_len": 5, "max_len": 8},
        2: {"min_len": 8, "max_len": 12},
        3: {"min_len": 12, "max_len": 20},
        4: {"min_len": 20, "max_len": 30},
        5: {"min_len": 30, "max_len": 50}
    }
    return rules.get(level, {"min_len": 50, "max_len": 80})

def classify_beat(score):
    if score >= 0.95:
        return "SS"
    elif score >= 0.85:
        return "S"
    elif score >= 0.7:
        return "A"
    elif score >= 0.5:
        return "B"
    else:
        return "C"

def generate_comment(text):
    if len(text) > 100:
        return "✨Expressive and rich!"
    elif "?" in text:
        return "🤔Thought-provoking."
    else:
        return "🌱Gentle and well-rounded."

def generate_random_text(level=1):
    word_pool = ["hope", "memory", "sky", "truth", "shadow", "light", "heart", "dream"]
    rules = determine_difficulty(level)
    length = random.randint(rules["min_len"], rules["max_len"])
    words = random.choices(word_pool, k=length)
    sentence = " ".join(words).capitalize() + "."

    paraphrase = "Paraphrase: Something about feelings and imagery."
    summary = "Summary: " + " ".join(sentence.split()[:5]) + "..."
    question = f"What is the central emotion in: {sentence}"
    answer = "Hope and uncertainty."
    sim = random.uniform(0.6, 0.99)
    beat = classify_beat(sim)
    comment = generate_comment(sentence)

    return {
        "original": sentence,
        "paraphrase": paraphrase,
        "summary": summary,
        "Q": question,
        "A": answer,
        "score": round(sim, 3),
        "BEAT": beat,
        "comment": comment
    }
