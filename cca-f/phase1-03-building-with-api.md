<!-- markdownlint-disable -->

# Building with the Claude API

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api>  
**所要時間:** 約8.1時間  
**対象ドメイン:** D1, D4, D5  
**フェーズ:** Phase 1  

---

## カリキュラム

### レッスン 01: Welcome to the course

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287818>  

Open in Claude
0 seconds of 2 minutes, 14 secondsVolume 90%

---

### レッスン 02: Overview of Claude models

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287722>  

Open in Claude

---

### レッスン 03: Accessing the API

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287726>  

Open in Claude
0 seconds of 5 minutes, 18 secondsVolume 90%
00:00
05:18

When building applications with Claude, understanding the complete request lifecycle helps you make better architectural decisions and debug issues more effectively. Let's walk through what happens from the moment a user clicks "send" in your chat interface to when Claude's response appears on screen.

The Five-Step Request Flow

Every interaction with Claude follows a predictable pattern with five distinct phases: request to server, request to Anthropic API, model processing, response to server, and response to client.

Why You Need a Server

You should never make requests to the Anthropic API directly from client-side code. Here's why:

API requests require a secret API key for authentication
Exposing this key in client code creates a serious security vulnerability
Anyone could extract the key and make unauthorized requests

Instead, your web or mobile app sends requests to your own server, which then communicates with the Anthropic API using the securely stored key.

Making API Requests

When your server contacts the Anthropic API, you can use either an official SDK or make plain HTTP requests. Anthropic provides SDKs for Python, TypeScript, JavaScript, Go, and Ruby.

Every request must include these essential fields:

API Key - Identifies your request to Anthropic
Model - Name of the model to use (like "claude-3-sonnet")
Messages - List containing the user's input text
Max Tokens - Limit for how many tokens Claude can generate
Inside Claude's Processing

Once Anthropic receives your request, Claude processes it through four main stages: tokenization, embedding, contextualization, and generation.

Tokenization

Claude first breaks your input text into smaller chunks called tokens. These can be whole words, parts of words, spaces, or symbols. For simplicity, think of each word as one token.

Embedding

Each token gets converted into an embedding - a long list of numbers that represents all possible meanings of that word. Think of embeddings as numerical definitions that capture semantic relationships.

Words often have multiple meanings. For example, "quantum" could refer to:

A discrete unit of physical quantity (physics)
Quantum mechanics or quantum physics concepts
Something extremely small or subatomic
Quantum computing applications
Contextualization

Claude refines each embedding based on surrounding words to determine the most likely meaning in context. This process adjusts the numerical representations to highlight the appropriate definition.

Generation

The contextualized embeddings pass through an output layer that calculates probabilities for each possible next word. Claude doesn't always pick the highest probability word - it uses a mix of probability and controlled randomness to create natural, varied responses.

After selecting each word, Claude adds it to the sequence and repeats the entire process for the next word.

When Claude Stops Generating

After each token, Claude checks several conditions to decide whether to continue:

Max tokens reached - Has it hit the limit you specified?
Natural ending - Did it generate an end-of-sequence token?
Stop sequence - Did it encounter a predefined stop phrase?
The API Response

When generation completes, the API sends back a structured response containing:

Message - The generated text
Usage - Count of input and output tokens
Stop Reason - Why generation ended

Your server receives this response and forwards the generated text back to your client application, where it appears in the user interface.

Key Takeaways

Understanding this flow helps you:

Design secure architectures that protect your API keys
Set appropriate token limits for your use case
Handle different stop reasons in your application logic
Debug issues by understanding where they might occur in the pipeline

Don't worry about memorizing every detail - the goal is familiarizing yourself with the terminology and overall process you'll encounter when working with Claude's API.

---

### レッスン 04: Getting an API key

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/296766>  

Open in Claude

In the next video we will be making a request to the Anthropic API. To do so, you will need a secret API key. This guide will walk you through the process of creating an API key.

Step One: Navigate to the Anthropic API Console

In your browser, navigate to https://console.anthropic.com/ and log in to your Anthropic account. You'll then see a page like this:

Step Two: Click the 'Get API Keys' button

This button can be found towards the top right of the main dashboard page.

Step Three: Click the 'Create Key' button

At the top right of the page, find the 'Create Key' button and click it.

Step Four: Enter a workspace and name for your key

Create the key in workspace 'Default' and enter a name for your key. This name is used to help you identify the keys you generate. Let's use a name of 'Anthropic Course'.

Step Five: Copy the Key

Your API key will then be displayed in a pop up window. Copy this key and hold onto it - we will use it in the next video. This key will only be displayed once, so make sure you copy it!

If you accidentally close the window, delete the old key and generate it again.

---

### レッスン 05: Making a request

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287725>  

Open in Claude

Making your first request to the Anthropic API is straightforward once you understand the basic setup and structure. This guide walks through the essential steps to get Claude responding to your prompts using Python.

Setting Up Your Environment

Before making any API calls, you need to install the required packages and configure your API key securely.

First, install the necessary dependencies in your Jupyter notebook:

%pip install anthropic python-dotenv

Next, create a .env file in the same directory as your notebook to store your API key securely:

ANTHROPIC_API_KEY="your-api-key-here"

This approach keeps your API key out of your code and prevents accidentally committing it to version control. Always add .env to your .gitignore file.

Load the environment variables and create your API client:

from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"
The Create Function

The core of making API requests is the client.messages.create() function. This function requires three key parameters:

model - The name of the Claude model you want to use
max_tokens - A safety limit on response length (not a target)
messages - The conversation history you're sending to Claude

The max_tokens parameter acts as a safety mechanism. If you set it to 1000, Claude will stop generating after 1000 tokens even if it has more to say. Claude doesn't try to reach this limit - it just writes what it thinks is appropriate and stops if it hits the maximum.

Understanding Messages

Messages represent the conversation between you and Claude, similar to a chat application. There are two types of messages:

User messages - Content you want to send to Claude (written by humans)
Assistant messages - Responses that Claude has generated

Each message is a dictionary with a role (either "user" or "assistant") and content (the actual text).

Making Your First Request

Here's a complete example of making a request to Claude:

message = client.messages.create(
model=model,
max_tokens=1000,
messages=[
{
"role": "user",
"content": "What is quantum computing? Answer in one sentence"
}
]
)

When you run this code, Claude will process your request and return a response object containing the generated text along with metadata about the request.

Extracting the Response

The response object contains a lot of information, but you usually just want the generated text. Access it using:

message.content[0].text

This gives you clean, readable output like: "Quantum computing is a type of computation that leverages quantum mechanics principles like superposition and entanglement to process information using quantum bits (qubits), potentially solving certain complex problems exponentially faster than classical computers."

With these basics in place, you can start experimenting with different prompts and building more complex interactions with Claude.

---

### レッスン 06: Multi-Turn conversations

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287735>  

Open in Claude

When working with the Anthropic API and Claude, there's a crucial concept you need to understand: Claude doesn't store any of your conversation history. Each request you make is completely independent, with no memory of previous exchanges.

This means if you want to have a multi-turn conversation where Claude remembers context from earlier messages, you need to handle the conversation state yourself.

The Problem with Stateless Conversations

Let's say you ask Claude "What is quantum computing?" and get a good response. Then you follow up with "Write another sentence" - Claude has no idea what you're referring to. It will write a sentence about something completely random because it has no memory of the quantum computing discussion.

How Multi-Turn Conversations Work

To maintain conversation context, you need to do two things:

Manually maintain a list of all messages in your code
Send the complete message history with every request

Here's the flow that actually works:

Send your initial user message to Claude
Take Claude's response and add it to your message list as an assistant message
Add your follow-up question as another user message
Send the entire conversation history to Claude
Building Helper Functions

To make conversation management easier, you can create three helper functions:

def add_user_message(messages, text):
user_message = {"role": "user", "content": text}
messages.append(user_message)

def add_assistant_message(messages, text):
assistant_message = {"role": "assistant", "content": text}
messages.append(assistant_message)

def chat(messages):
message = client.messages.create(
model=model,
max_tokens=1000,
messages=messages,
)
return message.content[0].text
Putting It All Together

Here's how you use these functions to maintain a conversation:

# Start with an empty message list

messages = []

# Add the initial user question

add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response

answer = chat(messages)

# Add Claude's response to the conversation history

add_assistant_message(messages, answer)

# Add a follow-up question

add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context

final_answer = chat(messages)

Now Claude will understand that "Write another sentence" refers to expanding on the quantum computing definition, because you've provided the complete conversation context.

These helper functions will be useful throughout your work with Claude, making it much easier to build applications that can maintain meaningful conversations over multiple exchanges.

---

### レッスン 07: Chat exercise

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287727>  

Open in Claude

---

### レッスン 08: System prompts

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287733>  

Open in Claude
0 seconds of 6 minutes, 20 secondsVolume 90%

System prompts are a powerful way to customize how Claude responds to user input. Instead of getting generic answers, you can shape Claude's tone, style, and approach to match your specific use case.

Why System Prompts Matter

Consider building a math tutor chatbot. When a student asks "How do I solve 5x + 2 = 3 for x?", you want Claude to act like a real tutor, not just spit out the answer. A good math tutor should:

Initially give hints rather than complete solutions
Patiently walk students through problems step by step
Show solutions for similar problems as examples

You definitely don't want Claude to:

Immediately give direct answers
Tell students to just use a calculator
How System Prompts Work

System prompts provide Claude with guidance on how to respond. You define them as plain strings and pass them into the create function call. The key benefits are:

System prompts provide Claude guidance on how to respond
Claude will try to respond in the same way someone in the specified role would respond
Helps keep Claude on task

Here's the basic structure:

system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

client.messages.create(
model=model,
messages=messages,
max_tokens=1000,
system=system_prompt
)
Seeing the Difference

Without a system prompt, Claude gives a complete step-by-step solution immediately. This might be helpful, but it doesn't encourage the student to think through the problem themselves.

With the math tutor system prompt, Claude's response changes dramatically. Instead of providing the full solution, Claude asks guiding questions like "What do you think would be a good first step to isolate x? Consider what operation we might need to perform on both sides to start moving terms around."

Building a Flexible Chat Function

Rather than hard-coding system prompts, you can make your chat function more reusable by accepting system prompts as parameters:

def chat(messages, system=None):
params = {
"model": model,
"max_tokens": 1000,
"messages": messages,
}

if system:
params["system"] = system

message = client.messages.create(**params)
return message.content[0].text

This approach handles an important detail: Claude's API doesn't accept system=None, so you need to conditionally include the system parameter only when it's provided.

Now you can call your chat function with or without a system prompt:

# Without system prompt

answer = chat(messages)

# With system prompt

system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""
answer = chat(messages, system=system)

System prompts are essential for creating AI applications that behave consistently and appropriately for their intended purpose. They transform generic AI responses into specialized, role-appropriate interactions.

---

### レッスン 09: System prompts exercise

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287724>  

Open in Claude

---

### レッスン 10: Temperature

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287728>  

Open in Claude
0 seconds of 6 minutes, 7 secondsVolume 90%

Temperature is a powerful parameter that controls how predictable or creative Claude's responses will be. Understanding how to use it effectively can dramatically improve your AI applications.

How Claude Generates Text

Before diving into temperature, it helps to understand Claude's text generation process. When you send Claude a prompt like "What do you think?", it goes through three key steps:

Tokenization - Breaking your input into smaller chunks
Prediction - Calculating probabilities for possible next words
Sampling - Choosing a token based on those probabilities

In this example, Claude might assign a 30% probability to "about", 20% to "would", 10% to "of", and so on. The model then selects one token and repeats this entire process to build complete sentences.

What Temperature Does

Temperature is a decimal value between 0 and 1 that directly influences these selection probabilities. It's like adjusting the "creativity dial" on Claude's responses.

At low temperatures (near 0), Claude becomes very deterministic - it almost always picks the highest probability token. At high temperatures (near 1), Claude distributes probability more evenly across options, leading to more varied and creative outputs.

Interactive Temperature Demo

You can see temperature in action with Claude's interactive demo. Watch how the probability distribution changes as you adjust the temperature slider:

At temperature 0.0, "about" gets 100% probability - completely deterministic. At temperature 1.0, probabilities spread more evenly across all possible tokens, introducing randomness and creativity.

Choosing the Right Temperature

Different tasks call for different temperature ranges:

Low Temperature (0.0 - 0.3)
Factual responses
Coding assistance
Data extraction
Content moderation
Medium Temperature (0.4 - 0.7)
Summarization
Educational content
Problem-solving
Creative writing with constraints
High Temperature (0.8 - 1.0)
Brainstorming
Creative writing
Marketing content
Joke generation
Implementing Temperature in Code

Adding temperature support to your chat function is straightforward. Here's how to modify your existing function:

def chat(messages, system=None, temperature=1.0):
params = {
"model": model,
"max_tokens": 1000,
"messages": messages,
"temperature": temperature
}

if system:
params["system"] = system

message = client.messages.create(**params)
return message.content[0].text

The key changes are adding temperature=1.0 as a parameter and including "temperature": temperature in the params dictionary.

Testing Temperature Effects

To see temperature in action, try generating movie ideas with different settings:

# Low temperature - more predictable

answer = chat(messages, temperature=0.0)

# High temperature - more creative

answer = chat(messages, temperature=1.0)

At temperature 0.0, you might consistently get responses like "A time-traveling archaeologist must prevent ancient artifacts from being stolen." At temperature 1.0, you'll see much more variety in themes, characters, and plot elements.

Key Takeaways

Remember that temperature doesn't guarantee different outputs - it just changes the probability of getting them. Even at high temperatures, Claude might occasionally produce similar responses. The key is matching your temperature choice to your specific use case:

Need consistent, factual responses? Use low temperature
Want creative brainstorming? Dial up the temperature
Somewhere in between? Medium temperatures work well for most general tasks

Temperature is one of the most practical parameters you can adjust to fine-tune Claude's behavior for your specific needs.

---

### レッスン 11: Course satisfaction survey

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/297284>  

Open in Claude
Loading...

---

### レッスン 12: Response streaming

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287734>  

Open in Claude

When building chat applications with Claude, there's a significant user experience challenge: responses can take 10-30 seconds to generate, leaving users staring at a loading spinner. The solution is response streaming, which lets users see text appear chunk by chunk as Claude generates it, creating a much more responsive feel.

The Problem with Standard Responses

In a typical chat setup, your server sends a user message to Claude and waits for the complete response before sending anything back to the client. This creates an awkward delay where users have no feedback that anything is happening.

How Streaming Works

With streaming enabled, Claude immediately sends back an initial response indicating it has received your request and is starting to generate text. Then you receive a series of events, each containing a small piece of the overall response.

Your server can forward these text chunks to your client application as they arrive, allowing users to see the response building up word by word. All of these events are part of a single request to Claude.

Understanding Stream Events

When you enable streaming, Claude sends back several types of events:

MessageStart - A new message is being sent
ContentBlockStart - Start of a new block containing text, tool use, or other content
ContentBlockDelta - Chunks of the actual generated text
ContentBlockStop - The current content block has been completed
MessageDelta - The current message is complete
MessageStop - End of information about the current message

The ContentBlockDelta events contain the actual generated text that you'll want to display to users.

Basic Streaming Implementation

To enable streaming, add stream=True to your messages.create call:

messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

stream = client.messages.create(
model=model,
max_tokens=1000,
messages=messages,
stream=True
)

for event in stream:
print(event)
Simplified Text Streaming

Rather than manually parsing events, you can use the SDK's simplified streaming interface that extracts just the text content:

with client.messages.stream(
model=model,
max_tokens=1000,
messages=messages
) as stream:
for text in stream.text_stream:
print(text, end="")

This approach automatically filters out everything except the actual text content, which is usually what you need for displaying responses to users.

Getting the Complete Message

While streaming individual chunks is great for user experience, you often need the complete message for storage or further processing. After streaming completes, you can get the assembled final message:

with client.messages.stream(
model=model,
max_tokens=1000,
messages=messages
) as stream:
for text in stream.text_stream:

# Send each chunk to your client

pass

# Get the complete message for database storage

final_message = stream.get_final_message()

This gives you the best of both worlds: real-time streaming for users and a complete message object for your application logic.

---

### レッスン 13: Structured data

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287732>  

Open in Claude
0 seconds of 5 minutes, 59 secondsVolume 90%

When you need Claude to generate structured data like JSON, Python code, or bulleted lists, you'll often run into a common problem: Claude wants to be helpful and add explanatory text around your content. While this is usually great, sometimes you need just the raw data with nothing else.

Consider building a web app that generates AWS EventBridge rules. Users enter a description, click generate, and expect to see clean JSON they can immediately copy and use. If Claude returns the JSON wrapped in markdown code blocks with explanatory text, users can't simply copy the entire response - they have to manually select just the JSON portion.

The Problem with Default Responses

By default, when you ask Claude to generate JSON, you might get something like this:

```json
{
"source": ["aws.ec2"],
"detail-type": ["EC2 Instance State-change Notification"],
"detail": {
"state": ["running"]
}
}
```

This rule captures EC2 instance state changes when instances start running.

The JSON is correct, but it's wrapped in markdown formatting and includes explanatory text. For a web app where users need to copy the raw JSON, this creates friction in the user experience.

The Solution: Assistant Message Prefilling + Stop Sequences

You can combine assistant message prefilling with stop sequences to get exactly the content you want. Here's how it works:

messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])

This technique works by:

