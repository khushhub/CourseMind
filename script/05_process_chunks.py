import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
#from read_chunks import create_embedding
import time
import numpy as np
import joblib
import requests
#from openai import OpenAI 
from google import genai
from coinfig import api_key


client = genai.Client(api_key=api_key)
#client=OpenAI(api_key=api_key)

def create_embedding(text_list, batch_size=16, retries=3, delay=3):
    all_embeddings = []
    
    for i in range(0, len(text_list), batch_size):
        batch = text_list[i:i + batch_size]
        
        for attempt in range(retries):
            r = requests.post("http://localhost:11434/api/embed", json={
                "model": "bge-m3",
                "input": batch
            })
            data = r.json()
            
            if "embeddings" in data:
                all_embeddings.extend(data["embeddings"])
                break
            else:
                print(f"Batch {i}-{i+len(batch)} attempt {attempt+1} failed: {data}")
                if attempt < retries - 1:
                    time.sleep(delay)
                else:
                    raise RuntimeError(f"Failed after {retries} attempts: {data}")
    
    return all_embeddings

def inference(prompt):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            #"model": "deepseek-r1",
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    response=r.json()
    print(response)
    return response

#openai
def inference_openai(prompt):
    response=client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return response.output_text

#gemini
def inference_genai(prompt):
    response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents=prompt
    )
    return response.text

df=joblib.load('embeddings.joblib')
incoming_query=input("Ask any question : ")
question_embedding=create_embedding([incoming_query])[0]
#print (question_embedding)

#find similarity
similarities=cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
# print(np.vstack(df['embedding'].values))
# print(np.vstack(df['embedding'].shape))
#print(similarities)

top_result=19
max_index=similarities.argsort()[::-1][0:top_result]
#print(max_index)
new_df=df.loc[max_index]
#print(new_df[["title","number","text"]])

# prompt=f'''
# I am teaching web development in my sigma web development course. here are video subtitle chunks containing video title , video number, start time in seconds, end time in seconds, the text at that time:
# {new_df[["title","number","start","end","text"]].to_json(orient="records")}
# ------------------------
# "{incoming_query}"
# User asked this question related to the veideo chunks, you have to answer in a human way(dont mention the above format , its just for you) where and how much content is taught in which video(in which video and at what timestamp) and guide the user to go to that particular video. if usre ask unrelated question, tell him taht you can olny answer question related to the course
# '''
prompt = f"""
You are an AI assistant for Sigma Web Development.

Use ONLY the provided transcript chunks.

If the answer is not contained in the context, say:
"I couldn't find that in the course."

For every answer include:

1. Video Number
2. Video Title
3. Timestamp
4. Short explanation

Context:
{new_df[["title","number","start","end","text"]].to_json(orient="records")}

Question:
{incoming_query}
"""

with open("prompt.txt","w") as f:
    f.write(prompt)

#for llama
# response=inference(prompt)["response"]
# print(response)

#for opean ai
#response=inference_openai(prompt)

#for genai
response=inference_genai(prompt)

with open("response.txt","w") as f:
    f.write(response)

print (response)

# for index, item in new_df.iterrows():
#     print (index,item["title"],item["number"],item["text"],item["start"], item["end"])