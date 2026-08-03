<!-- markdownlint-disable -->

# Claude Platform 101

**URL:** <https://anthropic.skilljar.com/claude-platform-101>  
**所要時間:** 未記載  
**対象ドメイン:** D1, D4, D5  
**フェーズ:** API・開発基盤  

---

## カリキュラム

### レッスン 01: What is the Claude Developer Platform?

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486250>  

The Claude Developer Platform is Anthropic's infrastructure for building with Claude programmatically. Instead of chatting with Claude in a browser, you send structured requests from your code and get structured responses back — with control over every detail: which model to use, how many tokens to spend, what tools Claude can use, and what system instructions it follows.

Concretely, the platform is made up of a few pieces:

A REST API you can call from any language
SDKs for different programming languages
Command line interfaces
A console where you manage API keys, monitor usage, deploy managed agents, and test prompts
The three layers of the platform

A useful way to picture the platform is as three layers stacked on top of each other.

Primitives — the API building blocks tuned to Claude. This is the Messages API, tool use, files, web search, code execution, MCP servers, and skills. These are the pieces you actually call from your code.
Infrastructure — what you need to build and scale agentic systems past a prototype. Managed agents, retries, queues, observability — the plumbing that keeps things running when one Claude call becomes a thousand.
Controls — the tools for running those systems in production, like dashboards and evals. These are the dials your team uses once it's live.

The shorthand: build with primitives, scale on infrastructure, run with control.

You can see this structure reflected in the Claude Console itself — it's where the infrastructure and control layers live, with sections for building, managing agents, and analytics.

A real example: drafting help desk replies

Say you manage a basic help desk app, and you've been asked to add a feature: draft a reply based on the contents of a ticket, following your team's tone and guidelines. You want to wire this up to a button in the UI.

This is a perfect use case for the Messages API. The flow looks like this:

Define a client
Retrieve the ticket the chat refers to
Call messages.create
Return the response to the button to render
client = anthropic.Anthropic()

response = client.messages.create(
model="claude-haiku-4-5",   # Haiku: a good fit for a simple drafting task
max_tokens=1024,
system=TONE_AND_GUIDELINES,
messages=[
{"role": "user", "content": ticket_content}
],
)

draft = response.content

Each parameter does a specific job:

model — which model handles the request. Here that's Haiku, since drafting a reply is a simple task.
max_tokens — caps how long Claude's response can be.
system — the system prompt, where you define the role Claude plays. The relevant tone and guidelines go here.
messages — an array of objects. The user role tells Claude this is user input; the ticket content goes there.

Then you retrieve the response and return it to the button to render. Done.

From "ask Claude a question" to "Claude is part of my product"

Notice what happened in that example: you're not building a chatbot from scratch. You're adding Claude into a product that already exists, and the API is how you wire it in.

That's the core idea. The Claude Platform is your API-level access to Claude's models, tools, and infrastructure. It's how you go from ask Claude a question to Claude is part of my product.

And when your product needs agents, the platform doesn't just hand you the model. With managed agents, it runs them for you.

Recap
The Claude Developer Platform is Anthropic's infrastructure for building with Claude programmatically: a REST API, SDKs, CLIs, and a console for keys, usage, managed agents, and prompt testing.
Think of it as three layers: primitives (Messages API, tool use, files, web search, code execution, MCP servers, skills), infrastructure (managed agents, retries, queues, observability), and controls (dashboards, evals).
The shorthand: build with primitives, scale on infrastructure, run with control.
A single messages.create call gives you full control over the model, response length, system prompt, and user input — enough to wire Claude into an existing feature like drafting help desk replies.
The platform takes you from asking Claude questions to making Claude part of your product — and with managed agents, it can run your agents for you.

---

### レッスン 02: Your first API call

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486251>  

Saying hi to Claude might warm your heart, but it's not really useful. In this lesson we'll send Claude something real and get structured insight back — in just under 20 lines of code.

Get set up

First, grab an API key from platform.claude.com. You'll need to purchase some credits beforehand.

Take the API key and store it in a .env.local file so it stays out of your version control. Hardcoding keys in source files is how they end up leaked on GitHub — keep them in environment files instead.

Next, install the SDK:

npm install @anthropic-ai/sdk
The anatomy of a request

Every API call goes through the messages.create function. You specify three things:

A model — which Claude model handles the request
A max tokens limit — a cap on how long the response can be
A list of messages — objects with either user or assistant roles, structured similarly to how you'd have a conversation with Claude elsewhere

Here's what that looks like in its most basic form:

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const msg = await client.messages.create({
model: "claude-opus-4-7",
max_tokens: 1024,
messages: [{
role: "user",
content: "Hello, Claude",
}],
});

A real example: reviewing buggy code

Let's give Claude something a little more interesting than "hello." We'll point it at some buggy code and ask for a review. Here's the whole thing — one file, about 20 lines of code:

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const buggyCode = `
function add(a, b) {
return a - b;
}
`;

const response = await client.messages.create({
model: "claude-opus-4-8",
max_tokens: 1024,
system: "You are a terse senior code reviewer. Give feedback in one paragraph.",
messages: [
{ role: "user", content: `Review this code:\n${buggyCode}` },
],
});

for (const block of response.content) {
if (block.type === "text") {
console.log(block.text);
}
}

Two things to notice here:

The system prompt is where you shape the persona. I want a terse senior reviewer, not a chatty one — so I just say that.
The message.content in the response is an array of blocks, not a string. For a basic text reply there's usually just one block of type text, but Claude can return multiple blocks — text, tool calls, thinking — so we always loop and check the type.

