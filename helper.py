import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def question_respondents(df, question):
    total = len(df)
    question = len(df[question][df[question].notnull()])
    print('Number of respondents who have answered this question: {} ({:.2f}%)'.format(question, question/total * 100))
    
def keep_categories(df, keep):
    for c in df.cat.categories:
        if not c in keep:
            df = df.cat.remove_categories([c])
    return df