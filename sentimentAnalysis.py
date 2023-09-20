import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from textblob import TextBlob


def perform_sentiment_analysis():
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV files", "*.csv")])

    if not file_path:
        return

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        result_text.config(state=NORMAL)
        result_text.insert(INSERT, f"Error: Could not read CSV. {e}\n")
        result_text.config(state=DISABLED)
        return

    if 'username' not in df.columns or 'caption' not in df.columns:
        result_text.config(state=NORMAL)
        result_text.insert(INSERT, "Error: CSV must have 'username' and 'caption' columns.\n")
        result_text.config(state=DISABLED)
        return

    df['Sentiment'] = df['caption'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    df['Sentiment_Category'] = df['Sentiment'].apply(
        lambda x: 'Positive captions' if x > 0 else 'Negative captions' if x < 0 else 'Neutral captions')

    output = df.groupby('Sentiment_Category').size().reset_index(name='Counts')

    result_text.config(state=NORMAL)
    result_text.delete(1.0, END)
    result_text.insert(INSERT, f"Sentiment Counts:\n{output}\n")
    result_text.config(state=DISABLED)


root = Tk()
root.geometry('600x400')
root.title('Social Media Analytics')
root.configure(bg='#0073e6')

frame1 = Frame(root, bg='#0073e6')
frame1.pack(pady=20)

frame2 = Frame(root, bg='#0073e6')
frame2.pack(pady=10)

# Adding components
Label(frame1, text="Upload a social media CSV file:", font=("Arial", 12), bg='#0073e6', fg='white').pack(side=LEFT,
                                                                                                         padx=5)
Button(frame1, text="Upload CSV", command=perform_sentiment_analysis, font=("Arial", 12), bg='#005bb5',
       fg='white').pack(side=LEFT)

result_text = Text(frame2, height=10, width=50, bg='#cce6ff', state=DISABLED)
result_text.pack(side=LEFT, fill=BOTH, expand=YES)

scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=result_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