Run it, and Claude spots that add is subtracting and tells you in one paragraph. That's it. That's the whole API call.

From script to product

In a real product, this same messages.create shape is the engine behind something like a summarize endpoint. Pull a meeting transcript out of the database, hand it to Claude with a system prompt that says "extract insights and risks," save the result back on the row, and return it to the UI. It's the same call — just wrapped in a route handler.

Recap
Your first API call is a messages.create function with a model, a token limit, and messages.
Store your API key in a .env.local file to keep it out of version control.
Add a system prompt to shape Claude's behavior.
The response content is an array of blocks — loop and check each block's type.
From here, everything builds on this pattern.

---

### レッスン 03: Choosing the right model

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486252>  

You're shipping an app with Claude. Which model do you pick? If you default to the smartest one, your API bill will surprise you. Pick the cheapest one, and the output might not hold up. Each model has different trade-offs, and picking the right one affects both quality and cost.

The model tiers

Anthropic currently offers four model tiers, and you choose between them with the model parameter in your API call.

Note that at the time of this course, Claude Fable was not generally available, and are not reflected in the video above. Learn more about Claude Fable and Claude Mythos here.

Claude Fable is our most capable model yet — a new tier that sits above Opus, built for your toughest challenges. It comes at a significantly higher cost than Opus, so reserve it for work where that extra capability is worth paying for.
Claude Opus is the most capable of the three core model families, but also the slowest and highest cost of the three. Use it for deep reasoning, complex analysis, multi-step coding, and nuanced writing.
Claude Haiku is the fastest and lowest cost, optimized for speed and cost efficiency rather than maximum intelligence. Use it for high-volume, low-complexity work like classification, extraction, and routing.
Claude Sonnet sits in the sweet spot: a balanced combination of intelligence, speed, and cost that works well for most production work.
Start with a simple evaluation

Before you write production code, set up a simple evaluation: a set of example inputs that you run through each model and score against what good output means for your use case. You don't need anything fancy — 20 or 30 representative examples from your actual workload is enough to start.

Then work your way up the tiers:

Run your examples through Haiku first. If the quality holds, you're done — and you just saved a lot of money.
If it doesn't, step up to Sonnet.
Only reach for Opus when the task needs it.
Comparing the tiers side by side

Let's see the difference between the tiers, not just talk about it. We'll send the same prompt through all three models and watch the latency and token counts:

models = ["claude-haiku-4-5", "claude-sonnet-4-6", "claude-opus-4-7"]

for model in models:
response = client.messages.create(
model=model,
max_tokens=300,
messages=[{"role": "user", "content": prompt}],
)
print(model, response.usage)

Two things are going on here:

The loop swaps the model field on each request. Same prompt, same max tokens — only the model changes.
response.usage gives you the input and output tokens straight back from the API, which is what your bill is calculated on.

Run it and you'll see three models and three sets of numbers. Opus takes the longest and reads the most polished — but for a two-sentence definition, that polish is wasted. Sonnet tightens the writing up a little. And Haiku comes back, often in under a second, with a very competent two-sentence answer. It's honestly perfect for this kind of scenario.

And that's the whole point: the right model is the cheapest one whose output you'd actually ship. For a definition, Haiku is plenty. For drafting a regulatory response, you'd run the same comparison and probably end up on Opus. The eval is the same shape every single time.

Routing different work to different models

In a real app, you'd route different kinds of work to different models inside the same endpoint. Take an operations dashboard with a document processing route:

Every incoming file gets classified with Haiku.
Client updates get drafted with Sonnet.
Only RFP responses reach for Opus.

One queue, three models, picked per task.

Recap
Anthropic offers three model tiers: Opus for hard problems, Sonnet for daily work, and Haiku for volume.
Set up a simple evaluation — 20 or 30 representative examples from your real workload — before writing production code.
Run the eval from Haiku upward and stop at the cheapest model whose output you'd actually ship.
response.usage reports input and output tokens, which is what your bill is based on.
In production, route different tasks to different models inside the same endpoint instead of picking one model for everything.

---

### レッスン 04: The agent loop explained

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486254>  

You've made API calls, but a single call only returns one response. If you want to automate a workflow, Claude needs to act, look at the result, decide what's next, and keep going. That pattern is what people mean when they talk about agentic workflows.

What an agent actually is

An agent is an autonomous version of Claude, running both sides of the messaging loop without a human in the middle. An agent receives a task, picks a tool, and executes code in a loop until Claude decides the task is done.

The easiest way to implement an agent loop looks like this:

Send a message to Claude with tools available.
Claude responds with either a final answer or a request to use a tool you defined.
Your code executes that tool.
You send the result back to Claude.
Repeat until the stop reason is end_turn.

Think of it as a conversation where the turns alternate: the user kicks things off, the agent calls a tool, the tool returns a result, and the agent keeps going until it has an answer.

A minimal working example

To see this loop run end to end without dragging in a database or a UI, we'll wire up a fake tool called get_weather and ask Claude what to wear in Austin today. Claude has no way to know the weather on its own, so it has to call the tool, read the result, and then give you an answer.

Here's the whole script:

import anthropic

client = anthropic.Anthropic()

# The tools array tells Claude what's available

# a name, a description, and a JSON schema for the inputs

tools = [
{
"name": "get_weather",
"description": "Get the current weather for a city.",
"input_schema": {
"type": "object",
"properties": {
"city": {
"type": "string",
"description": "The city to get weather for",
}
},
"required": ["city"],
},
}
]

