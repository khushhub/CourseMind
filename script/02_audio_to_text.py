import whisper
import json

model=whisper.load_model("large-v2")
result=model.transcribe(audio="audio/sample.mp3", language="hi", task="translate", word_timestamps=False)
#print(result["segments"])
chunks=[]
for segments in result["segments"]:
    chunks.append({"start":segments["start"],"end":segments["end"], "text":segments["text"]})

print (chunks)
with open ("output.json","w") as f:
    json.dump(chunks,f)