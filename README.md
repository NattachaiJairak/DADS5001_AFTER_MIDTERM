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
![image](https://github.com/NattachaiJairak/DADS5001_AFTER_MIDTERM/assets/156494047/8fd65b1f-6204-4909-9231-c612d670771a)
![image](https://github.com/NattachaiJairak/DADS5001_AFTER_MIDTERM/assets/156494047/54acf025-e062-479d-8bbb-6c0abcc51581)
![image](https://github.com/NattachaiJairak/DADS5001_AFTER_MIDTERM/assets/156494047/6133f11c-bcad-4d29-b230-f83ea8fa9c56)

### Choosing Treemap for Visualization

Treemaps are chosen for visualizing the data because they are effective in illustrating hierarchical data structures and comparing proportions across categories. Here's why treemaps are suitable for this particular dataset:

1. **Hierarchical Representation**: Treemaps allow for the hierarchical representation of data, making it easy to visualize the breakdown of budget amounts at different levels (e.g., 'Classificated', 'Cost center name', 'Project name').

2. **Comparing Proportions**: Treemaps visually represent proportions within each category. The size of each rectangle in the treemap corresponds to the proportion of the total budget amount, providing an intuitive way to compare the contribution of different categories to the overall budget.

3. **Interactive Visualization**: Plotly Express provides interactive visualization capabilities, allowing users to hover over rectangles to see detailed information and drill down into specific categories for deeper analysis.

### Code Explanation

The provided code generates a treemap using Plotly Express. Here's a breakdown of the code:

1. **Creating Treemap**: `fig = px.treemap(grouped_df, path=['Classificated', 'Cost center name', 'Project name'], values=' Budget Amount (THB) ')` creates a treemap visualization using the grouped DataFrame (`grouped_df`). The `path` parameter specifies the hierarchical structure of the treemap, and the `values` parameter specifies the numerical values to be represented by the size of the rectangles.

2. **Displaying Treemap**: `fig.show()` displays the treemap visualization.

### Conclusion

Treemaps offer a visually engaging and informative way to represent hierarchical data structures and compare proportions across categories. The interactive nature of the treemap generated by Plotly Express allows for deeper exploration and analysis of the budget allocation across different levels of categorization. Overall, treemaps provide a valuable perspective on the distribution of budget amounts within the dataset.

![newplot](https://github.com/NattachaiJairak/DADS5001_AFTER_MIDTERM/assets/156494047/9180f672-2503-4aa9-8df8-364524fd7a2d)
