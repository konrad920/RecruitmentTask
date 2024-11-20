import openai

openai.api_key = "your_api_key"

def readFile(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def convertToHTML(text):
     response = openai.completions.create(
          model = "gpt-3.5-turbo-instruct",
          prompt = f"Przekształć ten tekst na HTML, ale bez znaczników <html>, <head>, <body>?
          Czy możesz zaproponować miejsca na wstawienie grafiki, oznacz je tagiem <img> i nadaj atrybut src=\"image_placeholder.jpg,
          pod każdym zdjęciem wstaw opis z odpowiednim tagiem dla HTML\":\n\n{text}",
          max_tokens = 1500,
          temperature = 0.7
     )
     return response.choices[0].text.strip()
     

def main():
    file_path = r"C:\Users\konra\OneDrive\Dokumenty\Python\RecruitmentTask\artykul.txt"
    text = readFile(file_path)

    convertedText = convertToHTML(text)

    with open('artykul.html', 'w', encoding='utf-8') as output_file:
            output_file.write(convertedText)

main()