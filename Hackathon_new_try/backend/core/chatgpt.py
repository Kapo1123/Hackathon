from openai import OpenAI
import backend.config as config
client_id = config.SPOTIFY_CLIENT_ID
client_secret = config.SPOTIFY_CLIENT_SECRET
openAiClient = OpenAI(
    api_key = config.OPENAI_API_KEY,
    organization = config.OPENAI_ORGID
)
