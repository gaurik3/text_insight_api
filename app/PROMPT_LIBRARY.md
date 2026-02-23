
#### Model Used

Azure OpenAI
GPT-4o
API Version: 2024-12-01-preview

### Objective

## Summariztion of Context Data
To create concise summary of textual data while reducing verbosity and not ignoring key points.

### Zero Shot Prompt

#### User Prompt Template

1. Summarize the following text:
    {text}
2. Give me the summary for this:
    {text}
3. What do you understand from this paragraph:
    {text}
4. {text}
    Summarize this.

### Few Shot Prompt

#### User Prompt Template

1. Example:
    Text: The buisness incuured a loss of 12% and in the second quarter gained the profits by 30%
    Summary: The company incurred 18% profit.

    Now summarize:
    {text}

##
Zero-Shot relies on instruction clarification.
With few shot, we can specify the output pattern, and make it more consistent structure wise.
If specific length is given it reduces verbosity.
Zero-Shot might bemore verbose, but Few-Shot is more structured.
Both will be factually correct.


## Structured Text Extraction
Extract structured data in valid JSON format from unstructured text.

### Zero Shot Prompt

#### User Prompt Template

1. Extract name, date, and AccNo. from the following text:
    {text}
2. Convert this text into JSON format:
    {text}
3. Convert this text into stuctural format:
    {text}

### Few Shot Prompt

#### User Prompt Template

Example:
Text: At the first timestamp, 2026-02-23T08:52:44.000909Z, the formation is Shale with no anomalies or events. The rate of penetration is 67, rpm is 143, torque is 3.7, and wobble is 11.
Output:
{
  "Timestamp": "2026-02-23T08:52:44.000909Z",
  "Values": {
    "rop": 67,
    "wob": 11,
    "torque": 3.7,
    "rpm": 143
  },
  "Context": {
    "formation": "Shale",
    "bit_wear": 0
  },
  "Events": {
    "stick_slip": false,
    "motor_stall": false,
    "bit_bounce": false
  },
  "Anomaly": false
}

Now extract:
{text}

##
Zero-shot depends on instruction strength and sometimes may include explanatory text.
Few-Shot improves JSON validity and formatting consistency.
Specifying "valid JSON only" reduces hallucinations.


## Reasoned Decision making task
Provide structured reasoning followed by a clear decision.

### Zero Shot Prompt

#### User Prompt Template

1. Analyze the scenario and recommend action:
    {text}
2. What will be the decision for this scenario:    
    {text}
3. Give the decision for this problem along with the reason.
    {text}

### Few Shot Prompt

#### User Prompt Template

Example:
Scenario: Sales dropped 20%.
Reasoning:
    Market competition increased.
Decision:
    Increase marketing spend.

Now analyze:
{text}

##
Few shot produces clear sepration between reasoning and decision
Zero shot mixes reasoningand decision
Structured format reduces inconsistency.


###### PROMPT ENGINEERING PRINCIPLES
1. Constraints reduce verbosity.
2. Output format specification is more reliable
3. Clear role instructions reduces hallucinations
4. Temperature controlling also changes the evaluation accuracy.

# RECOMENDATIONS ON PROMPTS BSET PRACTCES BASED ON THE COMPARISON REPORT
1. Use examples when format really matters
If you need strict structure (like proper JSON), giving one example in the prompt helps the model follow the format correctly.

2. Clearly tell the model what NOT to do
Instructions like “Return only JSON” or “Do not use markdown” help prevent extra text or formatting mistakes.

3. Temperature mostly changes wording, not decisions
Higher temperature changed phrasing and explanation length, but the final answers stayed the same in your tests.

4. For consistent outputs, combine examples with clear rules
When you used few-shot + strict rules, the responses became very stable and almost identical across temperatures.

5. Show the desired length in your example
Few-shot responses were shorter because the example was short. The model copies the style and length you demonstrate.

6. Use zero-shot if you want slightly more detailed reasoning
Zero-shot answers explored a few more points and gave slightly broader explanations compared to few-shot.

7. Always define the output structure clearly
Writing a clear format like:
Reasoning:
Decision:
helps the model stay organized and avoid extra text.

8. Bigger prompts give better control but cost more tokens
Few-shot prompts used more tokens and sometimes more time, but the results were more reliable.

9. Describe the model’s role carefully
Calling it a “structured data transformation engine” made it behave more like a strict parser instead of a summarizer.

10. Clear constraints reduce creativity
When you gave strict rules, the model became more predictable and less creative — which is good for structured tasks.