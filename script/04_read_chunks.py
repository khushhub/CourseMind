import requests
import os
import json
import numpy as np
import time
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity

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


newjsons = os.listdir("newjsons")
my_dicts = []
chunk_id = 0

for json_file in newjsons:
    with open(f"newjsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating Embeddings for {json_file}")
    embeddings = create_embedding([c['text'] for c in content['chunks']])

    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)
        

df = pd.DataFrame.from_records(my_dicts)
#print(df)

#save this data frame
joblib.dump(df,'embeddings.joblib')

