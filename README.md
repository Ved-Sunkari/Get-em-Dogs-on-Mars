### 🤖🐶 Robotic Dog Simulation in Celestial Environments (Get em Dogs on Mars)

Welcome to the Robotic Dog Simulation project, where we simulate a robotic dog learning to walk in various celestial environments! This project aims to explore the adaptability and learning capabilities of a quadrupedal robot in different gravitational fields, terrain types, and atmospheric conditions found on planets and moons in our solar system.

### High Level Summary:
Our project explores the development of a robotic dog simulation system that adapts and learns to navigate different celestial environments, such as the varying gravitational fields, terrains, and atmospheric conditions found on planets and moons. Using reinforcement learning and advanced AI algorithms, we simulate the robot's ability to walk and interact with its surroundings. The system is integrated with a web-based interface where users can visualize the model’s behavior in real-time across different planetary environments. If the live application is unavailable, users can run local simulations via Python scripts. The project aims to enhance our understanding of robotic adaptability in extraterrestrial environments, providing valuable insights for future space exploration missions. Explore the project here: <>


### View our models on the test data in the outputs folder!

### 🔗 Live Website
The FastAPI app is available here: <>

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

## Key Features
Celestial Environment Simulation: The project recreates the unique conditions of various celestial bodies, allowing for realistic testing of robotic locomotion.
Reinforcement Learning: Advanced AI algorithms enable the robotic dog to adapt its gait and movement strategies to each new environment.
Facial Recognition VR Movement: Users can control the viewpoint using facial movements, enhancing the immersive experience.
Web-based Interface: A user-friendly web application provides easy access to the simulation results.

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

Run the FastAPI app locally:

bash
Copy code
python app.py
Open the browser and go to http://127.0.0.1:5000 to view the local instance of the app.


### Simulation and Graphics

## NVIDIA Isaac Sim
We leveraged NVIDIA Isaac Sim as our primary simulation environment. This powerful tool allowed us to create highly realistic celestial environments, accurately modeling the unique gravitational fields, terrain types, and atmospheric conditions of various planets and moons.

## Three.js
For rendering our 3D models and creating interactive web-based visualizations, we utilized Three.js. This JavaScript library enabled us to display the robotic dog and celestial environments in web browsers, providing an accessible and immersive user experience.

### Machine Learning and AI

## PyTorch
PyTorch served as our core framework for developing and training the reinforcement learning models. Its dynamic computational graph and extensive ecosystem of tools made it ideal for implementing complex AI algorithms for our robotic dog's adaptive behaviors.

## Reinforcement Learning Algorithms
We implemented various reinforcement learning algorithms to train our robotic dog to navigate and adapt to different celestial environments. These algorithms enabled the robot to learn optimal movement strategies for each unique planetary condition.

### 3D Modeling and Design

## Fusion 360
Autodesk Fusion 360 was used for designing and modeling our robotic dog. This powerful CAD software allowed us to create detailed 3D models of the robot, ensuring accurate physical simulations in the virtual environments.

### Backend and API

## FastAPI
We chose FastAPI to build our backend API, enabling efficient communication between the frontend interface and our AI models. FastAPI's high performance and easy-to-use syntax made it an excellent choice for handling real-time data processing and model interactions.

## Python
Python served as our primary programming language, used extensively for backend development, data processing, and integrating various components of the project. Its versatility and rich library ecosystem made it ideal for this complex, multifaceted project.

### Frontend Development

## HTML and JavaScript
For creating the user interface and handling client-side interactions, we used HTML and JavaScript. These web technologies allowed us to build an intuitive and responsive frontend for users to interact with our robotic dog simulation.

### Future Implications
This project has significant implications for:
Space Exploration: Improving the design of rovers and exploratory robots for various planetary surfaces.
Adaptive Robotics: Advancing the field of robotics by creating more versatile and environment-adaptive machines.
AI and Machine Learning: Enhancing reinforcement learning algorithms for complex, variable environments.

### 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

### 📝 License
This project is licensed under the MIT License.

### 📧 Contact
For any questions or feedback, feel free to reach out at mail.vedsunkari@gmail.com

