## 5. Hugging Face Transformers

[Home](README.md)

[Back: OpenCV](04_opencv.md)

In this section, we will learn about the Hugging Face `transformers` library and use it to interact with state-of-the-art pre-trained language models. These models can be used for tasks such as text generation, sentiment analysis, and translation.

### Before We Continue

As of September 16, 2024, Hugging Face Transformers uses NumPy 1.x. If you were following along with this workshop, you've probably installed the latest version of NumPy. If you encounter any issues with the Hugging Face Transformers installation, you may need to downgrade NumPy to version 1.x:

```bash
pip install 'numpy<2'
```

**Note**: This is a great example of when using a virtual environment can be helpful. If you have other projects that require the latest version of NumPy, you can [create a virtual environment](README.md#L29) for this workshop and install the required version of NumPy.

### Installing Hugging Face Transformers

1. **Open your terminal** (or command prompt) and run the following command to install the Hugging Face `transformers` library:

   ```bash
   pip install transformers
   ```

2. **Optional**: If you want to take advantage of GPU acceleration, install PyTorch as well. The Hugging Face `transformers` library can work with both TensorFlow and PyTorch, but PyTorch is commonly used:

   ```bash
   pip install torch
   ```

3. **Verify the installation** by opening a Python interpreter and running:

   ```python
   from transformers import pipeline
   print(pipeline)
   ```

   If there are no errors, the `transformers` library is installed correctly.

### Using a Pretrained Model for Text Generation

One of the powerful features of Hugging Face is that it allows easy access to pre-trained models like GPT, BERT, and others. Let's start by loading a pre-trained model for text generation.

1. **Loading a pre-trained model for text generation**:

   We will use the GPT-2 model, a popular language model, to generate text based on a prompt.

   ```python
   from transformers import pipeline

   # Initialize the text generation pipeline with GPT-2
   text_generator = pipeline("text-generation", model="gpt2")

   # Generate text based on a prompt
   prompt = "In the future, artificial intelligence will"
   generated_text = text_generator(prompt, max_length=50)

   print(generated_text)
   ```

   - **`pipeline()`**: Initializes the pipeline, specifying the task you want (e.g., "text-generation") and the model ("gpt2").
   - **`max_length`**: Specifies the maximum length of the generated text.

2. **Exploring the generated text**:

   The model will generate text based on the prompt. You can try different prompts and see how the model responds!

### Using a Pretrained Model for Sentiment Analysis

Now that we’ve explored text generation, let’s use another powerful feature of Hugging Face: **sentiment analysis**. This task classifies text as positive, negative, or neutral.

1. **Loading a pre-trained sentiment analysis model**:

   ```python
   # Initialize the sentiment analysis pipeline
   sentiment_analyzer = pipeline("sentiment-analysis")

   # Analyze the sentiment of a sentence
   result = sentiment_analyzer("I love learning about machine learning!")
   print(result)
   ```

   - The result will tell you whether the sentence expresses a positive or negative sentiment, along with a confidence score.

2. **Trying different sentences**:

   Try inputting different sentences and observe how the model’s predictions change based on the text.

### Working with Named Entity Recognition (NER)

Named Entity Recognition (NER) is a common NLP task where we identify entities like people, organizations, and locations within a text. Let's explore this using Hugging Face.

1. **Loading a pre-trained model for NER**:

   ```python
   # Initialize the NER pipeline
   ner = pipeline("ner", grouped_entities=True)

   # Analyze named entities in a sentence
   sentence = "Hugging Face Inc. is a company based in New York."
   entities = ner(sentence)
   print(entities)
   ```

   - **`grouped_entities=True`**: This groups together entities of the same type (e.g., multiple words making up one entity like “Hugging Face Inc.”).

   The model will identify entities such as organizations and locations in the text.

### Exploring Other Tasks with Hugging Face

Hugging Face `transformers` supports many other NLP tasks, such as translation, question answering, and summarization. Here's a brief example of how to use a model for **translation**:

1. **Translating English to French**:

   ```python
   # Initialize the translation pipeline
   translator = pipeline("translation_en_to_fr")

   # Translate a sentence from English to French
   translated_text = translator("Machine learning is fascinating.")
   print(translated_text)
   ```

   The model will translate the input sentence into French.

### Fine-Tuning Pretrained Models

While Hugging Face provides access to pre-trained models, you can also fine-tune these models on your own datasets. However, for this workshop, we will focus on using the pre-trained models directly.

### Text Summarization

In this exercise, we will use Hugging Face to summarize long pieces of text.

1. **Summarize a longer text using the pipeline for summarization**:

   ```python
   # Initialize the summarization pipeline
   summarizer = pipeline("summarization")

   # Define a long piece of text
   long_text = """
   Machine learning is a branch of artificial intelligence (AI) focused on building applications
   that learn from data and improve their accuracy over time without being programmed to do so.
   In data-driven industries, machine learning is particularly valuable because it allows companies
   to turn data into actionable insights, automate processes, and improve decision-making.
   """

   # Summarize the long text
   summary = summarizer(long_text, max_length=50, min_length=25, do_sample=False)
   print(summary)
   ```

2. **Experiment with different texts** to see how well the model summarizes information.

### Creating a Question-Answering System

Hugging Face also makes it easy to build a question-answering system. For this exercise, we will use a pre-trained model to answer questions based on a given passage.

1. **Answer questions using the pipeline for question answering**:

   ```python
   # Initialize the question-answering pipeline
   qa = pipeline("question-answering")

   # Define a context and a question
   context = "Machine learning is a branch of AI that focuses on building models that learn from data."
   question = "What does machine learning focus on?"

   # Get the answer
   answer = qa(question=question, context=context)
   print(answer)
   ```

2. **Try asking different questions** based on the same or different contexts.

### Open source models

Here is a list of some popular open-source models you can use with transformers, along with a brief explanation of what they can be used for:

#### 1. **GPT-Neo (EleutherAI)**

- **Task**: Text Generation
- **Use Case**: GPT-Neo is an open-source alternative to OpenAI's GPT-3. It is well-suited for tasks that involve generating human-like text from a given prompt.
- **Example**: Create AI-generated text for creative writing or generate dialogues for a chatbot.

```python
from transformers import pipeline
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
prompt = "The future of technology is"
generated_text = generator(prompt, max_length=50)
print(generated_text)
```

#### 2. **BERT (Google)**

- **Task**: Text Classification, Named Entity Recognition (NER), Question-Answering
- **Use Case**: BERT is ideal for understanding the context of text. It can be used for sentiment analysis, recognizing entities in text (like names, places), and answering questions based on a passage.
- **Example**: Use BERT for customer feedback sentiment analysis.

```python
sentiment_analyzer = pipeline("sentiment-analysis")
result = sentiment_analyzer("I love working with data!")
print(result)
```

#### 3. **BLOOM (BigScience)**

- **Task**: Multilingual Text Generation
- **Use Case**: BLOOM is a powerful model capable of generating text in multiple languages. It is useful for creating multilingual content, chatbots, or summarizing texts in different languages.
- **Example**: Generate French or Spanish text from an English prompt.

```python
from transformers import pipeline
bloom_generator = pipeline("text-generation", model="bigscience/bloom-560m")
prompt = "La technologie de l'intelligence artificielle"
generated_text = bloom_generator(prompt, max_length=50)
print(generated_text)
```

#### 4. **DistilBERT (Hugging Face)**

- **Task**: Text Classification, Question Answering
- **Use Case**: DistilBERT is a smaller, faster version of BERT that is optimized for performance. It is perfect for tasks like text classification and question-answering where speed is important.
- **Example**: Build a lightweight FAQ answering system for customer support.

```python
question_answerer = pipeline("question-answering")
context = "Artificial Intelligence is revolutionizing many industries."
question = "What is AI revolutionizing?"
answer = question_answerer(question=question, context=context)
print(answer)
```

#### 5. **ResNet (PyTorch)**

- **Task**: Image Classification
- **Use Case**: ResNet is a popular model for classifying images into different categories. It is commonly used in applications such as facial recognition or identifying objects in photographs.
- **Example**: Build an image classification tool that identifies everyday objects in pictures.

#### 6. **YOLOv5 (Ultralytics)**

- **Task**: Object Detection
- **Use Case**: YOLOv5 is known for fast and accurate real-time object detection. It can detect multiple objects in images or videos, making it useful for applications like security systems or automated quality control.
- **Example**: Detect objects like cars, people, or animals in real-time from a video feed.

```python
from ultralytics import YOLO
model = YOLO('yolov5s')
results = model("sample_image.jpg")
results.show()
```

#### 7. **CLIP (OpenAI)**

- **Task**: Image-Text Matching
- **Use Case**: CLIP is a model that can understand images and their associated text. It's great for building systems that link images with descriptions, such as search engines or automated captioning systems.
- **Example**: Search for images using text descriptions.

In this section, we installed the Hugging Face `transformers` library and explored various NLP tasks like text generation, sentiment analysis, named entity recognition, translation, and more. Hugging Face provides a simple interface for working with pre-trained models, making it an excellent tool for NLP tasks and any machine learning project.

[Next: Jupyter Notebooks](06_jupyter_notebooks.md)
