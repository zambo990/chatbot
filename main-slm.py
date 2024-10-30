import ollama
import httpx


raw = httpx.get('https://www.investireoggi.it/wp-content/uploads/2024/08/contatore-acqua.jpg')
raw.raise_for_status()

prompt = '''
    You are an AI expert at extracting numerical values present within images. 
    In this case, you are provided with an image of a water meter displaying a numerical value. 
    Your sole task is to determine the numerical value shown on the meter and return it.
    You have to give me ONLY the number that is shown on the water meter, I don't want any other words.
    '''

response = ollama.generate(
    model='minicpm-v',
    prompt=prompt,
    images=[raw.content]
)

print(response)