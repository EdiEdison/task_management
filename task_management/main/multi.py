import pandas as pd

class Multi():
    def __init__(self, data):
        self.data = data

    def drill_down(self, dimension):
        return self.data.groupby(dimension).mean()

    def roll_up(self, dimension):
        return self.data.groupby(dimension).sum()

    def slice_and_dice(self, conditions):
        return self.data.query(conditions)

    def pivot(self, pivot_column, values_column):
        return self.data.pivot_table(index='Date', columns=pivot_column, values=values_column)

    def filter_data(self, condition):
        return self.data.query(condition)

    def calculate_aggregations(self):
        return {
            'average_completion_time': self.data['CompletionTime'].mean(),
            'total_tasks_completed': self.data['TaskID'].count()
        }

    def top_n_analysis(self, n, column):
        return self.data.nlargest(n, column)

    def trend_analysis(self, time_column, measure_column):
        return self.data.groupby(time_column)[measure_column].mean()
