from PracticeRepo.MachineLearning.EDA.BasicEDA import *

def create_interaction_features(data, cat_cols):
    # create empty dataframe
    interaction_df = create_empty_dataframe()

    # combined features list
    combination_features = combination_of_list(cat_cols)
    for col1, col2 in combination_features:
        combination_data = data[col1].map(str) + "_"+data[col2].map(str)
        interaction_df[col1+'_'+col2] = combination_data

    # Assign index back
    interaction_df.index = data.index

    return interaction_df

