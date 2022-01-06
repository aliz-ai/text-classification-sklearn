import pandas as pd
import argparse
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import os
import joblib
from google.cloud import storage


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data",
        type=str,
        required=True,
    )
    args = parser.parse_args()

    # Load data
    data = pd.read_csv(args.data, header=None, names=["ml_use", "text", "label"])

    # Create model
    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB()),
    ])

    # Train model
    text_clf.fit(data[data["ml_use"]=="training"]["text"], data[data["ml_use"]=="training"]["label"])

    # Save model
    artifact_filename = 'model.joblib'

    local_path = artifact_filename
    joblib.dump(text_clf, local_path)

    # Upload model artifact to Cloud Storage
    model_directory = os.environ['AIP_MODEL_DIR']
    storage_path = os.path.join(model_directory, artifact_filename)
    blob = storage.blob.Blob.from_string(storage_path, client=storage.Client())
    blob.upload_from_filename(local_path)