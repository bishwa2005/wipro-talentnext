import re


def extract_text_from_html(html):
    raw_texts = re.findall(r">([^<]+)<", html)
    texts = [text.strip() for text in raw_texts if text.strip()]
    return texts


if __name__ == "__main__":
    html_example = """
    <html>
      <head><title>Your Title Here</title></head>
      <body>
        <h1>This is a Header</h1>
        <h2>This is a Medium Header</h2>
        <p>This is a new paragraph!</p>
        <p>This is a another paragraph!</p>
        <div>This is a new sentence without a paragraph break, in <b>bold</b> italics.</div>
      </body>
    </html>
    """

    print("Extracted text:")
    for text in extract_text_from_html(html_example):
        print('-', text)
