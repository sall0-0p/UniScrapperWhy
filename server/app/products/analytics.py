import os
import pandas as pd
import numpy as np

def getAnalytics(data):
    pd_data = pd.DataFrame(data)

    opinions_count = pd_data.index.size
    pros_count = pd_data.pros.apply(lambda p: None if not p else p).count()
    cons_count = pd_data.cons.apply(lambda c: None if not c else c).count()
    average_score = pd_data.score.mean() 
    score_distribution = pd_data.score.value_counts().reindex(np.arange(0,1.2,0.2), fill_value = 0)

    print([opinions_count, pros_count, cons_count, average_score, score_distribution])

    return [opinions_count, pros_count, cons_count, average_score, score_distribution]
