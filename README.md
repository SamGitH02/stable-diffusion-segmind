## Please add and use your own Segmind API key in main.py before running the project.

# Image Generation App with Segmind API

This web application allows you to generate images using the power of Stable Diffusion, a state-of-the-art text-to-image model. The app leverages the Segmind API to seamlessly generate images based on your text prompts.

## Features

*   **Text-to-Image Generation:**  Input descriptive text prompts and watch as the app generates corresponding images using Stable Diffusion.
*   **Model Selection:**  Choose from a variety of Stable Diffusion models to tailor the image generation process to your needs.
*   **User-Friendly Interface:**  A simple and intuitive interface makes it easy to interact with the app and generate images.

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository.git](https://github.com/your-username/your-repository.git) 
    cd your-repository
    ```

2.  **Install Dependencies:**
    ```bash
    # Install frontend dependencies (if applicable)
    cd frontend 
    npm install

    # Install backend dependencies
    cd backend
    pip install -r requirements.txt
    ```

3.  **Obtain a Segmind API Key:**
    *   Sign up for a Segmind account and obtain an API key.
    *   Set the `SEGMIND_API_KEY` environment variable in your backend environment or configuration file.

## Usage

1.  **Start the Backend Server:**
    ```bash
    cd backend
    python app.py 
    ```

2.  **Start the Frontend (if applicable):**
    ```bash
    cd frontend
    npm start
    ```

3.  **Access the App:**
    *   Open your web browser and navigate to `http://localhost:3000` (or the appropriate port if you've configured it differently).

4.  **Enter a Text Prompt:**
    *   Provide a descriptive text prompt in the input field.

5.  **Select a Model (Optional):**
    *   Choose a specific Stable Diffusion model from the available options.

6.  **Generate Image:**
    *   Click the "Generate" button to initiate the image generation process.

7.  **View the Generated Image:**
    *   The generated image will be displayed on the screen.
  
  ## Example output
  ![image](https://github.com/user-attachments/assets/21582eda-0ee7-4320-94af-6da35ef1baf3)

  ![image](https://github.com/user-attachments/assets/ef95999d-4389-4fcc-a893-2610859c7b16)



## Important Notes

*   Ensure you have a valid Segmind API key and have set it up correctly in your backend environment.
*   Refer to the Segmind API documentation for details on available models and their usage.
*   The frontend code might require adjustments based on your specific framework or setup.

## Contributing

Contributions are welcome! If you have any ideas for improvements or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
