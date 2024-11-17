### 🤖🐶 Robotic Dog Simulation in Celestial Environments

Welcome to the Robotic Dog Simulation project, where we simulate a robotic dog learning to walk in various celestial environments! This project aims to explore the adaptability and learning capabilities of a quadrupedal robot in different gravitational fields, terrain types, and atmospheric conditions found on planets and moons in our solar system.

### View our models on the test data in the outputs folder!

### 🔗 Live Website
#The Flask app is available here: <>

Note: The website may not always be up and running. In that case, use the app.py script for local testing.

### 📂 Folder Structure
arduino
## Copy code
├── README.md
├── app.py
├── static/
├── templates/
├── requirements.txt
└── sample_data/
app.py: The main FastAPI application. The script for API calls, reinforcement learning scripts, and facial movement algorithms.
sample_data/: Folder containing sample glb files that are pretested.
static/ and templates/: Used for FastAPIs web interface.
requirements.txt: List of all dependencies required for the project.
### 🚀 Getting Started
Prerequisites
Make sure you have the following installed on your machine:

Python 3.7+
pip (Python package installer)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Ved-Sunkari/robotic-dog-model-api.git
cd robotic-dog-model-api
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
(Optional) Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

### 🌐 Using the Web Application
You can access the live web application at <>.

Click on one of the planets to load celestial body environment.
Turn on facial recognition VR movement.
View Results: Turn your head from side-to-side to see the trained robotic dog model.
Tip: Make sure to keep your browser connected and hide camera when canceling the facial recognition movement. 

### 🖥️ Running the predict.py Script Locally
If the web app is not accessible, you can use the local prediction script to get results from your seismic data.

Usage
Navigate to the project directory:

bash
Copy code
cd robotic-dog-model-api
Run the app.py script.

bash
Copy code
python app.py --/planet
Output
The script will run the environment using the trained AI reinforcement model.

### 🛠️ Development
Want to improve the app? Here’s how you can set up the project for development:

Run the Flask app locally:

bash
Copy code
python app.py
Open the browser and go to http://127.0.0.1:5000 to view the local instance of the app.

### 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

### 📝 License
This project is licensed under the MIT License.

### 📧 Contact
For any questions or feedback, feel free to reach out at mail.vedsunkari@gmail.com

