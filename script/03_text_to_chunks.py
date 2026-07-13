import whisper
import json
import os

model=whisper.load_model("large-v2")
audios=os.listdir("audio")
for audio in audios:
    #print(audio)
    if("_" in audio):
        number=audio.split("_")[0]
        title=audio.split("_")[1][:-4]
        print(number, title)
        result=model.transcribe(audio="audio/{audio}",
        #result=model.transcribe(audio="audio/sample.mp3", 
        language="hi", task="translate", word_timestamps=False)

        chunks=[]
        for segments in result["segments"]:
            chunks.append({"number":number, "title":title,"start":segments["start"],"end":segments["end"], "text":segments["text"]})

        chunk_with_metadata={"chunks": chunks, "text": result["text"]}

        #print (chunks)
        with open (f"json/{audio}.json","w") as f:
            json.dump(chunk_with_metadata,f)