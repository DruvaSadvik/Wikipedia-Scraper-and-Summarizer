# Wikipedia Scraper and Summarizer 📚📝
## Introduction 🌐

This project involves scraping information from Wikipedia and generating summaries of the scraped content. The project is divided into several components, including data scraping, text summarization, quality evaluation, chatbot integration, and dataset creation.


# Project Files 📂

📄 **Alexander.docx** - Extracted from Wikipedia
📄 **Alexander_summarized.docx** - Summarized data from Alexander.docx
📊 **Analysis.ipynb** - Quality Evaluation of Summarized Data
🤖 **ChatBot.py** - Chatbot created with summarized data
📋 **Report - Wikipedia Scraper and Summarizer.docx** - Detailed project report
📄 **Summarization.ipynb** - Summarization of scrapped data
🔍 **Wiki_Scrapper.ipynb** - Wikipedia page scraping
📝 **Creating_dataSet.py** - Python code for creating a dataset of main events
🚀 **end_2_end_pipeline.py** - Start-to-end pipeline for every event
📊 **Important_data.xlsx** - Excel file with important event dataset


### Flow of the Project 🚀

### Flowchart

![image](https://github.com/DruvaSadvik/Wikipedia-Scraper-and-Summarizer/assets/113775020/4ed2ccf4-5659-496c-9d7a-768d1a5b995a)

1. **Scrape Data from Wikipedia:** Use the Beautiful Soup library in Python to scrape text data from a chosen Wikipedia page. This involves making an HTTP request to the Wikipedia page's URL, parsing the HTML content, and extracting the relevant text.

2. **Text Summarization and Document Saving:** Apply a text summarization technique (extractive or abstractive) to condense the content into a concise summary. Save the resulting summary in a document or a file.

3. **Quality Evaluation of Summarized Data:** Assess the quality of the summarized data, evaluating criteria such as readability, coherence, and relevance. Compare the summary to the original text to ensure accuracy and completeness.

4. **Chatbot Creation for Summarization:** Create a chatbot using a natural language processing framework (Vertex AI). Train the chatbot to generate summaries based on user input and enable it to respond to user queries with relevant summaries.

5. **Dataset Creation of Important Events:** From the generated summaries, create a dataset of significant events, facts, or key points. This dataset can be used for further analysis, research, or machine learning model training.

## Report 📊

### Design Decisions 🛠️

#### Choice of Tools and Libraries 🧰

- Used Python for scripting.
- Utilized libraries such as requests, BeautifulSoup, docx, and pandas for web scraping, document creation, and dataset handling.
- Integrated the Vertex AI TextGenerationModel for text summarization.

#### Data Extraction Strategy 📜

- Employed web scraping techniques to retrieve content from the Wikipedia page.
- Identified key HTML tags (e.g., headings and paragraphs) for content extraction.

#### Text Summarization Approach 📃

- Used a language model (Vertex AI's TextGenerationModel) to generate text summaries.
- Created prompts based on extracted content to ensure contextually accurate summaries.

#### Dataset Creation Process 📊

- Defined a list of important keywords for data extraction.
- Extracted content containing these keywords and their corresponding summaries.
- Organized the extracted data into a structured dataset.

#### Chat Bot For Summarized doc 🤖

- Created a chatbot with summarized data, and the bot will provide replies for user prompts.

### Challenges Encountered 🧩

- Language Model Integration: Utilizing the language model required familiarity with Google Cloud, which presented challenges, especially without access to a credit card.
- Data Extraction Challenges: Identifying relevant keywords for extraction and handling variations in keyword appearances within the content.
- Chatbot Challenges: Acquiring credits for OpenAI to feed the document to the AI model presented difficulties.

### Error Analysis ❌

- Checked for data discrepancies between the scraped content and generated summaries.
- Evaluated the accuracy and coherence of text summaries generated by the language model.
- Verified the accuracy of keyword-based data extraction from the content.
- Analyzed the consistency of extracted data in the dataset, focusing on variations in content types.
