# Databricks notebook source
babynames = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Volumes/dbacademy/labuser9128531_1739377194/retail/babynames.csv")
babynames.createOrReplaceTempView("babynames_table")
years = spark.sql("select distinct(Year) from babynames_table").toPandas()['Year'].tolist()
years.sort()
dbutils.widgets.dropdown("year", "2014", [str(x) for x in years])
display(babynames.filter(babynames.Year == dbutils.widgets.get("year")))