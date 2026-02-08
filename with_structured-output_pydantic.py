from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field


load_dotenv()

model = ChatOpenAI()

# schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summmary of review")
    sentiment:Literal['pos','neg'] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros:Optional[list[str]] = Field(description="Write down all the pros inside the list")
    cons:Optional[list[str]] = Field(description="Write down all the cons inside the list")
    
    

    
structured_model = model.with_structured_output(Review)

result =structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed app that I cannot remove. Also, the UI lookes outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)