import random
import re
import os
import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__,static_folder='static')
CORS(app)

faq_file_path = os.path.join(os.path.dirname(__file__), "FAQ.txt")
# Load trained models
models = {
    "population": joblib.load("new_f1.joblib"),
    "cancer": joblib.load("breast-cancer-prediction.joblib"),
    "diabetes": joblib.load("diabetes-prediction.joblib"),
    "alzhiemer": joblib.load("alzheimers-predictionf3 (1).joblib"),
    "asthma": joblib.load("asthma-f3.joblib"),
}



def convert_to_float(value):
    """Handles numeric inputs, gender (Male/Female), and Yes/No responses."""
    value = value.strip().lower()  # Remove spaces and convert to lowercase

    # Encoding categorical variables
    if value in ["male", "m"]:
        return 1  # Assign 1 for Male
    elif value in ["female", "f"]:
        return 0  # Assign 0 for Female
    elif value in ["no"]:
        return 1  # Assign 1 for Yes
    elif value in ["yes"]:
        return 0  # Assign 0 for No
    elif value in ["high school"]:
        return 0
    elif value in ["bachelor's"]:
        return 0
    elif value in ["master's"]:
        return 1
    elif value in ["phd"]:
        return 1
    elif value in ["low"]:
        return 0
    elif value in ["moderate"]:
        return 0
    elif value in ["high"]:
        return 1
    elif value in ["non-smoker"]:
        return 0
    elif value in ["former smoker"]:
        return 1
    elif value in ["current smoker"]:
        return 1
    elif value in ["none"]:
        return 0
    elif value in ["ocassionally"]:
        return 1
    elif value in ["regularly"]:
        return 1
    elif value in ["mild"]:
        return 0
    elif value in ["severe"]:
        return 1
    elif value in ["balanced"]:
        return 0
    elif value in ["vegetarian"]:
        return 0
    elif value in ["fast food"]:
        return 1
    elif value in ["vegan"]:
        return 0
    elif value in ["not tested"]:
        return 0
    elif value in ["no risk"]:
        return 0
    elif value in ["one copy"]:
        return 1
    elif value in ["occasionally"]:
        return 1
    elif value in ["two copies"]:
        return 1
    
    elif "-" in value:  
        lower, upper = map(float, value.split("-"))
        return (lower + upper) / 2  # Convert range to average
    else:
        return float(value)  # Convert numerical values normally



