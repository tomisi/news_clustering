# News Clustering App

## Overview

This project is a News Clustering Application built using Python and Flask. The application leverages the Streamlit framework for the [user interface](#usage) and employs [unsupervised learning techniques](#overview) to cluster news articles based on their content.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
  - [Google Cloud Platform Deployment](#google-cloud-platform-deployment)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python (>=3.7)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) (if deploying to GCP)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/news-clustering-app.git
Navigate to the project directory:

bash
Copy code
cd news-clustering-app
Set up a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Visit http://localhost:8501 in your browser to interact with the app.

Deployment
Local Deployment
For local deployment, follow the Usage instructions. The app will be accessible on your local machine.

Google Cloud Platform Deployment
To deploy on Google Cloud Platform:

Push your code to GitHub.
Set up a GCP project and enable the App Engine API.
Install the Google Cloud SDK and authenticate with GCP (gcloud auth login).
Initialize your app and deploy it to App Engine.
The deployed app will be accessible at the provided GCP App Engine URL.

Contributing
If you'd like to contribute to this project, feel free to open issues and pull requests.