# run_tool is just a hardcoded lookup

# In a real app, this would hit your database, an API, whatever

def run_tool(name, tool_input):
if name == "get_weather":
return f"Weather in {tool_input['city']}: 95F, sunny"
raise ValueError(f"Unknown tool: {name}")

messages = [
{"role": "user", "content": "What should I wear in Austin today?"}
]

# The agent loop. Each iteration sends messages to Claude

# and switches on the response's stop reason

while True:
response = client.messages.create(
model="claude-sonnet-4-6",
max_tokens=1024,
tools=tools,
messages=messages,
)

if response.stop_reason == "end_turn":

# Claude is done. Print the final text and break

for block in response.content:
if block.type == "text":
print(block.text)
break

if response.stop_reason == "tool_use":

# Find the tool use blocks in the response and run each one

tool_results = []
for block in response.content:
if block.type == "tool_use":
result = run_tool(block.name, block.input)
tool_results.append(
{
"type": "tool_result",
"tool_use_id": block.id,
"content": result,
}
)

# Push the assistant's response and our tool results

# back into messages, then loop again so Claude can answer

messages.append({"role": "assistant", "content": response.content})
messages.append({"role": "user", "content": tool_results})

Three pieces to notice:

The tools array tells Claude what's available: a name, a description, and a JSON schema for the inputs.
run_tool is just a hardcoded lookup. In a real app, this would hit your database, an API, whatever.
The loop is the agent loop. Each iteration sends the messages to Claude and switches on the response's stop reason. On end_turn, Claude is done — print the final text and break. On tool_use, find the tool use blocks, run each one, push the assistant's response and your tool results back into messages, and loop again so Claude can answer.
Running it

When you run the script, you'll see two turns:

Turn one: the stop reason is tool_use. Claude requests get_weather for Austin, and your code returns the temperature and conditions.
Turn two: the stop reason is end_turn, and Claude tells you to wear something light and breathable.

Two API calls, one tool execution, one final answer. That's the entire loop. Everything you build with the Claude API is going to be similar to this.

The same loop in production

In a real environment, this same loop powers something like an auto-review endpoint: a compliance agent that reads a structural report, looks up the relevant building codes via a tool, and writes risk findings back to the database one by one as it works.

The shape of the loop is identical to what you just ran. The differences are:

Real tools instead of a mock weather loo

---

### レッスン 05: What is tool use?

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486255>  

Your existing workflows rely on a lot of different technologies — project management software, databases, files. Claude can't just check these things itself. Instead, it relies on tools, which give Claude access to external data and actions.

What a tool is

Simply put, a tool is a function you define and expose to Claude. You describe what it does and what inputs it takes, and Claude decides when to call it.

Here's the key thing to internalize: Claude doesn't execute the tool — your code does. The flow looks like this:

Claude requests a tool call.
Your code executes the function.
The result goes back to Claude, and it keeps going.
How tools are defined

Tools are JSON schemas with three parts: a name, a description, and an input schema. You pass them to Claude in the request body as a tools array.

The description is what Claude reads to decide whether to call the tool. If you write a vague description, you get bad tool use. This is the number one reason agents misfire or don't grab the tools that are available to them. Be specific.

Here's what a tool definition looks like:

{
"name": "lookup_building_code",
"description": "Look up a specific building code section by its identifier. Returns the full text of that code section.",
"input_schema": {
"type": "object",
"properties": {
"section": {
"type": "string",
"description": "The building code section to look up"
}
},
"required": ["section"]
}
}

So what happens when we use this? Say we send an agent a compliance report. On the first turn, Claude comes back with stop_reason: "tool_use" — that's our signal. Here's what that response looks like:

Our loop calls lookup_building_code with the parameter Claude requested, then feeds the result back as a tool result — a user message containing a tool_result block tied to the tool call's id:

And Claude keeps going. At that point, we can keep calling tools and returning results to Claude until it has what it needs.

Multiple tools: letting Claude pick

One tool is useful, but the interesting part is giving Claude multiple tools and watching it pick which one to use, in what order.

Picture this scenario: you're packing for a three-day trip to Denver, and you want both today's weather and the forecast for the next few days. So we declare two tools instead of one:

const tools = [
{
name: "get_weather",
description: "Get today's current weather for a city.",
input_schema: {
type: "object",
properties: {
city: { type: "string", description: "The city to check" }
},
required: ["city"]
}
},
{
name: "get_forecast",
description: "Get the weather forecast for the next few days for a city.",
input_schema: {
type: "object",
properties: {
city: { type: "string", description: "The city to check" }
},
required: ["city"]
}
}
];

The loop is identical to the agent loops we've already seen. The only new piece is a runTool function that dispatches on the tool name with a switch statement — this block of code is just where your code actually runs:

function runTool(name, input) {
switch (name) {
case "get_weather":
return getWeather(input.city);
case "get_forecast":
return getForecast(input.city);
}
}

while (true) {
const response = await client.messages.create({
model: "claude-sonnet-4-6",
max_tokens: 1024,
messages,
tools,
});

if (response.stop_reason !== "tool_use") {
// Claude is done — this is the final answer
break;
}

messages.push({ role: "assistant", content: response.content });

const toolResults = response.content
.filter((block) => block.type === "tool_use")
.map((block) => ({
type: "tool_result",
tool_use_id: block.id,
content: runTool(block.name, block.input),
}));

messages.push({ role: "user", content: toolResults });
}

And that's the whole pattern. Want a third tool? Add it to the array, add a case to the switch, and you're done.