The user message tells Claude what to generate
The prefilled assistant message makes Claude think it already started a markdown code block
Claude continues by writing just the JSON content
When Claude tries to close the code block with ```, the stop sequence immediately ends generation

The result is clean JSON with no extra formatting:

{
"source": ["aws.ec2"],
"detail-type": ["EC2 Instance State-change Notification"],
"detail": {
"state": ["running"]
}
}
Processing the Response

You might notice some extra newline characters in the response. These are easy to handle:

import json

# Clean up and parse the JSON

clean_json = json.loads(text.strip())
Beyond JSON

This technique isn't limited to JSON generation. Use it anytime you need structured data without commentary:

Python code snippets
Bulleted lists
CSV data
Any formatted content where you want just the content, not explanations

The key is identifying what Claude naturally wants to wrap your content in, then using that as your prefill and stop sequence. For code, it's usually markdown code blocks. For lists, it might be different formatting markers.

This approach gives you precise control over Claude's output format, making it much easier to integrate AI-generated content into applications where clean, structured data is essential.

---

### レッスン 14: Structured data exercise

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287729>  

Open in Claude

---

### レッスン 15: Quiz on accessing Claude with the API

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289117>  

Open in Claude
Loading...

---

### レッスン 16: Prompt evaluation

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287731>  

Open in Claude

When working with Claude, writing a good prompt is just the beginning. To build reliable AI applications, you need to understand two critical concepts: prompt engineering and prompt evaluation. Prompt engineering gives you techniques for writing better prompts, while prompt evaluation helps you measure how well those prompts actually work.

Prompt Engineering vs Prompt Evaluation

Prompt engineering is your toolkit for crafting effective prompts. It includes techniques like:

Multishot prompting
Structuring with XML tags
Many other best practices

These techniques help Claude understand exactly what you're asking for and how you want it to respond.

Prompt evaluation takes a different approach. Instead of focusing on how to write prompts, it's about measuring their effectiveness through automated testing. You can:

Test against expected answers
Compare different versions of the same prompt
Review outputs for errors
Three Paths After Writing a Prompt

Once you've drafted a prompt, you typically face three options for what to do next:

Option 1: Test the prompt once and decide it's good enough. This carries a significant risk of breaking in production when users provide unexpected inputs.

Option 2: Test the prompt a few times and tweak it to handle a corner case or two. While better than option 1, users will often provide very unexpected outputs that you haven't considered.

Option 3: Run the prompt through an evaluation pipeline to score it, then iterate on the prompt based on objective metrics. This approach requires more work and cost, but gives you much more confidence in your prompt's reliability.

Why Most Engineers Fall Into Testing Traps

Options 1 and 2 are common traps that all engineers fall into, myself included. It's natural to write a prompt for a serious application and not test it thoroughly enough. We tend to underestimate how many edge cases real users will encounter.

The reality is that when you deploy a prompt to production, users will interact with it in ways you never anticipated. What seemed like a solid prompt during your limited testing can quickly break down when faced with the full variety of real-world inputs.

The Evaluation-First Approach

Option 3 represents a more systematic approach to prompt development. By running your prompt through an evaluation pipeline, you get objective metrics about its performance across a broader range of test cases. This data-driven approach lets you:

Identify weaknesses before they become production issues
Compare different prompt versions objectively
Iterate with confidence based on measurable improvements
Build more reliable AI applications

While this approach requires more upfront investment in time and testing infrastructure, it pays dividends in the reliability and robustness of your final application. The goal is to catch problems during development rather than after your users encounter them.

---

### レッスン 17: A typical eval workflow

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287736>  

Open in Claude

A typical prompt evaluation workflow follows five key steps that help you systematically improve your prompts through objective measurement. While there are many different ways to assemble these workflows and various open source and paid tools available, understanding the core process helps you start small and scale up as needed.

Step 1: Draft a Prompt

Start by writing an initial prompt that you want to improve. For this example, we'll use a simple prompt:

prompt = f"""
Please answer the user's question:

{question}
"""

This basic prompt will serve as our baseline for testing and improvement.

Step 2: Create an Eval Dataset

Your evaluation dataset contains sample inputs that represent the types of questions or requests your prompt will handle in production. The dataset should include questions that will be interpolated into your prompt template.

For this example, our dataset includes three questions:

"What's 2+2?"
"How do I make oatmeal?"
"How far away is the Moon?"

In real-world evaluations, you might have tens, hundreds, or even thousands of records. You can assemble these datasets by hand or use Claude to generate them for you.

Step 3: Feed Through Claude

Take each question from your dataset and merge it with your prompt template to create complete prompts. Then send each one to Claude to get responses.

For example, the first question becomes:

Please answer the user's question:
What's 2+2?

Claude might respond with "2 + 2 = 4" for the math question, provide oatmeal cooking instructions for the second question, and give the distance to the Moon for the third.

Step 4: Feed Through a Grader

The grader evaluates the quality of Claude's responses by examining both the original question and Claude's answer. This step provides objective scoring, typically on a scale from 1 to 10, where 10 represents a perfect answer and lower scores indicate room for improvement.

In our example, the grader might assign:

Math question: 10 (perfect answer)
Oatmeal question: 4 (needs improvement)
Moon question: 9 (very good answer)

The average score across all questions gives you an objective measurement: (10 + 4 + 9) ÷ 3 = 7.66

Step 5: Change Prompt and Repeat

Now that you have a baseline score, you can modify your prompt and run the entire process again to see if your changes improve performance.

For example, you might add more guidance to your prompt:

prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""

After running this improved prompt through the same evaluation process, you might get a higher average score of 8.7, indicating that the additional instruction helped Claude provide better responses.

Prompt Scoring

The key benefit of this workflow is getting objective measurements of prompt performance. You can:

Compare different prompt versions numerically
Use the version with the best score
Continue iterating to find even better approaches

This systematic approach removes guesswork from prompt engineering and gives you confidence that your changes are actually improvements rather than just different variations.

---

### レッスン 18: Generating test datasets

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287739>  

Open in Claude

Building a custom prompt evaluation workflow starts with creating a solid prompt and then generating test data to see how well it performs. Let's walk through setting up an evaluation system for a prompt that helps users write AWS-specific code.

Setting Up the Goal

Our prompt needs to assist users in writing three specific types of output for AWS use cases:

Python code
JSON configuration files
Regular expressions

The key requirement is that when a user requests help with a task, we return clean output in one of these formats without any extra explanations, headers, or footers.

Here's our starting prompt (version 1):

prompt = f"""
Please provide a solution to the following task:
{task}
"""
Creating an Evaluation Dataset

An evaluation dataset contains inputs that we'll feed into our prompt. For each combination of prompt and input, we'll run the prompt and analyze the results.

Our dataset will be an array of JSON objects, where each object contains a "task" property describing what we want Claude to accomplish. We can either create this dataset by hand or generate it automatically using Claude.

Since we're generating test data, this is a perfect opportunity to use a faster model like Haiku instead of the full Claude model.

Generating Test Data with Code

Let's create a function that automatically generates our test dataset. First, we'll need our helper functions for working with Claude:

def add_user_message(messages, text):
user_message = {"role": "user", "content": text}
messages.append(user_message)

def add_assistant_message(messages, text):
assistant_message = {"role": "assistant", "content": text}
messages.append(assistant_message)

def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
params = {
"model": model,
"max_tokens": 1000,
"messages": messages,
"temperature": temperature
}
if system:
params["system"] = system
if stop_sequences:
params["stop_sequences"] = stop_sequences

response = client.messages.create(**params)
return response.content[0].text

Now we'll create our dataset generation function:

def generate_dataset():
prompt = """
Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects, each representing task that requires Python, JSON, or a Regex to complete.

Example output:

```json
[
{
"task": "Description of task",
},
...additional
]
```

- Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
- Focus on tasks that do not require writing much code

Please generate 3 objects.
"""

To properly parse the JSON response, we'll use prefilling and stop sequences:

messages = []
add_user_message(messages, prompt)
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])
return json.loads(text)
Testing the Dataset Generation

Let's run our function and see what kind of test cases we get:

dataset = generate_dataset()
print(dataset)

This should return three different test cases covering our target outputs - Python functions, JSON configurations, and regular expressions for AWS-specific tasks.

Saving the Dataset

Once we have our dataset, we'll save it to a file so we can easily load it later during evaluation:

with open('dataset.json', 'w') as f:
json.dump(dataset, f, indent=2)

This creates a dataset.json file in the same directory as your notebook, containing your list of tasks ready for prompt evaluation.

With this foundation in place, you now have a systematic way to generate test data for evaluating how well your prompts perform across different types of AWS-related coding tasks.

Downloads
001_prompt_evals.ipynb
(opens in new tab)

---

### レッスン 19: Running the eval

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287743>  

Open in Claude

Now that we have our evaluation dataset ready, it's time to build the core evaluation pipeline. This involves taking each test case, merging it with our prompt, feeding it to Claude, and then grading the results.

The evaluation process follows a clear workflow: we take our dataset of test cases, combine each one with our prompt template, send it to Claude for processing, and then evaluate the output using a grader system.

Building the Core Functions

The evaluation pipeline consists of three main functions, each with a specific responsibility. Let's start with the simplest one - the function that handles individual prompts.

The run_prompt Function

This function takes a test case and merges it with our prompt template:

def run_prompt(test_case):
"""Merges the prompt and test case input, then returns the result"""
prompt = f"""
Please solve the following task:

{test_case["task"]}
"""

messages = []
add_user_message(messages, prompt)
output = chat(messages)
return output

Right now, we're keeping the prompt extremely simple. We're not including any formatting instructions, so Claude will likely return more verbose output than we need. We'll refine this later as we iterate on our prompt design.

The run_test_case Function

This function orchestrates running a single test case and grading the result:

def run_test_case(test_case):
"""Calls run_prompt, then grades the result"""
output = run_prompt(test_case)

# TODO - Grading

score = 10

return {
"output": output,
"test_case": test_case,
"score": score
}

For now, we're using a hardcoded score of 10. The grading logic is where we'll spend significant time in upcoming sections, but this placeholder lets us test the overall pipeline.

The run_eval Function

This function coordinates the entire evaluation process:

def run_eval(dataset):
"""Loads the dataset and calls run_test_case with each case"""
results = []

for test_case in dataset:
result = run_test_case(test_case)
results.append(result)

return results

This function processes every test case in our dataset and collects all the results into a single list.

Running the Evaluation

To execute our evaluation pipeline, we load our dataset and run it through our functions:

with open("dataset.json", "r") as f:
dataset = json.load(f)

results = run_eval(dataset)

The first time you run this, expect it to take some time - even with Claude Haiku, it can take around 30 seconds to process a full dataset. We'll cover optimization techniques later.

Examining the Results

The evaluation returns a structured JSON array where each object represents one test case result:

print(json.dumps(results, indent=2))

Each result contains three key pieces of information:

output: The complete response from Claude
test_case: The original test case that was processed
score: The evaluation score (currently hardcoded)

As you can see in the output, Claude generates quite verbose responses since we haven't provided specific formatting instructions yet. This is exactly the kind of issue we'll address as we refine our prompts.

What We've Accomplished

At this point, we've successfully built the core evaluation pipeline. We can take our dataset, process it through Claude, and collect structured results. The major missing piece is the grading system - that hardcoded score of 10 needs to be replaced with actual evaluation logic.

This pipeline represents the foundation of most AI evaluation systems. While it may seem simple, you've just built the majority of what an eval pipeline actually does. The complexity comes in the details - better prompts, sophisticated grading, and performance optimizations.

Next, we'll dive into the critical topic of graders, which will transform our hardcoded scores into meaningful evaluations of Claude's performance.

---

### レッスン 20: Model based grading

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287742>  

Open in Claude

When building prompt evaluation workflows, grading systems provide objective signals about output quality. A grader takes model output and returns some kind of measurable feedback - typically a number between 1 and 10, where 10 represents high quality and 1 represents poor quality.

Types of Graders

There are three main approaches to grading model outputs:

Code graders - Programmatically evaluate outputs using custom logic
Model graders - Use another AI model to assess the quality
Human graders - Have people manually review and score outputs
Code Graders

Code graders let you implement any programmatic check you can imagine. Common uses include:

Checking output length
Verifying output does/doesn't have certain words
Syntax validation for JSON, Python, or regex
Readability scores

The only requirement is that your code returns some usable signal - usually a number between 1 and 10.

Model Graders

Model graders feed your original output into another API call for evaluation. This approach offers tremendous flexibility for assessing:

Response quality
Quality of instruction following
Completeness
Helpfulness
Safety
Human Graders

Human graders provide the most flexibility but are time-consuming and tedious. They're useful for evaluating:

General response quality
Comprehensiveness
Depth
Conciseness
Relevance
Defining Evaluation Criteria

Before implementing any grader, you need clear evaluation criteria. For a code generation prompt, you might focus on:

Format - Should return only Python, JSON, or Regex without explanation
Valid Syntax - Produced code should have valid syntax
Task Following - Response should directly address the user's task with accurate code

The first two criteria work well with code graders, while task following is better suited for model graders due to their flexibility.

Implementing a Model Grader

Here's how to build a model grader function:

def grade_by_model(test_case, output):

# Create evaluation prompt

eval_prompt = """
You are an expert code reviewer. Evaluate this AI-generated solution.

Task: {task}
Solution: {solution}

Provide your evaluation as a structured JSON object with:

- "strengths": An array of 1-3 key strengths
- "weaknesses": An array of 1-3 key areas for improvement
- "reasoning": A concise explanation of your assessment
- "score": A number between 1-10
"""

messages = []
add_user_message(messages, eval_prompt)
add_assistant_message(messages, "```json")

eval_text = chat(messages, stop_sequences=["```"])
return json.loads(eval_text)

The key insight is asking for strengths, weaknesses, and reasoning alongside the score. Without this context, models tend to default to middling scores around 6.

Integrating Grading into Your Workflow

Update your test case runner to call the grader:

def run_test_case(test_case):
output = run_prompt(test_case)

# Grade the output

model_grade = grade_by_model(test_case, output)
score = model_grade["score"]
reasoning = model_grade["reasoning"]

return {
"output": output,
"test_case": test_case,
"score": score,
"reasoning": reasoning
}

Finally, calculate an average score across all test cases:

from statistics import mean

def run_eval(dataset):
results = []

for test_case in dataset:
result = run_test_case(test_case)
results.append(result)

average_score = mean([result["score"] for result in results])
print(f"Average score: {average_score}")

return results

This gives you an objective metric to track as you iterate on your prompt. While model graders can be somewhat capricious, they provide a consistent baseline for measuring improvements.

Downloads
001_prompt_evals_grader.ipynb
(opens in new tab)

---

### レッスン 21: Code based grading

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287737>  

Open in Claude

When evaluating AI models that generate code, you need more than just checking if the response makes sense. You also need to verify that the generated code actually has valid syntax and follows the correct format. This is where code-based grading comes in.

How Code Grading Works

Code grading validates two key aspects of AI-generated responses:

Format - The response should return only the requested code type (Python, JSON, or Regex) without explanations
Valid Syntax - The generated code should actually parse correctly as the intended language
Task Following - The response should directly address what was asked and be accurate

The first two criteria are handled by the code grader, while task following is evaluated by the model grader. Together, they provide a comprehensive evaluation.

Syntax Validation Functions

To check if generated code has valid syntax, you can create three helper functions that attempt to parse the output:

def validate_json(text):
try:
json.loads(text.strip())
return 10
except json.JSONDecodeError:
return 0

def validate_python(text):
try:
ast.parse(text.strip())
return 10
except SyntaxError:
return 0

def validate_regex(text):
try:
re.compile(text.strip())
return 10
except re.error:
return 0

Each function tries to parse the text as its respective format. If parsing succeeds, it returns a perfect score of 10. If it fails with an error, the syntax is invalid and returns 0.

Dataset Format Requirements

For the code grader to know which validator to use, your test cases need to specify the expected output format:

{
"task": "Create a Python function to validate an AWS IAM username",
"format": "python"
}

You can update your dataset generation prompt to automatically include this format field by adding it to the example output structure.

Improving Prompt Clarity

To get better results from your AI model, make your prompt instructions more specific about the expected output format:

- Respond only with Python, JSON, or a plain Regex
- Do not add any comments or commentary or explanation

You can also use a pre-filled assistant message with code blocks to encourage the model to return just the raw code:

add_assistant_message(messages, "```code")

This tells Claude to start generating code content without having to specify whether it's Python, JSON, or Regex ahead of time.

Combining Scores

The final step is merging the model grader score with the code grader score. A simple approach is to take the average:

model_grade = grade_by_model(test_case, output)
model_score = model_grade["score"]
syntax_score = grade_syntax(output, test_case)

score = (model_score + syntax_score) / 2

This gives equal weight to both content quality and technical correctness. You might adjust these weights based on what matters more for your specific use case.

Testing Your Implementation

Once you've implemented code grading, run your evaluation to get a baseline score. The score itself isn't inherently good or bad - what matters is whether you can improve it by refining your prompts. This gives you a quantitative way to measure prompt engineering progress rather than relying on subjective assessment.

Downloads
001_prompt_evals_fns.ipynb
(opens in new tab)

---

### レッスン 22: Exercise on prompt evals

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287738>  

Open in Claude
Downloads
001_prompt_evals_complete.ipynb
(opens in new tab)

---

### レッスン 23: Quiz on prompt evaluation

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289118>  

Open in Claude
Loading...

---

### レッスン 24: Prompt engineering

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287745>  

Open in Claude

Prompt engineering is about taking a prompt you've written and improving it to get more reliable, higher-quality outputs. This process involves iterative refinement - starting with a basic prompt, evaluating its performance, then systematically applying engineering techniques to improve it.

The Iterative Improvement Process

The approach follows a clear cycle that you can repeat until you achieve your desired results:

Set a goal - Define what you want your prompt to accomplish
Write an initial prompt - Create a basic first attempt
Evaluate the prompt - Test it against your criteria
Apply prompt engineering techniques - Use specific methods to improve performance
Re-evaluate - Verify that your changes actually improved the results

You repeat the last two steps until you're satisfied with the performance. Each iteration should show measurable improvement in your evaluation scores.

Setting Up Your Evaluation Pipeline

To demonstrate this process, we'll work with a practical example: creating a prompt that generates one-day meal plans for athletes. The prompt needs to take into account an athlete's height, weight, goals, and dietary restrictions, then produce a comprehensive meal plan.

The evaluation setup uses a PromptEvaluator class that handles dataset generation and model grading. When creating your evaluator instance, you can control concurrency with the max_concurrent_tasks parameter:

evaluator = PromptEvaluator(max_concurrent_tasks=5)

Start with a low concurrency value (like 3) to avoid rate limit errors. You can increase it if your API quota allows for faster processing.

Generating Test Data

The evaluation system can automatically generate test cases based on your prompt requirements. You define what inputs your prompt needs:

dataset = evaluator.generate_dataset(
task_description="Write a compact, concise 1 day meal plan for a single athlete",
prompt_inputs_spec={
"height": "Athlete's height in cm",
"weight": "Athlete's weight in kg",
"goal": "Goal of the athlete",
"restrictions": "Dietary restrictions of the athlete"
},
output_file="dataset.json",
num_cases=3
)

Keep the number of test cases low (2-3) during development to speed up your iteration cycle. You can increase this for final validation.

Writing Your Initial Prompt

Start with a simple, naive prompt to establish a baseline. Here's an example of a deliberately basic first attempt:

def run_prompt(prompt_inputs):
prompt = f"""
What should this person eat?

- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}
"""

messages = []
add_user_message(messages, prompt)
return chat(messages)

This basic prompt will likely produce poor results, but it gives you a starting point to measure improvement against.

Adding Evaluation Criteria

When running your evaluation, you can specify additional criteria that the grading model should consider:

results = evaluator.run_evaluation(
run_prompt_function=run_prompt,
dataset_file="dataset.json",
extra_criteria="""
The output should include:

- Daily caloric total
- Macronutrient breakdown
- Meals with exact foods, portions, and timing
"""
)

This helps ensure your prompt is evaluated against the specific requirements that matter for your use case.

Analyzing Results

After running an evaluation, you'll get both a numerical score and a detailed HTML report. The report shows you exactly how each test case performed, including the model's reasoning for each score.

Don't be discouraged by low initial scores - a score of 2.3 out of 10 is typical for a first attempt. The goal is to see consistent improvement as you apply engineering techniques.

The detailed evaluation report helps you understand exactly where your prompt is failing and what improvements are needed. Use this feedback to guide your next iteration.

Next Steps

With your baseline established, you're ready to start applying specific prompt engineering techniques. Each technique you learn should result in measurable improvement in your evaluation scores, gradually transforming your basic prompt into a reliable, high-performing tool.

Remember that prompt engineering is an iterative process. The key is to make one change at a time, evaluate the impact, and build on what works. This systematic approach ensures you understand which techniques provide the most value for your specific use case.

Downloads
001_prompting.ipynb
(opens in new tab)
002_prompting_completed.ipynb
(opens in new tab)

---

### レッスン 25: Being clear and direct

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287744>  

Open in Claude

The first line of your prompt is the most important part of your entire request. This is where you set the stage for everything that follows, and getting it right can dramatically improve your results.

Being Clear and Direct

When crafting that crucial first line, you want to focus on two key principles: clarity and directness. This means using simple language that leaves no room for ambiguity about what you want Claude to do.

Clear Communication

Being "clear" means:

Use simple language that anyone can understand
State exactly what you want without beating around the bush
Lead with a straightforward statement of Claude's task

Instead of writing something vague like "I need to know about those things people put on their roofs that use sun - those solar panel things, I think they're called," be direct and write: "Write three paragraphs about how solar panels work."

Direct Instructions

Being "direct" focuses on how you structure your request:

Use instructions, not questions
Start with direct action verbs like "Write," "Create," or "Generate"

Rather than asking "I was reading about renewable energy and geothermal energy sounds neat. What countries use it?" try: "Identify three countries that use geothermal energy. Include generation stats for each."

Putting It Into Practice

Let's see this technique in action. Starting with a weak prompt that simply asked "What should this person eat?" we can apply our clear and direct approach.

The improved version becomes: Generate a one-day meal plan for an athlete that meets their dietary restrictions.

This revision immediately tells Claude:

What action to take (generate)
What to create (a meal plan)
Key constraints (one day, for an athlete, meeting dietary restrictions)
Results Matter

This simple change can have a significant impact on performance. In our example, the evaluation score jumped from 2.32 to 3.92 - a substantial improvement from just restructuring that opening line.

The key takeaway is that Claude responds best when you treat it like a capable assistant who needs clear direction rather than someone who has to guess what you want. Start strong with a direct action verb, be specific about the task, and you'll see better results right away.

---

### レッスン 26: Being specific

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287740>  

Open in Claude

When working with Claude, one of the most effective ways to improve your results is to be specific about what you want. Instead of leaving everything up to the model's interpretation, you can provide clear guidelines or steps that direct Claude toward the kind of output you're looking for.

Think about it this way: if you ask Claude to "write a short story about a character who discovers a hidden talent," Claude could go in countless directions. The story might be 200 words or 2,000 words. It might have one character or five. It could focus on any type of talent discovery scenario.

By adding specific guidelines, you give Claude a clearer target to aim for. This dramatically improves both the consistency and quality of the output.

Two Types of Guidelines

There are two main approaches to being specific in your prompts, and you'll often see them used together in professional applications.

Output Quality Guidelines

The first type focuses on listing qualities that your output should have. These guidelines help you control:

Length of the response
Structure and format
Specific attributes or elements to include
Tone or style requirements

For example, you might specify that a story should be under 1,000 words, include a clear action that reveals the character's talent, and feature at least one supporting character.

Process Steps

The second type provides specific steps for Claude to follow. This approach is particularly useful when you want Claude to think through a problem systematically or consider multiple perspectives before arriving at a final answer.

Instead of jumping straight to writing, you might ask Claude to:

