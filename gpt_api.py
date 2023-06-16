import openai
import os

os.environ["HTTP_PROXY"] = "http://127.0.0.1:64835"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:64835"

openai.api_key = 'YOU API KEYS'


def q2a(q):
	rsp = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "工程师"},
			{"role": "user", "content": q}
		]
	)

	return(rsp.get("choices")[0]["message"]["content"])