Run this, and you'll see Claude call get_weather and then get_forecast — sometimes in the same turn, sometimes one after the other. Then it answers: pack layers, expect snow flurries today, warming through the week.

Now notice how Claude chose. It read the descriptions, mapped your prompt to "today's weather" and "the next few days," and picked the right tool for each. That's why your tool descriptions really matter.

The tool runner: skip the boilerplate

You've probably already spotted two red flags with what we just wrote:

That's a lot of code for two simple lookups.
In a real codebase, you don't want to handwrite JSON schemas for every function you have. It's like writing your code twice.

That's where the tool runner comes in. It ships in the Claude SDK for TypeScript, Python, and Ruby. The runner takes your actual functions, reads the types and docs to build the schema for you, and handles the entire tool

---

### レッスン 06: What is thinking?

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486256>  

Some tasks need more than a quick answer. Claude can work through a problem before responding — a feature called extended thinking. In this lesson, we'll look at what thinking is, how to turn it on, and when it actually helps.

Here's the failure mode we're trying to avoid. Ask a model a multi-step question and have it answer immediately, and it can confidently get it wrong:

What is extended thinking?

Extended thinking lets Claude reason step by step before producing a final response. When it's enabled, Claude generates internal reasoning tokens — often called a chain of thought — and then delivers the answer. The reasoning isn't hidden: you can see it in the response alongside the final text.

Adaptive thinking on Opus 4.7

With Opus 4.7, thinking is adaptive. You don't pick a token budget. You just turn it on, and Claude decides dynamically when to think and how much.

To control how much Claude thinks, use the effort parameter. One gotcha: it goes inside output_config, not next to the thinking block. The levels are:

low
medium
high (the default)
xhigh (extra high)
max
When to use it (and when to skip it)

Extended thinking helps with:

Math and multi-step logic
Code debugging
Regulatory analysis
Anything that involves trade-offs or comparing options

Skip it for simple classification, extraction, or boilerplate. For those tasks it just adds latency and cost without actually improving the results.

Thinking in action

Let's see it work. Here's an agent loop with one weather tool, and we'll ask Claude to plan a road trip out of San Francisco — two stops, weighing weather and drive time. That's a real trade-off, the kind of question where thinking earns its keep.

import anthropic

client = anthropic.Anthropic()

weather_tool = {
"name": "get_weather",
"description": "Get the current weather for a city.",
"input_schema": {
"type": "object",
"properties": {
"city": {"type": "string", "description": "City name"}
},
"required": ["city"],
},
}

response = client.messages.create(
model="claude-opus-4-7",
max_tokens=16000,
thinking={"type": "adaptive"},
output_config={"effort": "high"},  # low | medium | high | xhigh | max
tools=[weather_tool],
messages=[
{
"role": "user",
"content": "Plan a road trip out of San Francisco with two stops, "
"weighing weather and drive time.",
}
],
)

When you run this, the output is more interesting than usual. You'll see thinking blocks where Claude works through the trade-offs, followed by tool calls to check each city, and finally a text block with the actual recommendation.

The reasoning is visible — that's the whole point.

Why this matters in production

In a production app, this is the difference between an agent that finds problems one at a time and an agent that connects them. Take a compliance review app: toggling adaptive thinking on the auto-review call lets the agent reason across report sections — catching things like a wind load spec in section three that conflicts with the material spec elsewhere in the document.

Recap
Extended thinking gives Claude room to reason before it answers, and the reasoning is visible in the response.
With Opus 4.7, turn it on with thinking: {"type": "adaptive"} — no token budget needed; Claude decides when and how much to think.
Dial the depth with the effort parameter inside output_config: low, medium, high (default), xhigh, or max.
Use it for hard, trade-off-heavy problems. Skip it for simple ones — there it just costs latency and tokens.

---

### レッスン 07: Built-in tools

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486258>  

You can build your own custom tools, but some capabilities are common enough that Anthropic ships them pre-built. You don't write the code. You don't host the sandbox. You just declare the tool, and Anthropic runs it.

Server tools: declared by you, run by Anthropic

Anthropic provides server tools that run on their infrastructure. You don't execute these — Anthropic does. That means you don't need an agent loop for these calls. Claude calls the tools on its own, and the result comes back inside the same response.

The main ones are:

Web search — searches the internet and returns results with citations
Code execution — writes and runs Python in a sandbox
Web fetch — retrieves full content from URLs
Two server tools in one file

Let's check out some of the big ones in one file: two messages.create calls, one with web search and one with code execution.

import anthropic

client = anthropic.Anthropic()

# Call 1: web search — Anthropic runs the search server-side

search_response = client.messages.create(
model="claude-opus-4-8",
max_tokens=1024,
tools=[{"type": "web_search_20260209", "name": "web_search"}],
messages=[
{"role": "user", "content": "What is Anthropic's latest model release? Answer in one sentence."}
],
)

for block in search_response.content:
if block.type == "server_tool_use":
print(f"Tool call: {block.name} — {block.input}")
elif block.type == "text":
print(block.text)

# Call 2: code execution — Claude writes and runs Python in a sandbox

code_response = client.messages.create(
model="claude-opus-4-8",
max_tokens=1024,
tools=[{"type": "code_execution_20260120", "name": "code_execution"}],
messages=[
{"role": "user", "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"}
],
)

for block in code_response.content:
if block.type == "server_tool_use":
print(f"Tool call: {block.name} — {block.input}")
elif block.type == "bash_code_execution_tool_result":
print(f"stdout: {block.content.stdout}")
elif block.type == "text":
print(block.text)