Brainstorm three talents that would create dramatic tension
Pick the most interesting talent
Outline a pivotal scene that reveals the talent
Brainstorm supporting character types that could increase the impact
Real-World Impact

The difference that specificity makes is dramatic. In testing a meal planning prompt, adding guidelines improved the evaluation score from 3.92 to 7.86 - more than doubling the quality of the output simply by telling Claude exactly what elements to include.

Guidelines:

1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned
When to Use Each Approach

Here's a practical guide for when to use each type of specificity:

Always Use Output Guidelines

You should include quality guidelines in almost every prompt you write. They're your safety net for getting consistent, useful results.

Use Process Steps For Complex Problems

Add step-by-step instructions when you're dealing with:

Troubleshooting complex problems
Decision-making scenarios
Critical thinking tasks
Any situation where you want Claude to consider multiple angles

For instance, if you're asking Claude to analyze why a sales team's performance dropped, you'd want to guide it through examining market metrics, industry changes, individual performance, organizational changes, and customer feedback - rather than letting it focus on just one potential cause.

Combining Both Approaches

In professional prompting, you'll often see both techniques used together. You might have guidelines that control the format and content of your output, plus steps that ensure Claude thinks through the problem thoroughly before responding.

This combination gives you both consistency in your results and confidence that Claude has considered all the important factors in reaching its conclusion.

---

### レッスン 27: Structure with XML tags

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287741>  

Open in Claude
0 seconds of 4 minutes, 0Volume 90%

When you're building prompts that include a lot of content, Claude can sometimes struggle to understand which pieces of text belong together or what different sections are supposed to represent. XML tags provide a simple way to add structure and clarity to your prompts, especially when you're interpolating large amounts of data.

Why Structure Matters

Consider a prompt where you need to analyze 20 pages of sales records. Without clear boundaries, Claude might have trouble distinguishing between your instructions and the actual data you want analyzed.

The example above shows how unclear boundaries can make it difficult for Claude to parse your intent. By wrapping the sales records in XML tags like <sales_records> and </sales_records>, you create clear delimiters that help Claude understand the structure of your prompt.

Practical Example: Code and Documentation

Here's a more dramatic example of why XML tags matter. If you ask Claude to debug code using provided documentation, mixing everything together creates confusion:

The "Not Great" version makes it nearly impossible to tell what's code versus documentation. The "Better" version uses <my_code> and <docs> tags to create clear boundaries.

Custom Tag Names

You don't need to use official XML tags. Create descriptive names that make sense for your content:

<sales_records> is better than <data>
<athlete_information> clearly identifies user details
<my_code> and <docs> separate different types of content

The more specific and descriptive your tag names, the better Claude can understand the purpose of each section.

When to Use XML Tags

XML tags are most useful when:

Including large amounts of context or data
Mixing different types of content (code, documentation, data)
You want to be extra clear about content boundaries
Working with complex prompts that interpolate multiple variables

Even for shorter content, XML tags can help serve as delimiters that make your prompt structure more obvious to Claude.

Real-World Application

In practice, you might structure a prompt like this:

<athlete_information>

- Height: 6'2"
- Weight: 180 lbs
- Goal: Build muscle
- Dietary restrictions: Vegetarian
</athlete_information>

Generate a meal plan based on the athlete information above.

This makes it crystal clear that the height, weight, goal, and restrictions are all related athlete data that should be considered together when generating the meal plan.

While you might not see dramatic improvements with simple prompts, XML tags become increasingly valuable as your prompts grow more complex and include larger amounts of varied content.

---

### レッスン 28: Providing examples

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287746>  

Open in Claude

Providing examples in your prompts is one of the most effective prompt engineering techniques you'll use. This approach, known as "one-shot" or "multi-shot" prompting, involves giving Claude sample input/output pairs to guide its responses.

How Examples Work

Let's look at a sentiment analysis example. Say you want Claude to categorize whether a tweet is positive or negative:

The challenge here is sarcasm. A tweet like "Yeah, sure, that was the best movie I've seen since 'Plan 9 from Outer Space'" appears positive on the surface, but it's actually sarcastic and negative (Plan 9 is famously one of the worst movies ever made).

Adding Examples to Handle Corner Cases

To solve this, you can add examples that show Claude how to handle tricky cases:

The improved prompt includes:

A clear positive example: "Great game tonight!" → "Positive"
A sarcastic example: "Oh yeah, I really needed a flight delay tonight! Excellent!" → "Negative"
Context explaining why sarcasm should be treated carefully

Notice how the examples are wrapped in XML tags like <sample_input> and <ideal_output>. This structure makes it crystal clear to Claude what each part represents.

When to Use Examples

Examples are particularly useful for:

Capturing corner cases or edge scenarios
Defining complex output formats (like specific JSON structures)
Showing the exact style or tone you want
Demonstrating how to handle ambiguous inputs
One-Shot vs Multi-Shot

One-Shot: Provide a single example to establish the pattern

Multi-Shot: Provide multiple examples to cover different scenarios

Use multi-shot when you need to handle various edge cases or want to show different types of valid responses.

Finding Good Examples from Evaluations

When running prompt evaluations, look for your highest-scoring outputs to use as examples:

Find responses that scored 10 (or your highest available score) and use those input/output pairs as examples in your prompt. This helps Claude understand what "perfect" output looks like for your specific use case.

Adding Context to Examples

Don't just provide the input/output pair - explain why the output is good:

<ideal_output>
[Your example output here]
</ideal_output>

This example is well-structured, provides detailed information
on food choices and quantities, and aligns with the athlete's
goals and restrictions.

This additional context helps Claude understand the reasoning behind good responses, not just the format.

Best Practices
Always use XML tags to structure your examples clearly
Be explicit about what you're showing: "Here is an example input with an ideal response"
Include examples that address your most common failure cases
Explain why your example outputs are considered ideal
Keep examples relevant to your specific task

Examples are especially powerful because they show rather than tell. Instead of trying to describe exactly what you want in words, you demonstrate it directly. This makes your prompts much more reliable and helps Claude understand subtle requirements that might be hard to express in instructions alone.

---

### レッスン 29: Exercise on prompting

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287748>  

Open in Claude

---

### レッスン 30: Quiz on prompt engineering techniques

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289121>  

Open in Claude
Loading...

---

### レッスン 31: Introducing tool use

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287747>  

Open in Claude

Tools allow Claude to access information from the outside world, extending its capabilities beyond what it learned during training. By default, Claude only knows information from its training data and can't access current events, real-time data, or external systems. Tool use solves this limitation by creating a structured way for Claude to request and receive fresh information.

The Problem Without Tools

When users ask Claude for current information, it hits a wall. For example, if someone asks "What's the weather in San Francisco, California?" Claude has to respond with something like "I'm sorry, but I don't have access to up-to-date weather information."

This creates a frustrating user experience when people need real-time data that Claude could theoretically help with if it just had access to current information.

How Tool Use Works

Tool use follows a specific back-and-forth pattern between your application and Claude. Here's the complete flow:

Initial Request: You send Claude a question along with instructions on how to get extra data from external sources
Tool Request: Claude analyzes the question and decides it needs additional information, then asks for specific details about what data it needs
Data Retrieval: Your server runs code to fetch the requested information from external APIs or databases
Final Response: You send the retrieved data back to Claude, which then generates a complete response using both the original question and the fresh data
Weather Example in Practice

Let's see how this works with the weather question. The process becomes much more specific:

When a user asks about current weather, you include instructions in your prompt about how to retrieve weather data. Claude recognizes it needs current information and requests weather data for the specific location. Your server then calls a weather API to get real-time conditions and sends that data back to Claude. Finally, Claude combines the fresh weather data with the user's question to provide an accurate, current response.

Key Benefits
Real-time Information: Access current data that wasn't available during Claude's training
External System Integration: Connect Claude to databases, APIs, and other services
Dynamic Responses: Provide answers based on the latest available information
Structured Interaction: Claude knows exactly what information it needs and how to ask for it

Tool use transforms Claude from a static knowledge base into a dynamic assistant that can work with live data. This opens up possibilities for building applications that need current information, whether that's weather data, stock prices, database queries, or any other real-time information your users might need.

---

### レッスン 32: Project overview

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287751>  

Open in Claude

We're going to build a practical project that teaches Claude how to set reminders for future dates. This might sound simple at first, but it reveals several interesting challenges that we'll solve using custom tools.

The goal is straightforward: we want to be able to tell Claude "Set a reminder for my doctor's appointment. It's a week from Thursday" and have Claude respond with "OK, I will remind you." But to make this work, we need to address some limitations in how Claude handles time and reminders.

Why This Is Challenging

While Claude knows the current date, there are three specific problems we need to solve:

Limited time awareness: Claude might know the current date, but not the exact time
Date calculation issues: Claude doesn't always handle time-based addition well, especially when looking many days into the future
No reminder capability: Claude doesn't know how to set a reminder - it has no built-in mechanism for this

Each of these limitations represents a gap between what Claude can do naturally and what we need for our reminder system. Tools are how we bridge these gaps.

Tools We Need

We'll create three separate tools to handle each challenge:

Get the current date time: Claude needs to know the current date and time precisely
Add duration to date time: Claude isn't perfect with date time addition, so we'll give it a reliable tool for this
Set a reminder: We need a way to actually set a reminder in the system

We'll implement these tools one at a time, starting with the simplest one. This approach lets us understand how tool calling works before building more complex functionality. By the end, Claude will be able to handle natural language requests like "remind me in a week" by combining these tools to calculate the exact time and set the reminder.

This project demonstrates a key principle of working with AI: when the model has limitations, we extend its capabilities through tools rather than trying to work around those limitations in our prompts.

---

### レッスン 33: Tool functions

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287756>  

Open in Claude

When building AI applications with Claude, you'll often need to give it access to real-time information or the ability to perform actions. This is where tool functions come in - they're Python functions that Claude can call when it needs additional data to help users.

The image above shows three essential tools we'll be implementing: getting the current date/time, adding duration to dates, and setting reminders. Let's start with the first one.

What Are Tool Functions?

A tool function is a plain Python function that gets executed automatically when Claude decides it needs extra information to help a user. For example, if someone asks "What time is it?", Claude would call your date/time tool to get the current time.

Here's an example of a weather tool function. Notice how it validates inputs and provides clear error messages - these are important best practices.

Best Practices for Tool Functions

When writing tool functions, follow these guidelines:

Use descriptive names: Both your function name and parameter names should clearly indicate their purpose
Validate inputs: Check that required parameters aren't empty or invalid, and raise errors when they are
Provide meaningful error messages: Claude can see error messages and might retry the function call with corrected parameters

The validation is particularly important because Claude learns from errors. If you raise a clear error like "Location cannot be empty", Claude might try calling the function again with a proper location value.

Building Your First Tool Function

Let's create a function to get the current date and time. This function will accept a date format parameter so Claude can request the time in different formats:

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
if not date_format:
raise ValueError("date_format cannot be empty")
return datetime.now().strftime(date_format)

This function uses Python's datetime module to get the current time and format it according to the provided format string. The default format gives us year-month-day hour:minute:second.

You can test it with different formats:

# Default format: "2024-01-15 14:30:25"

get_current_datetime()

# Just hour and minute: "14:30"

get_current_datetime("%H:%M")

The validation check ensures Claude can't pass an empty string for the date format. While this specific error is unlikely, it demonstrates the pattern of validating inputs and providing helpful error messages that Claude can learn from.

Next Steps

Creating the function is just the first step. Next, you'll need to write a JSON schema that describes the function to Claude, then integrate it into your chat system. This tool function approach gives Claude powerful capabilities while keeping your code organized and maintainable.

Downloads
001_tools.ipynb
(opens in new tab)

---

### レッスン 34: Tool schemas

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287753>  

Open in Claude

After writing your tool function, the next step is creating a JSON schema that tells Claude what arguments your function expects and how to use it. This schema acts as documentation that Claude reads to understand when and how to call your tools.

Understanding JSON Schema

JSON Schema isn't specific to AI or tool calling - it's a widely-used data validation specification that's been around for years. The AI community adopted it because it's a convenient way to describe function parameters and validate data.

The complete tool specification has three main parts:

name - A clear, descriptive name for your tool (like "get_weather")
description - What the tool does, when to use it, and what it returns
input_schema - The actual JSON schema describing the function's arguments
Writing Effective Descriptions

Your tool description is crucial for helping Claude understand when to use your function. Best practices include:

Aim for 3-4 sentences explaining what the tool does
Describe when Claude should use it
Explain what kind of data it returns
Provide detailed descriptions for each argument
The Easy Way to Generate Schemas

Instead of writing JSON schemas from scratch, you can use Claude itself to generate them. Here's the process:

Copy your tool function code
Go to Claude and ask it to write a JSON schema for tool calling
Include the Anthropic documentation on tool use as context
Let Claude generate a properly formatted schema following best practices

The prompt should be something like: "Write a valid JSON schema spec for the purposes of tool calling for this function. Follow the best practices listed in the attached documentation."

Implementing the Schema in Code

Once Claude generates your schema, copy it into your code file. Here's a good naming pattern to follow:

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
if not date_format:
raise ValueError("date_format cannot be empty")
return datetime.now().strftime(date_format)

get_current_datetime_schema = {
"name": "get_current_datetime",
"description": "Returns the current date and time formatted according to the specified format",
"input_schema": {
"type": "object",
"properties": {
"date_format": {
"type": "string",
"description": "A string specifying the format of the returned datetime. Uses Python's strftime format codes.",
"default": "%Y-%m-%d %H:%M:%S"
}
},
"required": []
}
}

Use the pattern of function_name followed by function_name_schema to keep your schemas organized and easy to match with their corresponding functions.

Adding Type Safety

For better type checking, import and use the ToolParam type from the Anthropic library:

from anthropic.types import ToolParam

get_current_datetime_schema = ToolParam({
"name": "get_current_datetime",
"description": "Returns the current date and time formatted according to the specified format",

# ... rest of schema

})

While not strictly necessary for functionality, this prevents type errors when you use the schema with Claude's API and makes your code more robust.

---

### レッスン 35: Handling message blocks

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287757>  

Open in Claude

When working with Claude's tool functionality, you'll encounter a new type of response structure that's different from the simple text responses you've seen before. Instead of just getting back a single text block, Claude can now return multi-block messages that contain both text and tool usage information.

Making Tool-Enabled API Calls

To enable Claude to use tools, you need to include a tools parameter in your API call. Here's how to structure the request:

messages = []
messages.append({
"role": "user",
"content": "What is the exact time, formatted as HH:MM:SS?"
})

response = client.messages.create(
model=model,
max_tokens=1000,
messages=messages,
tools=[get_current_datetime_schema],
)

The tools parameter takes a list of JSON schemas that describe the available functions Claude can call.

Understanding Multi-Block Messages

When Claude decides to use a tool, it returns an assistant message with multiple blocks in the content list. This is a significant change from the simple text-only responses you've worked with before.

A multi-block message typically contains:

Text Block - Human-readable text explaining what Claude is doing (like "I can help you find out the current time. Let me find that information for you")
ToolUse Block - Instructions for your code about which tool to call and what parameters to use

The ToolUse block includes:

An ID for tracking the tool call
The name of the function to call (like "get_current_datetime")
Input parameters formatted as a dictionary
The type designation "tool_use"
Managing Conversation History with Multi-Block Messages

Remember that Claude doesn't store conversation history - you need to manage it manually. When working with tool responses, you must preserve the entire content structure, including all blocks.

Here's how to properly append a multi-block assistant message to your conversation history:

messages.append({
"role": "assistant",
"content": response.content
})

This preserves both the text block and the tool use block, which is crucial for maintaining the conversation context when you make subsequent API calls.

The Complete Tool Usage Flow

The tool usage process follows this pattern:

Send user message with tool schema to Claude
Receive assistant message with text block and tool use block
Extract tool information and execute the actual function
Send tool result back to Claude along with complete conversation history
Receive final response from Claude

Each step requires careful handling of the message structure to ensure Claude has the full context it needs to provide accurate responses.

Updating Helper Functions

If you've been using helper functions like add_user_message() and add_assistant_message(), you'll need to update them to handle multi-block content. The current versions likely only support single text blocks, but now they need to accommodate the more complex content structures that include tool use blocks.

This multi-block message handling is essential for building robust applications that can seamlessly integrate Claude's tool capabilities while maintaining proper conversation flow.

---

### レッスン 36: Sending tool results

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287752>  

Open in Claude

After Claude requests a tool call, you need to execute the function and send the results back. This completes the tool use workflow by providing Claude with the information it requested.

Running the Tool Function

When Claude responds with a tool use block, you extract the input parameters and call your function. Here's how to access the tool parameters:

response.content[1].input

This gives you a dictionary of the arguments Claude wants to pass to your function. Since your function expects keyword arguments rather than a dictionary, you use Python's unpacking syntax:

get_current_datetime(**response.content[1].input)
Tool Result Block

After running the tool function, you need to send the results back to Claude using a tool result block. This block goes inside a user message and tells Claude what happened when you executed the tool.

The tool result block has several important properties:

tool_use_id - Must match the id of the ToolUse block that this ToolResult corresponds to
content - Output from running your tool, serialized as a string
is_error - True if an error occurred
Handling Multiple Tool Calls

Claude can request multiple tool calls in a single response. For example, if a user asks "What's 10 + 10 and what's 30 + 30?", Claude might respond with two separate ToolUse blocks.

Each tool call gets a unique ID, and you must match these IDs when sending back results. This ensures Claude knows which result corresponds to which request, even if the results arrive in a different order.

Building the Follow-up Request

Your follow-up request to Claude must include the complete conversation history plus the new tool result. Here's the structure:

messages.append({
"role": "user",
"content": [{
"type": "tool_result",
"tool_use_id": response.content[1].id,
"content": "15:04:22",
"is_error": False
}]
})

The complete message history now contains:

Original user message
Assistant message with tool use block
User message with tool result block
Making the Final Request

When sending the follow-up request, you must still include the tool schema even though you're not expecting Claude to make another tool call. Claude needs the schema to understand the tool references in your conversation history.

client.messages.create(
model=model,
max_tokens=1000,
messages=messages,
tools=[get_current_datetime_schema]
)

Claude will then respond with a final message that incorporates the tool results into a natural response for the user. The tool use workflow is now complete - you've successfully enabled Claude to access real-time information through your custom function.

---

### レッスン 37: Multi-turn conversations with tools

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287750>  

Open in Claude

When building applications with multiple tools, you need to handle scenarios where Claude might need to call several tools in sequence to answer a single user question. For example, if a user asks "What day is 103 days from today?", Claude needs to first get the current date, then add 103 days to it.

This creates a multi-turn conversation pattern where Claude makes multiple tool requests before providing a final answer. Your application needs to handle this automatically.

The Multi-Turn Tool Pattern

Here's what happens behind the scenes when Claude needs multiple tools:

User asks: "What day is 103 days from today?"
Claude responds with a tool use block requesting get_current_datetime
Your server calls the function and returns the result
Claude realizes it needs more information and requests add_duration_to_datetime
Your server calls that function and returns the result
Claude now has enough information to provide the final answer
Building a Conversation Loop

To handle this pattern, you need a conversation loop that continues until Claude stops requesting tools:

def run_conversation(messages):
while True:
response = chat(messages)

add_assistant_message(messages, response)

# Pseudo code

if response isn't asking for a tool:
break

tool_result_blocks = run_tools(response)
add_user_message(messages, tool_result_blocks)

return messages
Refactoring Helper Functions

Before implementing the conversation loop, you need to update your helper functions to handle multiple message blocks properly.

Updating Message Handlers

Your add_user_message and add_assistant_message functions currently assume you're always working with plain text. Update them to handle full message objects:

from anthropic.types import Message

def add_user_message(messages, message):
user_message = {
"role": "user",
"content": message.content if isinstance(message, Message) else message
}
messages.append(user_message)

This allows you to pass in either a string, a list of blocks, or a complete message object.

Updating the Chat Function

Modify your chat function to accept a list of tools and return the full message instead of just text:

def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
params = {
"model": model,
"max_tokens": 1000,
"messages": messages,
"temperature": temperature,
"stop_sequences": stop_sequences,
}

if tools:
params["tools"] = tools

if system:
params["system"] = system

message = client.messages.create(**params)
return message
Extracting Text from Messages

Since you're now returning full message objects, create a helper to extract text when needed:

def text_from_message(message):
return "\n".join(
[block.text for block in message.content if block.type == "text"]
)

This function finds all text blocks in a message and joins them together, which is useful when you need to display the final response to users.

Key Improvements

These refactoring steps prepare your code for robust tool handling:

Flexible message handling - Your helper functions can now work with different message formats
Tool support in chat - The chat function can receive and pass through tool schemas
Full message returns - You get complete message objects instead of just text, preserving all blocks
Text extraction utility - Easy way to get readable text from complex messages

