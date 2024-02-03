# app.py
from flask import Flask, render_template, jsonify
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_news')
def get_news():
    api_key = 'a10ddfd94f374f63ad87937dcec8985d'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}&pageSize=20'  # Fetch top 20 headlines for Nigeria
    
    try:
        response = requests.get(url)
        data = response.json()

        # Check if 'articles' key exists in the response
        if 'articles' not in data:
            return jsonify({'error': 'No articles found'})

        # Extract article details including title, descripion, URL, and image URL
        articles = [{'title': article['title'], 
                     'description': article['description'], 
                     'url': article['url'], 
                     'imageUrl': article['urlToImage'] if 'urlToImage' in article else None} for article in data['articles']]

        # Handle None values in 'description'
        for article in articles:
            article['description'] = article['description'] or ''  # Replace None with an empty string

        # Perform K-means clustering
        num_clusters = 3  # You can adjust the number of clusters based on your needs
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform([article['title'] + ' ' + article['description'] for article in articles])
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(X)

        # Add cluster labels to articles
        for i, label in enumerate(kmeans.labels_):
            articles[i]['cluster'] = int(label)

        return jsonify(articles)

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
