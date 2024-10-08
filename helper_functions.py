def add_xmonth_default_flag(ap_df, mo_df, m, y=3, col_suffix='_new'):
    """
    add is_bad_Xm column to ap_df
    ap_df: DataFrame, application data
    mo_df: DataFrame, monthly data
    m: int, month (e.g 3m, 12m)
    y: int, How many payments missed for flag to be true
    col_suffix: str, suffix for the new column (eg. 'is_bad_12m_new')

    returns: DataFrame, ap_df with new column
    """
    # order mo_df by unique_id and date
    mo_df = mo_df.sort_values(by=['unique_id', 'date'], ascending=[True, True]).reset_index(drop=True)
    # row_number for each unique_id
    mo_df['row_number'] = mo_df.groupby('unique_id').cumcount()+1
    # keep only row-X for each unique_id
    mo_df_reduced =  mo_df.query(f'row_number=={m}')
    # Check if by row-X, y payments have been missed
    mo_df_reduced[f'is_bad_{m}m{col_suffix}']  = mo_df_reduced['status'].apply(lambda x: 1.0 if x>=y else 0.0)
    mo_df_reduced = mo_df_reduced[['unique_id', f'is_bad_{m}m{col_suffix}']]
    # left join with ap_df
    ap_df = ap_df.merge(mo_df_reduced, on='unique_id', how='left')
    return ap_df

def classification_power(df, target, score):
    from sklearn.metrics import roc_curve, roc_auc_score
    """
    Calculate AUC, FPR, TPR

    df: DataFrame, with target and score columns
    target: str, target column name
    score: str, score column name
    returns: auc_score, fpr, tpr, thresholds, sample_size, bad_rate
    """
    y_true = df[target]
    y_pred = df[score]
    fpr, tpr, thresholds = roc_curve(y_true, y_pred)
    auc_score = roc_auc_score(y_true, y_pred)
    sample_size = len(y_true)
    bad_rate = round(y_true.mean(),4)
    return auc_score, fpr, tpr, thresholds, sample_size, bad_rate