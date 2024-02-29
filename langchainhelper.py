import os
os.environ['OPENAI_API_KEY']='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'
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
llm = OpenAI(temperature=0.6)

def generate_name(cuisine):
    llm = OpenAI(temperature=0.6)
    name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. suggest a fancy name for this."
    )
    name_chain = LLMChain(llm=llm, prompt=name, output_key="name")

    items = PromptTemplate(
        input_variables=['name'],
        template="suggest some menu items for {name}. Return it as comma seprated list."
    )
    food_items = LLMChain(llm=llm, prompt=items, output_key="Menu")

    chain = SequentialChain(chains=[name_chain, food_items],
                            input_variables=['cuisine'], output_variables=['name', 'Menu'])
    response=chain.invoke({'cuisine': cuisine})

    return response

if __name__ == "__main__":
    print(generate_name("Italian"))
