# How to use this RAG AI Teaching assistant on your own data
## Step 1 - Collect your videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by ruunning video_to_mp3 (video_to_voice.py)

## Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by ruunning mp3_to_json(audio_to_text.py)

## Step 4 - Convert the json files to Vectors
Use the file preprocess_json to convert the json files to a dataframe with Embeddings and save it as a joblib pickle(text_to_chunks.py) (read_chunks.py)

## Step 5 - Prompt generation and feeding to LLM

Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM(process_chunks.py)


