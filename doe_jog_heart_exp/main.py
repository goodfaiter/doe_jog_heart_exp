from doe_jog_heart_exp.helpers.loader import load_data
import statsmodels.api as sm
import statsmodels.formula.api as smf

if __name__ == "__main__":
    data = load_data()

    # Normalize the target variables (change in BMP, RPE, and questionnaire scores)
    data['bmp_change'] = data['after_bmp'] - data['before_bmp']
    data['bmp_change_normalized'] = 2 * (data['bmp_change'] - data['bmp_change'].min()) / (data['bmp_change'].max() - data['bmp_change'].min()) - 1

    data['rpe_change'] = data['after_rpe'] - data['before_rpe']
    data['rpe_change_normalized'] = 2 * (data['rpe_change'] - data['rpe_change'].min()) / (data['rpe_change'].max() - data['rpe_change'].min()) - 1

    data['q_change'] = data['questionnaire_q2'] - data['questionnaire_q1']
    data['q_change_normalized'] = 2 * (data['q_change'] - data['q_change'].min()) / (data['q_change'].max() - data['q_change'].min()) - 1

    data['q3'] = data['questionnaire_q3']  # Keep q3 as is for potential use in the model
    data['q3_normalized'] = 2 * (data['q3'] - data['q3'].min()) / (data['q3'].max() - data['q3'].min()) - 1

    # Create binary variables for categorical factors
    data['X1'] = data['type'].apply(lambda x: 1 if x == 'Running' else -1)  # Categorical to binary
    data['X2'] = data['weight'].apply(lambda x: 1 if x == '5 kg' else -1)  # Categorical to binary
    data['X3'] = data['frequency'].apply(lambda x: 1 if x == '5 / week' else -1)  # Categorical to binary
    data['X4'] = data['distance'].apply(lambda x: 1 if x == '5 km' else -1)  # Categorical to binary

    # Uncomment for simple model without interactions
    formula = 'y ~ X1 + X2 + X3 + X4'
    anova_type = 2
    
    # Uncomment for model with interactions
    # formula = 'y ~ X1 + X2 + X3 + X4 + X1:X2 + X1:X3 + X1:X4'
    # anova_type = 1

    # print("\n============Model for BMP Change============")
    data['y'] = data['bmp_change_normalized']  # Target variable
    model = smf.ols(formula=formula, data=data).fit()  # Fit the model with robust standard errors
    print(sm.stats.anova_lm(model, typ=anova_type)) # Print ANOVA table for the model
    print(model.summary())

    # print("\n============Model for RPE Change============")
    data['y'] = data['rpe_change_normalized']  # Target variable
    model = smf.ols(formula=formula, data=data).fit()
    print(sm.stats.anova_lm(model, typ=anova_type)) # Print ANOVA table for the model
    print(model.summary())

    # print("\n============Model for Questionnaire Change============")
    data['y'] = data['q_change_normalized']  # Target variable
    model = smf.ols(formula=formula, data=data).fit()
    print(sm.stats.anova_lm(model, typ=anova_type)) # Print ANOVA table for the model
    print(model.summary())

    print("\n============Model for Questionnaire Q3============")
    data['y'] = data['q3_normalized']  # Target variable
    model = smf.ols(formula=formula, data=data).fit()
    print(sm.stats.anova_lm(model, typ=anova_type)) # Print ANOVA table for the model
    print(model.summary())




