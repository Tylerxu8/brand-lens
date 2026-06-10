from dotenv import load_dotenv
from anthropic import Anthropic


load_dotenv()
client = Anthropic()


message = client.messages.create(
	model="claude-haiku-4-5",
	max_tokens=300,
	messages=[
		{"role": "user", "content": "In one sentence, what is a brand's value proposition?"}
	],
)


print(message.content[0].text)