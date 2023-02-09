import pandas as pd
import multiprocessing

# Create a DataFrame


def process_dataframe(df):
    # Do something with the DataFrame
    df.iloc[0, 1] += 19
    print(id(df))
    print(df)

if __name__ == '__main__':
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

    # Create a Process
    p = multiprocessing.Process(target=process_dataframe, args=(df,))
    p2 = multiprocessing.Process(target=process_dataframe, args=(df,))

    # Start the Process
    p.start()
    p2.start()

    # Wait for the Process to finish
    p.join()
    p2.join()

    print(id(df))
    print(df)