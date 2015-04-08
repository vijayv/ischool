import pandas as pd


def main():
    # Load data
    df00 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission00.csv', header=False, names=['passenger_id', 'prediction00'])
    df01 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission01.csv', header=False, names=['passenger_id', 'prediction01'])
    df03 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission03.csv', header=False, names=['passenger_id', 'prediction03'])
    df04 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission04.csv', header=False, names=['passenger_id', 'prediction04'])
    df05 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission05.csv', header=False, names=['passenger_id', 'prediction05'])
    df05_5 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission05.5.csv', header=False, names=['passenger_id', 'prediction05_5'])
    df06 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission06.csv', header=False, names=['passenger_id', 'prediction06'])
    df07 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission07.csv', header=False, names=['passenger_id', 'prediction07'])
    df08 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission08.csv', header=False, names=['passenger_id', 'prediction08'])
    df09 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission09.csv', header=False, names=['passenger_id', 'prediction09'])
    df10 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission10.csv', header=False, names=['passenger_id', 'prediction10'])
    df11 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission11.csv', header=False, names=['passenger_id', 'prediction11'])
    df12 = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submission12.csv', header=False, names=['passenger_id', 'prediction12'])
    df_anand = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submissions_anand.csv', header=False, names=['passenger_id', 'prediction_anand'])
    df_nico = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submissions_nico.csv', header=False, names=['pred_nico_00', 'pred_nico_01', 'pred_nico_02', 'pred_nico_03', 'pred_nico_04'])
    df_sindhuja = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submissions_sindhuja.csv', header=False, names=['passenger_id', 'prediction_sindhuja'])
    df_vijay = pd.read_csv('/Users/JS/Data/_INFO290T/Lab6/submissions_anand.csv', header=False, names=['passenger_id', 'prediction_vijay'])

    # Combine predictions
    predictions = df00.merge(df01, on='passenger_id').merge(df03, on='passenger_id').merge(df04, on='passenger_id').merge(df05, on='passenger_id').merge(df05_5, on='passenger_id').merge(df06, on='passenger_id').merge(df07, on='passenger_id').merge(df08, on='passenger_id').merge(df09, on='passenger_id').merge(df10, on='passenger_id').merge(df11, on='passenger_id').merge(df12, on='passenger_id').merge(df_anand, on='passenger_id').merge(df_sindhuja, on='passenger_id').merge(df_vijay, on='passenger_id')
    predictions[['pred_nico_00', 'pred_nico_01', 'pred_nico_02', 'pred_nico_03', 'pred_nico_04']] = df_nico[['pred_nico_00', 'pred_nico_01', 'pred_nico_02', 'pred_nico_03', 'pred_nico_04']]

    # Median of all predictions
    predictions['survived'] = predictions.median(axis=1)

    # Output format
    df_out = predictions[['passenger_id', 'survived']].astype(int)
    df_out.to_csv('/Users/JS/Data/_INFO290T/Lab6/submission_ensemble_00.csv', index=False)


if __name__ == '__main__':
    main()
