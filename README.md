# Query Enhancer and Article Retrieval

This is a Django web application that enhances user-provided queries using the OpenAI GPT-3.5 API and retrieves top 10 related articles from NewsAPI based on the enhanced query. The articles include titles, summaries, and images.

## Features

- Enhance user-provided queries using OpenAI GPT-4.
- Fetch top 10 articles related to the enhanced query from GNewsAPI.
- Display original and enhanced queries side-by-side.
- Display articles with titles, summaries, and images.

## Prerequisites

- Python 3.6 or higher
- Django 3.0 or higher
- OpenAI API key
- GNewsAPI key

## Important Commands
- .\env\Scripts\Activate.ps1
- django-admin startproject QueryEnhancer
- cd QueryEnhancer
- django-admin startapp enhancement