Two things to notice:

There's no agent loop here. We don't switch on stop_reason. We don't push tool results back. Anthropic runs the tool server-side, and the response already contains the result.
The response has new block types. A server_tool_use block for the tool call, a code execution tool result block for the output, plus the regular text blocks.
Running it

For web search, you'll see Claude's tool call printed, then a one-sentence answer about the latest model release with the search citations folded in.

For code execution, you'll see the actual Python Claude wrote, the stdout from the sandbox running it, and a final text answer.

We didn't have to spin up a search crawler. We didn't run a Python sandbox. We declared two tools and got both for free.

The other category: client tools

Worth knowing the other category exists. Client tools run where your code runs. They're shipped in the Claude SDK, so you don't have to define the schema yourself. Two examples:

Memory — Claude reads and writes memory across sessions
Bash — a persistent bash shell so Claude can execute commands

They have the same shape as a custom tool, but the SDK gives you the schema and a sensible runner.

Why this matters in production

In a production app, this is the shortest path to features that would otherwise take weeks. Web search can power a fact-check endpoint that verifies every numeric and regulatory claim in a draft against the live web.

One reminder, though: just because something is validated on the internet doesn't mean it's true. Always double-check Claude's work.

Recap
Server tools — web search, code execution, web fetch — are declared in your tools array. Anthropic runs them.
You get the result in the same response, with no agent loop required. Look for server_tool_use and tool result blocks alongside the regular text blocks.
Client tools like memory and bash run where your code runs, but the SDK ships the schema and a runner for you.
The "hosted by Anthropic" idea scales all the way up: managed agents apply it to the entire agent, not just one tool.

---

### レッスン 08: Skills

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486259>  

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. At the core of every Skill is a SKILL.md file — a packaged set of instructions you upload once and then attach to any messages.create call. You're teaching Claude how you do something: your status report format, your review checklist, your release notes. Claude reads the Skill, follows the procedure, and produces output in your shape.

Skills vs. tools

It's worth being clear on the difference, because the two solve different problems:

Tools connect Claude to data and actions. "Look up this code section," "send this email" — Claude calls the tool, and something else runs.
Skills teach Claude a procedure. "Generate the daily status report following this template" — it's a playbook Claude reads and follows, which sometimes means running bundled scripts itself.

A simple way to remember it: tools are about what Claude can do, while Skills are about how you want it done.

One more thing worth knowing: Skills don't load fully into context on startup. Only the name and description load at first. When your agent decides a Skill is relevant, it then loads the full Skill into context. That keeps your context lean even when many Skills are available.

Uploading a Skill

Skills are uploaded once to your workspace, then referenced by ID. You can upload directly on the Claude Platform, or do it programmatically:

skill = client.beta.skills.create(
display_title="Status Report Generator",
files=files_from_dir("status-report-skill"),  # folder containing SKILL.md
)

print(skill.id)  # reference this ID in future requests

For this example, I want a status report generator. All the rules for what makes a good status report — sections, tone, how to summarize, how to handle blockers — live in a Skill packaged ahead of time. The activity log itself is just a string passed in at request time.

Attaching a Skill to a request

Skills attach to a request through the container configuration — a skills array inside the container, where each entry names a skill_id and version. Here's the full call for the status report generator:

response = client.beta.messages.create(
model="claude-sonnet-4-5",
max_tokens=4096,
betas=["skills-2025-10-02", "code-execution-2025-08-25"],
container={
"skills": [
{
"type": "custom",
"skill_id": skill.id,
"version": "latest",
}
]
},
tools=[
{
"type": "code_execution_20250825",
"name": "code_execution",
}
],
messages=[
{
"role": "user",
"content": f"Generate the daily status report from this activity log:\n\n{activity_log}",
}
],
)

A few things worth pointing out:

We're calling client.beta.messages.create, not the standard one, and passing the skills feature via the beta header. As of this video, Skills are still a beta feature.
container.skills is where the Skill attaches. It's a list, so you can layer multiple Skills onto one call.
Code execution is turned on here too. Skills often pair well with code execution, because Skill procedures can do real work — like running scripts in a terminal.
Running it

The output is a status report formatted exactly the way the Skill says to format it. Sections, tone, blocker handling — all of it comes from the SKILL.md file you uploaded. The user prompt is one line; the procedure lives in the Skill.

In a production app, this is how a team standardizes output across an entire feature. With this daily status report endpoint, every PM gets the same structure, the same tone, the same sections, in the same order — without anyone copy-pasting a template into a prompt.

Recap
Skills package your procedures. A SKILL.md file (plus any scripts and resources) teaches Claude how you want something done.
Tools vs. Skills: tools are about what Claude can do; Skills are about how you want it done.
Skills load progressively. Only the name and description load at startup; the full Skill loads into context when the agent decides to use it.
Upload once with client.beta.skills.create, then attach with container.skills on any messages.create call — a list, so you can layer multiple Skills.
Pair with code execution when the Skill's procedure needs to do real work.
Reach for a Skill when the how matters as much as the what.

---

### レッスン 09: MCP

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486260>  

We have tools, skills, and connectors. So why does MCP exist? At first glance it looks like a second API stacked on top of the API. Fair question — and the answer comes down to who maintains the integration code.

The maintenance problem

Say your agent needs to pull tasks from Asana, check a Google Calendar, and search Slack — all in one go. With custom tools, you have to write three integrations. That part is doable. The painful part comes after: you also have to maintain those integrations every time one of those services changes its API, which happens often. Congratulations, you're now maintaining a pile of third-party API wrappers.

