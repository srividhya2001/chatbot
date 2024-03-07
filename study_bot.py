import openai
from langchain.chat_models import ChatOpenAI
import PyPDF2



key = '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'

def chat(prompt):
    chat = ChatOpenAI(
        openai_api_key = key,
        model_name="gpt-3.5-turbo",
        temperature=0.2
    )

    return chat.predict(prompt)


custom_prompt = f'''

question: who are the employees with salary more than 5000:
Answer: 
  Sql query :
  sample table: show some sample data of 3 rows
'''
print(chat(custom_prompt))
