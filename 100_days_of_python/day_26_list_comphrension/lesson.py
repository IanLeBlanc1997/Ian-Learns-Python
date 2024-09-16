# new_list = [(new_item) for (item) in (list) if (condition)]

# new dict = {(new_key):(new_value) for (key),(value) in (dict.items()) if (condition)}
import pandas
student_scores = {"student":['Ian','Aiiden','Chris'],"score":[60,52,8]}
scores_df = pandas.DataFrame(student_scores)

for (index, row) in scores_df.iterrows():
    print(row)
