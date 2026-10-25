---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "The right answer attached to a training example, which a machine learning model learns to predict."
related:
  - "[[Machine Learning Basics]]"
  - "[[Feature Engineering and Feature Store]]"
  - "[[AutoML]]"
  - "[[Agent Evaluation and Tracing]]"
  - "[[Experiment Tracking]]"
aliases:
  - "Labels"
  - "target"
  - "target variable"
  - "ground truth"
  - "y"
last_verified: 2026-10-25
tags:
  - glossary
  - flashcards
---

# Label

> [!eli5] Summary
> A label is the known correct answer attached to an example in a training dataset. A machine learning model studies many labeled examples so it can predict the answer for new ones.

**In data work:** In supervised machine learning, each row of training data has [[Feature|features]] (the inputs) and a label (the known outcome). If a gym wants to predict which members will cancel, the features might be visits last month and membership age, and the label is a yes or no column saying whether that member cancelled. The [[Model|model]] learns the link between features and label during [[Training|training]]. Labels are often the scarcest and most expensive part of a project, because someone has to know or record the true answer. Wrong labels teach the model wrong lessons.

**In Databricks:** In Databricks you usually build a training set by joining a label table with feature tables from [[Feature Engineering and Feature Store|feature engineering in Unity Catalog]]. [[AutoML]] asks you to pick the target (label) column. For generative AI apps, human reviewers act as labelers: with MLflow 3, domain experts review traces in the Review App through labeling sessions, recording feedback or expected answers that become evaluation data (see [[Agent Evaluation and Tracing]]). Do not confuse ML labels with tags on Unity Catalog objects, which are metadata for governance.

Seen in: [[Machine Learning Basics]], [[AutoML]], [[Feature Engineering and Feature Store]]

## Recall

Label::The known correct answer for a training example (for example, did this customer cancel?), which a supervised model learns to predict.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Create and manage labeling sessions (AWS)](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/concepts/labeling-sessions)
> - [Review App (AWS)](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/concepts/review-app)
