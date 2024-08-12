# Lyzr Cold Email Generator

Welcome to the **Lyzr Cold Email Generator**, an advanced tool designed to help you craft the perfect cold email. This application leverages Lyzr's AI capabilities to iteratively refine your email content, ensuring it's polished and effective.

## Features

- **Automated Research and Content Synthesis**: The application conducts thorough research on the target audience and product, synthesizing the information into a complete overview.
- **Iterative Email Draft Creation**: Generates an initial email draft based on the research, which undergoes multiple iterations and critiques to achieve perfection.
- **Critique and Refinement**: The email draft is critiqued by an agent, with identified issues being corrected through multiple iterations until all checks are green.
- **User Review and Final Approval**: The refined email is presented for final user review and approval before being finalized.

## Installation

1. Clone this repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd lyzr-cold-email-generator
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up environment variables by creating a `.env` file in the root directory and adding your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    LYZR_API_KEY=your_lyzr_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
2. Open the application in your browser at the default Streamlit URL, typically `http://localhost:8501`.
3. Enter the product description and target audience in the provided text area.
4. Click the "Generate" button to start the email creation process.

## Code Overview

- **`LyzrAgent` Integration**: The `LyzrAgent` class is used to interact with the Lyzr API, handling environment and agent creation.
- **`@st.cache_resource`**: The `create_agent` function is cached to optimize performance, ensuring the agent is only created once per session.
- **`Environment Setup`**: An environment with specific features and tools is created to manage the cold email generation process.
- **`Email Generation Flow`**:
    - **User Input and Initial Data Gathering**: The user provides essential inputs, including target audience and product information.
    - **Research and Content Synthesis**: The agent conducts thorough research, synthesizing the information into a Scratchpad Display.
    - **Email Draft Creation and Refinement**: The agent drafts an initial email, critiques it, and iteratively refines it until perfection is achieved.
    - **Final Approval**: The refined email is presented to the user for review and approval.