With these foundations in place, you're ready to implement the conversation loop that handles multiple tool calls automatically, creating a seamless experience where Claude can use as many tools as needed to answer user questions.

Downloads
001_tools_007.ipynb
(opens in new tab)

---

### レッスン 38: Implementing multiple turns

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287758>  

Open in Claude

Building a conversation system with tools requires implementing a loop that keeps calling Claude until it stops requesting tool usage. When Claude no longer asks for tools, that signals it has a final response ready for the user.

Detecting Tool Requests

The key to knowing whether Claude wants to use a tool lies in the stop_reason field of the response message. When Claude decides it needs to call a tool, this field gets set to "tool_use". This gives us a clean way to check if we need to continue the conversation loop:

if response.stop_reason != "tool_use":
break  # Claude is done, no more tools needed
The Conversation Loop

The main conversation function follows a simple pattern:

def run_conversation(messages):
while True:
response = chat(messages, tools=[get_current_datetime_schema])
add_assistant_message(messages, response)
print(text_from_message(response))

if response.stop_reason != "tool_use":
break

tool_results = run_tools(response)
add_user_message(messages, tool_results)

return messages

This loop continues until Claude provides a final answer without requesting any tools.

Handling Multiple Tool Calls

Claude can request multiple tools in a single response. The message content contains a list of blocks, and we need to process each tool use block separately:

The run_tools function handles this by filtering for tool use blocks and processing each one:

def run_tools(message):
tool_requests = [
block for block in message.content if block.type == "tool_use"
]
tool_result_blocks = []

for tool_request in tool_requests:

# Process each tool request

Tool Result Blocks

Each tool use block must be answered with a corresponding tool result block. The connection between them is maintained through matching IDs:

The tool result block structure includes:

tool_result_block = {
"type": "tool_result",
"tool_use_id": tool_request.id,
"content": json.dumps(tool_output),
"is_error": False
}
Error Handling

Robust tool execution requires handling potential errors. When a tool fails, we still need to provide a result block to Claude:

try:
tool_output = run_tool(tool_request.name, tool_request.input)
tool_result_block = {
"type": "tool_result",
"tool_use_id": tool_request.id,
"content": json.dumps(tool_output),
"is_error": False
}
except Exception as e:
tool_result_block = {
"type": "tool_result",
"tool_use_id": tool_request.id,
"content": f"Error: {e}",
"is_error": True
}
Scalable Tool Routing

To support multiple tools, create a routing function that maps tool names to their implementations:

def run_tool(tool_name, tool_input):
if tool_name == "get_current_datetime":
return get_current_datetime(**tool_input)
elif tool_name == "another_tool":
return another_tool(**tool_input)

# Add more tools as needed

This approach makes it easy to add new tools without modifying the core conversation logic.

Complete Workflow

The complete multi-turn conversation works like this:

Send user message to Claude with available tools
Claude responds with text and/or tool requests
Execute all requested tools and create result blocks
Send tool results back as a user message
Repeat until Claude provides a final answer

This creates a seamless experience where Claude can use multiple tools across several turns to fully answer complex user requests. The conversation history maintains the complete context, allowing Claude to build upon previous tool results to provide comprehensive responses.

Downloads
001_tools_008.ipynb
(opens in new tab)

---

### レッスン 39: Using multiple tools

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287749>  

Open in Claude

Adding multiple tools to your Claude implementation becomes straightforward once you have the core tool-handling infrastructure in place. This tutorial shows how to integrate additional tools by following a simple pattern.

The Tools We're Adding

We need three main capabilities for our reminder system:

Get current date time - Claude needs to know the current date and time
Add duration to date time - Claude isn't perfect with date time addition
Set a reminder - Need a way to set a reminder

The good news is that most of the implementation work is already done. The add_duration_to_datetime function and set_reminder function are provided, along with their corresponding schemas.

Adding Tools to the Conversation

First, update the run_conversation function to include the new tool schemas in the tools list:

response = chat(messages, tools=[
get_current_datetime_schema,
add_duration_to_datetime_schema,
set_reminder_schema
])

This tells Claude about all three available tools it can use during the conversation.

Updating the Tool Router

Next, modify the run_tool function to handle the new tool calls. Add elif cases for each new tool:

def run_tool(tool_name, tool_input):
if tool_name == "get_current_datetime":
return get_current_datetime(**tool_input)
elif tool_name == "add_duration_to_datetime":
return add_duration_to_datetime(**tool_input)
elif tool_name == "set_reminder":
return set_reminder(**tool_input)

The pattern is simple: check the tool name, call the corresponding function with the provided input, and return the result.

Testing Multiple Tool Usage

To test the system, try a request that requires multiple tools: "Set a reminder for my doctors appointment. Its 177 days after Jan 1st, 2050."

This request forces Claude to:

Calculate the date (using add_duration_to_datetime)
Set the reminder (using set_reminder)

Claude handles this by first explaining what it needs to do, then making the appropriate tool calls in sequence. The conversation shows Claude calculating June 27, 2050 as the target date, then setting the reminder for that date.

Understanding the Message Flow

When you examine the conversation history, you'll see the complete message structure:

User message with the request
Assistant message containing both text and tool use blocks
Tool result messages
Follow-up assistant messages

This demonstrates how Claude can include multiple blocks in a single message - combining explanatory text with tool usage requests.

The Simple Pattern for Adding Tools

Once you have the core tool infrastructure, adding new tools follows this pattern:

Create the tool function implementation
Define the tool schema
Add the schema to the tools list in run_conversation
Add a case for the tool in run_tool

This modular approach makes it easy to expand your AI assistant's capabilities without restructuring existing code. Each new tool integrates seamlessly with the existing conversation flow and tool-handling logic.

Downloads
001_tools_009.ipynb
(opens in new tab)

---

### レッスン 40: Fine grained tool calling

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/313160>  

Open in Claude

When you combine tool use with streaming in Claude, you get real-time updates as the AI generates tool arguments. This creates a more responsive user experience, but there are some important details to understand about how it works behind the scenes.

Basic Tool Streaming

With streaming enabled, Claude sends back different types of events as it processes your request. You're already familiar with events like ContentBlockDelta for regular text generation. For tool use, you'll also need to handle a new event type called InputJsonEvent.

Each InputJsonEvent contains two key properties:

partial_json - A chunk of JSON representing part of the tool arguments
snapshot - The cumulative JSON built up from all chunks received so far

Here's how you handle these events in your streaming pipeline:

for chunk in stream:
if chunk.type == "input_json":

# Process the partial JSON chunk

print(chunk.partial_json)

# Or use the complete snapshot so far

current_args = chunk.snapshot

How JSON Validation Works

Here's where things get interesting. The Anthropic API doesn't immediately send you every chunk as Claude generates it. Instead, it buffers chunks and validates them first.

The API waits for complete top-level key-value pairs before sending anything. For example, if your tool expects this structure:

{
"abstract": "This paper presents a novel...",
"meta": {
"word_count": 847,
"review": "This paper introduces QuanNet..."
}
}

The API will:

Wait until the entire abstract value is complete
Validate that key-value pair against your schema
Send all the buffered chunks for abstract at once
Repeat the process for the meta object

This validation process explains why you see delays followed by bursts of text, even with streaming enabled. The chunks are being held back until a complete, valid top-level key-value pair is ready.

Fine-Grained Tool Calling

If you need faster, more granular streaming - perhaps to show users immediate updates or start processing partial results quickly - you can enable fine-grained tool calling.

Fine-grained tool calling does one main thing: it disables JSON validation on the API side. This means:

You get chunks as soon as Claude generates them
No buffering delays between top-level keys
More traditional streaming behavior
Critical: JSON validation is disabled - your code must handle invalid JSON

Enable it by adding fine_grained=True to your API call:

run_conversation(
messages,
tools=[save_article_schema],
fine_grained=True
)

With fine-grained tool calling, you might receive a word_count value much earlier in the stream, without waiting for the entire meta object to be completed.

Handling Invalid JSON

When using fine-grained tool calling, Claude might generate invalid JSON like "word_count": undefined instead of a proper number. Your application needs to handle these cases gracefully:

try:
parsed_args = json.loads(chunk.snapshot)
except json.JSONDecodeError:

# Handle invalid JSON appropriately

print("Received invalid JSON, continuing...")

Without fine-grained tool calling, the API's validation would catch this error and potentially wrap problematic values in strings, which might not match your expected schema.

When to Use Fine-Grained Tool Calling

Consider enabling fine-grained tool calling when:

You need to show users real-time progress on tool argument generation
You want to start processing partial tool results as quickly as possible
The buffering delays negatively impact your user experience
You're comfortable implementing robust JSON error handling

For most applications, the default behavior with validation is perfectly adequate. But when you need that extra responsiveness, fine-grained tool calling gives you the control to get chunks as fast as Claude can generate them.

Downloads
003_tool_streaming.ipynb
(opens in new tab)
003_tool_streaming_completed.ipynb
(opens in new tab)

---

### レッスン 41: The text edit tool

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287760>  

Open in Claude
0 seconds of 8 minutes, 41 secondsVolume 90%

Important Note: Tool version strings can for all model versions can be found here: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool

Claude comes with one built-in tool that you don't need to create from scratch: the text editor tool. This tool gives Claude the ability to work with files and directories just like you would in a standard text editor.

What the Text Editor Tool Can Do

The text editor tool provides Claude with a comprehensive set of file manipulation capabilities:

View file or directory contents
View specific ranges of lines in a file
Replace text in a file
Create new files
Insert text at specific lines in a file
Undo recent edits to files

This dramatically expands Claude's abilities and essentially gives it the power to act as a software engineer right out of the gate.

Understanding the Implementation Requirements

Here's where things get a bit confusing: while the tool schema is built into Claude, you still need to provide the actual implementation. Think of it this way - Claude knows how to ask for file operations, but you need to write the code that actually performs those operations.

When you use other tools, you write both the JSON schema and the function implementation. With the text editor tool, Claude provides the schema knowledge, but you must write functions to handle Claude's requests to create files, read directories, replace text, and so on.

Schema Versions

While the main schema is built into Claude, you do need to include a small schema stub when making requests. The exact schema depends on which Claude model you're using:

def get_text_edit_schema(model):
if model.startswith("claude-3-7-sonnet"):
return {
"type": "text_editor_20250124",
"name": "str_replace_editor",
}
elif model.startswith("claude-3-5-sonnet"):
return {
"type": "text_editor_20241022",
"name": "str_replace_editor",
}

Claude sees this small schema and automatically expands it into the full text editor tool specification behind the scenes.

Practical Example

Let's see the text editor tool in action. When you ask Claude to work with files, it will use the tool to read, modify, and create files as needed.

For example, if you ask Claude to "Open the ./main.py file and summarize its contents", Claude will:

Use the text editor tool to view the file
Read the contents
Provide you with a summary

You can take this further by asking Claude to modify files. For instance: "Open the ./main.py file and write out a function to calculate pi to the 5th digit. Then create a ./test.py file to test your implementation."

Claude will:

View the existing main.py file
Replace its contents with a new implementation including the pi calculation function
Create a new test.py file with appropriate unit tests
Why Use the Text Editor Tool?

You might wonder why this tool exists when modern code editors already have AI assistants built in. The text editor tool becomes valuable in scenarios where:

You're building applications that need to programmatically edit files
You're working in environments without access to full-featured code editors
You want to integrate file editing capabilities directly into your Claude-powered applications

Essentially, the text editor tool lets you replicate much of the functionality of a fancy AI-powered code editor within your own applications, giving you fine-grained control over how Claude interacts with your file system.

Downloads
005_text_editor_tool.ipynb
(opens in new tab)

---

### レッスン 42: The web search tool

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287755>  

Open in Claude

Important note: Your organization must enable the Web Search tool in the settings console before using it. You can find this setting here: https://console.anthropic.com/settings/privacy

Claude includes a built-in web search tool that lets it search the internet for current or specialized information to answer user questions. Unlike other tools where you need to provide the implementation, Claude handles the entire search process automatically - you just need to provide a simple schema to enable it.

Setting Up the Web Search Tool

To use the web search tool, you create a schema object with these required fields:

web_search_schema = {
"type": "web_search_20250305",
"name": "web_search",
"max_uses": 5
}

The max_uses field limits how many searches Claude can perform. Claude might do follow-up searches based on initial results, so this prevents excessive API calls. A single search returns multiple results, but Claude may decide additional searches are needed.

How the Response Works

When Claude uses the web search tool, the response contains several types of blocks:

Text blocks - Claude's explanation of what it's doing
ServerToolUseBlock - Shows the exact search query Claude used
WebSearchToolResultBlock - Contains the search results
WebSearchResultBlock - Individual search results with titles and URLs
Citation blocks - Text that supports Claude's statements

The response structure lets you see exactly what Claude searched for and which sources it found. Citations include the specific text Claude used to support its answers, along with the source URLs.

Restricting Search Domains

You can limit searches to specific domains using the allowed_domains field. This is particularly useful when you want reliable, authoritative sources:

web_search_schema = {
"type": "web_search_20250305",
"name": "web_search",
"max_uses": 5,
"allowed_domains": ["nih.gov"]
}

For example, when asking about medical or exercise advice, restricting to domains like PubMed (nih.gov) ensures you get evidence-based information rather than random blog content.

Rendering Search Results

The different block types in the response are designed for specific UI rendering:

Render text blocks as regular content
Display web search results as a list of sources at the top
Show citations inline with the text, including the source domain, page title, URL, and quoted text

This structure helps users understand how Claude arrived at its answers and provides transparency about the sources being used. The citation format makes it clear which specific information came from which sources, building trust in the AI's responses.

Practical Usage

The web search tool works best for:

Current events and recent developments
Specialized information not in Claude's training data
Fact-checking and finding authoritative sources
Research tasks requiring up-to-date information

Simply include the schema in your tools array when making API calls, and Claude will automatically decide when a web search would help answer the user's question.

Downloads
006_web_search.ipynb
(opens in new tab)
006_web_search_complete.ipynb
(opens in new tab)

---

### レッスン 43: Quiz on tool use with Claude

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289122>  

Open in Claude
Loading...

---

### レッスン 44: Introducing Retrieval Augmented Generation

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287763>  

Open in Claude

Retrieval Augmented Generation (RAG) is a technique that helps you work with large documents that are too big to fit into a single prompt. Instead of cramming everything into one massive prompt, RAG breaks documents into chunks and only includes the most relevant pieces when answering questions.

The Problem with Large Documents

Imagine you have an 800-page financial document and want to ask Claude specific questions about it, like "What risk factors does this company have?" You need to get the relevant information from the document to Claude somehow, but there are limits to how much text you can include in a prompt.

Option 1: Include Everything in the Prompt

The first approach is straightforward - extract all text from the document and stuff it into your prompt along with the user's question. Your prompt might look like this:

Answer the user's question about the financial document.

<user_question>
{user_question}
</user_question>

<financial_document>
{financial_document}
</financial_document>

This approach has serious limitations:

There's a hard limit on prompt length - your document might be too long
Claude becomes less effective with very long prompts
Larger prompts cost more to process
Larger prompts take longer to process
Option 2: Break Documents into Chunks

RAG takes a smarter approach. First, you break the document into smaller chunks during a preprocessing step. Then, when a user asks a question, you find the chunks most relevant to their question and only include those in your prompt.

Here's how it works: if someone asks "What risks does this company face?" you'd search through your chunks, find the "Risk Factors" section, and include just that relevant chunk in your prompt.

Benefits of RAG
Claude can focus on only the most relevant content
Scales up to very large documents
Works with multiple documents
Smaller prompts cost less and run faster
Challenges with RAG
Requires a preprocessing step to chunk documents
Need a search mechanism to find "relevant" chunks
Included chunks might not contain all the context Claude needs
Many ways to chunk text - which approach is best?

For example, you could split documents into equal-sized portions, or you could create chunks based on document structure like headers and sections. Each approach has trade-offs you'll need to evaluate for your specific use case.

When to Use RAG

RAG involves many technical decisions and requires more work than simply including everything in a prompt. You'll need to analyze whether the benefits outweigh the complexity for your particular application. It's especially valuable when working with very large documents, multiple documents, or when you need to optimize for cost and performance.

The key insight is that RAG trades simplicity for scalability and efficiency. While it requires more upfront work to implement properly, it enables you to work with document collections that would be impossible to handle with simple prompt stuffing.

---

### レッスン 45: Text chunking strategies

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287776>  

Open in Claude

Text chunking is one of the most critical steps in building a RAG (Retrieval Augmented Generation) pipeline. How you break up your documents directly impacts the quality of your entire system. A poor chunking strategy can lead to irrelevant context being inserted into your prompts, causing your AI to give completely wrong answers.

Consider this example: you have a document with sections on medical research and software engineering. If you chunk poorly, a user asking "How many bugs did engineers fix this year?" might get information about medical research instead of software engineering, simply because the medical section happened to contain the word "bug" in a different context.

This is why choosing the right chunking strategy matters so much. Let's explore three main approaches.

Size-Based Chunking

Size-based chunking is the simplest approach - you divide your text into strings of equal length. If you have a 325-character document, you might split it into three chunks of roughly 108 characters each.

This method is easy to implement and works with any type of document, but it has clear downsides:

Words get cut off mid-sentence
Chunks lose important context from surrounding text
Section headers might be separated from their content

To address these issues, you can add overlap between chunks. This means each chunk includes some characters from the neighboring chunks, providing better context and ensuring complete words and sentences.

Here's a basic implementation:

def chunk_by_char(text, chunk_size=150, chunk_overlap=20):
chunks = []
start_idx = 0

while start_idx < len(text):
end_idx = min(start_idx + chunk_size, len(text))
chunk_text = text[start_idx:end_idx]
chunks.append(chunk_text)

start_idx = (
end_idx - chunk_overlap if end_idx < len(text) else len(text)
)

return chunks
Structure-Based Chunking

Structure-based chunking divides text based on the document's natural structure - headers, paragraphs, and sections. This works great when you have well-formatted documents like Markdown files.

For a Markdown document, you can split on header markers:

def chunk_by_section(document_text):
pattern = r"\n## "
return re.split(pattern, document_text)

This approach gives you the cleanest, most meaningful chunks because each one represents a complete section. However, it only works when you have guarantees about your document structure. Many real-world documents are plain text or PDFs without clear structural markers.

Semantic-Based Chunking

Semantic-based chunking is the most sophisticated approach. You divide text into sentences, then use natural language processing to determine how related consecutive sentences are. You build chunks from groups of related sentences.

This method is computationally expensive but produces the most relevant chunks. It requires understanding the meaning of individual sentences and is more complex to implement than the other strategies.

Sentence-Based Chunking

A practical middle ground is chunking by sentences. You split the text into individual sentences using regular expressions, then group them into chunks with optional overlap:

def chunk_by_sentence(text, max_sentences_per_chunk=5, overlap_sentences=1):
sentences = re.split(r"(?<=[.!?])\s+", text)

chunks = []
start_idx = 0

while start_idx < len(sentences):
end_idx = min(start_idx + max_sentences_per_chunk, len(sentences))
current_chunk = sentences[start_idx:end_idx]
chunks.append(" ".join(current_chunk))

start_idx += max_sentences_per_chunk - overlap_sentences

if start_idx < 0:
start_idx = 0

return chunks
Choosing Your Strategy

Your choice depends entirely on your use case and document guarantees:

Structure-based: Best results when you control document formatting (like internal company reports)
Sentence-based: Good middle ground for most text documents
Size-based: Most reliable fallback that works with any content type, including code

Size-based chunking with overlap is often the go-to choice in production because it's simple, reliable, and works with any document type. While it may not give perfect results, it consistently produces reasonable chunks that won't break your pipeline.

Remember: there's no single "best" chunking strategy. The right approach depends on your specific documents, use cases, and the trade-offs you're willing to make between implementation complexity and chunk quality.

Downloads
001_chunking.ipynb
(opens in new tab)
report.md
(opens in new tab)

---

### レッスン 46: Text embeddings

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287759>  

Open in Claude

After breaking a document into chunks, the next step in a RAG pipeline is finding which chunks are most relevant to a user's question. This is essentially a search problem - you need to look through all your text chunks and identify the ones that relate to what the user is asking about.

Semantic Search

The most common approach for finding relevant chunks is semantic search. Unlike keyword-based search that looks for exact word matches, semantic search uses text embeddings to understand the meaning and context of both the user's question and each text chunk.

Text Embeddings

A text embedding is a numerical representation of the meaning contained in some text. Think of it as converting words and sentences into a format that computers can work with mathematically.

Here's how the process works:

