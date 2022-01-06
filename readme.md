# Custom model - Sklearn

You can find some tutorials and documentation on the following links:  
- Tutorial: [Vertex AI: Training and serving a custom model](https://codelabs.developers.google.com/vertex_custom_training_prediction)  
- YouTube tutorial: [Build a custom ML model with Vertex AI](https://www.youtube.com/watch?v=I2CJL3tQasw&ab_channel=GoogleCloudTech)
- [Exporting model artifacts](https://cloud.google.com/vertex-ai/docs/training/exporting-model-artifacts#scikit-learn)


## Create custom container

Example code that shows how to package your Python code:
```sh
python setup.py sdist --formats=gztar
gsutil cp dist/sklearn-text-classification-0.1.tar.gz gs://haba-ws/container/
```