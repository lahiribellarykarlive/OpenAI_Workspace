# OpenAI_Workspace: GenAI Use Cases demo

# GenAI Project

This project demonstrates the capabilities of GenAI through two distinct use cases:

1. **Translate PIR into a Knowledge Base Article**
2. **Extract Microsoft Teams Transcript to Create TODO Actions List**

## Project Overview

The project consists of two Python scripts:

1. **openaikbasearticle.py**
   - Reads input from `kbase.properties`
   - Accepts prompts and PIR as input
   - Returns the OpenAI JSON output, containing the knowledge base article created from the input PIR

2. **openaitodoaction.py**
   - Reads input from `todoaction.properties`
   - Accepts prompts and Microsoft Teams transcript as input
   - Returns the OpenAI JSON output, containing TODO actions extracted from the Teams meeting transcript

## Prerequisites

To run this project, you need the following:

1. **Python 3**
2. **OpenAI Key** added to your environment variables

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/genai-project.git
   cd genai-project
