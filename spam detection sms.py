{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5a6232f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import roc_auc_score, f1_score, confusion_matrix\n",
    "from sklearn.naive_bayes import MultinomialNB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fb11153e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "      <th>Unnamed: 2</th>\n",
       "      <th>Unnamed: 3</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        v1                                                 v2 Unnamed: 2  \\\n",
       "0      ham  Go until jurong point, crazy.. Available only ...        NaN   \n",
       "1      ham                      Ok lar... Joking wif u oni...        NaN   \n",
       "2     spam  Free entry in 2 a wkly comp to win FA Cup fina...        NaN   \n",
       "3      ham  U dun say so early hor... U c already then say...        NaN   \n",
       "4      ham  Nah I don't think he goes to usf, he lives aro...        NaN   \n",
       "...    ...                                                ...        ...   \n",
       "5567  spam  This is the 2nd time we have tried 2 contact u...        NaN   \n",
       "5568   ham              Will Ì_ b going to esplanade fr home?        NaN   \n",
       "5569   ham  Pity, * was in mood for that. So...any other s...        NaN   \n",
       "5570   ham  The guy did some bitching but I acted like i'd...        NaN   \n",
       "5571   ham                         Rofl. Its true to its name        NaN   \n",
       "\n",
       "     Unnamed: 3 Unnamed: 4  \n",
       "0           NaN        NaN  \n",
       "1           NaN        NaN  \n",
       "2           NaN        NaN  \n",
       "3           NaN        NaN  \n",
       "4           NaN        NaN  \n",
       "...         ...        ...  \n",
       "5567        NaN        NaN  \n",
       "5568        NaN        NaN  \n",
       "5569        NaN        NaN  \n",
       "5570        NaN        NaN  \n",
       "5571        NaN        NaN  \n",
       "\n",
       "[5572 rows x 5 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('spam.csv',encoding = 'ISO-8859-1')\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "81360026",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "      <th>Unnamed: 2</th>\n",
       "      <th>Unnamed: 3</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     v1                                                 v2 Unnamed: 2  \\\n",
       "0   ham  Go until jurong point, crazy.. Available only ...        NaN   \n",
       "1   ham                      Ok lar... Joking wif u oni...        NaN   \n",
       "2  spam  Free entry in 2 a wkly comp to win FA Cup fina...        NaN   \n",
       "3   ham  U dun say so early hor... U c already then say...        NaN   \n",
       "4   ham  Nah I don't think he goes to usf, he lives aro...        NaN   \n",
       "\n",
       "  Unnamed: 3 Unnamed: 4  \n",
       "0        NaN        NaN  \n",
       "1        NaN        NaN  \n",
       "2        NaN        NaN  \n",
       "3        NaN        NaN  \n",
       "4        NaN        NaN  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ab710152",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 5572 entries, 0 to 5571\n",
      "Data columns (total 5 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   v1          5572 non-null   object\n",
      " 1   v2          5572 non-null   object\n",
      " 2   Unnamed: 2  50 non-null     object\n",
      " 3   Unnamed: 3  12 non-null     object\n",
      " 4   Unnamed: 4  6 non-null      object\n",
      "dtypes: object(5)\n",
      "memory usage: 217.8+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0adc40b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method NDFrame.describe of         v1                                                 v2 Unnamed: 2  \\\n",
       "0      ham  Go until jurong point, crazy.. Available only ...        NaN   \n",
       "1      ham                      Ok lar... Joking wif u oni...        NaN   \n",
       "2     spam  Free entry in 2 a wkly comp to win FA Cup fina...        NaN   \n",
       "3      ham  U dun say so early hor... U c already then say...        NaN   \n",
       "4      ham  Nah I don't think he goes to usf, he lives aro...        NaN   \n",
       "...    ...                                                ...        ...   \n",
       "5567  spam  This is the 2nd time we have tried 2 contact u...        NaN   \n",
       "5568   ham              Will Ì_ b going to esplanade fr home?        NaN   \n",
       "5569   ham  Pity, * was in mood for that. So...any other s...        NaN   \n",
       "5570   ham  The guy did some bitching but I acted like i'd...        NaN   \n",
       "5571   ham                         Rofl. Its true to its name        NaN   \n",
       "\n",
       "     Unnamed: 3 Unnamed: 4  \n",
       "0           NaN        NaN  \n",
       "1           NaN        NaN  \n",
       "2           NaN        NaN  \n",
       "3           NaN        NaN  \n",
       "4           NaN        NaN  \n",
       "...         ...        ...  \n",
       "5567        NaN        NaN  \n",
       "5568        NaN        NaN  \n",
       "5569        NaN        NaN  \n",
       "5570        NaN        NaN  \n",
       "5571        NaN        NaN  \n",
       "\n",
       "[5572 rows x 5 columns]>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d836fae",
   "metadata": {},
   "source": [
    "## Dropping the unwanted columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9ca7ecf7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>v1</th>\n",
       "      <th>v2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     v1                                                 v2\n",
       "0   ham  Go until jurong point, crazy.. Available only ...\n",
       "1   ham                      Ok lar... Joking wif u oni...\n",
       "2  spam  Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3   ham  U dun say so early hor... U c already then say...\n",
       "4   ham  Nah I don't think he goes to usf, he lives aro..."
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = data.drop(columns=data.columns[2:5])\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "423f0b68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Category</th>\n",
       "      <th>Message</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Category                                            Message\n",
       "0         ham  Go until jurong point, crazy.. Available only ...\n",
       "1         ham                      Ok lar... Joking wif u oni...\n",
       "2        spam  Free entry in 2 a wkly comp to win FA Cup fina...\n",
       "3         ham  U dun say so early hor... U c already then say...\n",
       "4         ham  Nah I don't think he goes to usf, he lives aro...\n",
       "...       ...                                                ...\n",
       "5567     spam  This is the 2nd time we have tried 2 contact u...\n",
       "5568      ham              Will Ì_ b going to esplanade fr home?\n",
       "5569      ham  Pity, * was in mood for that. So...any other s...\n",
       "5570      ham  The guy did some bitching but I acted like i'd...\n",
       "5571      ham                         Rofl. Its true to its name\n",
       "\n",
       "[5572 rows x 2 columns]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns = ['Category', 'Message']\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "050fd83e",
   "metadata": {},
   "source": [
    "## To check the null value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "08018579",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Category    0\n",
       "Message     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "00cd64c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsAAAAIhCAYAAABANwzIAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAABCKElEQVR4nO3de3zP9f//8fvbTmbsjbHNGJNYNDpQjIo+DOXQ4Rs+qTmfjxNhnw7oIz5USA6hIlGrb9G3b2nlXGIz85lDqa+EiCHmPdPamNfvj357fXrbnDfv6Xm7Xi7vy6XX8/V4vV7P57tP78/d0/P9fDssy7IEAAAAGKKUpzsAAAAAXE8EYAAAABiFAAwAAACjEIABAABgFAIwAAAAjEIABgAAgFEIwAAAADAKARgAAABGIQADAADAKARgACXe9u3b1bNnT9WsWVOlS5dW2bJldeedd2rq1Kk6ceLEFd9vxYoVGj9+fNF3tIRyOBz2y8vLSxUqVNBtt92m/v37KykpqUD9vn375HA4tGjRoit6zrvvvqsZM2Zc0TWFPWv8+PFyOBz69ddfr+heF/Pdd99p/Pjx2rdvX4FzPXr0UERERJE9C0DJRwAGUKItWLBADRs2VEpKip5++mklJiZq+fLl6tSpk15//XX17t37iu+5YsUKTZgwoRh6W3I99thj2rRpkzZs2KCEhAR169ZNSUlJio6O1vDhw91qq1Spok2bNqldu3ZX9IyrCcBX+6wr9d1332nChAmFBuDnnntOy5cvL9bnAyhZvD3dAQC4kE2bNmngwIGKiYnRxx9/LD8/P/tcTEyMRo4cqcTERA/2sHjl5eXp7NmzbuO+WiEhIWrSpIl93KZNG8XFxalfv36aOXOmbrnlFg0cOFCS5Ofn51ZbHP48tuJ+1qXUqlXLo88HcP0xAwygxJo0aZIcDofmz59faAj09fVVx44d7eP3339frVu3VpUqVeTv76+6detq7NixOn36tF3To0cPzZ49W5L70oD8mUHLsjRnzhzdfvvt8vf3V4UKFfTYY4/pp59+cnu2ZVmaNGmSatSoodKlS6tRo0ZauXKlWrRooRYtWrjV/vzzz3ryyScVHBwsPz8/1a1bV6+88orOnTtn1+QvBZg6daomTpyomjVrys/PTytXrlT58uXVv3//AuPft2+fvLy89NJLL13xeytJXl5emjVrlipVquR2j8KWJRw7dkz9+vVTeHi4/Pz8VLlyZTVr1kyrVq2SJLVo0UKfffaZ9u/f7/a+Xmxsa9euvehyiwMHDujRRx9VYGCgnE6nnnzySR07dsytxuFwFLqcJSIiQj169JAkLVq0SJ06dZIk3X///Xbf8p9Z2BKI33//XfHx8apZs6Z8fX1VtWpVDR48WCdPnizwnPbt2ysxMVF33nmn/P39dcstt+itt966xLsPwJOYAQZQIuXl5WnNmjVq2LChwsPDL+ua3bt368EHH1RcXJwCAgL0/fffa8qUKdq8ebPWrFkj6Y+/7j59+rQ+/PBDbdq0yb62SpUqkqT+/ftr0aJFGjZsmKZMmaITJ07ohRdeUNOmTbVt2zaFhIRIkp555hlNnjxZ/fr106OPPqoDBw6oT58+OnPmjOrUqWPf99ixY2ratKlyc3P1z3/+UxEREfr00081atQo7dmzR3PmzHEbw8yZM1WnTh29/PLLCgwMVO3atdWrVy/Nnz9fU6dOldPptGvnzJkjX19f9erV6+reZEn+/v5q1aqVEhISdPDgQVWrVq3QutjYWG3dulUvvvii6tSpo5MnT2rr1q06fvy43Zd+/fppz549F1xOUNjYLuaRRx5R586dNWDAAH377bd67rnn9N133yk5OVk+Pj6XPcZ27dpp0qRJ+sc//qHZs2frzjvvlHThmV/LsvTwww9r9erVio+P17333qvt27dr3Lhx2rRpkzZt2uT2B7Jt27Zp5MiRGjt2rEJCQvTGG2+od+/euvnmm3Xfffdddj8BXEcWAJRA6enpliTr73//+1Vdf+7cOevMmTPW+vXrLUnWtm3b7HODBw+2Cvv427RpkyXJeuWVV9zaDxw4YPn7+1ujR4+2LMuyTpw4Yfn5+VldunQp9PrmzZvbbWPHjrUkWcnJyW61AwcOtBwOh/XDDz9YlmVZe/futSRZtWrVsnJzc91q9+zZY5UqVcqaPn263ZadnW0FBQVZPXv2vOR7IckaPHjwBc+PGTPGrY/5fVm4cKFdU7ZsWSsuLu6iz2nXrp1Vo0aNAu0XG1thzxo3bpwlyRoxYoRb7dKlSy1J1pIlS9zGNm7cuALPrFGjhtW9e3f7+L//+78tSdbatWsL1Hbv3t2t34mJiZYka+rUqW5177//viXJmj9/vttzSpcube3fv99uy87OtipWrGj179+/wLMAlAwsgQDwl/HTTz+pa9euCg0NlZeXl3x8fNS8eXNJ0q5duy55/aeffiqHw6Enn3xSZ8+etV+hoaG67bbbtG7dOklSUlKScnJy1LlzZ7frmzRpUuCv0tesWaN69erp7rvvdmvv0aOHLMuyZ6bzdezYscDs5k033aT27dtrzpw5sixL0h9fODt+/LiGDBlyyXFdSv49L+buu+/WokWLNHHiRCUlJenMmTNX/JzCxnYxTzzxhNtx586d5e3trbVr117xs69E/r+T/CUU+Tp16qSAgACtXr3arf32229X9erV7ePSpUurTp062r9/f7H2E8DVIwADKJEqVaqkMmXKaO/evZdVn5WVpXvvvVfJycmaOHGi1q1bp5SUFC1btkySlJ2dfcl7HDlyRJZlKSQkRD4+Pm6vpKQke1uu/L/2z18O8Wfntx0/ftxeXvFnYWFhbvfKV1itJA0fPly7d+/WypUrJUmzZ89WdHS0/df51yI/qOX3qTDvv/++unfvrjfeeEPR0dGqWLGiunXrpvT09Mt+zoXGdiGhoaFux97e3goKCirwnhW148ePy9vbW5UrV3ZrdzgcCg0NLfD8oKCgAvfw8/O7rP/NAfAM1gADKJG8vLzUsmVLff755xddm5pvzZo1OnTokNatW2fP+koq8KWli6lUqZIcDoe+/vrrQr90l9+WH3iOHDlSoCY9Pd1tFjgoKEiHDx8uUHfo0CH7mX+W/8Wx8/3tb39TVFSUZs2apbJly2rr1q1asmTJ5Q3sIrKzs7Vq1SrVqlXrou9xpUqVNGPGDM2YMUM///yzPvnkE40dO1ZHjx697J04LjS2C0lPT1fVqlXt47Nnz+r48eNugdPPz085OTkFrr2WkBwUFKSzZ8/q2LFjbiHYsiylp6frrrvuuup7AygZmAEGUGLFx8fLsiz17dtXubm5Bc6fOXNG//u//yvpP+Hq/OA6b968Atfl15w/Q9e+fXtZlqVffvlFjRo1KvCqX7++JKlx48by8/PT+++/73Z9UlJSgb/2btmypb777jtt3brVrX3x4sVyOBy6//77L/k+5Bs2bJg+++wzxcfHKyQkxN7Z4Grl5eVpyJAhOn78uMaMGXPZ11WvXl1DhgxRTEyM27iKetZz6dKlbscffPCBzp4967bLRkREhLZv3+5Wt2bNGmVlZbm1XejfeWFatmwpSQX+gPHRRx/p9OnT9nkANy5mgAGUWNHR0Zo7d64GDRqkhg0bauDAgbr11lt15swZ/fvf/9b8+fMVFRWlDh06qGnTpqpQoYIGDBigcePGycfHR0uXLtW2bdsK3Dc/yE6ZMkUPPPCAvLy81KBBAzVr1kz9+vVTz549tWXLFt13330KCAjQ4cOHtWHDBtWvX18DBw5UxYoV9dRTT2ny5MmqUKGCHnnkER08eFATJkxQlSpVVKrUf+YWRowYocWLF6tdu3Z64YUXVKNGDX322WeaM2eOBg4c6LZjxKU8+eSTio+P11dffaVnn31Wvr6+l33tkSNHlJSUJMuydOrUKe3cuVOLFy/Wtm3bNGLECPXt2/eC17pcLt1///3q2rWrbrnlFpUrV04pKSlKTEzUo48+6va+Llu2THPnzlXDhg1VqlQpNWrU6LL7eL5ly5bJ29tbMTEx9i4Qt912m9va69jYWD333HN6/vnn1bx5c3333XeaNWuW224ZkhQVFSVJmj9/vsqVK6fSpUurZs2ahS5fiImJUZs2bTRmzBhlZmaqWbNm9i4Qd9xxh2JjY696TABKCM99/w4ALk9aWprVvXt3q3r16pavr68VEBBg3XHHHdbzzz9vHT161K7buHGjFR0dbZUpU8aqXLmy1adPH2vr1q0FdhnIycmx+vTpY1WuXNlyOByWJGvv3r32+bfeestq3LixFRAQYPn7+1u1atWyunXrZm3ZssWuOXfunDVx4kSrWrVqlq+vr9WgQQPr008/tW677TbrkUcecev//v37ra5du1pBQUGWj4+PFRkZab300ktWXl6eXZO/G8JLL7100feiR48elre3t3Xw4MHLfv8k2a9SpUpZgYGBVv369a1+/fpZmzZtKlB//s4Mv//+uzVgwACrQYMGVmBgoOXv729FRkZa48aNs06fPm1fd+LECeuxxx6zypcvb7+vlxrbxXaBSE1NtTp06GCVLVvWKleunPX4449bR44ccbs+JyfHGj16tBUeHm75+/tbzZs3t9LS0grsAmFZljVjxgyrZs2alpeXl9szz98FwrL+2MlhzJgxVo0aNSwfHx+rSpUq1sCBA62MjAy3uho1aljt2rUrMK7mzZu77QYCoGRxWNZlfP0XAHBJe/fu1S233KJx48bpH//4R5HfPzc3VxEREbrnnnv0wQcfFPn9AcAULIEAgKuwbds2vffee2ra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o0aNVLZsWbVt21bHjh3zxPDxF0UABorZ22+/rYCAACUnJ2vq1Kl64YUX7J/lLlWqlGbOnKmdO3fq7bff1po1azR69Gi363/77TfNnDlTCQkJSkxM1Lp16/Too49qxYoVWrFihd555x3Nnz9fH374oSeGB+Av7PDhw3r88cfVq1cv7dq1y/78yf8JgdWrV2vXrl1au3at3nvvPS1fvlwTJkywrz99+rSeeuoppaSkaPXq1SpVqpQeeeQRnTt3zu0548aN07PPPqutW7fK29tbjz/+uEaPHq1XX31VX3/9tfbs2aPnn3/+uo4df3EWgGLTvHlz65577nFru+uuu6wxY8YUWv/BBx9YQUFB9vHChQstSdaPP/5ot/Xv398qU6aMderUKbutTZs2Vv/+/Yu49wBMl5qaakmy9u3bV+Bc9+7drYoVK1qnT5+22+bOnWuVLVvWysvLK/R+R48etSRZO3bssCzLsvbu3WtJst544w275r333rMkWatXr7bbJk+ebEVGRhbVsACLGWCgmDVo0MDtuEqVKjp69Kgkae3atYqJiVHVqlVVrlw5devWTcePH9fp06ft+jJlyqhWrVr2cUhIiCIiIlS2bFm3tvx7AkBRue2229SyZUvVr19fnTp10oIFC5SRkeF2vkyZMvZxdHS0srKydODAAUnSnj171LVrV910000KDAxUzZo1JUk///yz23P+/DkZEhIiSapfv75bG59xKEoEYKCY+fj4uB07HA6dO3dO+/fv14MPPqioqCh99NFHSk1N1ezZsyVJZ86cuej1F7onABQlLy8vrVy5Up9//rnq1aun1157TZGRkdq7d+9Fr3M4HJKkDh066Pjx41qwYIGSk5OVnJwsSW7rhCX3z7n8a89v4zMORcnb0x0ATLVlyxadPXtWr7zyikqV+uPPoh988IGHewUA7hwOh5o1a6ZmzZrp+eefV40aNbR8+XJJ0rZt25SdnS1/f39JUlJSksqWLatq1arp+PHj2rVrl+bNm6d7771XkrRhwwaPjQP4MwIw4CG1atXS2bNn9dprr6lDhw765ptv9Prrr3u6WwBgS05O1urVq9W6dWsFBwcrOTlZx44dU926dbV9+3bl5uaqd+/eevbZZ7V//36NGzdOQ4YMUalSpVShQgUFBQVp/vz5qlKlin7++WeNHTvW00MCJLEEAvCY22+/XdOmTdOUKVMUFRWlpUuXavLkyZ7uFgDYAgMD9dVXX+nBBx9UnTp19Oyzz+qVV17RAw88IElq2bKlateurfvuu0+dO3dWhw4d7K0eS5UqpYSEBKWmpioqKkojRozQSy+95MHRAP/hsKz/v5cJAADAZerRo4dOnjypjz/+2NNdAa4YM8AAAAAwCgEYAAAARmEJBAAAAIzCDDAAAACMQgAGAACAUQjAAAAAMAoBGAAAAEYhAAMAAMAoBGAAAAAYhQAMACVEenq6hg4dqptuukl+fn4KDw9Xhw4dtHr16su6ftGiRSpfvnzxdhIA/gK8Pd0BAIC0b98+NWvWTOXLl9fUqVPVoEEDnTlzRl988YUGDx6s77//3tNdvGJnzpyRj4+Pp7sBAAUwAwwAJcCgQYPkcDi0efNmPfbYY6pTp45uvfVWPfXUU0pKSpIkTZs2TfXr11dAQIDCw8M1aNAgZWVlSZLWrVunnj17yuVyyeFwyOFwaPz48ZKk3NxcjR49WlWrVlVAQIAaN26sdevWuT1/wYIFCg8PV5kyZfTII49o2rRpBWaT586dq1q1asnX11eRkZF655133M47HA69/vrreuihhxQQEKCJEyfq5ptv1ssvv+xWt3PnTpUqVUp79uwpujcQAK4AARgAPOzEiRNKTEzU4MGDFRAQUOB8fhAtVaqUZs6cqZ07d+rtt9/WmjVrNHr0aElS06ZNNWPGDAUGBurw4cM6fPiwRo0aJUnq2bOnvvnmGyUkJGj79u3q1KmT2rZtq927d0uSvvnmGw0YMEDDhw9XWlqaYmJi9OKLL7r1Yfny5Ro+fLhGjhypnTt3qn///urZs6fWrl3rVjdu3Dg99NBD2rFjh3r16qVevXpp4cKFbjVvvfWW7r33XtWqVatI3j8AuGIWAMCjkpOTLUnWsmXLrui6Dz74wAoKCrKPFy5caDmdTreaH3/80XI4HNYvv/zi1t6yZUsrPj7esizL6tKli9WuXTu380888YTbvZo2bWr17dvXraZTp07Wgw8+aB9LsuLi4txqDh06ZHl5eVnJycmWZVlWbm6uVblyZWvRokVXNFYAKErMAAOAh1mWJemPJQQXs3btWsXExKhq1aoqV66cunXrpuPHj+v06dMXvGbr1q2yLEt16tRR2bJl7df69evtJQg//PCD7r77brfrzj/etWuXmjVr5tbWrFkz7dq1y62tUaNGbsdVqlRRu3bt9NZbb0mSPv30U/3+++/q1KnTRccKAMWJAAwAHla7dm05HI4CYfLP9u/frwcffFBRUVH66KOPlJqaqtmzZ0v648tmF3Lu3Dl5eXkpNTVVaWlp9mvXrl169dVXJf0RwM8P3/mh/M8Kqzm/rbAlHH369FFCQoKys7O1cOFCdenSRWXKlLlgnwGguBGAAcDDKlasqDZt2mj27NmFzuaePHlSW7Zs0dmzZ/XKK6+oSZMmqlOnjg4dOuRW5+vrq7y8PLe2O+64Q3l5eTp69Khuvvlmt1doaKgk6ZZbbtHmzZvdrtuyZYvbcd26dbVhwwa3to0bN6pu3bqXHN+DDz6ogIAAzZ07V59//rl69ep1yWsAoDgRgAGgBJgzZ47y8vJ0991366OPPtLu3bu1a9cuzZw5U9HR0apVq5bOnj2r1157TT/99JPeeecdvf766273iIiIUFZWllavXq1ff/1Vv/32m+rUqaMnnnhC3bp107Jly7R3716lpKRoypQpWrFihSRp6NChWrFihaZNm6bdu3dr3rx5+vzzz91md59++mktWrRIr7/+unbv3q1p06Zp2bJl9hftLsbLy0s9evRQfHy8br75ZkVHRxftmwcAV8qjK5ABALZDhw5ZgwcPtmrUqGH5+vpaVatWtTp27GitXbvWsizLmjZtmlWlShXL39/fatOmjbV48WJLkpWRkWHfY8CAAVZQUJAlyRo3bpxlWX988ez555+3IiIiLB8fHys0NNR65JFHrO3bt9vXzZ8/36patarl7+9vPfzww9bEiROt0NBQt/7NmTPHuummmywfHx+rTp061uLFi93OS7KWL19e6Nj27NljSbKmTp16ze8TAFwrh2UVstALAGC0vn376vvvv9fXX39dJPf75ptv1KJFCx08eFAhISFFck8AuFr8EhwAQC+//LJiYmIUEBCgzz//XG+//bbmzJlzzffNycnRgQMH9Nxzz6lz586EXwAlAmuAAQDavHmzYmJiVL9+fb3++uuaOXOm+vTpc833fe+99xQZGSmXy6WpU6cWQU8B4NqxBAIAAABGYQYYAAAARiEAAwAAwCgEYAAAABiFAAwAAACjEIABAABgFAIwAAAAjEIABgAAgFEIwAAAADDK/wMSoHWvcHy8qAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 800x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "category_counts = data['Category'].value_counts().reset_index()\n",
    "category_counts.columns = ['Category', 'Count']\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.barplot(x='Category', y='Count', data=category_counts)\n",
    "plt.xlabel('Category')\n",
    "plt.ylabel('Count')\n",
    "plt.title('Category Distribution')\n",
    "\n",
    "for i, count in enumerate(category_counts['Count']):\n",
    "    plt.text(i, count, str(count), ha='center', va='bottom')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "4d472bb7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Category</th>\n",
       "      <th>Message</th>\n",
       "      <th>spam</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ham</td>\n",
       "      <td>Go until jurong point, crazy.. Available only ...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ham</td>\n",
       "      <td>Ok lar... Joking wif u oni...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>spam</td>\n",
       "      <td>Free entry in 2 a wkly comp to win FA Cup fina...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ham</td>\n",
       "      <td>U dun say so early hor... U c already then say...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ham</td>\n",
       "      <td>Nah I don't think he goes to usf, he lives aro...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5567</th>\n",
       "      <td>spam</td>\n",
       "      <td>This is the 2nd time we have tried 2 contact u...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5568</th>\n",
       "      <td>ham</td>\n",
       "      <td>Will Ì_ b going to esplanade fr home?</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5569</th>\n",
       "      <td>ham</td>\n",
       "      <td>Pity, * was in mood for that. So...any other s...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5570</th>\n",
       "      <td>ham</td>\n",
       "      <td>The guy did some bitching but I acted like i'd...</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5571</th>\n",
       "      <td>ham</td>\n",
       "      <td>Rofl. Its true to its name</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5572 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Category                                            Message  spam\n",
       "0         ham  Go until jurong point, crazy.. Available only ...     0\n",
       "1         ham                      Ok lar... Joking wif u oni...     0\n",
       "2        spam  Free entry in 2 a wkly comp to win FA Cup fina...     1\n",
       "3         ham  U dun say so early hor... U c already then say...     0\n",
       "4         ham  Nah I don't think he goes to usf, he lives aro...     0\n",
       "...       ...                                                ...   ...\n",
       "5567     spam  This is the 2nd time we have tried 2 contact u...     1\n",
       "5568      ham              Will Ì_ b going to esplanade fr home?     0\n",
       "5569      ham  Pity, * was in mood for that. So...any other s...     0\n",
       "5570      ham  The guy did some bitching but I acted like i'd...     0\n",
       "5571      ham                         Rofl. Its true to its name     0\n",
       "\n",
       "[5572 rows x 3 columns]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['spam']= data['Category'].apply(lambda x: 1 if x=='spam' else 0)\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24d18810",
   "metadata": {},
   "source": [
    "## Training and testing of data "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4dbe0b54",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(data.Message,data.spam, test_size=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "beed11d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "featurer = CountVectorizer()\n",
    "X_train_count = featurer.fit_transform(X_train.values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b8f9958a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<4457x7701 sparse matrix of type '<class 'numpy.int64'>'\n",
       "\twith 59271 stored elements in Compressed Sparse Row format>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train_count"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae6e071c",
   "metadata": {},
   "source": [
    "## Applying the Naive Bayes Method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e57734a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>MultinomialNB()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">MultinomialNB</label><div class=\"sk-toggleable__content\"><pre>MultinomialNB()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "MultinomialNB()"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = MultinomialNB()\n",
    "model.fit(X_train_count,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b20c2e91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9874439461883409"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test_count = featurer.transform(X_test)\n",
    "model.score(X_test_count, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "990bc6d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.pipeline import Pipeline\n",
    "clf = Pipeline([\n",
    "    ('vectorizer', CountVectorizer()),\n",
    "    ('nb', MultinomialNB())\n",
    "])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "21239e7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {color: black;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>Pipeline(steps=[(&#x27;vectorizer&#x27;, CountVectorizer()), (&#x27;nb&#x27;, MultinomialNB())])</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" ><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">Pipeline</label><div class=\"sk-toggleable__content\"><pre>Pipeline(steps=[(&#x27;vectorizer&#x27;, CountVectorizer()), (&#x27;nb&#x27;, MultinomialNB())])</pre></div></div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" ><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">CountVectorizer</label><div class=\"sk-toggleable__content\"><pre>CountVectorizer()</pre></div></div></div><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" ><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">MultinomialNB</label><div class=\"sk-toggleable__content\"><pre>MultinomialNB()</pre></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "Pipeline(steps=[('vectorizer', CountVectorizer()), ('nb', MultinomialNB())])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "02bf7ac2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9874439461883409"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(X_test,y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2bb41ab9",
   "metadata": {},
   "source": [
    "## Now design a pre_build model to detect spam and not spam message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "66117ac4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'Your account have 100 debeted, is waiting to be collected. Simply text the password \\MIX\" to 85069 to verify. Get Usher and Britney. FML' is a spam message.\n"
     ]
    }
   ],
   "source": [
    "# Pre-trained model\n",
    "pretrained_model = model \n",
    "new_sentences = [\n",
    "    \"Your account have 100 debeted, is waiting to be collected. Simply text the password \\MIX\\\" to 85069 to verify. Get Usher and Britney. FML\"\n",
    "]\n",
    "\n",
    "new_sentences_count = featurer.transform(new_sentences)\n",
    "# Predict whether each sentence is spam (1) or not (0)\n",
    "predictions = pretrained_model.predict(new_sentences_count)\n",
    "\n",
    "for sentence, prediction in zip(new_sentences, predictions):\n",
    "    if prediction == 1:\n",
    "        print(f\"'{sentence}' is a spam message.\")\n",
    "    else:\n",
    "        print(f\"'{sentence}' is not a spam message.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "410e0c9b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}