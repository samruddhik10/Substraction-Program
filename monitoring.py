import pandas as pd
from evidently import Report
from evidently.presets import DataSummaryPreset

# Sample subtraction data
data = {
    "num1": [20, 30, 50, 10, 40],
    "num2": [10, 15, 20, 5, 25],
    "result": [10, 15, 30, 5, 15]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Create Evidently report
report = Report([
    DataSummaryPreset()
])

# Generate report
snapshot = report.run(df, None)

# Save report as HTML
snapshot.save_html("evidently_report.html")

print("Evidently report generated successfully!")