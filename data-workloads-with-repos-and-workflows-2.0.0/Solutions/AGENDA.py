# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC
# MAGIC ## Data Workload with Repos and Workflows
# MAGIC
# MAGIC In this lesson, you will learn how to seamlessly transition your data pipeline to production.
# MAGIC Moving a data pipeline to production means more than just confirming that code and data are working as expected. By scheduling tasks with Databricks Jobs, applications can be run automatically to keep tables in the Lakehouse fresh. Using Databricks SQL to schedule updates to queries and dashboards allows quick insights using the newest data. In this course, students will be introduced to task orchestration using the Databricks Workflow Jobs UI. Additionally, they will configure and schedule dashboards and alerts to reflect updates to production data pipelines.
# MAGIC
# MAGIC
# MAGIC ## Course agenda
# MAGIC
# MAGIC | Time | Module &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Lessons &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 30m    | **[Databricks Workspace]($./DWRW  01 - Databricks Workspace/DWRW 1.0 - Module Introduction)** | Databricks Workspace <br>[Module Introduction]($./DWRW  01 - Databricks Workspace/DWRW 1.0 - Module Introduction) </br> [Create and Manage Interactive Clusters]($./DWRW  01 - Databricks Workspace/DWRW 1.1 - Create and Manage Interactive Clusters) </br> [Notebook Basics]($./DWRW  01 - Databricks Workspace/DWRW 1.2 - Notebook Basics) </br> [Lab: Getting Started with the Databricks Platform Lab]($./DWRW  01 - Databricks Workspace/DWRW 1.3L - Getting Started with the Databricks Platform Lab) |
# MAGIC | 120m    | **[Wokflow Jobs]($./DWRW  02 -  Workflow Jobs/DWRW 2.0 - Module Introduction)** | Workflow Jobs </br> [Module Introdution]($./DWRW  02 -  Workflow Jobs/DWRW 2.0 - Module Introduction) </br> Scheduling Tasks with the Jobs UI </br> [Demo: Task Orchestration]($./DWRW  02 -  Workflow Jobs/DWRW 2.1 - Scheduling Tasks with the Jobs UI/DWRW 2.1.1 - Task Orchestration) </br> [Demo: Reset]($./DWRW  02 -  Workflow Jobs/DWRW 2.1 - Scheduling Tasks with the Jobs UI/DWRW 2.1.2 - Reset) </br> [Demo: DLT Job]($./DWRW  02 -  Workflow Jobs/DWRW 2.1 - Scheduling Tasks with the Jobs UI/DWRW 2.1.3 - DLT Job) </br> Jobs Lab </br> [Lab: Lab Instructions]($./DWRW  02 -  Workflow Jobs/DWRW 2.2L - Jobs Lab/DWRW 2.2.1L - Lab Instructions) </br> [Lab: Batch Job]($./DWRW  02 -  Workflow Jobs/DWRW 2.2L - Jobs Lab/DWRW 2.2.2L - Batch Job) </br> [Lab: DLT Job]($./DWRW  02 -  Workflow Jobs/DWRW 2.2L - Jobs Lab/DWRW 2.2.3L - DLT Job) </br> [Lab: Exploring Results]($./DWRW  02 -  Workflow Jobs/DWRW 2.2L - Jobs Lab/DWRW 2.2.4L - Exploring Results) </br> |

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * To run demo and lab notebooks, you need to use one of the following Databricks runtime(s): **12.2.x-cpu-ml-scala2.12**

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2024 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
