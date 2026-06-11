def generate_summary(text):
    sentences = text.split(".")
    return ".".join(sentences[:3]) + "."
