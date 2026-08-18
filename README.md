# 🛒 RetailIQ — AI-Powered Retail Intelligence Platform

RetailIQ is an end-to-end **AI-powered retail intelligence platform** that combines **Machine Learning, Deep Learning, Computer Vision, Recommendation Systems, and Generative AI** into a unified application.

The platform enables retailers to:

* 📈 Forecast store sales
* 🛒 Generate personalized product recommendations
* 🖼️ Classify retail product images
* 🤖 Ask questions about the entire AI project using a RAG-powered Gemini assistant

The application is built using **Python and Streamlit**, with trained ML/DL models integrated into an interactive dashboard.

---

# 🚀 Key Features

## 📈 1. Sales Forecasting

RetailIQ uses **XGBoost** to predict store sales based on retail and temporal features.

### Features Used

The forecasting module considers features such as:

* Store ID
* Day of week
* Store opening status
* Promotions
* School holidays
* Store type
* Assortment
* Competition distance
* Competition opening information
* Promo2 information
* Date-related features
* Weekend indicators
* Holiday flags

The trained model is integrated directly into the Streamlit application for interactive predictions.

---

## 🛒 2. Product Recommendation

The recommendation module uses a trained **Artificial Neural Network (ANN)** to generate personalized product recommendations.

### Recommendation Pipeline

```text
Customer Selection
        ↓
User Encoding
        ↓
Available Products
        ↓
ANN Recommendation Model
        ↓
Recommendation Scores
        ↓
Top-N Products
        ↓
Product ID → Product Description
        ↓
Recommended Products
```

The system:

1. Selects a customer.
2. Encodes the customer using the trained user encoder.
3. Evaluates available products through the trained recommendation model.
4. Generates recommendation scores.
5. Selects the highest-scoring products.
6. Maps product IDs to human-readable product descriptions.
7. Displays the recommended products to the user.

Users can select how many recommendations they want to receive.

---

## 🖼️ 3. Product Image Classification

RetailIQ uses **MobileNetV2 Transfer Learning** for automated product image classification.

### Classification Pipeline

```text
Product Image
      ↓
Image Preprocessing
      ↓
Resize to 224 × 224
      ↓
MobileNetV2
      ↓
Class Probabilities
      ↓
Predicted Product Category
```

### Supported Image Formats

* JPG
* JPEG
* PNG
* WEBP
* AVIF

### Classification Results

The interface displays:

* Predicted category
* Prediction confidence
* Top-3 predictions

---

# 🤖 4. Generative AI Project Assistant

One of the key features of RetailIQ is its **RAG-powered AI Project Assistant**.

Instead of relying only on the LLM's general knowledge, the assistant retrieves information from the project's own documentation before generating an answer.

### Example Questions

Users can ask questions such as:

* Why was XGBoost selected?
* Where is XGBoost used?
* Why did we use MobileNetV2?
* Explain the recommendation system.
* What datasets were used?
* Explain the project architecture.
* What models are used in RetailIQ?

---

# 🧠 RAG Architecture

The RAG pipeline uses:

* **Sentence Transformers** — document and query embeddings
* **FAISS** — vector similarity search
* **Project Documentation** — knowledge base
* **Google Gemini** — response generation

### Workflow

```text
                    User Question
                          ↓
                 Sentence Transformer
                          ↓
                   Query Embedding
                          ↓
                        FAISS
                          ↓
                 Relevant Documents
                          ↓
                      Context
                          ↓
                   Google Gemini
                          ↓
                  Grounded Response
                          ↓
                  Sources / Documents
```

This allows the assistant to provide answers grounded in the project's documentation.

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │    Streamlit UI     │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
     ┌────────────────┐    ┌────────────────┐    ┌────────────────────┐
     │ Sales          │    │ Recommendation │    │ Image              │
     │ Forecasting    │    │ System         │    │ Classification     │
     └───────┬────────┘    └───────┬────────┘    └─────────┬──────────┘
             │                     │                       │
             ▼                     ▼                       ▼
         ┌────────┐           ┌────────┐             ┌────────────┐
         │ XGBoost│           │  ANN   │             │MobileNetV2 │
         └────┬───┘           └────┬───┘             └─────┬──────┘
              │                    │                       │
              └────────────────────┼───────────────────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │ Retail Intelligence │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │  AI Project         │
                        │  Assistant           │
                        └──────────┬──────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
             ┌────────────┐              ┌────────────────────┐
             │   FAISS    │              │ Sentence           │
             │ Vector DB  │              │ Transformers       │
             └──────┬─────┘              └─────────┬──────────┘
                    │                              │
                    └──────────────┬───────────────┘
                                   ▼
                         ┌────────────────────┐
                         │ Retrieved Context  │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │   Google Gemini    │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ Final AI Response  │
                         └────────────────────┘