@app.route('/predict/asthma', methods=['POST'])
def predict_asthma():
    try:
        data = request.form  
        print("Received data:", data)  # Debugging step

        # Convert input data with error handling
        processed_data = [convert_to_float(data[key]) for key in data.keys()]
        print(processed_data)
        
        features = np.array(processed_data).reshape(1, -1)

        prediction = models["asthma"].predict(features)

        result = "Asthma Detected" if prediction[0] == 1 else "No Asthma"

        # return jsonify({"condition": "asthma", "prediction": result})
        return render_template('asthma_result.html',  prediction=result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/predict/diabetes', methods=['POST'])
def predict_diabetes():
    try:
        data = request.form  
        print("Received data:", data)  # Debugging step

        # Convert input data with error handling
        processed_data = [convert_to_float(data[key]) for key in data.keys()]
        print(processed_data)
        
        features = np.array(processed_data).reshape(1, -1)

        prediction = models["diabetes"].predict(features)

        result = "Diabetes Detected" if prediction[0] == 1 else "No Diabetes"

        # return jsonify({"condition": "asthma", "prediction": result})
        return render_template('diabetes_result.html',  prediction=result)




    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict/cancer', methods=['POST'])
def predict_cancer():
    try:
        data = request.form 
        print("Received data:", data)  # Debugging step

        # Convert input data with error handling
        processed_data = [convert_to_float(data[key]) for key in data.keys()]
        print(processed_data)
        
        features = np.array(processed_data).reshape(1, -1)

        prediction = models["cancer"].predict(features)

        result = "Cancer Detected" if prediction[0] == 1 else "Cancer Free"

        
        return render_template('cancer_result.html',  prediction=result)


    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/predict/alzhiemer', methods=['POST'])
def predict_alzhiemer():
    try:
        data = request.form 
        print("Received data:", data)  # Debugging step

        # Convert input data with error handling
        processed_data = [convert_to_float(data[key]) for key in data.keys()]
        print(processed_data)
        
        features = np.array(processed_data).reshape(1, -1)

        prediction = models["alzhiemer"].predict(features)

        result = "Alzhiemer Detected" if prediction[0] == 1 else "Alzhiemer Free"

        
        return render_template('alzhiemer_result.html',  prediction=result)




    except Exception as e:
        return jsonify({"error": str(e)}), 500


class Chatbot:
    def __init__(self, faq_file_path):
        self.greetings = ["hello", "hi", "hey"]
        self.greeting_responses = ["Hello! How can I assist you?", "Hi there!", "Greetings!"]
        self.default_responses = ["I'm here to help.", "What can I assist you with today?"]
        self.faq_responses = {}
        self.vectorizer = None
        self.faq_questions = []
        self.load_faqs(faq_file_path)

    def preprocess_text(self, text):
        return re.sub(r"[^\w\s]", "", text.lower().strip())

    def load_faqs(self, faq_file_path):
        """Loads FAQs from the dataset file and creates vector representations."""
        if not os.path.exists(faq_file_path):
            print("Dataset file not found!")
            return

        with open(faq_file_path, "r", encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(":", 1)
                if len(parts) == 2:
                    question, answer = parts
                    processed_question = self.preprocess_text(question)
                    self.faq_responses[processed_question] = answer.strip()

        self.faq_questions = list(self.faq_responses.keys())
        
        # Only fit vectorizer if questions exist
        if self.faq_questions:
            self.vectorizer = TfidfVectorizer().fit(self.faq_questions)

    def find_best_match(self, user_input):
        """Finds the best matching question based on similarity."""
        processed_input = self.preprocess_text(user_input)

        # Exact match first
        if processed_input in self.faq_responses:
            return processed_input

        # If vectorizer is not ready, return None
        if not self.vectorizer or not self.faq_questions:
            return None

        # Compute similarity scores
        user_input_vector = self.vectorizer.transform([processed_input])
        faq_vectors = self.vectorizer.transform(self.faq_questions)
        similarities = cosine_similarity(user_input_vector, faq_vectors)
        max_sim_index = similarities.argmax()

        # Return matched question only if similarity is above threshold
        return self.faq_questions[max_sim_index] if similarities[0, max_sim_index] > 0.1 else None

    def get_response(self, user_input):
        """Returns an appropriate response based on the input."""
        processed_input = self.preprocess_text(user_input)

        # Handle greetings
        if any(greet in processed_input for greet in self.greetings):
            return random.choice(self.greeting_responses)

        # Find best matching question
        best_match = self.find_best_match(user_input)

        # Return matched response or default response
        response = self.faq_responses.get(best_match, random.choice(self.default_responses))

        # Debugging Output
        print(f"User input: {user_input}, Best match: {best_match}, Response: {response}")

        return response

chatbot = Chatbot(faq_file_path)

@app.route('/population_', methods=['POST'])
def population_():
    try:
        data = request.form 
        print("Received data:", data)  # Debugging step
        processed_data = [convert_to_float(data[key]) for key in data.keys()]
        print(processed_data)
        features = np.array(processed_data).reshape(1, -1)
        print(features)
        prediction = models["population"].predict(features)
        print(prediction)
        return render_template("population_result.html",prediction=prediction   ,year=int(processed_data[0]))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/population')
def population():
    return render_template("population.html")

@app.route('/')
def home():
    return render_template("webpage.html")  # Make sure `webpage.html` exists

@app.route('/chatbot')
def chatbot_page():
    return render_template("chatbot.html")  # Ensure `chatbot.html` exists

@app.route('/uid')
def uid():
    return render_template("uidinput.html") 

@app.route('/report')
def report():
    return render_template("report.html") 

@app.route('/asthma')
def asthma():
    return render_template("asthma.html")

@app.route('/ehr')
def ehr():
    return render_template("ehr.html")

@app.route('/cancer')
def cancer():
    return render_template("cancer.html")

@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")

@app.route('/alzhiemer')
def alzhiemer():
    return render_template("alzhiemer.html")

@app.route('/population_prediction')
def population_prediction():
    return render_template("alzhiemer.html")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({"response": "Please send a message."}), 400

    response = chatbot.get_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)  # Change to `host='0.0.0.0'` for deployment
