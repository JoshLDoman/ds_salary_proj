#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 06:52:35 2020

@author: josh
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/josh/Desktop/ds_salary_proj/chromedriver"

df = gs.get_jobs("data scientist", 1000, False, path, 1000)

df.to_csv("glassdoor_jobs.csv", index = False)