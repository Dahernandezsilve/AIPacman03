import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'results_exact_final.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(df.head())

# Function to compare win rates based on different parameters
bottomVal = 0.3


def compare_win_rates(df, param):
    win_rates = df.groupby(param)['win'].mean()
    print(f"\nWin rates by {param} (ExactInference):")
    print(win_rates)
    win_rates.plot(kind='bar')
    plt.title(f'Win rates by {param} (ExactInference)')
    plt.ylabel('Win Rate')
    plt.xlabel(param)
    plt.subplots_adjust(bottom=bottomVal)
    plt.show()

# Function to compare average scores based on different parameters


def compare_average_scores(df, param):
    average_scores = df.groupby(param)['score'].mean()
    print(f"\nAverage scores by {param} (ExactInference):")
    print(average_scores)
    average_scores.plot(kind='bar')
    plt.title(f'Average scores by {param} (ExactInference)')
    plt.ylabel('Average Score')
    plt.xlabel(param)
    plt.subplots_adjust(bottom=bottomVal)
    plt.show()

# Function to compare execution times based on different parameters


def compare_execution_times(df, param):
    execution_times = df.groupby(param)['execution_time'].mean()
    print(f"\nExecution times by {param} (ExactInference):")
    print(execution_times)
    execution_times.plot(kind='bar')
    plt.title(f'Execution times by {param} (ExactInference)')
    plt.ylabel('Execution Time (s)')
    plt.xlabel(param)
    plt.subplots_adjust(bottom=bottomVal)
    plt.show()

# Function to compare L2 errors based on different parameters


def compare_l2_errors(df, param):
    l2_errors = df.groupby(param)['l2_error'].mean()
    print(f"\nL2 errors by {param} (ExactInference):")
    print(l2_errors)
    l2_errors.plot(kind='bar')
    plt.title(f'L2 errors by {param} (ExactInference)')
    plt.ylabel('L2 Error')
    plt.xlabel(param)
    plt.subplots_adjust(bottom=bottomVal)
    plt.show()

# Function to compare KL divergences based on different parameters


def compare_kl_divergences(df, param):
    kl_divergences = df.groupby(param)['kl_divergence'].mean()
    print(f"\nKL divergences by {param} (ExactInference):")
    print(kl_divergences)
    kl_divergences.plot(kind='bar')
    plt.title(f'KL divergences by {param} (ExactInference)')
    plt.ylabel('KL Divergence')
    plt.xlabel(param)
    plt.subplots_adjust(bottom=bottomVal)
    plt.show()


# Create a new variable for observe and elapse interaction using names instead of boolean values
df['observe_elapse'] = df['observe'].map(
    {True: 'observe', False: '_'}) + '_' + df['elapse'].map({True: 'elapse', False: '_'})


# Compare win rates
compare_win_rates(df, 'observe_elapse')
compare_win_rates(df, 'numGhosts')
compare_win_rates(df, 'mapName')

# Compare average scores
compare_average_scores(df, 'observe_elapse')
compare_average_scores(df, 'numGhosts')
compare_average_scores(df, 'mapName')


# Compare execution times
compare_execution_times(df, 'observe_elapse')
compare_execution_times(df, 'numGhosts')
compare_execution_times(df, 'mapName')

# Compare L2 errors
compare_l2_errors(df, 'observe_elapse')
compare_l2_errors(df, 'numGhosts')
compare_l2_errors(df, 'mapName')

# Compare KL divergences
compare_kl_divergences(df, 'observe_elapse')
compare_kl_divergences(df, 'numGhosts')
compare_kl_divergences(df, 'mapName')