MCP shifts that maintenance to the service provider. Asana publishes an MCP server. Slack publishes one. Google publishes one. Each server exposes its own tools — with descriptions, schemas, and authentication — through a standard protocol. When their API changes, they update their server. You change nothing.

Tools vs. skills vs. MCP

These three features do different jobs:

Tools connect Claude to your internal systems — your database, your project tracker, your proprietary APIs. You own the code, so you also own the maintenance.
Skills teach Claude a procedure — your report template, your review checklist. Skills are instructions, not necessarily integrations.
MCP connects Claude to third-party services, where the service provider maintains the integration. You don't write the Asana wrapper — Asana did.

The short version: tools are for your stuff, skills are for your processes, and MCP is for everyone else's stuff.

Connecting to an MCP server

The cleanest way to get a feel for MCP is to point Claude at any MCP server and let it discover what's there. For this example, we'll use the Linear MCP server, with the connection details and auth token stored in a .env file.

Two pieces work together in the request. The mcp_servers key declares the connection — a type, a URL, a name to refer to it by, and optionally an auth token. Then a tool with the type mcp_toolset configures which tools Claude can use from that server. The default is all of them, but if you want to scope it down, this is where you do it.

import os
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
model="claude-opus-4-8",
max_tokens=1000,
messages=[
{"role": "user", "content": "What tools do you have available?"}
],
mcp_servers=[
{
"type": "url",
"url": "https://mcp.linear.app/mcp",
"name": "linear",
"authorization_token": os.environ["LINEAR_MCP_TOKEN"],
}
],
tools=[
{
"type": "mcp_toolset",
"mcp_server_name": "linear",
}
],
betas=["mcp-client-2025-11-20"],
)

print(response)

Notice that we never wrote a single tool schema. Claude introspects the server, gets the list of tools and their schemas back, and picks the right one for the prompt. As of this lesson, the MCP connector is in beta — note the beta header in the request.

Run it, and if your MCP URL points at Linear's MCP endpoint, Claude lists Linear's tools and then calls one. The same works for basically any compliant server. We didn't define a single tool. We didn't write a Linear client. Linear is maintaining that.

Filtering which tools Claude can use

MCP servers often expose many, many tools — and you don't always want Claude using all of them. Maybe you don't want it to have write permissions, or you just don't want all those tool definitions taking up context.

The fix: disable everything by default, then enable only the specific tools you want. Here's that pattern with a Slack MCP server:

tools=[
{
"type": "mcp_toolset",
"mcp_server_name": "slack",
"default_config": {
"enabled": False,
},
"configs": {
"search_messages": {"enabled": True},
"list_channels": {"enabled": True},
},
}
]

Now Claude can search Slack and list channels, but it can't post or delete. This is useful when you trust a service for reads but don't want Claude writing on your behalf by accident.

Recap
MCP exists so you don't have to maintain integrations someone else has already built. The service provider publishes an MCP server and keeps it up to date — you change nothing when their API changes.
Pick the right feature for the job: tools for your data, skills for your process, MCP for third-party services.
Declare the connection in mcp_servers (type, URL, name, optional auth token) and grant access with an mcp_toolset entry in tools. Claude introspects the server and discovers the tools on its own — no schemas to write.
Scope down access by setting default_config: {"enabled": False} and enabling specific tools in configs — handy for keeping a server read-only.
The MCP connector is currently in beta, so include the beta header on your requests.
Visit modelcontextprotocol.io for the li

---

### レッスン 10: Context management

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486261>  

Every request you send Claude has a context window. A million tokens sounds like a lot, but it runs out faster than you think once you're shipping a real agent. That's where context management comes in: it's how you stay inside the window without losing what matters.

What counts as context

Context is everything Claude sees on a given turn:

The system prompt
The message history
Tool definitions and tool results
Attached files and skills
Thinking blocks

It's the input to every single API call. You pay for it on the way in, and you pay for it on the way out. And once the window is full, the request fails.

So the goal isn't to fit everything in. The goal is to fit the right things in.

Anthropic publishes four patterns for managing context in long-running agents. Three are first-class API features, and one is a design pattern.

Pattern 1: Just-in-time context

Don't load everything upfront. Load what the agent needs now, and let it pull more in via tools when it asks.

Think of a compliance review agent. It doesn't get the entire building code book stuffed into its system prompt — it calls a lookup_building_code tool when it needs a specific section. This is the design pattern of the four: nothing special in the API, just a deliberate choice about what you load and when.

Pattern 2: Server-side compaction

When a conversation runs long, Anthropic's server-side compaction summarizes old turns into a single block. You opt in by adding a context_management key to your request, holding an edit with a type:

response = client.messages.create(
model="claude-sonnet-4-5",
max_tokens=1024,
context_management={
"edits": [
{"type": "compact"}
]
},
messages=messages,
)

The API auto-summarizes when the input crosses the trigger threshold. You don't have to track conversation length yourself.

Pattern 3: Prompt caching

Prompt caching lets you mark the stable parts of a request — the system prompt, the tool definitions, a long document — and reuse them across calls at a fraction of the cost.

The math matters more than it looks. If your system prompt is 4,000 tokens and you call it 100 times an hour, caching is the difference between a usable bill and a phone call from finance.

Pattern 4: The memory tool

Some context needs to survive across sessions: user preferences, the agent's running notes, what was decided last week. The recommended primitive for this is the memory tool.

Here's how it works:

