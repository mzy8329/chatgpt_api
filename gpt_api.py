import openai
import os

API_KEYS = 'YOU API KEYS'

os.environ["HTTP_PROXY"] = "http://127.0.0.1:64835"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:64835"

openai.api_key = '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'


def q2a(q):
	rsp = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "工程师"},
			{"role": "user", "content": q}
		]
	)

	return(rsp.get("choices")[0]["message"]["content"])
