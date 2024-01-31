# Your Django Survival Prediction App

This Django web application predicts survival based on input features using a pre-trained machine learning model.

## Getting Started

These instructions will help you set up and run the application on your local machine.

### Prerequisites

- Python (3.6 or higher)
- Django
- Required Python packages 
- Pre-trained machine learning model ('ml_model.sav')
- Scaler file ('scaler.sav')

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-django-survival-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-django-survival-app
    ```

3. Install required packages:


4. Place the pre-trained machine learning model ('ml_model.sav') and the scaler file ('scaler.sav') in the project directory.

### Running the Application

1. Run Django migrations:

    ```bash
    python manage.py migrate
    ```

2. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

3. Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

## Usage

1. Input the required features on the homepage.
2. Click on the "Submit" button to get the survival prediction result.
3. The result page will display whether the passenger survived or not.

## Acknowledgments

- This application is built using Django and leverages a pre-trained machine learning model for survival prediction.