Claude reads and writes to a memory directory via tool calls.
You implement the storage backend client-side — a file system, a database, an encrypted store, whatever you want.
Anthropic auto-injects a system instruction telling Claude to check the memory directory before starting work.
Layering the patterns

In a production app, you'll usually layer all four at once. The compliance review agent caches its system prompt and tool definitions, and pulls building code sections in just in time via lookup_building_code.

Each pattern handles a different failure mode: cost, window size, statelessness. Pick the ones that match what's breaking for you.

Recap
Context is everything Claude sees on a turn — and it isn't free or infinite. Once the window fills, the request fails.
Just-in-time context: load what's needed now, let tools pull in the rest. This is the design pattern of the four.
Server-side compaction: add a context_management key, and the API summarizes old turns automatically when input crosses the trigger threshold.
Prompt caching: mark stable parts of the request and reuse them across calls at a fraction of the cost.
The memory tool: Claude reads and writes a memory directory via tool calls; you own the storage backend, so context survives across sessions.
Four patterns, one goal. Wire them up by hand, or use Claude managed agents, which ship with caching and compaction on by default.

---

### レッスン 11: What are managed agents?

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486263>  

Claude Managed Agents is a suite of APIs for building and deploying agents at scale. You define agents with specific tools, personas, and capabilities. You configure sandbox environments with the right packages and network controls. Then you fire off sessions from your own application, and Claude does the work inside an isolated container with full file system access, bash execution, and web search.

The agent loop, hosted for you

Under the hood, this is an agent loop: Claude reasons, calls a tool, reads the result, and repeats until the job is done. If you've built agents before, you've probably written this kind of loop yourself. Managed agents takes that same loop and hosts it on Anthropic's infrastructure, so you don't have to run it.

You'll find Managed Agents in its own section of the Claude Console.

The best way to understand what this unlocks is to walk through a few examples.

Example 1: A Kanban board that does the work

Picture a Kanban board sitting on top of managed agents. You drag a ticket into the "in progress" column, and that fires off a session automatically. Say the ticket reads "optimize website performance." Here's what happens:

Your back end creates a session.
The session points to an environment you configured with Lighthouse and Puppeteer pre-installed.
Your GitHub repo gets mounted into the container.

Now Claude has the codebase, the tools, and a rubric that defines what done looks like:

Lighthouse score above 90
No render-blocking resources
All images lazy loaded

Claude runs the audit, then starts compressing images, inlining CSS, and deferring scripts. Every tool call streams back to the board in real time through the event stream, so you can watch the work as it happens.

Then the rubric kicks in. A separate grader, running in its own context window, evaluates the output against your criteria. Claude reads that feedback, goes back in, fixes what it missed, and resubmits. In the demo, that loop takes the Lighthouse score up to 96.

One more thing: you can drag a second ticket over while the first is still running. Two sessions, two containers, two separate tasks running in parallel.

Example 2: A recurring research agent with memory

Here's a different shape of agent: one whose job is to track prices and plan changes across every SaaS tool your company pays for, with a report ready before stand-up.

On each run, the agent:

Searches the web for current pricing pages, checks for plan tier changes, and flags new features that might affect your contracts
Runs a cost analysis in Python inside the sandbox
Uses an Excel spreadsheet skill and writes an executive summary
Posts a link to Slack and creates a review task in Asana, both through MCP servers

The agent also reads from and writes to a memory store. Before it starts, it checks what it found last week. After it finishes, it stores what changed. So next Monday's report can say "compute costs are 15% lower since last week" instead of listing the same static pricing data every time.

Example 3: Incident response with multiple agents

Now imagine an alert fires from your monitoring stack. A custom tool on your back end receives the alert payload and sends it into a new session as a tool result. This session uses multi-agent coordination:

A coordinator agent receives the alert and delegates to three specialists.
Each specialist runs in its own context window on the same shared file system.
The specialists report back, and the coordinator synthesizes their findings into a single incident summary.

Before the summary goes to Slack, the permissions policy fires. You see the draft on screen, approve it, and the message goes out. Sensitive actions wait for a human.

Memory ties all of this together. The coordinator checks past incidents in the memory store and flags a pattern: "this looks like the DNS resolution issue from two weeks ago that was caused by a misconfigured TTL." The next time a similar alert fires, the agent starts with that context instead of diagnosing from scratch.

The building blocks

Across these examples, managed agents gives developers the tools to deliver a fully managed, stateful agent experience built on:

Agents — definitions with specific tools, personas, and capabilities
Sessions — individual runs you fire off from your own application
Environments — sandboxes with the right packages and network controls
Tools — including custom tools on your back end
MCP — connections to services like Slack and Asana
Memory — a store the agent reads before starting and writes to when done
Outcomes — rubrics and graders that define and check what done looks like
Multi-agent coordination — coordinators delegating to specialists
Recap
Claude Managed Agents is a suite of APIs for building and deploying agents at scale, hosted on Anthropic's infrastructure.
It runs the familiar agent loop — reason, call a tool, read the result, repeat — inside an isolated container with file system access, b

---

### レッスン 12: Building your first managed agent

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486264>  

If you've built an agent loop by hand, you know the drill: while loops, stop reason switches, tool executions. That works, and for a lot of features it's actually the right shape. But sometimes that loop is going to run for a very long time — minutes, maybe even hours — across many tools, with state to keep, files to write, and work to resume after a network hiccup. At that point, you don't want to run the loop on your server. You want to delegate it. That's what managed agents are.

What is a managed agent?

A managed agent is an agent loop that runs on Anthropic's infrastructure instead of yours. You describe the agent once, you give it an environment to work in, and you start a session. Anthropic runs the loop, and you just stream the events back out as it works.

