



def get_stock_return(spots_dict):

    for ticker, spots_df in spots_dict.items():
        for i in range(1, len(spots_df)):
            spots_df.loc[i, 'returns'] = (spots_df.loc[i, 'Close'] / spots_df.loc[i-1, 'Close'])-1
            spots_df.loc[i, 'returns_avg_50'] = (spots_df.loc[i, 'avg_50'] / spots_df.loc[i - 1, 'avg_50']) - 1
            spots_df.loc[i, 'returns_avg_200'] = (spots_df.loc[i, 'avg_200'] / spots_df.loc[i - 1, 'avg_200']) - 1
            spots_df.loc[i, 'returns_avg_1000'] = (spots_df.loc[i, 'avg_1000'] / spots_df.loc[i - 1, 'avg_1000']) - 1
    return spots_dict