### Data Source Description

The data source pertains to CAPEX (Capital Expenditure) for investments in 2024, categorized by cost center. This dataset provides insights into the allocation of financial resources across different areas of the organization, facilitating informed decision-making aligned with strategic objectives. The data is available in a CSV format accessible via the following URL:

[Data_Homework.csv](https://raw.githubusercontent.com/NattachaiJairak/DADS5001_AFTER_MIDTERM/main/DADS5001_2024-03-23/Data_Homework.csv)

This dataset serves as a valuable resource for analysis, planning, and optimizing investment strategies to drive growth and innovation within the organization.

### Notebook Link

For additional analysis and visualization, you can explore the provided Jupyter Notebook on Google Colab:

[DADS5001_2024_03_23_line_charts_Homework.ipynb](https://colab.research.google.com/github/NattachaiJairak/DADS5001_AFTER_MIDTERM/blob/main/DADS5001_2024-03-23/DADS5001_2024_03_23_line_charts_Homework.ipynb#scrollTo=AREw0UVjIFR8)

Certainly! Here's the explanation of why line charts were chosen for visualizing the data, along with the provided code:

### Choosing Line Charts for Visualization

Line charts are chosen for visualizing the data because they are effective in illustrating trends and changes over time or across categories. Here's why line charts are suitable for this particular dataset:

1. **Tracking Changes Over Time**: Line charts excel at showing how values change over time. In this case, if the budget amounts vary over time (e.g., monthly or quarterly budgets), a line chart would provide a clear visualization of these changes.

2. **Comparing Multiple Categories**: Line charts allow for easy comparison of multiple categories. Each line on the chart represents a different category (in this case, different values of 'Classificated'), making it simple to compare budget amounts across these categories.

3. **Showing Trends and Patterns**: Line charts help identify trends and patterns in the data. By plotting budget amounts against cost center names for each category, it's possible to spot trends or patterns that may emerge, such as which cost centers have consistently higher or lower budgets.

### Code Explanation

The provided code generates line charts for each unique value in the 'Classificated' column. Here's a breakdown of the code:

1. **Get Unique Values**: `unique_classificated_values = df['Classificated'].unique()` retrieves the unique values from the 'Classificated' column.

2. **Plot Line Charts**: The `for` loop iterates over each unique value in 'Classificated'. For each value:
   - The DataFrame is filtered to include only rows with the current 'Classificated' value.
   - A line chart is created using `plt.plot()` with 'Cost center name' on the x-axis and 'Budget Amount (THB)' on the y-axis.
   - Additional formatting options such as title, labels, rotation of x-axis labels, and grid are applied.
   - `plt.show()` displays the line chart.

### Conclusion

Overall, line charts are a suitable choice for visualizing this dataset as they effectively highlight trends, comparisons, and patterns in the budget amounts across different categories of 'Classificated'. The provided code generates separate line charts for each category, offering a comprehensive view of the data.

![image](https://github.com/NattachaiJairak/DADS5001_AFTER_MIDTERM/assets/156494047/a7c31fe7-8af1-4620-9d95-0a3a938db9f7)