Managed agents are enabled by default for every API account — no special access needed.

The four primitives

There are four primitives, and they come in order:

Agent — the persona: model, system prompt, and toolset. This is reusable across many runs.
Environment — where the agent runs: cloud or local, networking config, and so on.
Session — a single run of an agent inside a certain environment. The session is the unit of work.
Events — the messages flowing in and out: the agent's actions, the tool calls, the results, the replies.

Here's how the pieces fit together: your app talks to a session, the session drives work inside the environment, and everything that happens flows back out through the event stream:

Notice the shift here: you're not running a while loop. You're sending events and reading events.

The smallest possible managed agent

Let's build the smallest managed agent that does something useful: create a file in the temp drive, count its lines, and report back.

For tools, we'll use the agent toolset — Anthropic's bundled file, bash, and web tools. They work fine for this task, so we don't have to define any tools ourselves.

Step 1: Create the agent

First, we create the agent. Note the agent toolset defined right in the tools array — that's the bundled toolset:

import anthropic

client = anthropic.Anthropic()

agent = client.beta.agents.create(
name="Line Counter",
model="claude-opus-4-8",
system="You are a helpful agent that completes small file tasks.",
tools=[
{"type": "agent_toolset_20260401", "default_config": {"enabled": True}}
],
)

Remember: the agent is reusable. Create it once and run it across many sessions.

Step 2: Create the environment

Next, the environment. This spins up the container template — cloud, with unrestricted networking. This is the sandbox where the file actually gets written:

environment = client.beta.environments.create(
name="line-counter-env",
config={
"type": "cloud",
"networking": {"type": "unrestricted"},
},
)

Step 3: Create the session

Then we create a session with our agent and environment, plus an optional title. The session is the unit of work:

session = client.beta.sessions.create(
agent=agent.id,
environment_id=environment.id,
title="Count lines demo",
)

Step 4: Open the stream, then send the kickoff

Now we open the event stream — and notice that we do this first. The stream only delivers events that occur after it opens, so always open it before sending the kickoff message. Then we send the user message into the live stream:

with client.beta.sessions.events.stream(session_id=session.id) as stream:

# Stream is open — now send the kickoff

client.beta.sessions.events.send(
session_id=session.id,
events=[
{
"type": "user.message",
"content": [
{
"type": "text",
"text": "Create a file in the temp directory, "
"count its lines, and report back.",
}
],
}
],
)

Notice it's events — plural. Events are how everything flows in this API.

Step 5: Consume the stream

Finally, we consume the stream. There are three event types that matter for this demo:

agent.message — Claude's text
agent.tool_use — what tool Claude picked
session.status_idle — the agent is done
for event in stream:
if event.type == "agent.message":
for block in event.content:
if block.type == "text":
print(block.text, end="", flush=True)
elif event.type == "agent.tool_use":
print(f"\n[tool] {event.name}")
elif event.type == "session.status_idle":
print("\n--- Agent done ---")
break

Run it, and the output is the agent reasoning out loud — actual text, the tools it picks, and a final answer. All of it running inside Anthropic's container, not yours:

The trade

Usually with agents, we have our own loop where we have to control everything. With managed agents, you delegate that l

---

### レッスン 13: Building with Claude Code

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486266>  

Writing code that calls the Claude API by hand works fine, but there's an even faster path: have Claude write it for you. In this lesson, we'll use Claude Code to fill in an API integration from a stubbed-out file — using the same primitives you've learned throughout this course.

Starting from a stub

The project is simple: a TypeScript file that gets weather. It contains two stubs:

getWeather — accepts a city and returns the temperature and conditions.
run — a function that should use the tool runner and the Claude TypeScript SDK.

The tool runner is the piece that handles tool calling and the agent loop for you, so you don't have to wire that up manually.

The Claude API skill

Claude Code comes with a built-in skill called Claude API. You can invoke it directly with /claude-api, or Claude Code will invoke it automatically when it detects that you're using the TypeScript SDK.

If you don't see the skill, you can add it from the marketplace:

/plugin marketplace add AnthropicsSkills

Note the s at the end of Anthropics — it's easy to miss.

One prompt, working code

Open the project folder in your terminal and launch Claude Code.

From there, it takes a single prompt. A good prompt does three things:

It names the file you want changed.
It names the pattern you want used.
It names the end state you expect.

Claude Code then fills in getWeather and run against the types, appends a call at the bottom of the file, executes the script, and reports the output. If something errors out, it reads the error message and patches the code in place.

What Claude Code produced

In this run, Claude Code created a Zod tool that parsed the input and returned the output based on the city type. It also created the tool runner and the run function we asked for, and printed the final results of the agent loop.

The pattern to remember

Most of what you write against the Claude API has a familiar shape:

Define a tool.
Hand it to a runner.
Return the result.

You don't need to type that from memory every single time. Instead, stub the file, hand it to Claude Code, and just review the diff.

Recap
Claude Code is an agent that edits files and runs commands inside your terminal.
The built-in Claude API skill loads automatically when Claude Code detects the TypeScript SDK, or you can invoke it with /claude-api.
Give it a prompt that names the file, the pattern, and the end state — it writes the code, runs it, and fixes errors in place.
Claude API code follows a familiar shape: define a tool, hand it to a runner, return the result. Stub it, delegate it, review the diff.

---

### レッスン 14: Claude Platform 101 Quiz

**URL:** <https://anthropic.skilljar.com/claude-platform-101/486268>  

Loading...

---
