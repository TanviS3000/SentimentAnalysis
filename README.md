# SentimentAnalysis

## Introduction:
The Social Media Analytics Tool is a user-friendly GUI application designed to perform sentiment analysis on social media posts using the `TextBlob` library. Users can upload a CSV file containing social media captions, and the tool will classify them as Positive, Negative, or Neutral based on sentiment scores.

## Features:
1. **Easy Upload**: A button to browse and upload a CSV file.
2. **Sentiment Analysis**: Analyzes the sentiment of each caption in the CSV and classifies it as Positive, Negative, or Neutral.
3. **Results Display**: Shows the number of captions under each sentiment category in the output box.

## Prerequisites:

### Software:
1. **Python**: Ensure you have Python installed.

### Python Libraries:
Ensure the following Python libraries are installed:
1. `tkinter` - For the GUI interface.
2. `pandas` - Data manipulation and analysis.
3. `textblob` - Natural language processing tasks.

You can install them using `pip`:

```bash
pip install pandas textblob
```

(Note: `tkinter` is included with most standard Python installations.)

## How to Run:

1. Save the provided Python script to a file, for example, `sentimentAnalysis.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the command:

```bash
python sentimentAnalysis.py
```

## Usage:
1. **Upload CSV**:
    - Click on the "Upload CSV" button.
    - Select your CSV file which should contain at least two columns: 'username' and 'caption'.
    - The application will then display the sentiment counts in the result box.

2. **Expected CSV Format**:
    - Your CSV file should contain at least two columns with the exact names 'username' and 'caption'. 
    - The 'username' column will contain the usernames of the social media accounts.
    - The 'caption' column should contain the captions or posts for sentiment analysis.

## Error Handling:
The tool incorporates robust error handling:
- If the CSV file can't be read or if it doesn't contain the required columns, an error message will be displayed in the result box.
- The tool ensures valid sentiment scores are calculated for each caption.

## Conclusion:
The Social Media Analytics Tool provides a seamless way to perform sentiment analysis on social media posts. With an intuitive GUI, it offers valuable insights into the mood and sentiment of social media content, which can be pivotal for marketers, researchers, and social media enthusiasts.
