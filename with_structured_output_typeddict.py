from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

# schema
class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summmary of review" ]
    sentiment: Annotated[Literal["pos","neg"] ,"Return sentiment of the review either negative, positive or neutral"]
    pros:Annotated[Optional[list[str]], "Write down all the pros inside the list"]
    cons:Annotated[Optional[list[str]], "Write down all the cons inside the list"]

    
structured_model = model.with_structured_output(Review)

result =structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed app that I cannot remove. Also, the UI lookes outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)