You feed text into an embedding model
The model outputs a long list of numbers (the embedding)
Each number ranges from -1 to +1
These numbers represent different qualities or features of the input text
Understanding the Numbers

Each number in an embedding is essentially a "score" for some quality of the input text. However, here's the important caveat: we don't know precisely what each number represents.

While it's helpful to imagine that one number might represent "how happy the text is" or "how much the text talks about oceans," these are just conceptual examples. The actual meaning of each dimension is learned by the model during training and isn't directly interpretable by humans.

VoyageAI for Embeddings

Since Anthropic doesn't currently provide embedding generation, the recommended provider is VoyageAI. You'll need to:

Sign up for a separate VoyageAI account
Get an API key (free to get started)
Add the key to your environment variables

In your .env file, add:

VOYAGE_API_KEY="your_key_here"
Implementation

First, install the VoyageAI library:

%pip install voyageai

Then set up the client and create a function to generate embeddings:

from dotenv import load_dotenv
import voyageai

load_dotenv()
client = voyageai.Client()

def generate_embedding(text, model="voyage-3-large", input_type="query"):
result = client.embed([text], model=model, input_type=input_type)
return result.embeddings[0]

When you run this function on a text chunk, you'll get back a list of floating-point numbers representing the embedding. The process is quick and straightforward - the real challenge is understanding how to use these embeddings effectively in your RAG pipeline for finding the most relevant content.

The next step is learning how to compare embeddings to determine which chunks are most similar to a user's question, which forms the core of the semantic search process.

Downloads
002_embeddings.ipynb
(opens in new tab)
VoyageAI API Key Directions.pdf
(opens in new tab)

---

### レッスン 47: The full RAG flow

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287764>  

Open in Claude

Now that we've covered the basics of RAG, text chunking, and embeddings, let's walk through the complete RAG pipeline step by step. This example will show you exactly how all these pieces work together to retrieve relevant information and generate responses.

Step 1: Chunk Your Source Text

First, we take our source document and break it into manageable chunks. For this example, we'll use two simple text sections:

Section 1: Medical Research - "This year saw significant strides in our understanding of XDR-47, a 'bug' we have not seen before."
Section 2: Software Engineering - "This division dedicated significant effort to studying various infection vectors in our distributed systems"
Step 2: Generate Embeddings

Next, we convert each text chunk into numerical embeddings using an embedding model. To make this easier to understand, let's imagine we have a perfect embedding model that always returns exactly two numbers, and we know what each number represents.

In our imaginary model:

The first number represents how much the text talks about the medical field
The second number represents how much the text talks about software engineering

For the medical research section, we might get [0.97, 0.34] - very medical-focused but with some software elements due to the word "bug". For the software engineering section, we get [0.30, 0.97] - heavily software-focused but with medical undertones from "infection vectors".

Normalization

The embedding API typically performs a normalization step that scales each vector to have a magnitude of 1.0. You don't need to worry about the math here - it's handled automatically. This gives us normalized vectors like [0.944, 0.331] and [0.295, 0.955].

We can visualize these embeddings on a unit circle, where each point represents one of our text chunks.

Step 3: Store in Vector Database

We store these embeddings in a vector database - a specialized database optimized for storing, comparing, and searching through long lists of numbers like our embeddings.

At this point, we pause. All the work so far has been preprocessing that happens ahead of time. Now we wait for a user to submit a query.

Step 4: Process User Query

When a user asks a question like "I'm curious about the company. In particular, what did the software engineering dept do this year?", we run their query through the same embedding model.

This query gets embedded as something like [0.1, 0.89] - low medical score, high software engineering score. After normalization, we get [0.112, 0.993].

Step 5: Find Similar Embeddings

We send the user's query embedding to our vector database and ask it to find the most similar stored embeddings.

The database returns the software engineering section because it's the closest match to what the user asked about.

How Similarity Works: Cosine Similarity

The vector database uses cosine similarity to determine which embeddings are most similar. This measures the cosine of the angle between two vectors.

Key points about cosine similarity:

Results range from -1 to 1
Values close to 1 mean high similarity
Values close to -1 mean very different
0 means perpendicular (no relationship)

In our example, the cosine similarity between the user query and the software engineering chunk is 0.983 - very high similarity. The similarity with the medical research chunk is only 0.398 - much lower.

Cosine Distance

You'll often see "cosine distance" in vector database documentation. This is simply calculated as (1 - cosine similarity). With cosine distance:

Values close to 0 mean high similarity
Larger values mean less similarity

This adjustment makes the numbers easier to interpret in many contexts.

Step 6: Create the Final Prompt

Finally, we take the user's question and the most relevant text chunk we found, combine them into a prompt, and send it to Claude for a response.

The prompt might look like:

Answer the user's question about the financial document.

<user_question>
How many bugs did engineers fix this year?
</user_question>

<report>
## Section 2: Software Engineering
This division dedicated significant effort to studying various infection vectors in our distributed systems
</report>

And that's the complete RAG pipeline! The system successfully retrieved the most relevant information based on semantic similarity and provided it as context for generating an accurate response.

---

### レッスン 48: Implementing the RAG flow

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287761>  

Open in Claude

Now that we understand the RAG flow conceptually, let's implement it step by step. We'll walk through a complete example that demonstrates how to chunk text, generate embeddings, store them in a vector database, and perform similarity searches.

The Five-Step RAG Implementation

Our implementation follows the same five steps we discussed previously:

Chunk the text by section
Generate embeddings for each chunk
Create a vector store and add each embedding to it
Generate an embedding for the user's question
Search the store to find the most relevant chunks

This diagram shows how we transform user queries into embeddings and search our vector database to find the most relevant content.

Step 1: Chunking the Text

First, we load our document and split it into manageable sections:

with open("./report.md", "r") as f:
text = f.read()

chunks = chunk_by_section(text)
chunks[2]  # Test to see the table of contents

We use the same chunk_by_section function from earlier to split our document into logical sections.

Step 2: Generate Embeddings

Next, we create embeddings for all our chunks at once:

embeddings = generate_embedding(chunks)

The embedding function has been updated to handle both single strings and lists of strings, making it more efficient for batch processing.

Step 3: Store in Vector Database

Now we create our vector store and populate it with embeddings and their associated text:

store = VectorIndex()

for embedding, chunk in zip(embeddings, chunks):
store.add_vector(embedding, {"content": chunk})

Notice that we store both the embedding and the original text content. This is crucial because when we search later, we need to return the actual text, not just the numerical embedding values.

Why Store the Original Text?

When we query our vector database, getting back just the embedding numbers isn't useful. We need the actual text that was used to generate those embeddings. That's why we include the original chunk text (or at least a reference to it) alongside each embedding in our database.

Step 4: Process User Queries

When a user asks a question, we generate an embedding for their query:

user_embedding = generate_embedding("What did the software engineering dept do last year?")
Step 5: Find Relevant Content

Finally, we search our vector store to find the most similar chunks:

results = store.search(user_embedding, 2)

for doc, distance in results:
print(distance, "\n", doc["content"][0:200], "\n")

This search returns the two most relevant chunks along with their similarity scores (cosine distances).

The search results show us which sections of our document are most relevant to the user's question, along with similarity scores.

Understanding the Results

When we run our example query about the software engineering department, we get back:

Section 2: Software Engineering with a distance of 0.71 (closest match)
Methodology section with a distance of 0.72 (second closest)

Lower distance values indicate higher similarity, so Section 2 is the most relevant to our query.

What's Next?

This implementation works well for basic cases, but there are scenarios where it doesn't perform as expected. In the next sections, we'll explore improvements to make our RAG system more robust and accurate.

The key takeaway is that RAG is fundamentally about converting text to numbers (embeddings), storing those numbers efficiently, and then using mathematical similarity to find relevant content when users ask questions.

Downloads
003_vectordb.ipynb
(opens in new tab)

---

### レッスン 49: BM25 lexical search

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287767>  

Open in Claude

When building RAG pipelines, you'll quickly discover that semantic search alone doesn't always return the best results. Sometimes you need exact term matches that semantic search might miss. The solution is to combine semantic search with lexical search using a technique called BM25.

The Problem with Semantic Search Alone

Let's say you're searching for a specific incident ID like "INC-2023-Q4-011" in a document. While semantic search excels at understanding context and meaning, it might return sections that are semantically related but don't actually contain the exact term you're looking for.

In the example above, semantic search returned the cybersecurity section (which does contain the incident ID) but also returned a financial analysis section that doesn't mention the incident at all. This happens because semantic search focuses on conceptual similarity rather than exact term matching.

Hybrid Search Strategy

The solution is to run both semantic and lexical searches in parallel, then merge the results. This gives you the best of both worlds:

Semantic search finds conceptually related content using embeddings
Lexical search finds exact term matches using classic text search
Merged results combine both approaches for better accuracy
How BM25 Works

BM25 (Best Match 25) is a popular algorithm for lexical search in RAG systems. Here's how it processes a search query:

Step 1: Tokenize the query
Break the user's question into individual terms. For example, "a INC-2023-Q4-011" becomes ["a", "INC-2023-Q4-011"].

Step 2: Count term frequency
See how often each term appears across all your documents. Common words like "a" might appear 5 times, while specific terms like "INC-2023-Q4-011" might appear only once.

Step 3: Weight terms by importance
Terms that appear less frequently get higher importance scores. The word "a" gets low importance because it's common, while "INC-2023-Q4-011" gets high importance because it's rare.

Step 4: Find best matches
Return documents that contain more instances of the higher-weighted terms.

Implementing BM25 Search

Here's how to set up a basic BM25 search system:

# 1. Chunk your text by sections

chunks = chunk_by_section(text)

# 2. Create a BM25 store and add documents

store = BM25Index()
for chunk in chunks:
store.add_document({"content": chunk})

# 3. Search the store

results = store.search("What happened with INC-2023-Q4-011?", 3)

# Print results

for doc, distance in results:
print(distance, "\n", doc["content"][:200], "\n----\n")

When you run this search, you'll get much better results than semantic search alone. The BM25 algorithm prioritizes sections that actually contain your specific search terms, especially rare terms like incident IDs.

Notice how the results now properly prioritize the Software Engineering section and Cybersecurity section - both of which actually contain the incident ID you're searching for.

Why This Works Better

BM25 excels at finding exact matches because it:

Gives higher weight to rare, specific terms
Ignores common words that don't add search value
Focuses on term frequency rather than semantic meaning
Works especially well for technical terms, IDs, and specific phrases

The key insight is that both search methods have complementary strengths. Semantic search understands context and meaning, while lexical search ensures you don't miss exact term matches. By combining them, you create a more robust search system that handles both conceptual queries and specific lookups effectively.

In the next step, you'll learn how to merge results from both search systems to create a unified hybrid search experience.

Downloads
004_bm25.ipynb
(opens in new tab)

---

### レッスン 50: A Multi-Index RAG pipeline

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287766>  

Open in Claude

We've built separate implementations for semantic search (using vector embeddings) and lexical search (using BM25). Now it's time to combine them into a unified search pipeline that leverages the strengths of both approaches.

The Multi-Index Architecture

Both our VectorIndex and BM25Index classes share nearly identical APIs - they both have add_document() and search() methods. This consistency makes it straightforward to wrap them together in a new class called Retriever.

The Retriever acts as a coordinator that forwards user queries to both indexes, collects their results, and merges them using a technique called reciprocal rank fusion.

Understanding Reciprocal Rank Fusion

Merging results from different search methods isn't as simple as just concatenating lists. Each method uses different scoring systems, so we need a way to normalize and combine their rankings fairly.

Here's how reciprocal rank fusion works with an example. Let's say we search for information about "INC-2023-Q4-011" and get these results:

VectorIndex returns: Section 2 (rank 1), Section 7 (rank 2), Section 6 (rank 3)
BM25Index returns: Section 6 (rank 1), Section 2 (rank 2), Section 7 (rank 3)

We combine these into a single table showing each text chunk's rank from both indexes, then apply the RRF formula:

RRF_score(d) = Σ(1 / (k + rank_i(d)))