```

---

# 🧰 Technology Stack

| Category             | Technologies                  |
| -------------------- | ----------------------------- |
| Programming Language | Python                        |
| Web Application      | Streamlit                     |
| Machine Learning     | XGBoost, Scikit-learn         |
| Deep Learning        | TensorFlow / Keras            |
| Computer Vision      | MobileNetV2                   |
| Recommendation       | Artificial Neural Network     |
| Generative AI        | Google Gemini                 |
| RAG                  | FAISS + Sentence Transformers |
| Data Processing      | Pandas, NumPy                 |
| Model Persistence    | Joblib                        |
| Image Processing     | Pillow                        |

---

# 📂 Project Structure

```text
RetailIQProject/
│
├── App/
│   └── app.py
│
├── Data/
│   └── Dataset files
│
├── Docs/
│   ├── architecture.md
│   ├── classification.md
│   ├── datasets.md
│   ├── faq.md
│   ├── forecasting.md
│   ├── model_selection.md
│   ├── project_overview.md
│   └── recommendation.md
│
├── Models/
│   ├── xgboost_sales_forecaster.pkl
│   ├── ann_recommender.h5
│   ├── mobilenetv2_classifier.keras
│   ├── user_encoder.pkl
│   ├── product_encoder.pkl
│   └── cnn_label_encoder.pkl
│
├── Utils/
│   ├── forecasting_ui.py
│   ├── recommendation_ui.py
│   ├── classification_ui.py
│   ├── assistant_ui.py
│   ├── rag.py
│   ├── gemini.py
│   ├── chat.py
│   └── build_vectorstore.py
│
├── VectorStore/
│   ├── index.faiss
│   └── documents.pkl
│
├── .env
├── requirement.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd RetailIQProject
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirement.txt
```

---

# 🔑 Gemini API Configuration

The AI Project Assistant requires a **Google Gemini API key**.

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

The application uses the **Google GenAI SDK** to communicate with Gemini.

> ⚠️ Never commit your `.env` file or expose your API key publicly.

Add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# 🧠 Building the RAG Vector Database

The project documentation is stored inside the `Docs/` directory.

To create the FAISS vector database:

```bash
python Utils/build_vectorstore.py
```

### Vector Database Creation Pipeline

```text
Markdown Documents
        ↓
Document Loading
        ↓
Text Processing
        ↓
Sentence Transformer
        ↓
Embeddings
        ↓
FAISS Index
        ↓
VectorStore/
```

After successful execution, the `VectorStore/` directory should contain the generated vector database files.

---

# ▶️ Running the Application

From the project root:

```bash
streamlit run App/app.py
```

The application will open in your browser at:

**http://localhost:8501**

---

# 💬 Example AI Assistant Questions

The RAG assistant can answer questions related to the project documentation.

### Model Selection

> Why was XGBoost selected for sales forecasting?

### Architecture

> Explain the architecture of RetailIQ.

### Recommendation

> How does the recommendation system work?

### Computer Vision

> Why was MobileNetV2 used?

### Dataset

> What datasets are used in the project?

### General Project

> What are the different modules of RetailIQ?

---

# 🔍 RAG Pipeline Example

For a question such as:

> **Where are we using XGBoost?**

The system performs the following steps:

```text
Question
   ↓
Generate Query Embedding
   ↓
FAISS Similarity Search
   ↓
Retrieve Relevant Documentation
   ↓
┌───────────────────────┐
│ forecasting.md        │
│ model_selection.md    │
│ faq.md                │
└───────────┬───────────┘
            ↓
      Build Context
            ↓
 Send Context + Question
            ↓
       Google Gemini
            ↓
      Generate Answer
```

The assistant therefore uses the project's documentation as its knowledge source rather than generating an answer completely from general model knowledge.

---

# 🎯 Project Objectives

RetailIQ was designed to demonstrate how multiple AI technologies can work together within a single real-world application.

The project covers:

* Machine Learning
* Feature Engineering
* Gradient Boosting
* Recommendation Systems
* Neural Networks
* Computer Vision
* Transfer Learning
* Vector Databases
* Semantic Search
* Retrieval-Augmented Generation
* Large Language Models
* Generative AI
* Interactive AI Applications

---

# 📌 Future Improvements

Potential future enhancements include:

* Hybrid retrieval using FAISS + BM25
* Cross-encoder reranking
* Streaming Gemini responses
* Improved conversational memory
* Document upload and automatic indexing
* Advanced retail analytics dashboards
* Model monitoring
* Cloud deployment
* User authentication
* Recommendation explanations
* Forecast visualization
* Historical trend analysis

---

# 👨‍💻 Author

**Shashvat Mishra**

*AI/ML Engineer | Technical Research Analyst*

---

# ⭐ Project Highlights

```text
Machine Learning
       +
Deep Learning
       +
Computer Vision
       +
Recommendation Systems
       +
Generative AI
       +
RAG
       +
Vector Search
       ↓
    RetailIQ
```

RetailIQ demonstrates an end-to-end approach to building an **AI-powered business intelligence application** by integrating predictive models, recommendation systems, computer vision, and a documentation-aware Generative AI assistant into one unified platform.

---

## ⭐ If you found this project useful

Give the repository a ⭐ on GitHub!