Where k is a constant (often 60, but we'll use 1 for clearer results) and rank_i(d) is the rank of document d in the i-th ranking.

For our example:

Section 2: 1.0/(1+1) + 1.0/(1+2) = 0.833
Section 7: 1.0/(1+2) + 1.0/(1+3) = 0.583
Section 6: 1.0/(1+3) + 1.0/(1+1) = 0.75

The final ranking becomes: Section 2 (0.833), Section 6 (0.75), Section 7 (0.583). This makes intuitive sense - Section 2 performed well in both indexes, so it rises to the top.

Implementation Details

The Retriever class wraps multiple search indexes and provides a unified interface:

class Retriever:
def **init**(self, *indexes: SearchIndex):
if len(indexes) == 0:
raise ValueError("At least one index must be provided")
self._indexes = list(indexes)

def add_document(self, document: Dict[str, Any]):
for index in self._indexes:
index.add_document(document)

def search(self, query_text: str, k: int = 1, k_rrf: int = 60):

# Get results from all indexes

all_results = []
for idx, results in enumerate(all_results):
for rank, (doc, _) in enumerate(results):

# Track document ranks across indexes

# Apply RRF scoring formula

# Return merged and sorted results

The key insight is that by maintaining consistent APIs across different search implementations, we can easily combine them without tight coupling.

Testing the Hybrid Approach

Remember our earlier problem where searching for "what happened with INC-2023-Q4-011?" returned unexpected results from the vector-only approach? The cybersecurity incident (Section 10) came first, but financial analysis (Section 3) came second instead of the more relevant software engineering section.

With our hybrid retriever, we now get much better results:

Section 10: Cybersecurity Analysis - Incident Response Report (most relevant)
Section 2: Software Engineering - Project Phoenix Stability Enhancements (second most relevant)
Section 5: Legal Developments (third)

This demonstrates how combining semantic and lexical search can overcome the limitations of either approach used alone.

Extensibility

The beauty of this architecture is its extensibility. Since all indexes implement the same SearchIndex protocol with add_document() and search() methods, you can easily add new search methodologies:

Want to add a keyword-based index? A graph-based search? A specialized domain index? Just implement the same interface and the Retriever will automatically incorporate it into the fusion process.

This modular approach keeps each search implementation focused and testable while providing a clean way to combine their strengths in the final system.

Downloads
005_hybrid.ipynb
(opens in new tab)

---

### レッスン 51: Extended thinking

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287773>  

Open in Claude

Important Note: Extended Thinking is not compatible with some other features, notable message pre-filling and temperature. See the full list of restrictions here: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#feature-compatibility

Extended thinking is Claude's advanced reasoning feature that gives the model time to work through complex problems before generating a final response. Think of it as Claude's "scratch paper" - you can see the reasoning process that leads to the answer, which helps with transparency and often results in better quality responses.

How Extended Thinking Works

When extended thinking is enabled, Claude's response changes from a simple text block to a structured response containing two parts:

With thinking enabled, you get both the reasoning process and the final answer:

The key benefits include:

Better reasoning capabilities for complex tasks
Increased accuracy on difficult problems
Transparency into Claude's thought process

However, there are important trade-offs:

Higher costs (you pay for thinking tokens)
Increased latency (thinking takes time)
More complex response handling in your code
When to Use Extended Thinking

The decision is straightforward: use your prompt evaluations. Run your prompts without thinking first, and if the accuracy isn't meeting your requirements after you've already optimized your prompt, then consider enabling extended thinking. It's a tool for when standard prompting isn't quite getting you there.

Response Structure and Security

Extended thinking responses include a special signature system for security:

The signature is a cryptographic token that ensures you haven't modified the thinking text. This prevents developers from tampering with Claude's reasoning process, which could potentially lead the model in unsafe directions.

Redacted Thinking

Sometimes you'll receive a redacted thinking block instead of readable reasoning text:

This happens when Claude's thinking process gets flagged by internal safety systems. The redacted content contains the actual thinking in encrypted form, allowing you to pass the complete message back to Claude in future conversations without losing context.

Implementation

To enable extended thinking in your code, you need to add two parameters to your chat function:

def chat(
messages,
system=None,
temperature=1.0,
stop_sequences=[],
tools=None,
thinking=False,
thinking_budget=1024
):

The thinking budget sets the maximum tokens Claude can use for reasoning. The minimum value is 1024 tokens, and your max_tokens parameter must be greater than your thinking budget.

Add the thinking configuration to your API parameters:

if thinking:
params["thinking"] = {
"type": "enabled",
"budget": thinking_budget
}

Then call it with thinking enabled:

chat(messages, thinking=True)
Testing Redacted Responses

For testing purposes, you can force Claude to return a redacted thinking block by sending a special trigger string. This helps ensure your application handles redacted responses gracefully without crashing.

Extended thinking is a powerful feature when you need Claude to tackle complex reasoning tasks, but use it judiciously given the cost and latency implications. Start with standard prompting, optimize thoroughly, then add thinking when you need that extra reasoning capability.

Downloads
001_thinking_complete.ipynb
(opens in new tab)
001_thinking.ipynb
(opens in new tab)

---

### レッスン 52: Image support

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287778>  

Open in Claude

Claude's vision capabilities let you include images in your messages and ask Claude to analyze them in countless ways. You can ask Claude to describe what's in an image, compare multiple images, count objects, or perform complex visual analysis tasks.

Image Handling Basics

There are several important limitations to keep in mind when working with images:

Up to 100 images across all messages in a single request
Max size of 5MB per image
When sending one image: max height/width of 8000px
When sending multiple images: max height/width of 2000px
Images can be included as base64 encoding or a URL to the image
Each image counts as tokens based on its dimensions: tokens = (width px × height px) / 750

To send an image to Claude, you include an image block in your user message alongside text blocks. Here's the structure:

with open("image.png", "rb") as f:
image_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

add_user_message(messages, [

# Image Block

{
"type": "image",
"source": {
"type": "base64",
"media_type": "image/png",
"data": image_bytes,
}
},

# Text Block

{
"type": "text",
"text": "What do you see in this image?"
}
])
Message Flow

The conversation works just like text-only interactions. Your server sends a user message containing both image and text blocks to Claude, and Claude responds with a text block containing its analysis.

Prompting Techniques

The key to getting good results with images is applying the same prompting engineering techniques you'd use with text. Simple prompts often lead to poor results. For example, asking "How many marbles are in this image?" might return an incorrect count.

You can dramatically improve Claude's accuracy by:

Providing detailed guidelines and analysis steps
Using one-shot or multi-shot examples
Breaking down complex tasks into smaller steps
Step-by-Step Analysis

Instead of a simple question, provide Claude with a methodology:

Analyze this image of marbles and determine the exact count using this methodology:

1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.

What is the exact, verified number of marbles in this image?
One-Shot Examples

You can also improve accuracy by providing examples within your message. Include an image with a known count, state the correct answer, then ask about your target image. This gives Claude a reference point for the type of analysis you want.

Real-World Example: Fire Risk Assessment

Here's a practical application: automating fire risk assessments for home insurance. Instead of sending inspectors to every property, insurance companies can use satellite imagery and Claude's analysis.

The system analyzes satellite images to identify:

Dense, close-packed trees near the residence
Difficult access routes for emergency services
Branches overhanging the residence

Rather than a simple prompt like "provide a fire risk score," a well-structured prompt breaks down the analysis into specific steps:

Analyze the attached satellite image of a property with these specific steps:

1. Residence identification: Locate the primary residence on the property by looking for:

- The largest roofed structure
- Typical residential features (driveway connection, regular geometry)
- Distinction from other structures (garages, sheds, pools)

2. Tree overhang analysis: Examine all trees near the primary residence:

- Identify any trees whose canopy extends directly over any portion of the roof
- Estimate the percentage of roof covered by overhanging branches (0-25%, 25-50%, 50-75%, 75%+)
- Note particularly dense areas of overhang

3. Fire risk assessment: For any overhanging trees, evaluate:

- Potential wildfire vulnerability (ember catch points, continuous fuel paths to structure)
- Proximity to chimneys, vents, or other roof openings if visible
- Areas where branches create a "bridge" between wildland vegetation and the structure

4. Defensible space identification: Assess the property's overall vegetative structure:

- Identify if trees connect to form a continuous canopy over or near the home
- Note any obvious fuel ladders (vegetation that can carry fire from ground to tree to roof)

5. Fire risk rating: Based on your analysis, assign a Fire Risk Rating from 1-4:

- Rating 1 (Low Risk): No tree branches overhanging the roof, good defensible space around the home
- Rating 2 (Moderate Risk): Minimal overhang (<25% of roof), some separation between tree canopies
- Rating 3 (High Risk): Significant overhang (25-50% of roof), connected tree canopies, multiple vulnerability points
- Rating 4 (Severe Risk): Extensive overhang (>50% of roof), dense vegetation against structure

For each item

---

### レッスン 53: PDF support

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287768>  

Open in Claude

Claude can read and analyze PDF files directly, making it a powerful tool for document processing. This capability works similarly to image processing, but with a few key differences in how you structure your code.

Setting Up PDF Processing

To process a PDF file with Claude, you'll use nearly identical code to what you'd use for images. The main differences are in the file type specifications and variable names for clarity.

Here's how to modify your existing image processing code for PDFs:

with open("earth.pdf", "rb") as f:
file_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

messages = []

add_user_message(
messages,
[
{
"type": "document",
"source": {
"type": "base64",
"media_type": "application/pdf",
"data": file_bytes,
},
},
{"type": "text", "text": "Summarize the document in one sentence"},
],
)

chat(messages)
Key Changes from Image Processing

When adapting your image processing code for PDFs, you need to update several elements:

Change the file extension from .png to .pdf
Update the variable name from image_bytes to file_bytes for clarity
Set the type to "document" instead of "image"
Change the media type to "application/pdf" instead of "image/png"
What Claude Can Extract from PDFs

Claude's PDF processing capabilities go beyond simple text extraction. It can analyze and understand:

Text content throughout the document
Images and charts embedded in the PDF
Tables and their data relationships
Document structure and formatting

This makes Claude essentially a one-stop solution for extracting any type of information from PDF documents, whether you need summaries, data analysis, or specific content extraction.

The example above shows Claude successfully processing a Wikipedia article about Earth that was saved as a PDF, demonstrating how it can understand and summarize complex document content in a single sentence.

Downloads
earth.pdf
(opens in new tab)

---

### レッスン 54: Citations

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287771>  

Open in Claude

When Claude answers questions based on documents you provide, users might assume it's just drawing from its training data. But what if Claude could show exactly where it found specific information? That's where citations come in - a powerful feature that lets Claude reference specific parts of your source documents and show users exactly where each piece of information comes from.

Why Citations Matter

Imagine asking Claude about how Earth's atmosphere formed and getting a detailed answer. Without citations, users have no way to verify the information or understand that Claude is actually referencing a specific document you provided. Citations solve this transparency problem by creating a clear trail from Claude's response back to your source material.

Enabling Citations

To enable citations, you need to modify your document message structure. Add two new fields to your document block:

{
"type": "document",
"source": {
"type": "base64",
"media_type": "application/pdf",
"data": file_bytes,
},
"title": "earth.pdf",
"citations": { "enabled": True }
}

The title field gives your document a readable name, while citations: {"enabled": True} tells Claude to track where it finds information.

Understanding Citation Structure

When citations are enabled, Claude's response becomes more complex. Instead of simple text, you get structured data that includes citation information for each claim.

Each citation contains several key pieces of information:

cited_text - The exact text from your document that supports Claude's statement
document_index - Which document Claude is referencing (useful when you provide multiple documents)
document_title - The title you assigned to the document
start_page_number - Where the cited text begins
end_page_number - Where the cited text ends
Building User Interfaces with Citations

The real power of citations comes from building user interfaces that make this information accessible. You can create interactive elements where users can hover over citation markers to see exactly where information came from.

This creates a transparent experience where users can:

See that Claude's answers are grounded in actual source material
Verify the information by checking the original document
Understand the context around each cited piece of information
Citations with Plain Text

Citations aren't limited to PDF documents. You can also use them with plain text sources. When working with text, modify your document structure like this:

{
"type": "document",
"source": {
"type": "text",
"media_type": "text/plain",
"data": article_text,
},
"title": "earth_article",
"citations": { "enabled": True }
}

With plain text sources, instead of page numbers, you'll get character positions that pinpoint exactly where in the text Claude found each piece of information.

When to Use Citations

Citations are particularly valuable when:

Users need to verify information for accuracy
You're working with authoritative documents that users should be able to reference
Transparency about information sources is critical for your application
Users might want to explore the broader context around specific facts

By implementing citations, you transform Claude from a "black box" that provides answers into a transparent research assistant that shows its work. This builds user trust and enables them to dive deeper into your source materials when needed.

Downloads
002_citations_complete.ipynb
(opens in new tab)
earth.pdf
(opens in new tab)

---

### レッスン 55: Prompt caching

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287772>  

Open in Claude

Prompt caching is a feature that speeds up Claude's responses and reduces the cost of text generation by reusing computational work from previous requests. Instead of throwing away all the processing work after each request, Claude can save and reuse it when you send similar content again.

How Claude Normally Processes Requests

To understand prompt caching, let's first look at what happens during a typical request without caching enabled.

When you send a message to Claude, it doesn't immediately start generating a response. Instead, Claude does a tremendous amount of preprocessing work on your input:

Tokenizes the prompt into smaller pieces
Creates embeddings for each token
Adds context based on surrounding text
Only then generates the actual output text

After sending you the response, Claude throws away all this computational work - the tokenization, embeddings, and context analysis all get discarded.

The Problem with Discarding Work

This becomes inefficient when you make follow-up requests that include the same content. For example, in a conversation where you're asking Claude to refine a summary of the same long text:

Claude has to repeat all the same preprocessing work on content it just analyzed moments ago. As Claude might think to itself: "I just processed that message and threw away all the work I did - I could have reused it!"

How Prompt Caching Solves This

Prompt caching changes this workflow by saving the preprocessing work instead of discarding it:

When you make an initial request, Claude performs all the usual preprocessing but stores the results in a cache instead of throwing them away. The cache acts like a lookup table that says "If I ever see this message again, I'll reuse this work I already did."

Key Benefits and Limitations

Prompt caching offers several advantages:

Faster responses: Requests using cached content execute more quickly
Lower costs: You pay less for the cached portions of your requests
Automatic optimization: The initial request writes to the cache, follow-up requests read from it

However, there are important limitations to keep in mind:

Cache duration: Cached content only lives for one hour
Limited use cases: Only beneficial when you're repeatedly sending the same content
High frequency requirement: Most effective when the same content appears extremely frequently in your requests

Prompt caching works best for scenarios like document analysis workflows, where you're asking multiple questions about the same large document, or iterative editing tasks where the base content remains constant while you refine specific aspects.

---

### レッスン 56: Rules of prompt caching

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287770>  

Open in Claude

Prompt caching in Claude works by storing the computational work done on your messages so it can be reused in follow-up requests. This makes subsequent requests both faster and cheaper to execute, but only when you're repeatedly sending identical content.

The process is straightforward: your initial request writes processing work to the cache, and follow-up requests can read from that cache instead of reprocessing the same content. The cache lives for one hour, so this feature is only useful if you're repeatedly sending the same content within that timeframe.

Cache Breakpoints

Caching isn't enabled automatically - you need to manually add cache breakpoints to specific blocks in your messages. Here's how it works:

Work done on messages is not cached automatically
You must manually add a 'cache breakpoint' to a block
Work done for everything before the breakpoint will be cached
Cache will only be used on follow-up requests if the content up to and including the breakpoint is identical

To add a cache breakpoint, you need to use the longhand form for writing text blocks instead of the shorthand:

The shorthand form doesn't provide a place to add the cache control field, so you must use the expanded format with the cache_control field set to {"type": "ephemeral"}.

How Cache Breakpoints Work

When you place a cache breakpoint in a message, Claude caches all the processing work up to and including that breakpoint. Content after the breakpoint is processed normally without caching.

For the cache to be useful in follow-up requests, the content must be identical up to the breakpoint. Even small changes like adding the word "please" will invalidate the cache and force Claude to reprocess everything.

Cross-Message Caching

Cache breakpoints can span across multiple messages and message types. If you place a breakpoint in a later message, all previous messages (user, assistant, etc.) will be included in the cached content.

This is particularly useful for conversations where you want to cache the entire context up to a certain point.

System Prompts and Tools

You're not limited to text blocks - cache breakpoints can be added to:

System prompts
Tool definitions
Image blocks
Tool use and tool result blocks

System prompts and tool definitions are excellent candidates for caching since they rarely change between requests. This is often where you'll get the most benefit from prompt caching.

Cache Ordering

Behind the scenes, Claude processes your request components in a specific order: tools first, then system prompt, then messages. Understanding this order helps you place breakpoints effectively.

You can add up to four cache breakpoints total. For example, you might cache your tools, then add another breakpoint partway through your conversation history. This gives you flexibility in what gets cached when different parts of your request change.

Minimum Content Length

There's a minimum threshold for caching: content must be at least 1024 tokens long to be cached. This is the sum of all messages and blocks you're trying to cache, not individual blocks.

A simple "Hi there!" message won't meet this threshold, but if you duplicate that content 500 times (or have a genuinely long prompt), it will exceed 1024 tokens and be eligible for caching.

The key to effective prompt caching is identifying which parts of your requests stay consistent across multiple calls and placing breakpoints strategically to maximize reuse while minimizing cache invalidation.

---

### レッスン 57: Prompt caching in action

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287774>  

Open in Claude

Prompt caching is a powerful optimization feature that makes your API requests both faster and cheaper when you're repeatedly sending the same content to Claude. Let's explore how to implement it effectively in your applications.

How Prompt Caching Works

When you enable prompt caching, the first request writes content to a cache that lives for one hour. Follow-up requests can then read from this cache instead of processing the same content again. This is particularly valuable when you're sending:

Large system prompts (like a 6K token coding assistant prompt)
Complex tool schemas (around 1.7K tokens for multiple tools)
Repeated message content

The key insight is that caching only helps if you're repeatedly sending identical content - but in many applications, this happens extremely frequently.

Setting Up Tool Schema Caching

To cache your tool schemas, you need to add a cache control field to the last tool in your list. Here's the proper way to do it without modifying your original tool definitions:

if tools:
tools_clone = tools.copy()
last_tool = tools_clone[-1].copy()
last_tool["cache_control"] = {"type": "ephemeral"}
tools_clone[-1] = last_tool
params["tools"] = tools_clone

This approach creates copies of both the tools list and the last tool schema before adding the cache control field. While you could directly modify tools[-1]["cache_control"], the copying approach prevents issues if you later reorder your tools.

System Prompt Caching

For system prompts, you need to structure them as a text block with cache control:

if system:
params["system"] = [
{
"type": "text",
"text": system,
"cache_control": {"type": "ephemeral"}
}
]

This converts your system prompt from a simple string into a structured format that supports caching.

Understanding Cache Behavior

When you run requests with caching enabled, you'll see different usage patterns in the response:

First request: cache_creation_input_tokens=1772 - Claude writes to cache
Follow-up requests: cache_read_input_tokens=1772 - Claude reads from cache
Changed content: New cache creation tokens appear

The cache is extremely sensitive - changing even a single character in your tools or system prompt invalidates the entire cache for that component.

Cache Ordering and Breakpoints

You can set multiple cache breakpoints in a single request. The order matters:

Tools (if provided)
System prompt (if provided)
Messages

If you change your system prompt but keep the same tools, you'll see a partial cache read (for tools) and a cache write (for the new system prompt). This granular caching means you only pay for processing the parts that actually changed.

Practical Considerations

Prompt caching is most effective when you have:

Consistent tool schemas across requests
Stable system prompts
Applications that make multiple requests with similar context

Remember that the cache only lasts for one hour, so it's designed for applications with relatively frequent API usage rather than long-term storage.

Downloads
003_caching.ipynb
(opens in new tab)

---

### レッスン 58: Code execution and the Files API

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287777>  

Open in Claude

The Anthropic API offers two powerful features that work exceptionally well together: the Files API and Code Execution. While they might seem separate at first, combining them opens up some really interesting possibilities for delegating complex tasks to Claude.

Files API

The Files API provides an alternative way to handle file uploads. Instead of encoding images or PDFs directly in your messages as base64 data, you can upload files ahead of time and reference them later.

Here's how it works:

Upload your file (image, PDF, text, etc.) to Claude using a separate API call
Receive a file metadata object containing a unique file ID
Reference that file ID in future messages instead of including raw file data

This approach is particularly useful when you want to reference the same file multiple times or when working with larger files that would be cumbersome to include in every request.

Code Execution Tool

Code execution is a server-based tool that doesn't require you to provide an implementation. You simply include a predefined tool schema in your request, and Claude can optionally execute Python code in an isolated Docker container.

Key characteristics of the code execution environment:

Runs in an isolated Docker container
No network access (can't make external API calls)
Claude can execute code multiple times during a single conversation
Results are captured and interpreted by Claude for the final response
Combining Files API and Code Execution

The real power comes from using these features together. Since the Docker containers have no network access, the Files API becomes the primary way to get data in and out of the execution environment.

Here's a typical workflow:

Upload your data file (like a CSV) using the Files API
Include a container upload block in your message with the file ID
Ask Claude to analyze the data
Claude writes and executes code to process your file
Claude can generate outputs (like plots) that you can download
Practical Example

Let's look at a real example using streaming service data. The CSV file contains user information including subscription tiers, viewing habits, and whether they've churned (canceled their subscription).

First, upload the file using a helper function:

file_metadata = upload('streaming.csv')

Then create a message that includes both the uploaded file and a request for analysis:

messages = []
add_user_message(
messages,
[
{
"type": "text",
"text": """Run a detailed analysis to determine major drivers of churn.
Your final output should include at least one detailed plot summarizing your findings."""
},
{"type": "container_upload", "file_id": file_metadata.id},
],
)

chat(
messages,
tools=[{"type": "code_execution_20250522", "name": "code_execution"}]
)
Understanding the Response

When Claude uses code execution, the response contains multiple types of blocks:

Text blocks - Claude's analysis and explanations
Server tool use blocks - The actual code Claude decided to run
Code execution tool result blocks - Output from running the code

Claude might execute code multiple times during a single response, iteratively building up its analysis. Each execution cycle includes the code and its results.

Downloading Generated Files

One of the most powerful features is Claude's ability to generate files (like plots or reports) and make them available for download. When Claude creates a visualization, it gets stored in the container and you can download it using the Files API.

Look for blocks with type: "code_execution_output" in the response - these contain file IDs for generated content:

download_file("file_id_from_response")

The result is a comprehensive analysis with professional visualizations that would have taken significant manual coding to produce.

Beyond Data Analysis

While data analysis is a natural fit, the combination of Files API and code execution opens up many possibilities:

Image processing and manipulation
Document parsing and transformation
Mathematical computations and modeling
Report generation with custom formatting

The key is that you can delegate complex, computational tasks to Claude while maintaining control over the inputs and outputs through the Files API. This creates a powerful workflow where Claude becomes your coding assistant that can actually execute and iterate on solutions.

Downloads
streaming.csv
(opens in new tab)
005_code_execution.ipynb
(opens in new tab)

---

### レッスン 59: Quiz on features of Claude

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289124>  

Open in Claude
Loading...

---

### レッスン 60: Introducing MCP

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287780>  

Open in Claude

Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Think of it as a way to shift the burden of tool definitions and execution away from your server to specialized MCP servers.

When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connecting to MCP Servers that contain tools, prompts, and resources. Each MCP server acts as an interface to some outside service.

Understanding MCP Through a Real Example

Let's say you're building a chat interface where users can ask Claude about their GitHub data. A user might ask "What open pull requests are there across all my repositories?" To answer this, Claude needs tools to access GitHub's API.

Without MCP, you'd need to create all the GitHub integration tools yourself. This means writing schemas and functions for every piece of GitHub functionality you want to support.

The Tool Function Problem

GitHub has massive functionality - repositories, pull requests, issues, projects, and much more. To build a complete GitHub chatbot, you'd need to author an incredible number of tools:

Each tool requires both a schema definition and a function implementation. This represents a lot of code that you have to write, test, and maintain as a developer.

How MCP Solves This

MCP shifts the burden of tool definitions and execution from your server to MCP servers. Instead of you writing all those GitHub tools, they're authored and executed inside a dedicated MCP server.

The MCP server acts as a wrapper around GitHub's functionality, providing pre-built tools that you can use without having to implement them yourself.

MCP servers provide access to data or functionality implemented by outside services. They package up complex integrations into reusable components that any application can connect to.

Common Questions About MCP
Who Authors MCP Servers?

Anyone can create an MCP server implementation. Often, service providers themselves will make their own official MCP implementations. For example, AWS might release an official MCP server with tools for their various services.

How is MCP Different from Direct API Calls?

MCP servers provide tool schemas and functions already defined for you. If you call an API directly, you're responsible for authoring those tool definitions yourself. MCP saves you that implementation work.

Isn't MCP Just Tool Use?

This is a common misconception. MCP servers and tool use are complementary but different concepts. MCP is about who does the work of creating and maintaining the tools. With MCP, someone else has already written the tool functions and schemas for you - they're packaged inside the MCP server.

The key insight is that MCP servers provide tool schemas and functions already defined for you, eliminating the need to build and maintain complex integrations yourself.

---

### レッスン 61: MCP clients

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287775>  

Open in Claude

The MCP client serves as the communication bridge between your server and MCP servers. Think of it as your access point to all the tools that an MCP server provides. When you need to use external tools or services, the client handles all the message passing and protocol details for you.

Transport Agnostic Communication

One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can talk to each other using different communication methods. The most common setup runs both the MCP client and server on the same machine, where they communicate through standard input/output.

But you're not limited to that approach. MCP clients and servers can also connect over:

HTTP
WebSockets
Various other network protocols
Message Types

Once connected, the client and server exchange specific message types defined in the MCP specification. The main message types you'll work with are:

ListToolsRequest/ListToolsResult: The client asks the server "what tools do you provide?" and gets back a list of available tools.

CallToolRequest/CallToolResult: The client asks the server to run a specific tool with certain arguments, then receives the results.

Complete Flow Example

Here's how all the pieces work together in a real scenario. Let's say a user asks "What repositories do I have?" - here's the complete communication flow:

The process starts when a user submits a query to your server. Your server realizes it needs to provide Claude with a list of available tools before making the request.

Your server asks the MCP client for tools, which sends a ListToolsRequest to the MCP server and receives a ListToolsResult back.

Now your server has everything needed to make the initial request to Claude - both the user's question and the available tools.

Claude examines the tools and decides it needs to call one to answer the question. It responds with a tool use request.

Your server asks the MCP client to execute the tool Claude requested. The MCP client sends a CallToolRequest to the MCP server, which then makes the actual request to GitHub.

GitHub returns the repository data, which flows back through the MCP server as a CallToolResult, then to the MCP client, and finally to your server.

Your server sends the tool results back to Claude in a follow-up message. Claude now has all the information it needs to formulate a complete response.

Finally, Claude responds with the formatted answer, which your server passes back to the user.

Yes, this flow involves many steps, but each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on building your application logic. As we implement our own MCP client and server, you'll see how each piece fits together in practice.

---

### レッスン 62: Project setup

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287785>  

Open in Claude

We're going to build a CLI-based chatbot to better understand how MCP clients and servers work together. This hands-on project will give you practical experience with both sides of the MCP architecture.

What We're Building

Our chatbot will allow users to interact with a collection of documents through a command-line interface. The system consists of two main components:

An MCP client that handles user interactions
A custom MCP server that manages document operations

The server will provide two essential tools: one for reading document contents and another for updating them. All documents will be stored in memory for simplicity - no database required.

Important Architecture Note

In real-world projects, you typically implement either an MCP client or an MCP server, not both. You might create:

An MCP server to expose your service to other developers
An MCP client to connect to existing MCP servers

We're building both components in this project purely for educational purposes - to understand how they communicate and work together.

Project Setup

Download the cli_project.zip file attached to this lesson and extract it to your preferred development directory. Open your code editor in the project folder.

The project includes a comprehensive README file with setup instructions. Follow these steps:

Add your Anthropic API key to the .env file
Install dependencies using either UV (recommended) or pip
Run the starter application to verify everything works
Running the Application

Navigate to your project directory in the terminal. You'll see the main project files including main.py, mcp_client.py, and mcp_server.py.

To start the application, use one of these commands:

# If using UV (recommended)

uv run main.py

# If using standard Python

python main.py

When the application starts successfully, you'll see a chat prompt. Test it by asking a simple question like "what's 1+1?" - you should get a quick response from Claude.

With the basic setup complete, we're ready to start implementing MCP features and exploring how clients and servers communicate through the Model Control Protocol.

Downloads
cli_project.zip
(opens in new tab)
cli_project_COMPLETE.zip
(opens in new tab)

---

### レッスン 63: Defining tools with MCP

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287797>  

Open in Claude

Building an MCP server becomes much simpler when you use the official Python SDK. Instead of manually writing complex JSON schemas for tools, the SDK handles all that complexity for you with decorators and type hints.

In this example, we're creating an MCP server that manages documents stored in memory. The server will provide two essential tools: one to read document contents and another to update them through find-and-replace operations.

Setting Up the MCP Server

The Python MCP SDK makes server creation incredibly straightforward. You can initialize a complete MCP server with just one line:

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")

For this implementation, documents are stored in a simple Python dictionary where keys are document IDs and values contain the document content:

docs = {
"deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
"report.pdf": "The report details the state of a 20m condenser tower.",
"financials.docx": "These financials outline the project's budget and expenditure",
"outlook.pdf": "This document presents the projected future performance of the",
"plan.md": "The plan outlines the steps for the project's implementation.",
"spec.txt": "These specifications define the technical requirements for the equipment"
}
Tool Definition with Decorators

The SDK transforms tool creation from a verbose process into something clean and readable. Instead of writing lengthy JSON schemas, you use Python decorators and type hints.

Creating the Document Reader Tool

The first tool allows Claude to read any document by its ID. Here's the complete implementation:

@mcp.tool(
name="read_doc_contents",
description="Read the contents of a document and return it as a string."
)
def read_document(
doc_id: str = Field(description="Id of the document to read")
):
if doc_id not in docs:
raise ValueError(f"Doc with id {doc_id} not found")

return docs[doc_id]

The @mcp.tool decorator automatically generates the JSON schema that Claude needs. The Field class from Pydantic provides parameter descriptions that help Claude understand what each argument expects.

Building the Document Editor Tool

The second tool performs simple find-and-replace operations on documents:

@mcp.tool(
name="edit_document",
description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
doc_id: str = Field(description="Id of the document that will be edited"),
old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
new_str: str = Field(description="The new text to insert in place of the old text.")
):
if doc_id not in docs:
raise ValueError(f"Doc with id {doc_id} not found")

docs[doc_id] = docs[doc_id].replace(old_str, new_str)

This tool takes three parameters: the document ID, the text to find, and the replacement text. The implementation uses Python's built-in string replace() method for simplicity.

Error Handling

Both tools include basic error handling to manage cases where Claude requests a document that doesn't exist. When an invalid document ID is provided, the tools raise a ValueError with a descriptive message that Claude can understand and potentially act upon.

Key Benefits of the SDK Approach
Automatic JSON schema generation from Python type hints
Clean, readable code that's easy to maintain
Built-in parameter validation through Pydantic
Reduced boilerplate compared to manual schema writing
Type safety and IDE support for development

The MCP Python SDK transforms what used to be a complex process of writing tool definitions into something that feels natural for Python developers. You focus on the business logic while the SDK handles the protocol details.

---

### レッスン 64: The server inspector

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287781>  

Open in Claude

When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time.

Starting the Inspector

First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:

mcp dev mcp_server.py

This starts a development server on port 6277 and gives you a local URL to open in your browser. The inspector interface will load, showing the MCP Inspector dashboard.

Important Note About the Interface

The MCP inspector is actively being developed, so the interface you see might look different from current screenshots. However, the core functionality for testing tools, resources, and prompts should remain similar.

Connecting and Testing Tools

Click the "Connect" button on the left side to start your MCP server. Once connected, you'll see a navigation bar with sections for Resources, Prompts, Tools, and other features.

To test your tools:

Navigate to the Tools section
Click "List Tools" to see all available tools
Select a tool to open its testing interface
Fill in the required parameters
Click "Run Tool" to execute and see results
Testing Document Operations

For example, to test a document reading tool, you'd enter a document ID (like "deposition.md") and run the tool. The inspector shows the result, including any returned content or success messages.

You can chain operations to verify functionality. For instance, after editing a document by replacing text, you can immediately run the read tool again to confirm the changes were applied correctly.

Development Workflow

The inspector creates an efficient development loop:

Make changes to your MCP server code
Test individual tools through the inspector
Verify results without needing a full application setup
Debug issues in isolation

This tool becomes essential as you build more complex MCP servers. It eliminates the need to wire up your server to Claude or another application just to test basic functionality, making development much faster and more focused.

---

### レッスン 65: Implementing a client

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287793>  

Open in Claude

Now that we have our MCP server working, it's time to build the client side. The client is what allows our application to communicate with the MCP server and access its functionality.

Understanding the Client Architecture

In most real-world projects, you'll either implement an MCP client OR an MCP server - not both. We're building both in this project just so you can see how they work together.

The MCP client consists of two main components:

MCP Client - A custom class we create to make using the session easier
Client Session - The actual connection to the server (part of the MCP Python SDK)

The client session requires proper resource cleanup when we're done with it. That's why we wrap it in our custom MCP Client class - to handle all that cleanup automatically.

How the Client Fits Into Our Application

Remember our application flow? Our CLI code needs to do two main things with the MCP server:

Get a list of available tools to send to Claude
Execute tools when Claude requests them

The MCP client provides these capabilities through simple method calls that our application code can use.

Implementing the Core Methods

We need to implement two key methods in our client: list_tools() and call_tool().

List Tools Method

This method gets all available tools from the server:

async def list_tools(self) -> list[types.Tool]:
result = await self.session().list_tools()
return result.tools

It's straightforward - we access our session (the connection to the server), call the built-in list_tools() function, and return the tools from the result.

Call Tool Method

This method executes a specific tool on the server:

async def call_tool(
self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
return await self.session().call_tool(tool_name, tool_input)

We pass the tool name and input parameters (provided by Claude) to the server and return the result.

Testing the Client

To test our implementation, we can run the client directly. The file includes a testing harness that connects to our MCP server and calls our methods:

async with MCPClient(
command="uv", args=["run", "mcp_server.py"]
) as client:
result = await client.list_tools()
print(result)

When we run this test, we should see our tool definitions printed out, including the read_doc_contents and edit_document tools we created earlier.

Putting It All Together

Now that our client can list tools and call them, we can test the complete flow. When we run our main application and ask Claude about a document:

Our code uses the client to get available tools
These tools are sent to Claude along with the user's question
Claude decides to use the read_doc_contents tool
Our code uses the client to execute that tool
The result is sent back to Claude, who then responds to the user

For example, asking "What is the contents of the report.pdf document?" will trigger Claude to use our document reading tool, and we'll get back information about the 20m condenser tower document we set up in our server.

The client acts as the bridge between our application logic and the MCP server, making it easy to access server functionality without worrying about the underlying connection details.

---

### レッスン 66: Defining resources

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287782>  

Open in Claude

Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.

Understanding Resources Through an Example

Let's say you want to build a document mention feature where users can type @document_name to reference files. This requires two operations:

Getting a list of all available documents (for autocomplete)
Fetching the contents of a specific document (when mentioned)

When a user types @, you need to show available documents. When they submit a message with a mention, you automatically inject that document's content into the prompt sent to Claude.

How Resources Work

Resources follow a request-response pattern. Your client sends a ReadResourceRequest with a URI, and the MCP server responds with the data. The URI acts like an address for the resource you want to access.

Types of Resources

There are two types of resources:

Direct Resources: Static URIs that don't change, like docs://documents
Templated Resources: URIs with parameters, like docs://documents/{doc_id}

For templated resources, the Python SDK automatically parses parameters from the URI and passes them as keyword arguments to your function.

Implementing Resources

Resources are defined using the @mcp.resource() decorator. Here's how to create both types:

Direct Resource (List Documents)
@mcp.resource(
"docs://documents",
mime_type="application/json"
)
def list_docs() -> list[str]:
return list(docs.keys())
Templated Resource (Fetch Document)
@mcp.resource(
"docs://documents/{doc_id}",
mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
if doc_id not in docs:
raise ValueError(f"Doc with id {doc_id} not found")
return docs[doc_id]
MIME Types

Resources can return any type of data - strings, JSON, binary, etc. The mime_type parameter gives clients a hint about what kind of data you're returning:

application/json - Structured JSON data
text/plain - Plain text content
Any other valid MIME type for different data formats

The MCP Python SDK automatically serializes your return values. You don't need to manually convert to JSON strings.

Testing Resources

You can test your resources using the MCP Inspector. Run your server with:

uv run mcp dev mcp_server.py

Then connect to the inspector in your browser. You'll see:

Resources: Lists your direct/static resources
Resource Templates: Shows templated resources that accept parameters

Click on any resource to test it and see the exact response structure your client will receive.

Key Points
Resources expose data, tools perform actions
Use direct resources for static data, templated resources for parameterized queries
MIME types help clients understand response format
The SDK handles serialization automatically
Parameter names in templated URIs become function arguments

Resources provide a clean way to make data available to MCP clients, enabling features like document mentions, file browsing, or any scenario where you need to fetch information from your server.

---

### レッスン 67: Accessing resources

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287783>  

Open in Claude

Resources in MCP allow your server to expose data that can be directly included in prompts, rather than requiring tool calls to access information. This creates a more efficient way to provide context to AI models like Claude.

Understanding Resource Requests

When you've defined resources on your MCP server, your client needs a way to request and use them. The client acts as a bridge between your application and the MCP server, handling the communication and data parsing automatically.

The flow is straightforward: when a user wants to reference a document (like typing "@report.pdf"), your application uses the MCP client to fetch that resource from the server and include its contents directly in the prompt sent to Claude.

Implementing Resource Reading

The core functionality requires a read_resource function in your MCP client. This function takes a URI parameter identifying which resource to fetch:

async def read_resource(self, uri: str) -> Any:
result = await self.session().read_resource(AnyUrl(uri))
resource = result.contents[0]

The response from the MCP server contains a contents list. You typically only need the first element, which contains the actual resource data along with metadata like the MIME type.

Handling Different Content Types

Resources can return different types of content, so your client needs to parse them appropriately. The MIME type tells you how to handle the data:

if isinstance(resource, types.TextResourceContents):
if resource.mimeType == "application/json":
return json.loads(resource.text)

return resource.text

This approach ensures that JSON resources are properly parsed into Python objects, while plain text resources are returned as strings. The MIME type acts as your hint for determining the correct parsing strategy.

Required Imports

To make this work properly, you'll need these imports in your MCP client:

import json
from pydantic import AnyUrl

The json module handles parsing JSON responses, while AnyUrl ensures proper type handling for the URI parameter.

Testing Resource Access

Once implemented, you can test the functionality through your CLI application. When you type something like "What's in the @report.pdf document?", the system should:

Show available resources in an autocomplete list
Allow you to select a resource
Fetch the resource content automatically
Include that content in the prompt to Claude

The key advantage is that Claude receives the document content directly in the prompt, eliminating the need for tool calls to access the information. This makes interactions faster and more efficient.

Integration with Your Application

Remember that the MCP client code you write gets used by other parts of your application. The read_resource function becomes a building block that other components can call to fetch document contents, list available resources, or integrate resource data into prompts.

This separation of concerns keeps your code clean: the MCP client handles communication with the server, while your application logic focuses on how to use that data effectively.

---

### レッスン 68: Defining prompts

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287784>  

Open in Claude

Prompts in MCP servers let you define pre-built, high-quality instructions that clients can use instead of writing their own prompts from scratch. Think of them as carefully crafted templates that give better results than what users might come up with on their own.

Why Use Prompts?

Let's say you want Claude to reformat a document into markdown. A user could just type "convert report.pdf to markdown" and it would work fine. But they'd probably get much better results with a thoroughly tested prompt that includes specific instructions about formatting, structure, and output requirements.

The key insight is that while users can accomplish these tasks on their own, they'll get more consistent and higher-quality results when using prompts that have been carefully developed and tested by the MCP server authors.

How Prompts Work

Prompts define a set of user and assistant messages that clients can use directly. When a client requests a prompt, your server returns a list of messages that can be sent straight to Claude.

The basic structure looks like this:

Define prompts using the @mcp.prompt() decorator
Add a name and description for each prompt
Return a list of messages that form the complete prompt
These prompts should be high quality, well-tested, and relevant to your MCP server's purpose
Building a Format Command

Here's how to implement a document formatting prompt. First, you'll need to import the base message types:

from mcp.server.fastmcp import base

Then define your prompt function:

@mcp.prompt(
name="format",
description="Rewrites the contents of the document in Markdown format."
)
def format_document(
doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:

{doc_id}

Add in headers, bullet points, tables, etc as necessary. Feel free to add in extra formatting.
Use the 'edit_document' tool to edit the document. After the document has been reformatted...
"""

return [
base.UserMessage(prompt)
]
Testing Your Prompts

You can test prompts using the MCP Inspector. Navigate to the Prompts section, select your prompt, and provide any required parameters. The inspector will show you the generated messages that would be sent to Claude.

This lets you verify that your prompt interpolates variables correctly and produces the expected message structure before using it in a real application.

Best Practices

When creating prompts for your MCP server:

Focus on tasks that are central to your server's purpose
Write detailed, specific instructions rather than vague requests
Test your prompts thoroughly with different inputs
Include clear descriptions so users understand what each prompt does
Consider how the prompt will work with your server's tools and resources

Remember that prompts are meant to provide value that users couldn't easily get on their own - they should represent your expertise in the domain your MCP server covers.

---

### レッスン 69: Prompts in the client

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287786>  

Open in Claude

Prompts in MCP define a set of user and assistant messages that can be used by the client. These prompts should be high quality, well-tested, and relevant to the overall purpose of the MCP server.

Implementing List Prompts

The first step is implementing the list_prompts method in your MCP client. This method retrieves all available prompts from the server:

async def list_prompts(self) -> list[types.Prompt]:
result = await self.session().list_prompts()
return result.prompts

This simple implementation calls the session's list_prompts method and returns the prompts array from the result.

Getting Individual Prompts

The get_prompt method retrieves a specific prompt with arguments interpolated into it. When you request a prompt, you provide arguments that get passed to the prompt function as keyword arguments:

async def get_prompt(self, prompt_name, args: dict[str, str]):
result = await self.session().get_prompt(prompt_name, args)
return result.messages

The method returns the messages from the result, which form a conversation that can be fed directly into Claude.

How Prompt Arguments Work

When you define a prompt function on the server side, it can accept parameters. For example, a document formatting prompt might expect a doc_id parameter:

def format_document(doc_id: str):

# The doc_id gets interpolated into the prompt

When the client calls get_prompt, the arguments dictionary should contain the expected keys. The MCP server will pass these as keyword arguments to the prompt function, allowing dynamic content to be inserted into the prompt template.

Testing Prompts in the CLI

Once implemented, you can test prompts through the command-line interface. When you type a forward slash, available prompts appear as commands. Selecting a prompt may prompt you to choose from available options (like document IDs), and then the complete prompt gets sent to Claude.

The workflow looks like this:

User selects a prompt (like "format")
System prompts for required arguments (like which document to format)
The prompt gets sent to Claude with the interpolated values
Claude can then use tools to fetch additional data and complete the task
Prompt Best Practices

When creating prompts for your MCP server:

Make them relevant to your server's purpose
Test them thoroughly before deployment
Use clear, specific instructions
Design them to work well with your available tools
Consider what arguments users will need to provide

Prompts bridge the gap between predefined functionality and dynamic user needs, giving Claude structured starting points for complex tasks while maintaining flexibility through parameterization.

---

### レッスン 70: MCP review

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287790>  

Open in Claude

---

### レッスン 71: Quiz on Model Context Protocol

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289126>  

Open in Claude
Loading...

---

### レッスン 72: Anthropic apps

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287787>  

Open in Claude

In this module, we'll explore two powerful applications built by Anthropic: Claude Code and Computer Use. These aren't just useful tools on their own - they're perfect examples of AI agents in action. By understanding how they work, you'll get a solid foundation for building your own agents later.

Our Plan

We'll follow a progression that builds your understanding step by step:

Claude Code - Start with this agentic coding assistant that runs in your terminal
Computer Use - Explore this set of tools that lets Claude interact with desktop applications
Agents - Understand what makes these applications successful as agents
Claude Code

Claude Code is a terminal-based coding assistant that can help you with various programming tasks. Think of it as having Claude available right in your command line, ready to:

Edit files and fix bugs
Answer coding questions
Help with development workflows

We'll walk through the complete setup process and then use Claude Code on a small sample project so you can see exactly how it operates in practice.

Computer Use

Computer Use takes Claude's capabilities much further. It's a collection of tools that allow Claude to interact with a full desktop computer environment. This means Claude can:

Access websites and browse the internet
Interact with desktop applications
Perform tasks that require visual interface navigation

This dramatically expands what's possible compared to text-only interactions.

Why These Matter for Agents

Both Claude Code and Computer Use serve as excellent case studies for understanding agents. They demonstrate key principles that make agents effective:

Tool integration and usage
Multi-step task execution
Environmental interaction
Autonomous problem-solving

By examining these real-world implementations, you'll gain insights into what makes Claude Code and Computer Use successful, which will inform your own agent development work.

Let's start with the setup process for Claude Code in the next section.

---

### レッスン 73: Claude Code setup

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287788>  

Introduction to Model Context Protocol
0 of 14 lessons completed (0%)
Start

Curriculum

Course Overview
Introduction
Welcome to the course
Introducing MCP
MCP clients
Hands-on with MCP servers
Project setup
Defining tools with MCP
The server inspector
Course satisfaction survey
Connecting with MCP clients
Implementing a client
Defining resources
Accessing resources
Defining prompts
Prompts in the client
Assessment and wrap Up
Final assessment on MCP
MCP review

About this course

Data and Privacy
What is Skilljar and why am I logging into it?

Skilljar is a learning management system that hosts our educational content. You're logging into it to access the Anthropic course materials. This separate platform allows us to provide interactive learning experiences, track your progress, and ensure you have access to all course resources in an organized way.

What information does Skilljar collect about my learning activity?

Skilljar collects basic learning analytics such as course progress, lesson completion status, quiz scores, and time spent on materials. This data helps us understand how you're progressing through the course and allows us to provide you with completion certificates. All data collection is focused on improving your learning experience, and is subject to Skilljar's Privacy Policy.

How is my Skilljar data different from my Anthropic account data?

Skilljar only tracks your learning progress within this course platform, while your Anthropic account manages your access to the Anthropic Console and/or Claude AI services.

Is Skilljar secure? Where is my data stored?

Yes, Skilljar employs industry-standard security measures including data encryption, secure hosting, and regular security audits. Your learning data is stored on secure servers with appropriate access controls. Skilljar is SOC 2 compliant and follows best practices for data protection to ensure your information remains safe and private.

How do I delete my learning activity or account?

To request deletion of your learning data or account, email academy-support@anthropic.com. Your request will be processed in accordance with applicable privacy laws and our data retention policies. Note that some data may need to be retained for legitimate business purposes, such as compliance or security, but we'll delete all personal information where legally permissible.

Do I need an Anthropic account to access the learning content?

No, you don't need an Anthropic account to access this learning content. The course is hosted on Skilljar and only requires a Skilljar account for access. However, if you want to use Claude AI services after completing the course, you would need to create a separate Anthropic account at claude.ai.

© 2025 Anthropic PBC

---

### レッスン 74: Claude Code in action

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287805>  

Open in Claude

Claude Code isn't just a tool for writing code - it's designed to work alongside you throughout every phase of a software project. Think of it as another engineer on your team who can handle everything from initial setup to deployment and support.

The /init Command

When you start working with Claude Code on a project, the first thing you'll want to do is run the /init command. This tells Claude to scan your entire codebase and understand your project's structure, dependencies, coding style, and architecture.

Claude summarizes everything it learns in a special file called CLAUDE.md. This file automatically gets included as context in all future conversations, so Claude remembers important details about your project.

You can have multiple CLAUDE.md files for different scopes:

Project - Shared between all engineers working on the project
Local - Your personal notes that aren't checked into git
User - Used across all your projects

When running /init, you can add special directions for areas you want Claude to focus on. The generated file will include build commands, coding guidelines, and project-specific patterns that Claude should follow.

You can also quickly add notes to your CLAUDE.md file using the # command. For example, typing # Always use descriptive variable names will prompt you to add this guideline to your project, local, or user memory.

Common Workflows

Claude works best when you approach it as an effort multiplier. The more context and structure you provide, the better results you'll get. Here's the most effective workflow:

Step 1: Feed Context into Claude

Before asking Claude to build something, identify files in your codebase that are relevant to the feature you want to create. Ask Claude to read and analyze these files first. This gives Claude examples of your coding patterns and existing functionality it can build upon.

Step 2: Tell Claude to Plan a Solution

Instead of jumping straight to implementation, ask Claude to think through the problem and create a plan. Tell Claude specifically not to write any code yet - just focus on the approach and steps needed.

Step 3: Ask Claude to Implement the Solution

Once you have a solid plan, ask Claude to implement it. Claude will write code based on the context and planning work you've already done together.

Test-Driven Development Workflow

For even better results, you can use a test-driven approach:

Feed context into Claude - Same as before, show Claude relevant files
Ask Claude to think of test cases - Have Claude brainstorm what tests would validate your new feature
Ask Claude to implement those tests - Select the most relevant tests and have Claude write them
Ask Claude to write code that passes the tests - Claude will iterate on the implementation until all tests pass

This approach often produces more robust code because Claude has clear success criteria to work toward.

Practical Example

Here's how these workflows look in practice. Let's say you want to add a document conversion tool to an existing project:

// First, ask Claude to read relevant files
> Read the math.py and document.py files

// Then ask for planning (not implementation)
> Plan to implement document_path_to_markdown tool:

1. Create a function that:

- Takes a file path parameter
- Validates the file exists
- Determines file type from extension
- Reads binary data from file
- Leverages existing binary_document_to_markdown function
- Returns markdown string

2. Add appropriate documentation
3. Register the tool with MCP server
4. Add tests

// Finally, ask for implementation
> Implement the plan

Claude will then create the function, update the necessary files, write tests, and even run the test suite to verify everything works correctly.

Additional Commands

Claude Code includes several helpful commands:

/clear - Clears conversation history and resets context
/init - Scans codebase and creates CLAUDE.md documentation

# - Adds notes to your CLAUDE.md file

Claude can also handle routine development tasks like staging and committing changes to git, running tests, and managing dependencies. Instead of switching between your editor and terminal, you can ask Claude to handle these tasks while you focus on the bigger picture.

The key to success with Claude Code is remembering that it's designed to be a collaborative partner, not just a code generator. The more context and structure you provide, the more effectively Claude can help you build and maintain your projects.

Downloads
app_starter.zip
(opens in new tab)

---

### レッスン 75: Enhancements with MCP servers

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287792>  

Open in Claude
0 seconds of 2 minutes, 30 secondsVolume 90%

Claude Code has an MCP client built right into it, which means you can connect MCP servers to dramatically expand what Claude can do. This opens up some really powerful possibilities for customizing your development workflow.

How MCP Extends Claude

The Model Context Protocol allows Claude Code to connect to external services and tools through MCP servers. Instead of being limited to Claude's built-in capabilities, you can add custom functionality by connecting servers that provide specific tools, resources, or integrations.

Each MCP server can expose different types of functionality to Claude through three main components: Tools (for taking actions), Prompts (for templates), and Resources (for accessing data).

Setting Up an MCP Server

Adding an MCP server to Claude Code is straightforward. You use the command line to register your server:

claude mcp add [server-name] [command-to-start-server]

For example, if you have a document processing server that starts with uv run main.py, you'd run:

claude mcp add documents uv run main.py

Once registered, Claude Code will automatically connect to your server when it starts up.

Example: Document Processing

A practical example is creating a tool that lets Claude read PDF and Word documents. By building an MCP server with a "document_path_to_markdown" tool, you can ask Claude to convert document contents to markdown format.

When you ask Claude to "Convert the tests/fixtures/mcp_docs.docx file to markdown", it will automatically use your custom tool to read the document and return the converted content.

Popular MCP Integrations

The MCP ecosystem includes servers for many common development tools and services:

sentry-mcp - Automatically discover and fix bugs logged in Sentry
playwright-mcp - Gives Claude browser automation capabilities for testing and troubleshooting
figma-context-mcp - Exposes Figma designs to Claude
mcp-atlassian - Allows Claude to access Confluence and Jira
firecrawl-mcp-server - Adds web scraping capabilities to Claude
slack-mcp - Allows Claude to post messages or reply to specific threads
Building Your Development Workflow

The real power comes from combining multiple MCP servers that match your specific development process. You might set up:

A Sentry server to fetch production error details
A Jira server to read ticket requirements
A Slack server to notify your team when work is complete
Custom servers for your internal tools and APIs

This creates a development environment where Claude can seamlessly work with all the tools and services you already use, making it a much more powerful coding assistant tailored to your specific workflow.

---

### レッスン 76: Agents and workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287796>  

Open in Claude

Workflows and agents are strategies for handling user tasks that can't be completed by Claude in a single request. You've actually been creating both throughout this course - when you used tools and let Claude figure out how to complete tasks, that was an agent.

When to Use Workflows vs Agents

The decision comes down to how well you understand the task:

Use workflows when you can picture the exact flow or steps that Claude should go through to solve a problem, or when your app's UX constrains users to a set of tasks
Use agents when you're not sure exactly what task or task parameters you'll give to Claude

Workflows are a series of calls to Claude meant to solve a specific problem through a predetermined series of steps. Agents give Claude a goal and a set of tools, expecting Claude to figure out how to complete the goal through the provided tools.

Example: Image to CAD Workflow

Let's look at a practical workflow example. Imagine building a web app where users drag and drop an image of a metal part, and you create a STEP file (an industry standard for 3D models) from it.

Since we have a pretty good idea of exactly what to do when a user supplies an image file, and we can easily write all of this out with code as a predefined series of steps, this makes a perfect workflow candidate.

Here's how the workflow breaks down:

Feed an image into Claude, asking it to describe the object
Based on the description, ask Claude to use the CadQuery library to model the object
Create a rendering
Ask Claude to grade the rendering against the original image. If there are issues, fix them
The Evaluator-Optimizer Pattern

This modeling workflow is an example of an evaluator-optimizer pattern. Here's how it works:

Producer: Takes input and creates output (Claude using CadQuery to model the part and create a rendering)
Grader: Evaluates the output against some criteria
Feedback loop: If the grader doesn't accept the output, feedback goes back to the producer for improvement
Iteration: The cycle repeats until the grader accepts the output
Why Learn Workflow Patterns

The goal of identifying different workflows is to give you a set of repeatable recipes for implementing your own features. The Evaluator-Optimizer is one workflow pattern that has worked well for other engineers - consider using it in your own app!

Remember, identifying workflows doesn't inherently do anything for us - we still have to write the actual code to implement them. But these patterns have proven successful for many engineers, so they're worth understanding and applying to your own projects.

---

### レッスン 77: Parallelization workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287804>  

Open in Claude
0 seconds of 3 minutes, 44 secondsVolume 90%

When building AI applications, you'll often encounter tasks that seem simple on the surface but become complex when you try to implement them effectively. Let's explore a powerful pattern called parallelization workflows that can help you break down complex tasks into manageable, focused pieces.

The Problem with Complex Single Prompts

Imagine you're building a material designer application where users upload images of parts and receive recommendations for the best material to use. Your first instinct might be to send the image to Claude with a simple prompt asking it to choose between metal, polymer, ceramic, composite, elastomer, or wood.

While this approach might work, you're asking Claude to do a lot of heavy lifting in a single request. Without specific criteria for each material type, the results won't be as reliable as they could be.

You might think to improve this by adding detailed criteria for each material into one massive prompt. But this creates a new problem - Claude has to juggle all these different considerations simultaneously, which can lead to confusion and suboptimal results.

A Better Approach: Parallelization

Instead of cramming everything into one request, you can split the task into multiple parallel requests. Each request focuses on evaluating the part for a single material type with specialized criteria.

Here's how it works:

Send the same image to Claude multiple times simultaneously
Each request includes specialized criteria for one material (metal criteria, polymer criteria, ceramic criteria, etc.)
Claude evaluates the part's suitability for each material independently
Collect all the analysis results and feed them into a final aggregation step

The final step sends all the individual analysis results back to Claude with a request to compare them and make a final material recommendation.

How Parallelization Workflows Work

The parallelization pattern follows a simple structure:

Split a single task into multiple sub-tasks - Break down the complex decision into focused, specialized evaluations
Run the sub-tasks in parallel - Execute all evaluations simultaneously for faster processing
Aggregate the results together - Combine the specialized analyses into a final decision
The parallelized sub-tasks don't need to be identical - Each can have a specialized prompt, set of tools, or evaluation criteria
Benefits of This Approach

Parallelization workflows offer several key advantages:

Focused attention: Claude can concentrate on one specific aspect at a time rather than trying to balance multiple competing considerations simultaneously. This leads to more thorough and accurate analysis for each material type.

Easier optimization: You can improve and test the prompts for each material evaluation independently. If your metal analysis isn't working well, you can refine just that prompt without affecting the others.

Better scalability: Adding new materials to evaluate is straightforward - just add another parallel request. You don't need to rewrite existing prompts or worry about how the new criteria might interfere with existing ones.

Improved reliability: By breaking down the complex task, you reduce the cognitive load on the AI model and get more consistent, reliable results.

When to Use Parallelization

This pattern works well when you have a complex decision that can be broken down into independent evaluations. Look for situations where you're asking an AI to consider multiple criteria, compare several options, or make decisions that involve different domains of expertise.

The key is identifying tasks that can be meaningfully separated - each parallel sub-task should be able to operate independently and contribute a distinct piece of analysis to the final decision.

---

### レッスン 78: Chaining workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287800>  

Open in Claude

Chaining workflows might seem obvious at first, but they're actually one of the most useful patterns you'll encounter when working with Claude. This approach becomes especially valuable when you're dealing with complex tasks or long prompts that Claude struggles to handle consistently.

What is Workflow Chaining?

A chaining workflow breaks down a large, complex task into smaller, sequential subtasks. Instead of asking Claude to do everything at once, you split the work into focused steps that build on each other.

Here's a practical example: imagine you're building a social media marketing tool that creates and posts videos automatically. Rather than asking Claude to handle everything in one massive prompt, you could break it down like this:

Find related trending topics on Twitter
Select the most interesting topic (using Claude)
Research the topic (using Claude)
Write a script for a short format video (using Claude)
Use an AI avatar and text-to-speech to create a video
Post the video to social media
Why Chain Instead of One Big Prompt?

You might wonder why not just combine all the Claude tasks into a single prompt. The key benefit is focus - when you give Claude one specific task at a time, it can concentrate on doing that task well rather than juggling multiple requirements simultaneously.

The chaining approach offers several advantages:

Split large tasks into smaller, non-parallelizable subtasks
Optionally do non-LLM processing between each task
Keep Claude focused on one aspect of the overall task
The Long Prompt Problem

Here's where chaining becomes really valuable. You'll often encounter situations where you need Claude to write content with many specific constraints. Let's say you want Claude to write a technical article, and you specify that it should:

Not mention that it's written by an AI
Avoid using emojis
Skip clichéd or overly casual language
Write in a professional, technical tone

Even with all these constraints clearly stated, Claude might still produce content that violates some of your rules. You might get back an article that still uses emojis, mentions AI authorship, or sounds unprofessional.

The Chaining Solution

Instead of fighting with one massive prompt, use a two-step chaining approach:

Step 1: Send your initial prompt and accept that the first result might not be perfect. Claude will generate an article, but it might violate some of your constraints.

Step 2: Make a follow-up request that focuses specifically on fixing the issues. Provide the article Claude just wrote and give it targeted revision instructions:

Revise the article provided below. Follow these steps to rewrite the article: 1. Identify any location where the text identifies the author as an AI and remove them 2. Find and remove all emojis 3. Locate any cringey writing and replace it with text that would be written by a technical writer

This approach works because Claude can focus entirely on the revision task rather than trying to balance content creation with constraint adherence.

When to Use Chaining

Chaining workflows are particularly useful when:

You have complex tasks with multiple requirements
Claude consistently ignores some constraints in long prompts
You need to process or validate outputs between steps
You want to keep each interaction focused and manageable

While chaining might seem like extra work, it often produces better results than trying to cram everything into a single prompt. The key is recognizing when a task is complex enough to benefit from being broken down into focused, sequential steps.

---

### レッスン 79: Routing workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287801>  

Open in Claude

Routing workflows solve a common problem in AI applications: different types of user requests need different handling approaches. Instead of using a one-size-fits-all prompt, you can categorize incoming requests and route them to specialized processing pipelines.

The Problem with Generic Prompts

Consider a social media marketing tool that generates video scripts from user topics. A user might enter "programming" or "surfing" as their topic, but these should produce very different types of content:

Programming topics call for educational content with clear explanations and definitions. Surfing topics work better with entertainment-focused scripts that emphasize excitement and visual appeal. A single generic prompt can't handle both effectively.

Setting Up Content Categories

The first step is defining the different types of content your application might need to generate. You might categorize requests into genres like:

Entertainment - High-energy, culturally relevant content with trendy language
Educational - Clear, engaging explanations with relatable examples
Comedy - Sharp, unexpected content with clever observations and timing
Personal vlog - Authentic, intimate content with conversational storytelling
Reviews - Decisive, experience-based content highlighting strengths and weaknesses
Storytelling - Immersive content using vivid details and emotional connection

Each category gets its own specialized prompt template. For example, the educational prompt might ask Claude to "develop a clear, engaging script that transforms complex information into digestible insights using relatable examples and thought-provoking questions."

How Routing Works in Practice

The routing process happens in two steps:

Categorization - Send the user's topic to Claude with a request to categorize it into one of your predefined genres
Specialized Processing - Use the category result to select the appropriate prompt template and generate content

For example, if a user enters "Python functions" as their topic, you'd first ask Claude to categorize it:

Categorize the topic of a video into one of the listed categories:
<topic>Python functions</topic>

<categories>
- Educational
- Entertainment
- Comedy
- Personal vlog
- Reviews
- Storytelling
</categories>

Claude responds with "Educational", so you then use the educational prompt template to generate the actual script content.

Routing Workflow Architecture

A routing workflow follows this pattern:

User input goes to a router component first
The router categorizes the request using an initial Claude call
Based on the category, the input gets forwarded to one specific processing pipeline
Each pipeline can have its own workflow, prompts, or tools optimized for that category

The key insight is that user input only goes to one specialized pipeline, not all of them. This allows each pipeline to be highly optimized for its specific use case.

When to Use Routing

Routing workflows work well when:

Your application handles diverse types of requests that need different approaches
You can clearly define categories that cover your use cases
The categorization step can be handled reliably by Claude
The performance benefit of specialized processing outweighs the overhead of the routing step

This pattern is especially valuable for customer service bots, content generation tools, and any application where the "right" response depends heavily on understanding the type of request being made.

---

### レッスン 80: Agents and tools

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287803>  

Open in Claude

Agents represent a shift from the structured workflows we've been working with. While workflows are perfect when you know the exact steps needed to complete a task, agents shine when you're not sure what those steps should be. Instead of defining a rigid sequence, you give Claude a goal and a set of tools, then let it figure out how to combine those tools to achieve the objective.

This flexibility makes agents attractive for building applications that need to handle varied, unpredictable tasks. You can create an agent once, ensure it works reasonably well, and then deploy it to solve a wide range of problems. However, this flexibility comes with trade-offs in reliability and cost that we'll explore later.

How Tools Make the Agent

The real power of agents lies in their ability to combine simple tools in unexpected ways. Consider a basic set of datetime tools:

get_current_datetime - Gets the current date and time
add_duration_to_datetime - Adds time to a given date
set_reminder - Creates a reminder for a specific time

These tools seem simple individually, but Claude can chain them together to handle surprisingly complex requests:

For "What's the time?", Claude simply calls get_current_datetime. But for "What day of the week is it in 11 days?", it chains get_current_datetime followed by add_duration_to_datetime. For setting a gym reminder next Wednesday, it might use all three tools in sequence.

Claude can even recognize when it needs more information. If you ask "When does my 90-day warranty expire?", it knows to ask when you purchased the item before calculating the expiration date.

Tools Should Be Abstract

The key insight for building effective agents is providing reasonably abstract tools rather than hyper-specialized ones. Claude Code demonstrates this principle perfectly.

Claude Code has access to generic, flexible tools like:

bash - Run any command
read - Read any file
write - Create any file
edit - Modify files
glob - Find files
grep - Search file contents

It notably doesn't have specialized tools like "refactor code" or "install dependencies." Instead, Claude figures out how to use the basic tools to accomplish these complex tasks. This abstraction allows it to handle countless programming scenarios that the developers never explicitly planned for.

Best Practice: Combinable Tools

When designing agents, provide tools that Claude can combine in creative ways. For example, a social media video agent might include:

bash - Access to FFMPEG for video processing
generate_image - Create images from prompts
text_to_speech - Convert text to audio
post_media - Upload content to social platforms

This tool set enables both simple workflows (create and post a video) and more interactive experiences where the agent might generate a sample image first, get user approval, then proceed with video creation.

The agent can adapt its approach based on user feedback and preferences, something that would be difficult to achieve with a rigid workflow. This flexibility is what makes agents powerful for building dynamic, user-responsive applications.

---

### レッスン 81: Environment inspection

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287798>  

Open in Claude

When building AI agents, one crucial concept often gets overlooked: environment inspection. Claude operates blindly - it needs to be able to observe and understand the results of its actions to work effectively.

Why Environment Inspection Matters

Think about how Claude works with computer use. Every time Claude performs an action like typing text or clicking a button, it immediately receives a screenshot to understand what happened. This isn't just a nice-to-have feature - it's essential.

From Claude's perspective, clicking a button could navigate to a new page, open a menu, or trigger any number of changes. Without being able to see the results, Claude has no way to understand whether its action succeeded or what the new state of the environment looks like.

Reading Before Writing

This same principle applies to file operations. Before Claude can modify any file, it needs to understand the current contents. This might seem obvious, but it's a pattern you should always follow when building agents.

In the example above, when asked to add a new route to a Python file, Claude first reads the existing code to understand the current structure. Only then can it safely make the requested changes without breaking existing functionality.

System Prompts for Environment Inspection

You can guide Claude to inspect its environment through system prompts. For complex tasks like video generation, this becomes especially important.

Consider a video creation agent that needs to:

Generate video content using tools like FFmpeg
Verify that audio dialogue is placed correctly
Check that visual elements appear as expected

You might include system prompt instructions like:

Use the bash tool to run whisper.cpp and generate caption files with timestamps to verify dialogue placement
Use FFmpeg to extract screenshots from the video at regular intervals to visually inspect the output
Compare the generated content against the original requirements
Benefits of Environment Inspection

When Claude can inspect its environment, several things improve:

Better progress tracking - Claude can gauge how close it is to completing a task
Error handling - Unexpected results can be detected and corrected
Quality assurance - Output can be verified before considering a task complete
Adaptive behavior - Claude can adjust its approach based on what it observes
Practical Implementation

When designing your own agents, always ask: "How will Claude know if this action worked?" Whether you're working with files, APIs, or user interfaces, provide tools and instructions that let Claude observe the results of its actions.

This might mean:

Reading file contents before modifications
Taking screenshots after UI interactions
Checking API responses for expected data
Validating generated content against requirements

Environment inspection transforms Claude from a blind executor of commands into an agent that can truly understand and adapt to its working environment.

---

### レッスン 82: Workflows vs agents

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287794>  

Open in Claude

When building AI-powered applications, you'll often need to choose between two different architectural approaches: workflows and agents. Each has distinct advantages and trade-offs that make them suitable for different scenarios.

What Are Workflows?

Workflows are a predefined series of calls to Claude designed to solve a known problem or set of problems. You use workflows when you can picture the flow of steps ahead of time - essentially when you know the exact sequence needed to complete a task.

Think of workflows as breaking down a big task into much smaller, more specific subtasks. Each step focuses on a single area, which allows Claude to work more precisely.

What Are Agents?

With agents, Claude gets a set of basic tools and is expected to formulate a plan to use these tools to complete a task. Unlike workflows, you don't know exactly what tasks will be provided, so the system needs to be more adaptive.

Agents can creatively figure out how to handle a wide variety of challenges by combining tools in unexpected ways.

Benefits of Workflows
Claude can focus on one subtask at a time, generally leading to higher accuracy
Far easier to evaluate and test, since you know each exact step
More predictable and reliable execution
Better suited for solving specific, well-defined problems
Benefits of Agents
Allow for more flexible user experience
Far more flexible task completion - Claude can combine tools in unexpected ways to complete a wide variety of tasks
Can handle novel situations that weren't anticipated during development
Can ask users for additional input when needed
Downsides of Workflows
Far less flexible - dedicated to solving specific types of tasks
Generally more constrained user experience - you need to know the exact inputs to the flow
Require more upfront planning and design work
Downsides of Agents
Lower successful task completion rate compared to workflows
More challenging to instrument, test, and evaluate since you often don't know what series of steps an agent will execute
Less predictable behavior
When to Use Each Approach

Your primary goal as an engineer is to solve problems reliably. Users probably don't care that you've built a fancy agent - they want a product that works consistently.

The general recommendation is to always focus on implementing workflows where possible, and only resort to agents when they are truly required. Workflows provide the reliability and predictability that most production applications need, while agents offer flexibility for scenarios where the exact requirements can't be predetermined.

Consider workflows when you have well-defined processes and agents when you need to handle unpredictable, varied user requests that require creative problem-solving.

---

### レッスン 83: Quiz on Agents and Workflows

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/289130>  

Open in Claude
Loading...

---

### レッスン 84: Final Assessment

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/290899>  

Open in Claude
Loading...

---

### レッスン 85: Course Wrap Up

**URL:** <https://anthropic.skilljar.com/claude-with-the-anthropic-api/287802>  

Open in Claude

---
